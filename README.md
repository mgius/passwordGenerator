# Secure Password Generator

Generates secure but easily rememberable passwords by selecting N words
randomly from a dictionary and N-1 punctuation marks from a set list and
combining them into a long, unique password that is extremely difficult to
crack.

## How the hell is this secure?
The provided dictionary file is generated from wamerican-small.  The
dicionary was filtered for words without punctuation of at least length 5 and
converted to lowercase. 

> grep -P '^\w{5,}$' american-english-small | tr [:upper:] [:lower:] > dict

This results in 38465 words, or over 15 bits of randomness per word.

The provided punctuation file contains 8 punctuation marks for 3 bits of randomness.

A password consisting of 3 words and two punctuation marks results in a
password with 15 * 3 + 2 * 3 = 51 bits of randomness (actually, its a bit
more but I'm rounding down to make it look worse than it really is).

## English Please!
You make your password secure by making it hard to guess.  The way you
determine how hard a password is to guess is by the possible numbers of
passwords that your password could possibly be.  A three word and two
punctuation mark password using the default dictionary and punctuation list
contains 2^51 different possible passwords.

This means that an attacker has to go through a list of
possibly 2^51 (2 quadrillion or 2 million billion) to find yours, even if
they have access to this entire program and its dictionaries.  If they
don't know that you're using this program, you now have a 30+ character
password they have to go through.  Good luck cracking that!

## Shouldn't I make the dictionary bigger?
You can, but it doesn't actually add that much more security to the system
because you have to double the dictionary size to add another bit of
randomness to the equation.  I like keeping the punctuation list small
because punctuation marks are harder to remember than english words.
