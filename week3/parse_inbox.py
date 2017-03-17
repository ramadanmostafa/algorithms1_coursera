import re

mbox_file = open("mbox.txt")
for line in mbox_file:
    line = line.rstrip()
    if re.search('ˆFrom:.+@', line) :
        print line
    if re.search('From:', line) :
        print line

import re
s = 'Hello from csev@umich.edu to cwen@iupui.edu about the meeting @2PM'
lst = re.findall('\S+@\S+', s) #[a-zA-Z0-9]\S*@\S*[a-zA-Z]
print lst
