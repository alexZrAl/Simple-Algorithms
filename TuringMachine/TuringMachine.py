

class Tape:
    '''
        A Tape is made of an infinite number slots, each slot holds a character.
        The following characters are allowed on a tape:
            '0', 
            '1',
            ' '(space), 
            '*'(initial character),
            '#'(separation character)
        Slots with '0' or '1' characters can be marked(e.g. "m1-0" means '0' with mark "1")
    '''

    def __init__(self, lst):
        self.contents = lst


    def read(self, position):
        return self.contents[position]

    def write(self, position, value):
        self.contents[position] = value

    def print(self):
        for char in self.contents:
            print(char, end="")
        print("")

class Instruction:
    '''
        Part of a Turing Machine code {initial state}{read}{target state(endState)}{write}{pointer movement}
        {read}{write}{pointer movement} is encapsulated in member variable `condition`
    '''

    def __init__(self, endState, condition):
        '''
            if currentState && pointer reads == list[0], write list[1] BEFORE moving pointer according to list[2]
            after all these, switch current state to endState

            @param endState:    string, the resulting state of the beginState and the condition

            @param condition:   a list of length 3:
                                list[0] -> what the pointer reads
                                list[1] -> what the pointer writes
                                list[2] -> what direction the pointer should move
                                        directions: "L" -> move left
                                                    "R" -> move right
                                                    "S" -> no move
        '''
        self.condition = condition
        self.endState = endState

    def getCondition(self):
        return self.condition

    def getEndState(self):
        return self.endState

#-------------------------------------------------------------------------------------------------- #

class TuringMachine:
    '''
        A turing machine(TM) is a "machine" consisting of a finite number of states,
        a pointer capable of moving left/right on a infinite-long paper tape and reading/writing characters,
        
        The TM takes a Tape as input.
        The machine is capable of solving decision problems.(turing-decidable languages)
    '''

    def __init__(self, states):
        '''
            
            @param states:  A directed weighed graph of different machine states
                            Edge q0 --(condition)--> q1
                            means if current state is in q0 and pointer reads (condition)
                            The states are stored in a python dict(), dict[state] = Instruction
        '''
       # self.tape = tape
        self.adjList = states
        self.pointer = 0
    

    def movePtr(self, direction, steps):
        '''
            Moves the pointer of the TM left or right for some number of steps

            @param direction:   Must be either 'L' or 'R' in order to move pointer
                                if neither 'L' nor 'R' pointer is NOT moved
            @param steps:   Integer, preferably positive integer
        '''
        if direction == 'L':
            self.pointer -= steps
        elif direction == 'R':
            self.pointer += steps

    def execute(self, tape, initState):
        '''
            @param tape: input tape
            @param initState: string, the initial state of the TM
        '''
        self.pointer = 0
        curState = initState

        while (curState != "Y" and curState != "N"):
            # find the corresponding instruction for the current state,
            # according to contents read by the pointer
            for instruction in self.adjList[curState]:
                
                condition = instruction.getCondition()

                if tape.read(self.pointer) == condition[0]:
                    if condition[1] != '':
                        tape.write(self.pointer, condition[1])
                    self.movePtr(condition[2], 1)
                    curState = instruction.getEndState()

        if curState == "Y":
            print("YES")
        elif curState == "N":
            print("NO")
        else:
            print(curState)
    

    

if __name__ == "__main__":
    print("\nAuthor: alexZrAl\nImport this file in other .py files to use its content.")
    