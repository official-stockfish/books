#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 10:01:47 2020
@author: stephane

Usage : python epd2pgn.py <NAME_OF_EPD_FILE>

Example : python epd2pgn.py endgames.epd

"""


import hashlib
import os
import sys

def epd_to_pgn(bookname):
    
   tmpname     = bookname + '-md5.txt'
   suffledname = bookname + '-suffled.txt'
   pgnname     = bookname.replace('.epd', '.pgn')
    
   # Calculate the md5 of each position in the epd file
   book = open(bookname)
   tmp = open(tmpname, "w")
   line = book.readline()
   while line :
       md5 = hashlib.md5(line.encode('utf-8')).hexdigest()
       tmp.write(md5 + ' ' + line)
       line = book.readline()
   tmp.close()
   book.close()
   
   # Sort by md5 keys and rewrite the positions
   # This gives a epd file with positions in random order
   suffled = open(suffledname, "w")
   with open(tmpname, 'r') as tmp:
      for line in sorted(tmp):
          suffled.write(line.split(' ', 1)[1])
   suffled.close()
   
   # Transform each line of the epd file in the pgn format
   pgn = open(pgnname, "w")
   with open(suffledname, 'r') as suffled:
      for line in suffled:
          pgn.write('[FEN "' + line[:-1] + '"]\n')
          pgn.write('[Result "1/2-1/2"]\n' )
          pgn.write('\n')
          pgn.write('1/2-1/2\n\n')
   pgn.close()
   
   # Clean up the temp files
   os.remove(tmpname)
   os.remove(suffledname)



if __name__ == "__main__":
   epd_to_pgn(sys.argv[1])
