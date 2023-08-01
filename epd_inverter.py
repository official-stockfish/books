#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 1 10:01:47 2023
@author: Shahin M. Shahin (peregrine)

Usage : python epd_inverter.py <INPUT_FILE.epd> <OUTPUT_FILE.epd>

Example : python epd_inverter.py endgames.epd endgames_black.epd

"""

import sys

def invert_case(char):
    return char.upper() if char == char.lower() else char.lower()

def flip_FEN(FEN):
    position, turn, castle, ep, *rest = FEN.split()
    position = '/'.join(''.join(invert_case(char) for char in row) for row in reversed(position.split('/')))
    turn = 'b' if turn == 'w' else 'w'

    if castle != '-':
        castle = ''.join(invert_case(char) for char in sorted(castle))
    
    if ep != '-':
        ep = list(ep)
        ep[1] = '3' if ep[1] == '6' else '6'
        ep = ''.join(ep)

    return ' '.join([position, turn, castle, ep] + rest)

def convert_epd(input_file, output_file):
    with open(input_file, 'r') as input_f:
        fen_lines = input_f.readlines()

    converted_fens = [flip_FEN(fen.strip()) for fen in fen_lines]

    with open(output_file, 'w') as output_f:
        for fen in converted_fens:
            output_f.write(fen + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python epd_inverter.py <INPUT_FILE.epd> <OUTPUT_FILE.epd>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        convert_epd(input_file, output_file)