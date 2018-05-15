import TuringMachine as TM

def constructState():
    '''
        Construct a mapping of TM states and returns them
        (think of this as wiring an actual computer, what a pain in the back side)
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


def getStatesFromFile(filename):
    '''
        Use code from a file to configure the TM
        @param filename: a file with TM machine code
        @return states: formatted TM states
    '''
    states = dict()
    for line in open(filename, 'r'):
        line = line.strip("\n").split(' ')
        for i in range(0, len(line)):
            line[i] = line[i].strip("{").strip("}")
        if line[0] not in states:
            states[line[0]] = set()
        states[line[0]].add(TM.Instruction(line[2], [line[1], line[3], line[4]]))
    
    return states

if __name__ == "__main__":
    
    # construct turing machine
    states = getStatesFromFile("FindTwo1.txt")
    findTwoConsecutiveOnes = TM.TuringMachine(states)
    
    # This input has only '1', NO '11', ends at '#'
    print("Tape 1, does not have substring \'11\':")
    tapeNo = TM.Tape(['*', '0', '0', '1', '0', '0', '0', '0', '0', '0', '#', '1', '1']) 
    tapeNo.print()
    findTwoConsecutiveOnes.execute(tapeNo, "S1")

    # This input has a '11'
    print("Tape 2, does have substring \'11\':")
    tapeGood = TM.Tape(['*', '0', '0', '0', '0', '0', '1', '1', '0', '0', '#'])
    tapeGood.print()
    findTwoConsecutiveOnes.execute(tapeGood, "S1")

