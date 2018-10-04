# saytex
Saytex is a CLI that utilizes different voices to act out a script.

# Background
Mac OS X has a terminal command called 'say' which converts text to audible speech which can be found [here](https://ss64.com/osx/say.html).
There are also many voices to choose from which we can specify in our command.
```
say --voice=Alex "Hi, this is Alex speaking."
say --voice=Victoria "Now Victoria is speaking."
```

# Input
First we need to find a collection of well-formatted transcripts. We can use episode transcripts of SpongeBob Squarepants which are publicly available [here](http://spongebob.wikia.com/wiki/Category:Episode_transcripts).
We will use ["Chocolate with Nuts"](http://spongebob.wikia.com/wiki/Chocolate_with_Nuts/transcript) as our input example.

# Generating a saytex directory
We can generate a saytex directory by doing the following:
```
$ # saytex.py <input-file> <output-directory>
$ saytex.py choco_with_nuts_transcript.txt saytex_choco
```

# Playing a saytex directory
After a saytex directory has been generated, we can play it whenever we want:
```
$ # play.py <input-directory>
$ play.py saytex_choco
```

# Implementation
This was implemented in the span of several hours so the code is not very readable in its current state. Some major refactoring at some point in the future.
