#! python
#STRONG PASSWORD PROGRAM
import re, pyperclip


pw_compare_lower=re.compile(r'[a-z]')
pw_compare_upper=re.compile(r'[A-Z]')
pw_compare_digit=re.compile(r'[0-9]')
gr=str(input())
def Checker(gr):
    if len(gr)<8:
        return 0
    if pw_compare_lower.search(gr)==None:
        return 0
    if pw_compare_upper.search(gr)==None:
        return 0
    if pw_compare_digit.search(gr)==None:
        return 0
    return 1
if (Checker(gr))==1:
    print("Strong Password")
elif (Checker(gr))==0:
    print("Weak Password")
