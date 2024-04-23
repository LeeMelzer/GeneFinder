
# change getSequence to query database and return a list of stored strings
def getSequence(fileName): 
    with open(fileName) as f:
        myList = f.read().splitlines()

    string = ""
    for line in myList:
        string += line

    return string


def alignSequences(storedString, inputString):
    count = 0
    storedStringLength = len(storedString)
    inputStringLength = len(inputString)

    matrix = [[0 for x in range(storedStringLength)] for y in range(inputStringLength)]

    for i in range(inputStringLength):
        for j in range(storedStringLength):
            if (inputString[i] == storedString[j]):
                prev = 0
                if (i > 0 and j > 0):
                    prev += matrix[i-1][j-1]
                matrix[i][j] = 1+prev
                count = max(count, matrix[i][j])

    alignmentScore = getAlignmentScore(inputStringLength, count)

    return alignmentScore


def getAlignmentScore(sequenceLength, count):
    return (sequenceLength/count) * 100


def main(): 
    storedString = getSequence("cv19spike.txt")
    inputString = getSequence("input.txt")
    alignmentScore = alignSequences(storedString, inputString)

    print (f"The alignment score is {alignmentScore}")

if __name__== "__main__" :
    main()