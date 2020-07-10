class EventSourcer():
    # Do not change the signature of any functions

    # Eric Corbu
    # I haven't used event sourcing before so I'm not sure if this is implemented properly, however it passes the given 'test_python_solution.py'


    def __init__(self):
        self.value = 0
        self.currentEvent = -1
        self.events = []

    def add(self, num):
        self.value += num
        self.events.append(num)
        self.currentEvent += 1
        pass

    def subtract(self, num):
        self.value -=num
        self.events.append(-num)
        self.currentEvent += 1
        pass

    def undo(self):
        if self.currentEvent >= 0:
            self.value -= self.events[self.currentEvent]
            self.currentEvent -= 1            
        pass

    def redo(self):
        if len(self.events) -1 > self.currentEvent:
            self.currentEvent += 1
            self.value += self.events[self.currentEvent]
        pass

    def bulk_undo(self, steps):
        for _ in range(steps):
            self.undo()
        pass

    def bulk_redo(self, steps):
        for _ in range(steps):
            self.redo()
        pass

