#===
#import libraries
#===
import os


#===
#functions
#===

#list directories in log directory
def ListDir(ParentDirectory):
    thickLine(30)
    print('Current Archives')
    thickLine(30)
    print('')
    #assign all directories to a list
    directories=[f for f in os.listdir(ParentDirectory) if os.path.isdir(os.path.join(ParentDirectory,f))]
    #iterate over list
    for f in directories:
        print(f) #print list element
    print('')
    thickLine(30)
    print('')
    #return all directories
    return directories

#lists all files in log directory
def ListFiles(Directory):
    thickLine(30)
    print('Current Dictionaries')
    thickLine(30)
    print('')
    #assign all files in directory to a list
    files=[f for f in os.listdir(Directory) if os.path.isfile(os.path.join(Directory,f))]
    #iterate through directory, listing all files
    for f in files:
        print(f)
    print('')
    thickLine(30)
    print('')
    #return all files
    return files

#prints line
def Line(length):
    line='' #empty line string
    for i in range(0,length): #iterate over specified length
        line+='-' #elongate line string
    print(line)

#prints thick line
def thickLine(length):
    line='' #empty line string
    for i in range(0,length): #iterate over specified length
        line+='=' #elongate line string
    print(line)

#prints space
def Space(times):
    for i in range(0,times): #iterate over specified times
        print('') #print empty string

#asks for input directory
def InputDir(Parent):
    while True:
        #request and assign a directory
        Directory=str(input('Archive: '))
        #if the directory exists
        if os.path.exists(os.path.join(Parent,Directory))==True:
            #assign the directory name
            directory=os.path.join(Parent,Directory)
            #break the loop
            break
        #if directory does not exist
        else:
            #request it be re-entered
            print('Directory does not exist. Make sure your spelling is correct. Try again.')
    #return the directory
    return directory

#asks for input file
def Input(Directory):
    while True:
        #request and assign a file
        FileName=str(input("Dictionary: "))
        #if the file exist
        if os.path.exists(os.path.join(Directory,FileName))==True:
            #assign the filename
            File=os.path.join(Directory,FileName)
            #break the loop to advance
            break
        #if the file does not exist
        else:
            #request it be re-entered
            print('File does not exist. Make sure your spelling is correct. Try again.')
    #return the file name
    return File

#action selection
def Action():
    while True:
        #tui separation
        print('')
        thickLine(30)
        print('Option')
        thickLine(30)
        print('')
        #options string
        options=['Add Term (A)','Delete Term (D)','Search Term (S)','List Term (L)','Nothing (N)']
        #print options
        for i in range(len(options)):
            print(options[i])
        print('')
        Line(20)
        #ask what they would like to do
        action=str(input('Desired Action?: '))
        #check if the input was workable
        if action=='D' or action=='S' or action=='L' or action=='A' or action=='N':
            #break the loop
            break
        #if input not workable
        else:
            #request restatement of action
            print('Invalid Response. Please input a single, capitalized letter corresponding to the action you wish to complete')
    print('')
    #return the stored action
    return action

#archive selection menu
def ArchiveStart():
    while True:
        #clear terminal
        print("\033[2J\033[H", end="")
        #tui separation
        thickLine(30)
        print('Options')
        thickLine(30)
        print('')
        #options string
        options=['Select Archive (S)','New Archive (N)','Delete Archive (D)','List Archives (L)','Exit Application (E)']
        #print options
        for i in range(len(options)):
            print(options[i])
        print('')
        Line(20)
        #ask what they would like to do
        choice=str(input('Desired Action?: '))
        #check if the input was workable
        if choice=='S' or choice=='N' or choice=='E' or choice=='L' or choice=='D':
            #break the loop
            break
        #if input now workable
        else:
            #request restatemtn of action
            print('Invalid Response. Please input a single, capitalized letter corresponding to the action you wish to complete')
    print('')
    #clear terminal
    print("\033[2J\033[H", end="")
    #return the stored answer
    return choice

#start selection menu
def Start():
    while True:
        #clear terminal
        print("\033[2J\033[H", end="")
        #tui separation
        print('')
        thickLine(30)
        print('Modify Archive Options')
        thickLine(30)
        print('')
        #options string
        options=['Review Dictionaries (R)','Modify Dictionaries (M)','New Dictionary (N)','Delete Dictionary (D)','Exit Archive (E)']
        #print options
        for i in range(len(options)):
            print(options[i])
        print('')
        Line(20)
        #ask what they would like to do
        choice=str(input('Desired Action?: '))
        #check if the input was workable
        if choice=='R' or choice=='M' or choice=='E' or choice=='N' or choice=='D':
            #break the loop
            break
        #if input now workable
        else:
            #request restatemtn of action
            print('Invalid Response. Please input a single, capitalized letter corresponding to the action you wish to complete')
    print('')
    #clear terminal
    print("\033[2J\033[H", end="")
    #return the stored answer
    return choice

#asks if user would like to continue editing
def Continue(question,option1,option2):
    while True:
        #ask what they would like to do
        decision=str(input(question))
        #check if the input was workable
        if decision==option1 or decision==option2:
            #break the loop
            break
        #if input not workable
        else:
            #request restatement of action
            print('Invalid Response. Please input a single, capitalized letter corresponding to the action you wish to complete')
    #return the stored answer
    return decision

#asks if user would like to continue reviewing
def ContinueReview():
    Line(10)
    while True:
        #ask what they would like to do
        question=str(input('Next Flashcard [ENTER] or Exit (E): '))
        #check if input was workable
        if question=='' or question=='E':
            #break the loop
            break
        #if input not workable
        else:
            #request restatement of action
            print('Invalid Response.')
    #return the stored answer
    return question

#ask if user would like to continue adding
def ContinueAdd():
    while True:
        #ask what they would like to do
        x=str(input('Add Another Flashcard? Yes (Y) or No (N)?: '))
        #check if the input was workable
        if x=='Y' or x=='N':
            #break the loop
            break
        #if the input not workable
        else:
            #request restatement of action
            print('Invalid Response.')
    #return the stored answer
    return x

#lists/select directory
def SelectDir(ParentDirectory):
    #list all directories
    ListDir(ParentDirectory)
    #request directory input
    ChildDirectory=InputDir(ParentDirectory)
    #return selection
    return ChildDirectory

#lists/select file
def Select(directory):
    #list files in target directory
    ListFiles(directory)
    #request file input
    File=Input(directory)
    #return file
    return File

#adds term and asks if correct
def Add(document,phrase):
    while True:
        #ask for initial input
        answer=input(phrase)
        #combine answer to get one string
        question='Is ['+answer+'] correct? Y or N? '
        #reiterate and ask if input is correct
        ask=input(question)
        #if yes
        if ask=='Y':
            #write to file
            document.write(answer)
            document.write("\n")
            #end loop
            break
        #if no
        elif ask=='N':
            #pass to redo input
            pass
        #invalid input
        else:
            #return message
            print('Invalid Input, Please Try Again.')
            #pass to redo input
            pass

#order of reviewing
def Order():
    while True:
        #ask what they would like to do
        order=str(input('Whould you like to review in the listed order (L) or randomized (R)?: '))
        #check if the input was workable
        if order=='L' or order=='R':
            #break the loop
            break
        #if input not workable
        else:
            #request restatement of action
            print('Invalid Response. Please input a single, capitalized letter corresponding to the action you wish to complete')
    #return the stored answer
    return order

#ensures an empty name is not passed
def EdgeCase(string,prompt,character):
    while True: #iterate until specified otherwise
        if string=='': #if an empty string is passed
            print('Invalid input. Empty input cannot be accepted')
            string=input(prompt)
            string=RemoveCharacter(string,character)
        else: #if non-empty string is passed
            break #ignore and pass value
    return string #return value

#removes character
def RemoveCharacter(string,character):
    character=str(character)
    return string.replace(character,'') #return rectified string
