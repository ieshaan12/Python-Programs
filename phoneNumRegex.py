import re
phoneNumRegex=re.compile(r'(\d\d\d-\d\d\d-\d\d\d\d)+')
Str="My number is 845-186-2621, also my second number is 913-701-8661."
gr=phoneNumRegex.findall(Str)
print(gr)
