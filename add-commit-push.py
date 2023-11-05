import os 
import sys

print("testing")
numOfArgs = len(sys.argv)
message = "update files"
print("Total Arguments Passed: " , numOfArgs)
if numOfArgs == 3: 
    if sys.argv[1] == "-m":
        print("number of arguments = 3 and p2 = -m")
        message = sys.argv[2]

print(message)



print("Add Commit Push") 
print("\ngit status")
os.system("git status")

force = False
for x in range(len(sys.argv)):
    if sys.argv[x] == '-f' : 
        force = True 


if force == False: 
    print("Continue with add commit push? (y) :")
    confirm = input()
    if confirm != "y":
        print("Canceling", confirm)
        quit()

 
print("\ngit add -A")
os.system("git add -A")

commitStatement = '\ngit commit -m "' + message + '"'
print(commitStatement)
os.system(commitStatement)

print("\ngit push")
os.system("git push")
