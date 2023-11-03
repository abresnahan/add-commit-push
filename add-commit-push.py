import os 
import sys

print("testing")
numOfArgs = len(sys.argv)
print("Total Arguments Passed: " , numOfArgs)
if numOfArgs == 3: 
    if sys.argv[1] == "-m":
        print("number of arguments = 3 and p2 = -m")
        message = sys.argv[2]


print(message)



print("Add Commit Push") 
print("\ngit status")
os.system("git status")

# credit W3C schools line 6-8
print("Continue with add commit push? (y):")
confirm = input()
if confirm != "y": 
    print("Canceling", confirm)
    quit()
 
print("\ngit add -A")
os.system("git add -A")
print("\ngit commit -m 'update files.'")
os.system("git commit -m 'update files.'")
print("\ngit push")
os.system("git push")
