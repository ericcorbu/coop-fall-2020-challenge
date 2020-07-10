class EventSourcer():
    # Do not change the signature of any functions
    """
        Eric Corbu
        corb0400@mylaurier.ca
        
        I haven't used event sourcing before so I'm not sure if this is implemented properly, however it passes the given 'test_python_solution.py'
        Python Implementation (works the same as JS implementation)
    """
    def __init__(self):
        # initializing currentEvent as -1 seems strange, but the first operation should be at index 0
        
        self.value = 0
        self.currentEvent = -1
        self.events = []

    def add(self, num):
        # adds value to total pushes event to the list, and increments the current event
        
        self.value += num
        self.events.append(num)
        self.currentEvent += 1
        pass

    def subtract(self, num):
        # subtracts value from total, pushes event to the list (subtration event is represented by a nevative integer), increments current event
        
        self.value -= num
        self.events.append(-num)
        self.currentEvent += 1
        pass

    def undo(self):
        #checks that there has been an event pushed, so that undo is possible
        if self.currentEvent >= 0:
            # subtracts value of last event from total
            self.value -= self.events[self.currentEvent]
            # moves currentEvent back one place
            self.currentEvent -= 1            
        pass

    def redo(self):
        # checks that the currentEvent is not the last event, so that redo is possible
        if len(self.events) -1 > self.currentEvent:
            # moves currentEvent forward one place
            self.currentEvent += 1
            # adds value of last event to total
            self.value += self.events[self.currentEvent]
        pass

    def bulk_undo(self, steps):
        # calls undo function for number of steps
        for _ in range(steps):
            self.undo()
        pass

    def bulk_redo(self, steps):
        # calls redo function for number of steps
        for _ in range(steps):
            self.redo()
        pass

