#!/usr/bin/python
import re

with open("dict.tsv", encoding = "utf8", mode = "w") as outfile:
  with open("originaldict.tsv", encoding = "utf8", mode = "r") as infile:
    lines = infile.readlines()
    for line in lines:
      e = line.split("\t")
      if (not re.match(r"https?://", e[1])
      and not re.match(r"[\d:,./%\- ]*$", e[1])
      and not re.match(r"^www", e[1], re.IGNORECASE)
      and e[2] != "ukjent\n"
      and len(e[1]) < 40
      and len(e) == 3):
        outfile.write(line)
    infile.close()
  outfile.close()
  