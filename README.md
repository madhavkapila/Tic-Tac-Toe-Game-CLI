# TIC-TAC-TOE GAME
## A CLI based old-skool like tic-tac-toe game (with Multiplayer or Single Player)

This is a CLI based Tic-Tac-Toe game I developed as a free time project purely using python. 
In this game the user can play his/her school-time favourite tick-cross or X's and O's or Tic-tac-toe game with his/her friends or against a computer.

### Multi-Player Mode

In this mode a user can play against his/her friend for a timepass or enjoyment or just as a stress-buster. In this mode there is no algorithm so the person who plays most optimally and tactically wins the game. If both players play optimally then it leads to  a draw.

### Single-Player Mode

In this mode the player plays against the computer(also referred to as <b>AI</b> at some sites reffering to this game. In this mode the computer's playing technique is designed using an algorithm in such a way that Computer never loses. The only results of the game are either the computer wins or there is a draw.
The Algorithm used here is MinMax Algorithm also used in Computer vs. Human Chess Games. In this algorithm we can have only three options for computer/user based on symbol chosen. If computer choses symbol with number as 1 then it has following options:
Options       | Number associated
------------- | -----------------
Win           |  1
Draw          |  0
Lose          | -1

So we can use this rule table to design our Algo. If we give give the computer's symbol as 1 then we need to maximise score so that computer wins. Simultaneosly for user to win it wants to minimise score.
Similarly if computer choses symbol with number as -1 then it has following options:
Options       | Number associated
------------- | -----------------
Win           | -1
Draw          |  0
Lose          |  1

So in this case computer wants to minimise score in order to win. Simultaneosly user wants to maximise score in order to win.

So this MinMax algorithm in achieved using recursion which creates a structure looking like a tree where starting from leaf node we want to move score in such a MinMax way that reaching root we get MinMax accordingly as per the symbol chosen for computer.

So now as we got to know user cannot win :sweat_smile: , to make the child within him happy:smiley: by giving him the freedom to chose:
* To chose the symbol :negative_squared_cross_mark: or :o: for his/her whole game
* Whether he wants to start the game as 1st move or wnats the 2nd move by allowing Computer to start the game

## Below is an illustartion of my Game!!! :video_game:

### Multi-Player Mode

<details>
  <summary>
    Click to expand
  </summary>
Enter 1 for Single-Player game or 2 for Multi-Player Game: 2


Current State Of Board : 


\_ 	_ 	_ 	

\_ 	_ 	_ 	

\_ 	_ 	_ 	

Enter X's pos where you want to place it from [1-9]: 5




Current State Of Board : 


\_ 	_ 	_ 	

\_ 	X 	_ 	

\_ 	_ 	_ 	

Enter O's pos where you want to place it from [1-9]: 1


Current State Of Board : 


O 	_ 	_ 	

\_ 	X 	_ 	

\_ 	_ 	_ 	

Enter X's pos where you want to place it from [1-9]: 3




Current State Of Board : 


O 	_ 	X 	

\_ 	X 	_ 	

\_ 	_ 	_ 	

Enter O's pos where you want to place it from [1-9]: 8


Current State Of Board : 


O 	_ 	X 	

\_ 	X 	_ 	

\_ 	O 	_ 	

Enter X's pos where you want to place it from [1-9]: 9




Current State Of Board : 


O 	_ 	X 	

\_ 	X 	_ 	

\_ 	O 	X 	

Enter O's pos where you want to place it from [1-9]: 6


Current State Of Board : 


O 	_ 	X 	

\_ 	X 	O 	

\_ 	O 	X 	

Enter X's pos where you want to place it from [1-9]: 7




Current State Of Board : 


O 	_ 	X 	

\_ 	X 	O 	

X 	O 	X 	


Player 1 Won!

</details>

### Multi-Player Mode

<details>
  <summary>
    Click to expand
  </summary>
Enter 1 for Single-Player game or 2 for Multi-Player Game: 
1


What do you want to chose X or O: O

Computer:  X  Vs. You:  O 

Enter 1 to play 1(st) or 2 to play 2(nd): 1


Current State Of Board : 


\_       _       _ 

\_       _       _ 

\_       _       _ 


Enter  O 's pos where you want to place it from [1-9]: 
5


Current State Of Board : 


X       _       _ 

_       O       _ 

\_       _       _ 


Enter  O 's pos where you want to place it from [1-9]: 
7


Current State Of Board : 


X       _       X 

_       O       _ 

O       _       _ 


Enter  O 's pos where you want to place it from [1-9]: 
2


Current State Of Board : 


X       O       X 

_       O       _ 

O       X       _ 


Enter  O 's pos where you want to place it from [1-9]: 
6


Current State Of Board : 


X       O       X 

X       O       O 

O       X       _ 


Enter  O 's pos where you want to place it from [1-9]: 
9


Current State Of Board : 


X       O       X 

X       O       O 

O       X       O 


Draw!
</details>

