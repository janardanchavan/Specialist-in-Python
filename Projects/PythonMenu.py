import os
import pyttsx3 as pyt
os.system('cls')

print()
print("------ Welcome to my Python Menu World!------")
print()
print("    How would you like to proceed: ")
print("\n\t1. Enter program name\n\t2. Enter program number:")
pyt.speak("Welcome to Python Menu Programming. How would you like to proceed?")
print("\n\tEnter your choice: ",end="")
method = int(input())

while True:
    if method == 1:
        print("\n    Enter the program name from the below list: \n")
        optTxt = True
    else:
        print("\n    Enter the program number from the below list: \n")
        optTxt = False

    opt_list = ["Create New Directory","Open Notepad", "Open Chrome", "Open Paint Brush", "Open Calculator","Exit"]

    for i, item in enumerate(opt_list, start=1):
        print("\t", i, item)

#print("\n\tEnter option: ",end="")
#opt = input()

    if optTxt == True:
        Pcmd = input("\n\tEnter command name: ")
        
        if ("create" in Pcmd or "Create" in Pcmd) and ("directory" in Pcmd or "Directory" in Pcmd):
            DirName = input("\tEnter directory name: ")
            os.system("mkdir " + DirName)

        elif (("Open" in Pcmd or "open" in Pcmd) and ("notepad" in Pcmd or "Notepad" in Pcmd)) or ("notepad" in Pcmd or "Notepad" in Pcmd):
            os.system("notepad")

        elif (("Open" in Pcmd or "open" in Pcmd) and ("chrome" in Pcmd or "Chrome" in Pcmd)) or ("chrome" in Pcmd or "Chrome" in Pcmd):
            os.system("chrome")

        elif (("Open" in Pcmd or "open" in Pcmd) and ("mspaint" in Pcmd or "Mspaint" in Pcmd or "paint" in Pcmd or "Paint" in Pcmd)) or ("mspaint" in Pcmd or "Mspaint" in Pcmd or "paint" in Pcmd or "Paint" in Pcmd):
            os.system("mspaint")

        elif (("Open" in Pcmd or "open" in Pcmd) and ("Calculator" in Pcmd or "calculator" in Pcmd)) or ("Calculator" in Pcmd or "calculator" in Pcmd):
            os.system("calc")

        elif "exit" in Pcmd or "Exit" in Pcmd:
            os.system("exit()")
            break;

        else:
            print("\n\tInvalid option.")

    else:
        Pcmd = int(input("\n\tEnter program option: "))
        
        if Pcmd == 1:
            DirName = input("\tEnter directory name: ")
            os.system("mkdir " + DirName)

        elif Pcmd == 2:
            os.system("notepad")

        elif Pcmd == 3:
            os.system("chrome")

        elif Pcmd == 4:
            os.system("mspaint")

        elif Pcmd == 5:
            os.system("calc")

        elif Pcmd == 6:
            os.system("exit()")
            break

        else:
            print("\n\tInvalid option.")

    cnt = input("\n    Do you wnat to continue (y/n): ")
    if cnt == 'n' or cnt == 'N':
        break
        
    
