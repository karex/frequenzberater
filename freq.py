#!/usr/bin/python
import sys
import re

ver = "0.1"

print("FrequenzBerater (FrBr) v" + ver)
print("Using Python " + sys.version + "\n")

def error_exit(error):
  print("(FrBr Error): " + error)
  sys.exit()

if sys.version_info[0] < 3:
  error_exit("Must be using Python 3. Try py -3!")
  
try:
  inputfile = sys.argv[1]
except BaseException:
  error_exit("Specify the input file in the first argument.")
try:
  outputfile = sys.argv[2]
except BaseException:
  error_exit("Specify the output file in the second argument.")
  
try:
  f = open(inputfile, 'r')
except BaseException:
  error_exit('Cannot open input file for reading: ' + inputfile)
else:
  print("Input file:  ", inputfile)
  f.close()
try:
  f = open(outputfile, 'w')
except BaseException:
  error_exit('Cannot open output file for writing: ' + outputfile + ' (Maybe open?)')
else:
  print("Output file: ", outputfile)
  f.close()


dict = {}

def get_key(elements):
  return elements[1].replace("$", "") + "-" + re.sub(r"_(.*)", "", elements[2].replace("\n", ""))

print("Building dictionary", end="", flush=True)

with open("dict.tsv", encoding="utf8", mode="r") as f:
  lines = f.readlines()
  for line in lines:
    elements = line.split("\t")
    key = get_key(elements)
    dict[key] = elements[0]
    if (len(dict) % 100000 == 0):
      print(".", end="", flush=True)
  f.close()

print("\nDictionary built with", len(dict), "lemmas.\n")

linecount = 0
errcount = 0

with open(outputfile, encoding="utf8", mode="w") as outputf:
  with open(inputfile, encoding="utf8", mode="r") as inputf:
    lines = inputf.readlines()
    for line in lines:
      elements = line.split("\t")
      key = get_key(elements)
      if (key in dict):
        outputf.write(dict[key] + "\t" + line)
      else:
        print("No dictionary entry for:", key)
        outputf.write("?" + "\t" + line)
        errcount = errcount + 1
      linecount = linecount + 1
    print("\nFrBr run finished.\nProcessed", linecount, "lines.\nNo dictionary entry for", errcount, "lemmas.\nBye!")
    inputf.close()
  outputf.close()
