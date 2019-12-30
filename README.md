# BIP39 vanity generator

This software helps you generate easy-to-remember BIP39 mnemonic codes for use
as Bitcoin wallets.

## Theory
For most of the mnemonic code, you can freely choose words from the BIP39
word list.
However, the last word contains a checksum, which is based on the first words.
This means that, once you have chosen the first words, you have a limited choice
of words from which you can choose the last word.
This software helps you: you provide the first words of the mnemonic code,
and the software returns a list of valid options for the last word.

## Security
The security of the resulting wallet depends entirely on how easy it is for an
attacker to guess the mnemonic code.
Please take into account that an attacker may know all kinds of things about
you, and may be able to use fast computers to try millions of combinations of
words per second.

Optimal security requires a completely random choice of words, but that
completely defeats the purpose of this software: you'd be better of generating
your wallet with other software.
Wallets generated with this software should be considered less secure than
other BIP39-based wallets.
On the other hand, this software allows you to use easier to remember mnemonic
codes.
So, in the trade-off between security and useability, this software is more on
the useability side.
It is recommended to only use it for low-value wallets, where it makes little
sense for attackers to put much effort in trying to guess the mnemomic code.

## Requirements
Python 3

## Usage
* Choose the first 11 words from the word list in `english.txt`
* Run vanity.py
* Enter the first 11 words, separated by spaces, and press Enter
* vanity.py displays the options for the 12th word



