# Ultimate Battleships
**Ultimate Battleships** is Python terminal game, which runs in the Code Institute mock terminal in Heroku.

This game is made, so that two player can play against each other. They take turns, gama host places battleships on the board, after all battleships are placed, player guesses where those ships are on the board.

[Here is the live version of my **Ultimate Battleships** project](https://battleship1993.herokuapp.com/)

![Screen sizes](/images/screen.png)

## How to play
My Ultimate Battleships is based on classic battleships game.  
This version is played:
- Game host enters five battleship locations 
- In the board ship location is marked `X`
- After all ship all placed, player overtakes control and guesses ship locations
- If player guesses wrong location, on the board it is marked `/`
- When all five ships are destroyed, game is over

## Features
### Existing Features
- Board creation
 - Ships are placed on board by host manualy:
  - First host selects column from A to H
  - Then, selects row from 1 to 8
  - Repeats this steps five times

![Board creation](/images/boardcreation.png)  

- Player guesses ship location in the same way host creates board
  - Selects column from A to H
  - Selects row from 1 to 8
  - Guessin continues until all five ships are destroyed

![Game goal](/images/gameover.png) 

- Input validation 
  - Column input validation is checking for letter from A to H. Ignores if letter is entered in lowercase

![Column validation](/images/invalidcolumn.png)

  - Row validation checks for number in the input

![Row validation](/images/invalidcolumn.png)

### Future Features
- Add guesses counting

### Testing
I had manually tested this project by doing following:
 - Passed the code through a PEP8 Pyhon code checker with no faults
 - Given invalid inputs: letters and numbers that are out of range
 - Tested in my local terminal and Code institute Heroku terminal

### Bugs 
- No bugs were noticed

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