#! python
# Regex Version of Strip()
import re
def RegexStrip(mainString,charsToBeRemoved):
    if(charsToBeRemoved!=None):
        regex=re.compile(r'[%s]'%charsToBeRemoved)
        return regex.sub('',mainString)
    else:
        regex=re.compile(r'\s+')
        return regex.sub('',mainString)
    
Str='   hello3123my43name is antony    '
print(RegexStrip(Str,None))
