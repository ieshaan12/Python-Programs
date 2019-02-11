#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.
if __name__=="__main__":
    import pyperclip
    text=pyperclip.paste()

    lines=text.split('\n')
    for i in range(len(lines)):
        lines[i]='printf("'+lines[i]+'");'
    text='\n'.join(lines)
    pyperclip.copy(text)
