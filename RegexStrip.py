#! python
# Regex Version of Strip()
import re
def RegexStrip(mainString,charsToBeRemoved=None):
    if(charsToBeRemoved!=None):
        regex=re.compile(r'[%s]'%charsToBeRemoved)#Interesting TO NOTE
        return regex.sub('',mainString)
    else:
        regex=re.compile(r'^\s+')
        regex1=re.compile(r'$\s+')
        newString=regex1.sub('',mainString)
        newString=regex.sub('',newString)
        return newString
    
Str='   hello3123my43name is antony    '
print(RegexStrip(Str))
