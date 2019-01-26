#! python3
# Mad Libs program to replace ADJECTIVE, NOUN, ADVERB, or VERB
import re,shelve

readFile=open('C:\\Users\\IESHAAN .LAPTOP-U40CT3MF\\AppData\\Local\\Programs\\Python\\Python36-32\\python-programs\\readFile.txt')
contents=readFile.read()
readFile.close()
print(contents)
content=contents.split()
print(content)
i=0
for contents in content:
    print(contents)
    if('ADJECTIVE' in contents):
        regex1=re.compile(r'ADJECTIVE')
        content[i]=regex1.sub(input('What is the ADJECTIVE?\nEnter:'),contents)
    elif ('NOUN' in contents):
        regex1=re.compile(r'NOUN')
        content[i]=regex1.sub(input('What is the NOUN?\nEnter:'),contents)
    elif ('VERB' in contents):
        regex1=re.compile(r'VERB')
        content[i]=regex1.sub(input('What is the VERB?\nEnter:'),contents)
    elif ('ADVERB' in contents):
        regex1=re.compile(r'ADVERB')
        content[i]=regex1.sub(input('What is the ADVERB?\nEnter:'),contents)
    i=i+1
contents=' '.join(content)
print(contents)
writeFile=open('C:\\Users\\IESHAAN .LAPTOP-U40CT3MF\\AppData\\Local\\Programs\\Python\\Python36-32\\python-programs\\readFile.txt','w')
writeFile.write(contents)
writeFile.close()
