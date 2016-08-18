#!/usr/bin/env python3
import sys
import os

name = sys.argv[1]
if not os.path.exists(name):
  print("file doesn't exists")
  sys.exit(1)
fobj = open(name, 'r')
for lines in fobj:
  print(lines)
fobj.close()

