import os
import sqlite

def createDatabase(db):
    sequences = getSequencesToStore()
    db.create_table()
    db.insert_sequences(sequences)
    db.commit()

def updateDatabase(db):
    sequences = getSequencesToStore()
    db.insert_sequences(sequences)
    db.commit()

def deleteDatabase(db):
    db.close()
    os.remove("storedSequences.db") 

def getSequencesFromDatabase(db):
    sequences = db.get_sequences()
    return sequences

def testSequence(db):
    try:
        testSequence = getTestSequence("input.txt")
        storedSequences = getSequencesFromDatabase(db)

        maxAlignmentScore = 0
        species = ""
        gene = ""

        for entry in storedSequences:
            storedSequence = entry[2]
            alignmentScore = alignSequences(storedSequence, testSequence)
            if alignmentScore > maxAlignmentScore:
                maxAlignmentScore = alignmentScore
                species = entry[0]
                gene = entry[1]

        print(f"\nThe highest alignment score is {maxAlignmentScore} for {species} | {gene}")
    except FileNotFoundError:
        print("\nError: file \"input.txt\" not found. Please ensure input file is named properly\n")

def getTestSequence(fileName): 
    with open(fileName) as f:
        myList = f.read().splitlines()

    string = ""
    for line in myList:
        string += line

    return string

def getSequencesToStore():
    try:
        sequences = []
        tempList = []
        
        with open("dbSequences.txt") as f:
            lines = f.read().splitlines()

        sequence = ""
        for line in lines:
            if line:
                if line[0] == ">":
                    tempString = line[1:].split("|")
                    tempList.append(tempString[0])
                    tempList.append(tempString[1])
                else:
                    sequence += line
            else:
                tempList.append(sequence)
                sequence = ""
                entry = tuple(tempList)
                tempList.clear()
                sequences.append(entry)

        tempList.append(sequence)
        entry = tuple(tempList)
        sequences.append(entry)
        return sequences
    except FileNotFoundError:
        print("\nError: file \"dbSequences.txt\" not found. Please ensure input file is named properly\n")

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
    return (count/sequenceLength) * 100

def confirmDatabase(db):
    test = db.check_table_exists()
    return test

def main(): 
    while True:
        db = sqlite.Database()
        print("Please select an option:")
        print("1) Create a new database")
        print("2) Add sequence/sequences to current database")
        print("3) Delete current database")
        print("4) Test input sequence for species and gene identification")
        print("5) Exit")
        choice = input("")

        if choice == "1":
            if not confirmDatabase(db):
                createDatabase(db)
                print("\nDatabase successfully created!\n")
            else:
                print("\nError: database already exists!")
                print("Please delete current database before creating another\n")
        elif choice == "2":
            if confirmDatabase(db):
                updateDatabase(db)
                print("\nDatabase successfully updated!\n")
            else:
                print("\nError: no database was found")
                print("Please create a new database\n")
        elif choice == "3":
            if confirmDatabase(db):
                deleteDatabase(db)
                print("\nDatabase successfully deleted\n")
            else:
                print("\nError: no database was found")
                print("Please create a new database\n")
        elif choice == "4":
            if confirmDatabase(db):
                testSequence(db)
                print()
            else:
                print("\nError: no database was found")
                print("Please create a new database\n")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print(f"\n{choice} is not a valid command")
            print("Please select an option from the menu\n")

if __name__== "__main__" :
    main()