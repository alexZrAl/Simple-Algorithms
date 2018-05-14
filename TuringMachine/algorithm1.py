import TuringMachine as TM

def constructState():
    '''
        Construct a mapping of TM states and returns them
        (think of this as writing code in an actual computer)
    '''
    states = dict()

    states["S1"] = set()
    states["S1"].add(TM.Instruction("S1", ['*', '', 'R']))
    states["S1"].add(TM.Instruction("S1", ['0', '', 'R']))
    states["S1"].add(TM.Instruction("S2", ['1', '', 'R']))
    states["S1"].add(TM.Instruction("N", ['#', '', 'S']))
    
    states["S2"] = set()
    states["S2"].add(TM.Instruction("Y", ['1', '', 'S']))
    states["S2"].add(TM.Instruction("S1", ['0', '', 'R']))
    states["S2"].add(TM.Instruction("N", ['#', '', 'S']))

    return states

def parseMachineCode(states, code):
    '''
        Parses input string code into TM states(node, edge in a weighed graph)
        @param states: A directed graph of TM states, stored as python dict
        @param code: Machine code for TM, format: 
            "[current state] [read] [target state] [write] [pointer movement]"
            [read] can consist of multiple chars separated by comma
            [write] can have at most 1 character
            if [read] or [write] is empty, put a single comma ',' there
    '''
    code = code.split(' ')

    if code[0] not in states:
        states[code[0]] = set()
    
    reads = code[1].split(',')

    if code[3] == ',':  # this should work for now
        code[3] = ''

    for char in reads:
        states[code[0]].add(TM.Instruction(code[2], [char, code[3], code[4]]))


if __name__ == "__main__":

    #states = constructState()

    states = dict()

    parseMachineCode(states, "S1 *,0 S1 , R")
    parseMachineCode(states, "S1 1 S2 , R")
    parseMachineCode(states, "S1 # N , S")

    parseMachineCode(states, "S2 1 Y , S")
    parseMachineCode(states, "S2 0 S1 , R")
    parseMachineCode(states, "S2 # N , S")

    # This input has only '1', NO '11', ends at '#'
    tape = TM.Tape(['*', '0', '0', '1', '0', '0', '0', '0', '0', '0', '#', '1', '1']) 
    tape.print()
    findTwoConsecutiveOnes = TM.TuringMachine(tape, states)
    findTwoConsecutiveOnes.execute("S1")

    # This input has a '11'
    tapeGood = TM.Tape(['*', '0', '0', '0', '0', '0', '1', '1', '0', '0', '#'])
    tapeGood.print()
    findTwoConsecutiveOnes = TM.TuringMachine(tapeGood, states)
    findTwoConsecutiveOnes.execute("S1")

