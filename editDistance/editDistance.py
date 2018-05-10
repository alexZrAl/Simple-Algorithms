import numpy as np

def getEditDist(src, target):
    '''
        Compares the edit distance of string target with string src, in quadratic time
        @param src: The "sample" string
        @param target: The string we want to compare with the sample
    '''
    row = len(src) + 1
    col = len(target) + 1

    # chart stores the distance for each character
    chart = np.zeros((row, col))
    # calculate edit distances
    for i in range(0, row):
        chart[i][0] = i
    for j in range(0, col):
        chart[0][j] = j
    for i in range(1, row):
        for j in range(1, col):
            diff = (int)(src[i-1] != target[j-1])
            chart[i][j] = min(chart[i-1][j] + 1, chart[i][j-1] + 1, chart[i-1][j-1] + diff)
    
    return chart[len(src)][len(target)]

def constructWordMap(inputStr):
    '''
        Maps each sample word to its edit distance to the input word
        then return the mapping
        @param inputStr: input word provided by user
        @returns the mapping
    '''
    lstWords = list()
    for line in open("example.txt", "r"):
        lstWords.append(line.split()[0])

    wordDict = dict()
    for word in lstWords:
        wordDict[word] = getEditDist(word, inputStr)
    
    return wordDict

if __name__ == "__main__":
    '''
        Showcase with a given example of English words
    '''

    inputStr = input("Enter a word.  ")

    wordDict = constructWordMap(inputStr)

    # print output
    print("Results from shortest to longest edit distance: ")
    for k,v in sorted(wordDict.items(), key = lambda x : x[1]):
        print("Word: {} \t {}".format(k, v))
