import pprint # Module for pretty printing
message="Hello, my name is Ieshaan Saxena, I am 19-years-old"
char={}
for character in message:
    char.setdefault(character,0)
    char[character]+=1
pprint.pprint(char)
