from flask import Flask
import random


def readWords(wordFile='dict'):
    f = open(wordFile, 'r')
    words = [l.strip() for l in f.readlines()]
    f.close()
    return words


def readPunct(punctFile='punctuation'):
    f = open(punctFile, 'r')
    punct = [l.strip() for l in f.readlines()]
    f.close()
    return punct


app = Flask(__name__)


@app.route("/size/<int:numWords>")
def genPasswordOfLength(numWords):
    return genPassword(numWords=numWords)


@app.route("/")
def genPassword(numWords=3):
    rand = genPassword.random

    words = genPassword.words
    punct = genPassword.punct

    password = words[rand.randint(0, len(words)) - 1]
    for i in range(1, numWords):
        password += punct[rand.randint(0, len(punct)) - 1]
        password += words[rand.randint(0, len(words)) - 1]

    return password

if __name__ == '__main__':
    genPassword.words = readWords()
    genPassword.punct = readPunct()
    genPassword.random = random.SystemRandom()
    app.run()

# uncomment this and comment out above to convert to a cmdline app
#if __name__ == '__main__':
#    genPassword.words = readWords()
#    genPassword.punct = readPunct()
#    genPassword.random = random.SystemRandom()
#    print genPassword()
