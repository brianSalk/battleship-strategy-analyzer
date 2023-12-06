# battleship-strategy-analyzer
Various simulations testing the efficiency of different battleship strategies
## Strategy 1 - random guessing
this strategy is the easiest to simulate but not very practical.  You have never played a game of battleship  
against a human who guessed at random the entire time because most people know that once you have hit an opponent ship  
your next guess should be adjacent to your last hit.
### Summary Statistics
If you just guess at ranom, you will hit all of your opponents ships after about *95.3* guesses.  
It will take you 100 guesses 17% of the time, which makes sense because there are 17 spaces that you need to hit.  
The standard deviation of guesses required to sink all opponent ships is *approximately 4.8*.  
## Strategy 2 - random guessing followed by optimal adjacent guessing
This strategy is significanly harder to simulate due to the very complex and unintuitive rules optimal adjacent guessing.  
This strategy starts off like the previous where the computer guesses coordinates at random, but once a ship is hit,  
the computer guesses adjacent coordiates from there.  Here are the rules of optimal adjacent guessing:  
* If you hit an opponents ship, guess one of the four adjacent coordinates.
  * if you are near the middle of the board it does not matter which adjacent coordinate you guess first
  * if you are near one of the edges of the board (within 5 holes) guess towards the center, so if you get a hit at (2,5), guess (3,5)
* keep guessing in that direction until you get a miss, sink a ship, or run out of space on the grid
* if you sink a ship the same size as the number of spaces you hit, go back to your default strategy to find the next ship
* if you sank fewer ships that the number of spaces you hit, start guessing in the opposite direction of your first hit, keep guessing in that direction until you miss, sink a ship or run out of space.
* after doing this, guess perpendiculare to each guess hit that was not part of a sink
* if your first adjacent guess after a hit was a miss, pick a non-opposite direction for your next guess (if you get a hit at (5,5), but (6,5) was a miss, do not guess (4,5) next.)
