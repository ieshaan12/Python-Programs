import re
#phoneNumRegex=re.compile(r'(\d\d\d-\d\d\d-\d\d\d\d)+')
phoneRegex = re.compile(r'''(
 (\d{3}|\(\d{3}\))? # area code
 (\s|-|\.)? # separator
 (\d{3}) # first 3 digits
 (\s|-|\.) # separator
 (\d{4}) # last 4 digits
 (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
 )''', re.VERBOSE)
Str="My number is 845-186-2621, also my second number is 913-701-8661."
gr=phoneRegex.findall(Str)
print(gr)
