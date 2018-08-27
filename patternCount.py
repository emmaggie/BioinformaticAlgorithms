import utilities, math, cProfile, timeit
import numpy as np

def patternCount(text, pattern):
    '''Input:
            text:       a long string, e.g. genome sequence
            pattern:    a short string, e.g. motif
        Output: count of <pattern> occurrences in <text>
    '''

    count = 0
    for idx in range(0 ,len(text)-len(pattern)+1):
        if pattern == text[idx : idx+len(pattern)]:
            count +=1
    return count

def frequentWords(text, k):
    """
    Input:
          text:   a long string, e.g. genome sequence
           k: an integer, size of the kmer
          Output: a concatenated string with most
    """
    frequentPatterns = []
    count = []
    for idx in range(len(text)-k+1):
        pattern = text[idx : idx+k]
        count.append(patternCount(text, pattern))

    maxCount = max(count)

    for i in range(len(text)-k+1):
        if count[i] == maxCount:
            frequentPatterns.append(text[i:i+k])
    frequentPatterns = np.unique(frequentPatterns)

    #for pattern in frequentPatterns:
    #    sys.stdout.write(pattern+"\t")
    #sys.stdout.write("\n")
    #print(frequentPatterns)
    finalString = "\t".join(frequentPatterns)

    return finalString

def symbolToNumber(symbol):
    symbolToNumberDict = {'A':0, 'C':1, 'G':2, 'T':3}
    return symbolToNumberDict[symbol]

def numberToSymbol(index):
    numberToSymbolDict = {0:'A', 1:'C', 2:'G', 3:'T'}
    return numberToSymbolDict[index]

def quotient(index, base=4):
    return math.floor(index/base)

def remainder(index, base=4):
    return math.floor(index%base)

def patternToNumber(pattern):
    if pattern == "":
        return 0
    symbol = pattern[-1]
    prefix = pattern[:-1]
    return 4*patternToNumber(prefix) + symbolToNumber(symbol)

def numberToPattern(index, k):
    if k==1:
        return numberToSymbol(index)
    prefixIndex = quotient(index,4)
    r = remainder(index,4)
    symbol = numberToSymbol(r)
    prefixPattern = numberToPattern(prefixIndex,k-1)
    return prefixPattern+symbol

def computingFrequencies(text, k):
    frequencyArray = np.zeros(4**k, dtype=int)
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        j = patternToNumber(pattern)
        frequencyArray[j] += 1
    frequencyArray = list(map(str,list(frequencyArray)))
    return frequencyArray#" ".join(list(frequencyArray))

def fasterFrequentWords(text, k):
    frequentPatterns = []
    frequencyArray = computingFrequencies(text, k)
    #print(len(frequencyArray))
    #print(frequencyArray)
    maxCount = max(frequencyArray)
    #print(maxCount)
    for i in range(4**k):
        if frequencyArray[i] == maxCount:
            #print(maxCount)
            pattern = numberToPattern(i, k)
            #print(i, frequencyArray[i], maxCount)
            frequentPatterns.append(pattern)
    finalString = "\t".join(frequentPatterns)
    return finalString

def findingFrequentWordsBySorting(text, k):
    frequentPatterns = []
    count = np.ones(len(text)-k+1, dtype=int)
    index = np.zeros(len(text)-k+1, dtype=int)
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        index[i]=patternToNumber(pattern)
    #print(index)
    sortedIndex = np.sort(index)
    #print(sortedIndex)
    for i in range(1, len(text)-k+1):
        if sortedIndex[i]==sortedIndex[i-1]:
            #print(sortedIndex[i], sortedIndex[i-1])
            count[i] = count[i-1]+1
    maxCount = max(count)
    #print(maxCount)

    for i in range(len(text)-k+1):
        if count[i] == maxCount:
            pattern = numberToPattern(sortedIndex[i], k)
            frequentPatterns.append(pattern)
    return frequentPatterns

def reverseComplement(string):
    dictOfComp = {"A":"T",
                  "T":"A",
                  "C":"G",
                  "G":"C"}
    result = []
    for base in string:
        result.append(dictOfComp[base])
    #print(string)
    #print(result)
    result.reverse()
    #print(result)
    return "".join(result)

def patternFinder(pattern, genome):
    startCoord = []
    for i in range(len(genome)-len(pattern)+1):
        if genome[i:i+len(pattern)] == pattern:
            startCoord.append(i)

    return " ".join(map(str, startCoord))

def patternFinderRegEx(pattern, genome):
    pass



def main():
    ###codeChallenge1
    #text =   utilities.FileParser(utilities.CliParser().parseTheCli()).getInputLine1()
    #pattern = utilities.FileParser(utilities.CliParser().parseTheCli()).getInputLine2()
    #print(patternCount(text, pattern))
    #frequentWords('ACTGACTCCCACCCC ', 3)
    ###codeChallenge2
    #print(frequentWords("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4))
    #print(symbolToNumber('A'))
    #print(patternToNumber('AGT')) #11
    #print(patternToNumber("GGACCAGAATGCCTTGTCC")) #173175365557

    #print(quotient(619))
    #print(remainder(38))

    #print(numberToPattern(45,4)) #AGTC
    #print(numberToPattern(7103, 11))
    #print(computingFrequencies('ACGCGGCTCTGAAA', 2))

    #print(frequentWords('ACTGACTCCCACCCC', 3)) #CCC
    #print(fasterFrequentWords('ACTGACTCCCACCCC', 3)) #CCC

    #print(frequentWords("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4)) #CATG GCAT
    #print(fasterFrequentWords("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4)) #CATG GCAT
    #cProfile.run('frequentWords("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4)')
    #cProfile.run('fasterFrequentWords("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4)')
    #print(findingFrequentWordsBySorting("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4))
    #print(reverseComplement("AAAACCCGGT"))
    pass
if __name__ == "__main__":
    main()