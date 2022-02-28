import pickle
import csv
import random
import time
import os

def getKey(name, val, wordList):
    for key, value in wordList.items():
        if val == value:
            return key
        
def inpWords(name, wordList):    
    while True:
        german = input("\nTerm: ")
        if german == "":
            break
        else:
            english = input("Definition: ")
            while english == "" or english.title() in wordList.values():
                english = input("Definition: ")

        repeat = input("Right? ")
        if repeat == "":
            wordList[german.title()] = english.title()
        else:
            print("Overwriting last input...")
    if "test" in wordList:
        del wordList["test"]
    file = open(name.lower() + ".txt", "wb")
    pickle.dump(wordList, file)
    file.close()
    return

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
        if userInp == "":
            menu(name, wordList)
        elif userInp.title() == wordList[num]:
            print("Corret!\n")
            words.remove(num)
        else:
            print("Incorrect...\nCorrect answer (", wordList[num], ")\n")

    endTime = time.time()
    timeLapsed = endTime - startTime
    timeConvert(timeLapsed)
        
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
    keys = []
    values = []
    print("")
    for key in wordList.keys():
        keys.append(key)
    keys.sort()
    for i in range(0, len(keys)):
        print(keys[i], "=", wordList[keys[i]])
    if "test" in wordList.keys() and wordList["test"] == "one":
        print("This is the default input. It will be removed when another is added.")

def CSV(delName):    
    with open('docNames.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            docs1 = row
    csvfile.close()
    docs1.remove(delName.lower())
    with open('docNames.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(docs1)
    
def options(name, wordList):

    items = {}
    K = 1
    print("\n1. Delete input\n2. Delete entire set")
    while True:
        inp = input("= ")
        if inp == "1":
            while True:
                outputList(name, wordList)
                while True:
                    print("\nWhat would you like to delete? (input term or definition)")
                    delInp = input("= ")
                    if delInp == "":
                        options(name, wordList)
                    if len(wordList) == 1:
                        print("You cannot delete an item if it is the only item in a list.")
                        menu(name, wordList)
                    if delInp.title() in wordList.keys():
                        items[delInp.title()] = wordList[delInp.title()]
                    if delInp.title() in wordList.values():
                        K = getKey(name, delInp.title(), wordList)
                        items[K.title()] = delInp.title()
                    if len(items) > 1:
                        print("\nmore than one item had this input...")
                        outputList(name, items)
                        print("\nWhich item do you wish to delete? (input term)")
                        while True:
                            uInp = input("\n= ")
                            if uInp.title() in wordList.keys():
                                wordList.pop(uInp.title())
                                print("Deletion success...\n")
                                items = {}
                                K = 1
                                break
                            elif uInp == "":
                                options(name, wordList)
                            else:
                                print("Input invalid...")
                        break
                    elif len(items) == 1:
                        if K == 1:
                            K = delInp
                        K = K.title()
                        print("\nIs this the item you wish to remove?\n\n", K, "=", wordList[K])
                        inp = input("\n= ")
                        if inp != "" and inp[0].title() == "Y":
                            wordList.pop(K)
                            print("Deletion success...\n")
                            items = {}
                            K = 1
                    elif delInp == "":
                        options(name, wordList)
                    else:
                        print("Input invalid...")
                        
            file = open(name.lower() + ".txt", "wb")
            pickle.dump(wordList, file)
            file.close()
            break
        elif inp == "2":
            print("Are you sure you want to delete the entire set?\n(You can not undo this action)")
            uInp = input("\n= ")
            if uInp == "" or uInp[0].title() != "Y":
                break
            elif uInp[0].title() == "Y":
                os.remove(name.lower() + ".txt")
                CSV(name.title())
                mainMenu()
        elif inp == "3" or inp == "":
            menu(name, wordList)
        else:
            print("Input invalid")

def menu(name, wordList):
    
    while True:
        print("\n-----", name, "-----\n\n1. Input New Words\n2. Flashcard Test\n3. Print Words\n4. Main Menu\n5. Options", end="\n= ")
        activity = input()
        if activity == "1":
            inpWords(name, wordList)
        elif activity == "2":
            language(name, wordList)
        elif activity == "3":
            print("\n1. Print entire list\n2. Print the definition of a term")
            inp = input("= ")
            if inp == "1":
                outputList(name, wordList)
            elif inp == "2":
                while True:
                    inpTerm = input("Input Term: ")
                    if inpTerm.title() in wordList.keys():
                        print("\n",inpTerm.title(), "=", wordList[inpTerm.title()])
                        break
                    elif inpTerm == "":
                        menu(name, wordList)
                    else:
                        print("Input invalid...")
        elif activity == "4":
            mainMenu()
        elif activity == "5":
            options(name, wordList)
        else:
            print("Input invalid please try again...\n")
    

# MAIN CODE ================================================

def mainMenu():

    a = 0
    wordList = {}
    docs1 = []

    while True:
        try:
            with open('docNames.csv', 'r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    docs1 = row
                break
        except:
            with open('docNames.csv', 'w') as file:
                file.close()

                
    if len(docs1) > 0:
        docsLen = len(docs1)
        inp = 0

        print("\nWhat set do you want to use?\n")

        for i in range(docsLen):
            new = str(docs1[i]).title()
            print(i + 1, ".", new)
        print(i + 2, ". Create New Set")
        
    else:
        print("\nWhat set do you want to use?\n")
        print("1. Create New Set")
        i = 0
        a = 1
        docsLen = 0
        inp = 0

    while inp == 0:
        userInput = input("= ")
        if userInput.isdigit() == False:
            print("Input invalid...")
        elif userInput == "" or int(userInput) > len(docs1) + 1 or int(userInput) <= 0:
            print("Invalid input...")   
        else:
            userInput = int(userInput)
            inp = 1
        
    if userInput == i + 2 or a == 1:
            
        dictionary = {"test" : "one"}
        name = input("What would you like to name your set: ")
        docName = name.title() + ".txt"

        fileDoc = open(docName, 'wb')
        pickle.dump(dictionary, fileDoc)
        fileDoc.close()
        docs1.append(name)
        
        with open('docNames.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(docs1)
            
        mainMenu()

    elif userInput != i + 2:
        doc = str(docs1[userInput - 1].title())
        document = doc + ".txt"

        with open(document, 'rb') as handle:
            data = handle.read()

        wordList = pickle.loads(data)
        menu(doc.upper(), wordList)





mainMenu()
    
