# ConnectFourGame
Connect Four game with crude "AI" (lookahead assessment). Written in Spyder (Python 3.9.7).

How to Play:
1. Will need pygame package.
2. Import Files from this repository.
3. When executed, the "ConnectFourGUI.py" file will start the game between you and an AI opponent.
4. Choosing 1-6 on the keyboard will place a piece into the corresponding column.
5. When the game is won or is a tie, the GUI will disappear, and the terminal will display who won.

This was a personal project exploring the concepts of using recursion to create a crude AI system. In this game, a player will play against an AI with a lookahead of 2 moves, which means that the AI can "see" two moves ahead (the AI Player assumes that the opponent can only see one move ahead). However, by varying the lookahead variable passed to the AIPlayer when initialized, the AI can have any value for the lookahead, theoretically making the game harder.

I also began learning the pygame package, which included the GUI that the game is played on, as well as the keyboard input interpretation.

What I learned:
  The main takeaway was learning how to use Github to build repositories and publish my work. The actual project took time to figure out the recursion necessary for an AI, along with learning the modules of the pygame package.
