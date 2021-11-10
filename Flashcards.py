import pickle
import csv
import random

def inpWords(name, wordList):    
    while True:
        german = input("\nTerm: ")
        if german == "":
            break
        else:
            english = input("Definition: ")

        repeat = input("Right? ")
        if repeat == "":
            wordList[german] = english.capitalize()
        else:
            print("Overwriting last input...")
    if "test" in wordList:
        del wordList["test"]
    else:
        file = open(name.lower() + ".txt", "wb")
        pickle.dump(wordList, file)
        file.close()
    return

def testWords(name, wordList):
    div = 1
    a = 0
    listLen = len(wordList)
    for i in range(listLen):
        a += 1
        if a == 10:
            div =+ 1
            
    num = int(listLen / div)
    print("\n", num, "words selected.\n")
    test(num)

def language(name, wordList):
    a = 0
    while a == 0:
        lan = input("\nWhat language?\n1. Term to Definition\n2. Definition to Term\n= ")
        if lan == "1":
            a = 1
            print("")
            testG(name, wordList)
        elif lan == "2":
            a = 1
            print("")
            testE(name, wordList)
        else:
            print("Input invalid...")
            
def testG(name, wordList):
    fails = []
    words = []
    for key in wordList.keys():
        words.append(key)
        
    while len(words) > 0:
        a = random.randint(0, len(words) - 1)
        num = words[a]
        print(num, end=" = ")
        userInp = input()
        if userInp== "":
            menu(name, wordList)
        elif userInp == wordList[num]:
            print("Corret!\n")
            words.remove(num)
        else:
            print("Incorrect...\nCorrect answer (", wordList[num], ")\n")
            fails.append(num)
                    
    while len(fails) > 0:
        a = random.randint(0, len(fails) - 1)
        num = fails[a]
        print(num, end=" = ")
        userInp = input()
        if userInp == "":
            menu(name, wordList)
        elif userInp == wordList[num]:
            print("Corret!\n")
            fails.remove(num)
        else:
            print("Incorrect...\nCorrect answer (", wordList[fails[a]], ")\n")

def getKey(name, val, wordList):
    for key, value in wordList.items():
        if val == value:
            return key
        
def testE(name, wordList):
    fails = []
    words = []
    for value in wordList.values():
        words.append(value)
        
    while len(words) > 0:
        a = random.randint(0, len(words) - 1)
        num = words[a]
        print(num, end=" = ")
        userInp = input()
        ans = getKey(name, num, wordList)
        if userInp == "":
            menu(name, wordList)
        elif userInp == ans:
            print("Corret!\n")
            words.remove(num)
        else:
            print("Incorrect...\nCorrect answer (", ans, ")\n")
            fails.append(num)
                    
    while len(fails) > 0:
        a = random.randint(0, len(fails) - 1)
        num = fails[a]
        print(num, end=" = ")
        userInp = input()
        if userInp == "":
            menu(name, wordList)
        elif userInp == wordList[num]:
            print("Corret!\n")
            fails.remove(num)
        else:
            print("Incorrect...\nCorrect answer (", wordList[fails[a]], ")\n")

def outputList(name, wordList):
    print("")
    for key, value in wordList.items():
        print(key, "=", value)

def menu(name, wordList):
    
    while True:
        print("\n-----", name, "-----\n\n1. Input New Words\n2. Flashcard Test\n3. Print Words\n4. Main Menu", end="\n= ")
        activity = input()
        if activity == "1":
            inpWords(name, wordList)
        elif activity == "2":
            language(name, wordList)
        elif activity == "3":
            outputList(name, wordList)
        elif activity == "4":
            mainMenu()
        else:
            print("Input invalid please try again...\n")


# MAIN CODE ================================================

def mainMenu():
    
    wordList = {}
    docs = []

    with open('docNames.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            docs.append(row)

    docsLen = len(docs[0])
    inp = 0

    print("\nWhat set do you want to use?\n")

    for i in range(docsLen):
        print(i + 1, ".", docs[0][i])
    print(i + 2, ". create new set")     

    while inp == 0:
        userInput = int(input("= "))
        if userInput > len(docs[0]) + 1:
            print("Invalid input...")
        else:
            inp = 1

    if userInput != i + 2:
        document = docs[0][userInput - 1] + ".txt"

        with open(document, 'rb') as handle:
            data = handle.read()

        wordList = pickle.loads(data)
        menu(docs[0][userInput - 1].upper(), wordList)
        
    elif userInput == i + 2:
            
        dictionary = {"test" : "one"}
        name = input("What would you like to name your set: ")
        docName = name.title() + ".txt"

        fileDoc = open(docName, 'wb')
        pickle.dump(dictionary, fileDoc)
        fileDoc.close()
        docs[0].append(name)
        with open('docNames.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(docs[0])
        mainMenu()





mainMenu()
    
