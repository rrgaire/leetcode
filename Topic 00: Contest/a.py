from collections import deque 

class SupermarketCheckout:
    def __init__(self,):
        self.db = {}
        
    def on_customer_enter(self, customer_id, line_number, num_items):
        # TODO Implement
        if line_number not in self.db:
            self.db[line_number] = deque()
        self.db[line_number].append([customer_id, num_items, 0])


    def on_basket_change(self, customer_id, new_num_items):
        # TODO Implement
        for ln in self.db.keys():
            i = 0
            while i < len(self.db[ln]):
                cid, nitem, d = self.db[ln][i]
                if cid == customer_id:
                    if nitem < new_num_items:
                        del self.db[ln][i]
                        c, it, it2 = cid, new_num_items - nitem - d, d
                    else:
                        self.db[ln][i] = [cid, new_num_items]
                i += 1
            if c and it:
                self.db[ln].append([c, it, it2])
            
            
    def on_line_service(self, line_number, num_processed_items):
        
        i = 0   
        while num_processed_items and i < len(self.db[line_number]):
            if self.db[line_number][i][1] <= num_processed_items:
                num_processed_items -= self.db[line_number][i][1]
                self.db[line_number][i][1] = 0
                self.db[line_number][i][2] += num_processed_items
                self.on_customer_exit(self.db[line_number][i][0])
                self.db[line_number].popleft()
            else:
                self.db[line_number][i][1] -= num_processed_items
                self.db[line_number][i][2] += num_processed_items
                num_processed_items = 0
                i += 1
                      
    def on_lines_service(self):
        # TODO Implement
        for k, v in self.db.items():
            self.db[k][0][1] -= 1
            self.db[k][0][2] += 1
            if self.db[k][0][1] == 0:
                self.on_customer_exit(self.db[k][0][0])
                self.db[k].popleft()
        

    def on_customer_exit(self, customer_id):
        # Don't change this implementation.
        print(customer_id)


if __name__ == "__main__":
    import sys

    checkout_tracker = SupermarketCheckout()
    line = sys.stdin.readline().split()
    n = int(line[0])
    for _ in range(n):
        line = sys.stdin.readline().split()
        if line[0] == "CustomerEnter":
            customer_id = int(line[1])
            line_number = int(line[2])
            num_items = int(line[3])
            checkout_tracker.on_customer_enter(customer_id, line_number, num_items)
        elif line[0] == "BasketChange":
            customer_id = int(line[1])
            new_num_items = int(line[2])
            checkout_tracker.on_basket_change(customer_id, new_num_items);
        elif line[0] == "LineService":
            line_number = int(line[1])
            num_processed_items = int(line[2])
            checkout_tracker.on_line_service(line_number, num_processed_items);
        elif line[0] == "LinesService":
            checkout_tracker.on_lines_service();
        else:
            raise Exception("Malformed input!")
        


from dataclasses import dataclass

from collections import defaultdict
import heapq

@dataclass
class LionDescription:
    name: str
    height: int


@dataclass
class LionSchedule:
    name: str
    enter_time: int
    exit_time: int


class LionCompetition:
    def __init__(self, lions: list[LionDescription], schedule: list[LionSchedule]):
        self.sizeMap = {ln.name: ln.height for ln in lions}
        self.mine = set()

        self.ignoreMap = defaultdict(int)
        
        self.others = []
        self.othersLeft = defaultdict(int) 

        self.schedule = []
        for event in schedule:
            name, arrival, departure = event.name, event.enter_time, event.exit_time
            self.schedule.append((name, arrival, "arrive"))
            self.schedule.append((name, departure, "depart"))
            self.ignoreMap[(self.sizeMap[name], arrival, "arrival")] += 1
            self.ignoreMap[(self.sizeMap[name], departure, "departure")] += 1


        self.schedule.sort(key = lambda t: t[1])
        self.si = 0

    def lion_entered(self, current_time: int, height: int):
        key = (height, time, "arrival")
        if self.ignoreMap[key] > 0:
            self.ignoreMap[key] -= 1
        else:
            heapq.heappush(self.others, -height)

    def lion_left(self, current_time: int, height: int):
        key = (height, time, "departure")
        if self.ignoreMap[key] > 0:
            self.ignoreMap[key] -= 1
        else:
            self.othersLeft[height] += 1

    def get_biggest_lions(self) -> list[str]:
        while self.si < len(self.schedule) and self.schedule[self.si][1] <= time:
            name, _, type = self.schedule[self.si]
            if type == "arrive":
                self.mine.add((name, self.sizeMap[name]))
            else:
                self.mine.remove((name, self.sizeMap[name]))
            self.si += 1

        while self.others:
            cur = abs(self.others[0])
            if self.othersLeft[cur] > 0:
                heapq.heappop(self.others)
                self.othersLeft[cur] -= 1
            else:
                break

        tallestRival = abs(self.others[0])
        candidates = [name for name,height in self.mine if height >= tallestRival]
        candidates.sort()
        return candidates


if __name__ == "__main__":
    import sys

    read_line = lambda: sys.stdin.readline().split()

    descriptions: list[LionDescription] = []
    lion_schedule: list[LionSchedule] = []

    parse = True
    while parse:
        line = read_line()
        if line[0] == 'definition':
            name = line[1]
            size = int(line[2])
            description = LionDescription(name, size)
            descriptions.append(description)
        elif line[0] == 'schedule':
            name = line[1]
            enter_time = int(line[2])
            exit_time = int(line[3])
            schedule_entry = LionSchedule(name, enter_time, exit_time)
            lion_schedule.append(schedule_entry)
        elif line[0] == 'start':
            parse = False
        else:
            raise Exception('invalid input')

    lion_competition = LionCompetition(descriptions, lion_schedule)
    parse = True
    while parse:
        line = read_line()
        time = int(line[0])
        if line[1] == 'enter':
            size = int(line[2])
            lion_competition.lion_entered(time, size)
        elif line[1] == 'exit':
            size = int(line[2])
            lion_competition.lion_left(time, size)
        elif line[1] == 'inspect':
            biggest_lions = lion_competition.get_biggest_lions()
            print(len(biggest_lions), end='')
            for lion in biggest_lions:
                print(" " + lion, end='')
            print()
        elif line[1] == 'end':
            parse = False
        else:
            raise Exception('invalid input')