#! python3
# Regex Search
import os,re
ListOfAllFiles=os.listdir(os.getcwd())
#print((ListOfAllFiles))
#print(os.getcwd())
UserRegex=str(input('Matching User Regex: '))
TextFiles=[]
for i in ListOfAllFiles:
    if i[-4:len(i)]==".txt":
        TextFiles.append(i)
Loc=os.getcwd()
regexCheck=re.compile(r'\\')
Loc=regexCheck.sub(r'\\\\',Loc)
#print(TextFiles)
j=0
for i in TextFiles:
    j+=1
    print(j,end=" ")
    print('File Name: '+i)
    Location=Loc+r'\\'+i
    readFile=open(Location,encoding='utf-8')
    contents=readFile.readlines()
    stringRegex=re.compile(UserRegex)
    for line in contents:
        if stringRegex.search(line):
            print(line)
    readFile.close()
    
