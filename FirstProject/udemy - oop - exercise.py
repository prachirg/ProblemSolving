'''Write an object oriented program to create a precious stone.
Not more than 5 precious stones can be held in possession at a
given point of time. If there are more than 5 precious stones,
delete the first stone and store the new one.'''

from collections import deque
class StonePossession:
    def __init__(self):
        self.queue = deque([])

    def add_stone(self,stone):
        #self.counter = 0
        #for i in range(5):
        if len(self.queue) >= 5:
            self.queue.popleft()
            print("First stone deleted")
            print("Remaining stones",len(self.queue))
        self.queue.append(stone)
        print("Stone added:",stone)
        print("Total stones:",len(self.queue))

s = StonePossession()
StonePossession.add_stone(s, 1)
s.add_stone(1)
s.add_stone(2)
s.add_stone(3)
s.add_stone(4)
s.add_stone(5)
s.add_stone(6)










