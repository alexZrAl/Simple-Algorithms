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


if __name__ == "__main__":

    states = constructState()

    # This input has only '1', NO '11', ends at '#'
    tape = TM.Tape(['*', '0', '0', '1', '0', '0', '0', '0', '0', '0', '#', '1', '1']) 
    # This input has a '11'
    tapeGood = TM.Tape(['*', '0', '0', '0', '0', '0', '1', '1', '0', '0', '#'])

    # This TM decides if the input has a '11'
    # Says "YES" if one or more '11' exists, otherwise "NO"
    findTwoConsecutiveOnes = TM.TuringMachine(tape, states)
    findTwoConsecutiveOnes.execute("S1")

    findTwoConsecutiveOnes = TM.TuringMachine(tapeGood, states)
    findTwoConsecutiveOnes.execute("S1")

