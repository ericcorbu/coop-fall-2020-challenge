class EventSourcer {
  /*
    Eric Corbu
    corb0400@mylaurier.ca

    I haven't used event sourcing before so I'm not sure if this is implemented properly, but it passes the given tests with npm test'
    JavaScript Implementation (same in functionality as Python implementation)
  */
    
  constructor() {
    // initializing currentEvent as -1 seems strange, but the first operation should be at index 0
    this.value = 0;
    this.currentEvent = -1;
    this.events = [];
  }

  add(num) {
    // adds value to total pushes event to the list, and increments the current event

    this.value += num;
    this.events.push(num);
    this.currentEvent++;
  }

  subtract(num) {
    // subtracts value from total, pushes event to the list (subtration event is represented by a nevative integer), increments current event

    this.value -= num;
    this.events.push(-num);
    this.currentEvent ++;
  }

  undo() {
    // checks that there has been an event pushed, so that undo is possible

    if (this.currentEvent >= 0) {
      // subtracts value of last event from total
      this.value -= this.events[this.currentEvent];
      // moves currentEvent back one place
      this.currentEvent -= 1;
    }
  }

  redo() {
    // checks that the currentEvent is not the last event, so that redo is possible
    if (this.events.length -1 > this.currentEvent) {
      // moves currentEvent forward one place
      this.currentEvent++;
      // adds value of last event to total
      this.value += this.events[this.currentEvent];
     
    }
  }

  bulk_undo(num) {
    // calls undo function for number of steps
    for (let i = 0; i < num; i++) {
      this.undo();
    }
  }

  bulk_redo(num) {
    // calls redo function for number of steps
    for (let i = 0; i < num; i++){
      this.redo();
    }
  }
}

// ----- Do not modify anything below this line (needed for test suite) ------
module.exports = EventSourcer;
