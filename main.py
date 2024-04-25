import sqlite
db = sqlite.Database()

def createDatabase():
    # call getSequencesToStore function
    # sequences will be a list of tuples to pass to database
    sequences = getSequencesToStore("cv19spike.txt")
    db.create_table()
    db.insert_sequences(sequences)
    db.commit()

def updateDatabase():
    sequences = getSequencesToStore("filename")
    db.insert_sequences(sequences)
    db.commit()

def deleteDatabase():
    pass

def getSequencesFromDatabase():
    sequences = db.get_sequences()
    return sequences

def testSequence():
    testSequence = getTestSequence("input.txt")
    storedSequences = getSequencesFromDatabase()

    maxAlignmentScore = 0
    species = ""
    gene = ""
    # iterate over storedStrings and take max alignment Score
    # update species and gene accordingly
    storedSequence = "ATCG"
    alignmentScore = alignSequences(storedSequence, testSequence)

    # return alignmentScore, species, and gene
    print (f"The alignment score is {alignmentScore}")

def getTestSequence(fileName): 
    with open(fileName) as f:
        myList = f.read().splitlines()

    string = ""
    for line in myList:
        string += line

    return string

# add each entry to a tuple and append the tuple to sequences list
# return the sequences list of tuples
def getSequencesToStore(fileName):
    sequences = []
    currentEntry = ()

    with open(fileName) as f:
        myList = f.read().splitlines()

    # will insert spaces to signal stop entry and append to sequences

    return sequences

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
    while True:
        print("Please select an option:")
        print("1) Create a new database")
        print("2) Add sequence/sequences to current database")
        print("3) Delete current database")
        print("4) Test input sequence for species and gene identification")
        print("5) Exit")
        choice = input("")

        if choice == "1":
            # include test if database already exists
            createDatabase()
            print()
            print("Database successfully created!")
            print()
        elif choice == "2":
            # include test if database already exists
            updateDatabase()
            print()
            print("Database successfully updated!")
            print()
        elif choice == "3":
            # include test if database already exists
            deleteDatabase()
            print()
            print("Database successfully deleted")
            print()
        elif choice == "4":
            # include test for database present with error message if not
            testSequence()
            print()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print()
            print(f"{choice} is not a valid command")
            print("Please select an option from the menu")
            print()

if __name__== "__main__" :
    main()