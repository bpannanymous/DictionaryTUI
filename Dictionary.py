#===
#import libraries
#===
import Functions #functions library
from pathlib import Path #relative directory referencing
import time #delaying library
import random #random number library
import os
import shutil

#===
#log directory
#===
#logs directory variable
PARENT=Path("Logs")
#make log directory if non existent
PARENT.mkdir(parents=True,exist_ok=True)


#===
#operational functions
#===
def Perform(action,subdir):
    #if exiting
    if action=='N':
        #do nothing
        pass
    #otherwise
    else:
        #list/select active document
        File=Functions.Select(subdir)
        #TUI space buffer
        print('')
        Functions.Line(20)
        #add term
        if action=='A':
            #open selected file as addable
         with open(File,"a") as file:
                while True:
                    #request and add new term
                    Functions.Add(file,'Term: ')
                    #request and add definition
                    Functions.Add(file,'Definition: ')
                    #ask if they would like to add another term
                    answer=Functions.ContinueAdd()
                    #if they would like to add another
                    if answer=='Y':
                        #pass to next iteration
                        pass
                    #if they would not like to add another
                    else:
                        #end the loop
                        break
        #delete term
        elif action=='D':
            #open selected file as readable
            with open(File,"r") as file:
                #read all lines and assign them to a list
                All=file.readlines()
                #iterate over list
                for i in range(len(All)):
                    #if it is on an odd line
                    if i%2==0:
                        #print but remove newline character
                        print(All[i].strip())
                    #otherwise
                    else:
                        #ignore
                        pass
            #store number of terms in current document
            length=len(All)/2
            #ask what lines to delete
            delete=input('Term to DELETE: ')
            #check if the term exists
            for i in range(len(All)):
                if i>=len(All):
                    break
                else:
                    #if the term is found
                    if delete in All[i]:
                        #if it is a term
                        if i%2==0:
                            #list term and definition
                            print('')
                            print(All[i])
                            print(All[i+1])
                            #continuous loop
                            while True:
                                #ask for authorization
                                deleteQuestion=input('Would you like to delete the above term? Y or N ')
                                #if allowed to delete
                                if deleteQuestion=='Y':
                                    #TUI message
                                    print('Deleting',All[i])
                                    #delete term
                                    del All[i]
                                    #delete definition, which has now shifted down a slot
                                    del All[i]
                                    #increment counter by 1
                                    i+=1
                                    #1 second delay
                                    time.sleep(1)
                                    #resolved message
                                    print('The term was removed from your file')
                                    #end loop
                                    break
                                #if not allowed to delete
                                elif deleteQuestion=='N':
                                    #end loop
                                    break
                                #if the response is not valid
                                else:
                                    #error response
                                    print('Invalid Response. Please Try Again.')
            #open file as writeable
            with open(File,"w") as file:
                #write new updated list to the document
                file.writelines(All)
            pass

        #search term
        elif action=='S':
            #ask and assign search keyword
            keyword=input('Search Keyword: ')
            Functions.Line(20)
            #open selected file as readable
            with open(File,"r") as file:
                #read all lines and assign them to a list
                All=file.readlines()
                #iterate over list
                for i in range(len(All)):
                    #if the keyword is found in that list element
                    if keyword in All[i]:
                        #if it is a term
                        if i%2==0:
                            #print the current and next element (term and definition)
                            print(All[i])
                            print(All[i+1])
                        #if it is a definition
                        else:
                            #print previous and current element (term and definition)
                            print(All[i-1])
                            print(All[i])
                        #print TUI break
                        Functions.Line(20)
                        #if not found in that list element
                    else:
                        #do nothing
                        pass
            pass
        #list terms
        elif action=='L':
            #open selected file as readable
            with open(File,"r") as file:
                #read all lines and assign them to a list
                All=file.readlines()
                #iterate over list
                for i in range(len(All)):
                    #print the element
                    print(All[i])
                    #if it is a definition
                    if i%2!=0:
                        Functions.Line(10)
                        #if it is a term
                    else:
                        #do nothing
                        pass


#reviews flashcards
def Review(dictionary,sequence):
    #listed order
    if sequence=='L':
        while True:
            #open selected file as readable
            with open(dictionary,"r") as file:
                #read all lines and assign them to a list
                All=file.readlines()
                #iterate over entire length of list, taking only even numbers
                for i in range(0,len(All),2):
                    #show term
                    Functions.Line(10)
                    print('TERM/QUESTION:')
                    Functions.Space(2)
                    print(All[i])
                    Functions.Space(1)
                    #request clicking enter to continue
                    input('ENTER to see definition/answer')
                    print('')
                    Functions.Space(1)
                    print(All[i+1])
                    Functions.Space(1)
                    #ask if they would like to continue
                    select=Functions.ContinueReview()
                    #if they would like to continue
                    if select=='':
                        #next flashcard
                        pass
                    #if they would like to exit
                    else:
                        break
                if select=='E':
                    break
    #randomized order
    else:
        while True:
            #open selected file as readable
            with open(dictionary,"r") as file:
                #read all lines and assign them to a list
                All=file.readlines()
                #max value
                maxi=int(len(All)-1)
                #generate a random integer to select a card
                RandomNumber=random.randint(0,maxi)
                #if the number is even
                if RandomNumber%2==0:
                    #do nothing
                    pass
                #if the number is odd:
                else:
                    #subtract it by one so it is even
                    RandomNumber-=1
                #show term
                Functions.Line(10)
                print('TERM/QUESTION:')
                Functions.Space(2)
                print(All[RandomNumber])
                Functions.Space(1)
                #request clicking enter to continue
                input('ENTER to see definition/answer')
                Functions.Space(2)
                print(All[RandomNumber+1])
                Functions.Space(1)
            #ask if they would like to continue
            select=Functions.ContinueReview()
            #if they would like to continue
            if select=='':
                #continue as currently is
                pass
            else:
                break

#deleting dictionary
def DelDict(ActiveDirectory):
    while True:
        #list dictionaries
        Functions.ListFiles(ActiveDirectory)
        #request deletion assurance
        dele=Functions.Continue('Would you like to delete a dictionary? Yes (Y) or No (N)?: ','Y','N')
        #if does not want to continue
        if dele=='N':
            #end loop
            break
        #if does want to continue
        else:
            #request file input
            File=Functions.Input(ActiveDirectory)
            #request confirmation
            confirm=Functions.Continue('Are you sure you would like to delete ['+File+']? Yes (Y) or No (N)?: ','Y','N')
            #if does not want to delete
            if confirm=='N':
                #end loop
                break
            #if wants to continue
            else:
                #create relative path to file
                file_path=os.path.join(File)
                #response message and delay
                print('Deleting ',File,' . . .')
                time.sleep(1)
                #delete document
                os.remove(file_path)
                #response message and delay
                print('File successfully deleted')
                time.sleep(1)

#creates dictionary
def NewDict(ActiveDirectory):
    while True:
        #list current dictionary
        files=Functions.ListFiles(ActiveDirectory)
        #request creation assurance
        create=Functions.Continue('Would you like to create a new dictionary? Yes (Y) or No (N)?: ','Y','N')
        #if does not want to continue
        if create=='N':
            #end loop
            break
        #if does not want to continue
        else:
            #request new file name
            FileName=input('Filename: ')
            #add txt suffix to name
            FileName+='.txt'
            #check if proposed filename is already used
            if FileName not in files: #if file does not exist
                #request confirmation
                confirm=Functions.Continue('Are you sure you would like to create ['+FileName+']? Yes (Y) or No (N)?: ','Y','N')
            else: #if file already exists
                #overwrite request
                confirm=Functions.Continue('['+FileName+'] already exists. Would you like to overwrite this dictionary? Yes (Y) or No (N)?: ','Y','N')
            #if does not want to delete
            if confirm=='N':
                #end loop
                break
            #if wants to continue
            else:
                #make file path
                FilePath=ActiveDirectory / FileName
                #output message to denote file creation
                print('Creating Dictionary...')
                #1 second delay
                time.sleep(1)
                #briefly opens file as writeable
                with open(FilePath,"w") as file:
                    pass
                print(FileName, 'successfully created')
                time.sleep(1) #1 second delay

#deleting archive
def DelArc(ActiveDirectory):
    while True:
        #list archives
        Functions.ListDir(ActiveDirectory)
        #request deletion assurance
        dele=Functions.Continue('Would you like to delete a dictionary? Yes (Y) or No (N)?: ','Y','N')
        #if does not want to continue
        if dele=='N':
            #end loop
            break
        #if does want to continue
        else:
            #request file input
            File=Functions.InputDir(ActiveDirectory)
            #request confirmation
            confirm1=Functions.Continue('Are you sure you would like to delete ['+File+']? This will delete all dictionaries located inside of it. Yes (Y) or No (N)?: ','Y','N')
            #if does not want to delete
            if confirm1=='N':
                #end loop
                break
            #if wants to continue
            else:
                #continue loop
                pass
            #second confirmation request
            confirm2=Functions.Continue('This will delete all dictionaries in it permanently. Are you sure? Yes (Y) or No (N) ','Y','N')
            #if does not want to delete
            if confirm2=='N':
                #end loop
                break
            #if wants to continue
            else:
                #create relative path to file
                file_path=os.path.join(File)
                #response message and delay
                print('Deleting ',File,' . . .')
                time.sleep(1)
                #delete document
                shutil.rmtree(file_path)
                #response message and delay
                print('Archive successfully deleted')
                time.sleep(1)

#creates dictionary
def NewArc(ActiveDirectory):
    while True:
        #list current archives
        archives=Functions.ListDir(ActiveDirectory)
        #request creation assurance
        create=Functions.Continue('Would you like to create a new archive? Yes (Y) or No (N)?: ','Y','N')
        #if does not want to continue
        if create=='N':
            #end loop
            break
        #if does not want to continue
        else:
            #request new file name
            Archive=input('New Archive Name: ')
            #check if proposed filename is already used
            if Archive not in archives: #if file does not exist
                #request confirmation
                confirm=Functions.Continue('Are you sure you would like to create ['+Archive+']? Yes (Y) or No (N)?: ','Y','N')
            else: #if file already exists
                #overwrite request
                confirm=Functions.Continue('['+Archive+'] already exists. Would you like to overwrite this archive? Yes (Y) or No (N)?: ','Y','N')
            #if does not want to delete
            if confirm=='N':
                #end loop
                break
            #if wants to continue
            else:
                #make file path
                DirectoryPath=ActiveDirectory / Archive
                #output message to denote file creation
                print('Creating Archive...')
                #1 second delay
                time.sleep(1)
                #creates directory
                Path(DirectoryPath).mkdir()
                print(Archive, 'successfully created')
                time.sleep(1) #1 second delay



#===
#looped execution
#===
#ask for initial operation
path=Functions.ArchiveStart()
while True:
    if path=='S':
        Directory=Functions.SelectDir(PARENT)
        answer=Functions.Start()
        while True:
            #requested to review
            if answer=='R':
                #list/select active dictionary
                File=Functions.Select(Directory)
                #order of reviewing dictionary
                order=Functions.Order()
                #review
                Review(File,order)
                #ask for desired operation before reiterating while loop
                answer=Functions.Start()
            #requested to delete
            elif answer=='D':
                #delete dictionary
                DelDict(Directory)
                #ask for desired operation before reiterating while loop
                answer=Functions.Start()
            #requested to create
            elif answer=='N':
                #create dictionary
                NewDict(Directory)
                #ask for desired operation before reiterating while loop
                answer=Functions.Start()
            #requested to modify
            elif answer=='M':
                #iterative#request user operation
                action=Functions.Action()
                #read and react to selection
                Perform(action,Directory)
                #check if they would like to continue
                decision=Functions.Continue('Would you like to continue and/or perform another edit operation? Yes (Y) or No (N)?: ','Y','N')
                #if they would like to continue
                if decision=='Y':
                    #do not change current answer
                    pass
                #if they would not like to continue
                else:
                    #ask for desired operation before reiterating while loop
                    answer=Functions.Start()
            #requested to leave
            else:
                #original start menu
                path=Functions.ArchiveStart()
                #exit archive
                break

    elif path=='N':
        #create archive
        NewArc(PARENT)
        #start menu
        path=Functions.ArchiveStart()
    elif path=='D':
        #delete archive
        DelArc(PARENT)
        #start menu
        path=Functions.ArchiveStart()
    else:
        #exit app
        break
