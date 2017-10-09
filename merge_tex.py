#usage python merge_tex.py inFile.tex outFile.tex

import re,sys

inFile = sys.argv[1]
outFile = sys.argv[2]

infile = open(inFile, "r")
filew = open(outFile, "w")


def paste_text(filepath):
    subfile = open(filepath,"r")
    mergefiles(subfile)
    subfile.close()

def mergefiles(file):
    for line in file.readlines():
        #find input lines that are not commented
        if(line.find("\\input") > -1  and (line.find("%") < 0 or line.find("%") > 1)):
            m = re.search("\input{(.+?)}", line)
            filepath = m.group(1)
            #add tex extension is missing
            if (filepath.find(".tex") < 0):
                filepath+= ".tex"
            paste_text(filepath)
        else:
            filew.write(line)


mergefiles(infile)

infile.close()
filew.close()
