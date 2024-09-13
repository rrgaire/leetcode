"""
895. Maximum Frequency Stack
Solved
Hard
Topics
Companies
Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:

FreqStack() constructs an empty frequency stack.
void push(int val) pushes an integer val onto the top of the stack.
int pop() removes and returns the most frequent element in the stack.
If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.
 

Example 1:

Input
["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
[[], [5], [7], [5], [7], [4], [5], [], [], [], []]
Output
[null, null, null, null, null, null, null, 5, 7, 5, 4]

Explanation
FreqStack freqStack = new FreqStack();
freqStack.push(5); // The stack is [5]
freqStack.push(7); // The stack is [5,7]
freqStack.push(5); // The stack is [5,7,5]
freqStack.push(7); // The stack is [5,7,5,7]
freqStack.push(4); // The stack is [5,7,5,7,4]
freqStack.push(5); // The stack is [5,7,5,7,4,5]
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].
 

Constraints:

0 <= val <= 109
At most 2 * 104 calls will be made to push and pop.
It is guaranteed that there will be at least one element in the stack before calling pop.

"""

class FreqStack:
    # Using Heap: time: O(logn) | space: O(n)
    def __init__(self):
        self.dict = {}
        self.heap = []
        heapq.heapify(self.heap)
        self.i = 0

    def push(self, val: int) -> None:
        self.i += 1
        self.dict[val] = 1 + self.dict.get(val, 0)
        heapq.heappush(self.heap, (-self.dict[val], -self.i, val))

        

    def pop(self) -> int:
        freq, i, val = heapq.heappop(self.heap)
        self.dict[val] -= 1
        return val
        

    # Without using Heap: time: O(1) | space: O(n)

    def __init__(self):
        self.count = {}
        self.stacks = {}
        self.maxf = 0

    def push(self, val):
        self.count[val] = 1 + self.count.get(val, 0)
        if self.count[val] > self.maxf:
            self.maxf = self.count[val]
            self.stacks[self.maxf] = []
        self.stacks[self.count[val]].append(val)

    def pop(self):
        val = self.stacks[self.maxf].pop()
        self.count[val] -= 1
        if not self.stacks[self.maxf]:
            self.maxf -= 1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()