#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve,pyperclip,os,sys

mcbShelf=shelve.open('mcb')

#TODO:Read Contents from the command line
if len(sys.argv)==3:
    if sys.argv[1].lower()=='save':
        mcbShelf[sys.argv[2]]=pyperclip.paste()
    elif sys.argv[1].lower()=='delete':
        del mcbShelf[sys.argv[2]]
elif len(sys.argv)==2:
    if sys.argv[1].lower()=='list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    elif sys.argv[1].lower()=='delete':
        for i in mcbShelf.keys():
            del mcbShelf[i]
#MultiClipBoard.py delete 
        
    
#TODO:Do operation according to command line argument

mcbShelf.close()
