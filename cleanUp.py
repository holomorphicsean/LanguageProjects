#os logistics
import os
my_path = "C:\users\holom\Documents\Python\Language"
os.chdir(my_path)

import sys

#Get all of the files which have _ at the name of their end, and we're
#going to delete them

to_delete = [ f for f in os.listdir(my_path) if '_'  in f ]

#just leave if there's nothing there
if to_delete == []:
    print "Nothing to be done"
    sys.exit(0)

#now delete files
for d in to_delete:
    os.remove(d)
    

