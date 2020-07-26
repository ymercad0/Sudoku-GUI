#Sudoku

![PyGame][1] ![Python][2] ![License][3]

Sudoku game written in Python with the Pygame library 
to visualize the backtracking algorithm. 

Every time the program is run, a random, solvable board is created
and the user can attempt to solve it by clicking on the cells.
Entering a number into a grid will be entered as a tentative value. 
once the the user is sure that number is the correct entry, pressing the
enter key will attempt to input the number onto the board. Correct
answers will be permanently displayed while incorrect answers will be removed
and the incorrect counter shall begin to be displayed. Likewise,
values can be removed by pressing on the backspace or delete keys.
![Example 1][4]

If at any point the player decides to solve the board, the spacebar can be pressed.
This will commence a visual that demonstrates how the backtracking algorithm
is being applied in order to solve the board.
![Example 2][5]

##Controls
| Keys      | Actions                                            |
|-----------|----------------------------------------------------|
| `Left Click`   |Enters a value into that cell                  |
| `Backspace/Delete` | Deletes the number in that cell           |
| `Space`     | Solves the board via a backtracking algorithm visualizer|
| `h`       | Gives user a hint. Displays a random correct value on the board   |

##Requirements
In order to run the program, the following is required:
* Python 3 
* Pygame

Pygame can simply be installed from the command prompt by
running `pip install pygame` *or* `py -3.4 -m pip install pygame`
where `-3.4` should be replaced with your current version of Python. Alternatively,
you could download Pygame directly from their website.

##Downloading and running
After downloading and extracting the zip from the [releases][6] page, double
click on `sudoku_gui.py` to run the program. Alternatively, open it from an
IDE of choice.

[1]: https://img.shields.io/badge/pygame-1.9.6-red
[2]: https://img.shields.io/badge/python-3.6.6-blue
[3]: https://img.shields.io/badge/license-MIT-orange
[4]: https://i.imgur.com/Mmez8bz.gif "Entering values onto the board"
[5]: https://i.imgur.com/WMlvgxF.gif "Backtracking visualizer"
[6]: https://github.com/Mercrist/Sudoku-GUI/releases/tag/v1.0 "Download the program files"
