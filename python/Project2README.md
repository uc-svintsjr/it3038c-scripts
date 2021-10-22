# Project 2  
#### Spooky Halloween Themed Guessing Game
##### Rules: You will be given a hidden Halloween themed word. You will have a total of six guesses. You can only guess one letter at a time. If you guess the correct letter you keep your guesses, if you guess the wrong letter you lose a guess. If you manage to lose all your guesses you lose. If you manage to decode the word while having spare guesses you win!<br>
I wrote this script because it's near Halloween time and my friends and family thought it was a fun idea for the season. The results of the project were hysterical, so I got my friends and family to run this program and some were more emotional than others. This program will test your luck and patience, some will succeed, some will fail. Enjoy!  <br><br>
Before you can run this Python script, which use the time and random modules, you will need to install them to properly execute this script. In the Visual Studio terminal run these two lines.<br>
``` 
pip install time 
```
```
pip install random
```
You will also need to download the wordslist file to be prompted your Halloween words. <br>Make sure your directory is correct on your local machine
```
python it3038-scripts/python/wordslist.txt
```
Now, from the it3038c-scripts directory, run the program using Python
```
python it3038-scripts/python/Project2.py
```
First, you'll be given a hidden message like so.
```
Hidden word is: ------------

Enter a letter (Guess #1):
```
Example Output for Loser.
```
Enter a letter (Guess #6): g
Letters Guessed: aeiouslg

Loser! The word was howl.
```
Example Output for Winner.
```
Enter a letter (Guess #6): l
Letters Guessed: aeiousprnqbdtl

Winner! The word was supernatural.
```
Once a match is over, you will be prompted to.
```
Press Enter to play again
```
