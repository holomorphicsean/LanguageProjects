#os logistics
import os
os.chdir("C:\users\holom\Documents\Python\Language")
import sys

#to handle unicode characters
import codecs

#bring in file
file_name = "working on everything"

f = codecs.open(file_name + ".txt", 'r', encoding = 'utf-8')

#initialize lists
everything = []
french = []
german = []
spanish = []
italian = []
english = []
collection = []

#
for el in f:
    everything.append(el.split('/'))
f.close()

#check if all elements are valid, and no elements are missing
valid = set()
for i in everything:
    valid = set(map(len,everything))

#make sure all elements have length 5
if valid != set([5]):
    print "Program did not work; the following elements are inconsistent:"
    i = 0
    for el in everything:
        if len(el) != 5:
            print i + 1, " ", el
        i += 1
    sys.exit(0) #end the program

#transfer elements into our language lists
english = [ row[0] for row in everything]
french = [ row[1] for row in everything]
german = [ row[2] for row in everything]
spanish = [ row[3] for row in everything]
italian = [ row[4] for row in everything]
collection = [ french, german, spanish, italian]

#now, write into separate files. We will append our original file name with the
#language we're writing it in
languages = ["french", "german", "spanish", "italian"]
i = 0 #iterator over collection
for l in languages:
    fw = codecs.open(file_name + "_" + l + ".txt",'w', encoding = 'utf-8')
    #loop over every word
    for j in range(len(english)):
        fw.write(english[j].rstrip().lstrip() + ", " + collection[i][j].rstrip().lstrip() + "\n")
    fw.close()
    i += 1
    print l + " has been written"

print "Done!"
    
