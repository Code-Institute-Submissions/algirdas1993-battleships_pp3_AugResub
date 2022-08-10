# Ultimate Battleships
**Ultimate Battleships** is Python terminal game, which runs in the Code Institute mock terminal in Heroku.

This game is made, so that two player can play against each other. They take turns, gama host places battleships on the board, after all battleships are placed, player guesses where those ships are on the board.

[Here is the live version of my **Ultimate Battleships** project](https://battleship1993.herokuapp.com/)

![Screen sizes](/images/am_i_responsive.png)

## How to play
My Ultimate Battleships is based on classic battleships game.  
This version is played:
- Player enters his/hers name
- Program randomly places five ships for player to guess the locations of them
- Board with the placed ships remains hidden from the user
- User can see the guessing board, remaining turn(shells) and how many ships are hitted
- User needs to choose row and column coordinates, on which he/she wants to attack
- In the board hitted ship location is marked `@`
- If player guesses wrong location, on the board it is marked `/`
- The guessing game continues until player hit all five placed ships or runs out of turns

## Features
### Existing Features
- Player name is entered in the beginning of the game
- Program capitalizes entered name
- Empty input is not exepted

![Player name input](/images/username_input.png)  

- Then program places five ships in random places
- This board remains hidden from the player

![Hidden board](/images/hidden_comp_board.png) 

- Player inputs row coordinates on which he/she wants to place his attack. 
  - Row coordinates input takes in integer from 1 to 8.
  - Input only except number in the range, does not except empty input.

![Row validation](/images/row_input.png)

- Player inputs column coordinates on which he/she wants to place his attack. 
  - Column coordinates input takes in letters from A to H 
  - Input only except letters in that range, is not case sensitive and does not except emty input

![Column validation](/images/column_input.png)

- In every turn player is informed about how many turns are left, and how many ships are hitted

![User game progress](/images/player_info.png)

- If player runs out of turns, message is printed with the guessing board

![Loss message](/images/loss.png)

- If player hits all five ships, message is printed with the guessing board

![Loss message](/images/win.png)

### Testing
I had manually tested this project by doing following:
 - Passed the code through a PEP8 Pyhon code checker with no faults
 - Given invalid inputs: letters and numbers that are out of range
 - Tested in my local terminal and Code institute Heroku terminal

### Bugs 
- Noticed a bug, which made empty input to crash the program. It was fixed 
by adding extra condition to a while loop. 

### Deployment
This project was deployed using Code Institute's mock terminal for Heroku
- Steps for deployment:
   - Fork this repository
   - Create a new Heroku app
   - Set the buildbacks to Python and NodeJS in that order
   - Link the Heroku app to the repository
   - Click on **Deploy**

### Credits
- Code Institute for the mock deployment terminal   