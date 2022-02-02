#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 18:34:54 2022

@author: YouCanCallMeAll

Wordle!

What is wordle? It's a game where you have six chances
to guess a five letter word. If you fail to guess the 
word after your sixth guess, the game ends.

The UI for the game is a 5 L x 6 H grid. You type
your five letter word guess and the letters in 
the word populate on the UI. After you enter your guess,
the UI updates by coloring the five tiles. Green tiles
mean that the word contains that letter and that
the letter is in the correct position in the word.
A yellow tile means that the word contains that letter
but that the letter is in the wrong position. Lastly,
a grey tile means that the letter is not in the word.

If a player guesses all five letters in their correct
position, all five tiles in that row turn green and 
the game ends.

Inspired by: https://towardsdatascience.com/wordle-solver-using-python-3-3c3bccd3b4fb
"""
class Wordle:
    def __init__(self, word, rows=6, letters=5):
        self.g_count = 0
        self.word = word
        self.rows = rows
        self.letters = letters
        self.board = [['' for _ in range(letters)] for _ in range(rows)]
        self.colors = [['' for _ in range(letters)] for _ in range(rows)]
        self.alph = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# is_end function determines if game is over
    def is_end(self):
        if self.board[-1] != ['' for _ in range(self.letters)]:
            return True
        else:
            r = self.game_result()
            if r[0] == True:
                return True
            else:
                return False

# game_result determines the outcome of the game by returning a tuple
    def game_result(self):
        win = (False, 99)
        for i, r in enumerate(self.board):
            if self.word == ''.join(r):
                win = (True, i)
                break
        return win

# update_board updates board with latest guess    
    def update_board(self, u_inp):
        for i, s in enumerate(str(u_inp).upper()):
            self.board[self.g_count][i] = s
            if self.word[i] == s:
                self.colors[self.g_count][i] = 'G' #Correct place and letter
            elif s in self.word:
                self.colors[self.g_count][i] = 'Y' #Wrong place but letter in word
            else:
                self.colors[self.g_count][i] = 'B' #Letter not in word
        self.g_count += 1

# valid_guess determines if the player’s guess is valid or not
    def valid_guess(self, u_inp):
        if len(u_inp) == 5 and False not in [False for s in str(u_inp).upper() if s not in self.alph]:
            return True
        else:
            return False

