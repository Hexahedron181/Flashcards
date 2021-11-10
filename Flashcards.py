import pickle
import csv
import random
import time

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
        lan = input("\n1. Term to Definition\n2. Definition to Term\n3. Back\n= ")
        if lan == "1":
            a = 1
            print("")
            testG(name, wordList)
        elif lan == "2":
            a = 1
            print("")
            testE(name, wordList)
        elif lan == "3":
            a = 1
            menu(name, wordList)
        else:
            print("Input invalid...")

def timeConvert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time = {0}:{1}:{2}".format(int(hours),int(mins),int(sec)))
            
def testG(name, wordList):
    words = []
    for key in wordList.keys():
        words.append(key)

    startTime = time.time()
        
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

    endTime = time.time()
    timeLapsed = endTime - startTime
    timeConvert(timeLapsed)

def getKey(name, val, wordList):
    for key, value in wordList.items():
        if val == value:
            return key
        
def testE(name, wordList):
    words = []
    for value in wordList.values():
        words.append(value)

    startTime = time.time()
    
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

    endTime = time.time()
    timeLapsed = endTime - startTime
    timeConvert(timeLapsed)

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
    print(i + 2, ". Create New Set")     

    while inp == 0:
        userInput = input("= ")
        if userInput == "" or int(userInput) > len(docs[0]) + 1 or int(userInput) <= 0:
            print("Invalid input...")   
        else:
            userInput = int(userInput)
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
    
