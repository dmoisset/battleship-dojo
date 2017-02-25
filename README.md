# A game of battleships

Hi! This material will show you how to build your own battleship game with python. This is an intermediate project, if
you still haven't done the beginner tutorials, you should try those first (or ask for some extra help with this one, that's
fine too!).

When programmers write a bigger program like this one, they don't normally sit down and write the whole thing from top to
bottom. The best way to do it is to solve just a part of the problem, run it and see that it works (or fix it if it doesn't)
and only then add new parts. So that's the way we'll build this too.

## A bit more about our battleship game

There are many ways and variants of the battleship game, so let me first clarify about the one we're building before writing code. Each player will have a 5 squares by 5 squares board like this one:

![Empty Board](https://raw.githubusercontent.com/dmoisset/battleship-dojo/explanation/board-empty.png)

Note that columns are letters (`A`, `B`, `C`, `D`, `E`) and rows are numbers (`1`, `2`, `3`, `4`, `5`); some people do it the opposite way, but this one also works.

One of the players will choose 5 squares where their battleships will go, any square is fine. for example, let's say our players are called Alice and Bob. Alice chooses 5 squares and marks an `X` on them to represent their battleships:

![Alice Board](https://raw.githubusercontent.com/dmoisset/battleship-dojo/explanation/board-alice.png)

She will choose board locations by typing in the column(letter) and row (number) of each battleship. For example, to enter
the battleship on the left, she will enter `A` and `4`, because the ship is in the column labeled `A` and the row labeled `4`.
She will have to do this 5 times, to tell the computer the location of her 5 battleships.

After this Bob can start guessing. Turn by turn he will type board locations (also by letter and number) and the computer will
tell him if it was a hit or a miss. Bob will start with a blank board (because he doesn't know where Alice's ships are), and after each guess he'll mark an `X` if there was a hit, or a dot (`.`) if there was a miss. For example if his guesses are `D4`, `C3`, `A2`, his board will look like this:

![Bob Board](https://raw.githubusercontent.com/dmoisset/battleship-dojo/explanation/board-bob.png)

In a normal game of battleships Bob would also would have his own ships and alice her guessing board, but to make the program shorter we will just make this simple version. A nice project for taking home is to modify this into the full game.

## A battleship board in python

The program we're writing will need to remember the board of each player. When a program has to remember something that means
that you have to store it in a variable; we'll call it `board`. But python variables can store numbers like `42` or text  like `"lazy dog"` in them, but they can not store battleship boards, or can they?

The trick the programmers use in this case is finding a way that they can turn something they want to remember (like a battleship board) into something that Python can understand. There are some tricks that we can use this time:

 * Each square in the board can be represented by a string: `' '` if the square is empty or `'X'` if there's a battleship in it.
 * Each row of 5 squares can be represented by a list of 5 strings like the one above
 * The board has 5 rows, so you can represent them as a list of lists like the one above (yes, you can pust a list inside another list!). 
 
 Let's do that. Create a new python file (for example `battleship.py`) and enter the following:

```python
# A board is a list of rows, and each row is a list of cells with either an 'X' (a battleship)
# or a blank ' ' (water)
board = [
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
]

```

That's an empty board!

Now, when the users enter a position like `C4`, we need to translate it to a specific location on the list. Remember that python lists count their position from zero, not from one. So we need to convert `A`, `B`, `C`, `D`, `E` to 0, 1, 2, 3, 4 for columns, and `1`, `2`, `3`, `4`, `5` to list positions 0, 1, 2, 3, 4 for rows (this may sound a bit confusing at first, don't worry if you don't follow and try the code). So `C4` would be the column with list position 2, and the row with list position 3, and we'll write that as `board[3][2]` . The row translation is easy (just substracting 1 from the original number), but converting letters to numbers is a bit more complicated. We'll use a dictionary, which works like a table to say which number value corresponds like a letter value, we can write it like this (add this to the bottom of your python file)

```python
# We want to refer to columns by letter, but Python accesses lists by number. So we define
# a dictionary to translate letters to the corresponding number. Note that Python lists start in
# zero, not in one!
letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
}
```
## Placing battleships on the board

Now let's make it possible to add 5 battleships to the empty board. Add this code to the bottom of your program:

```python
# We want 5 battleships, so we use a for loop to ask for a ship 5 times!
for n in range(5):
    print("Where do you want ship ", n + 1, "?")
    column = input("column (A to E):")
    row = input("row (1 to 5):")
    # columns are letters, so here we use the dictionary to get the number corresponding to the
    # letter
    column_number = letters_to_numbers[column]
    # The player enters numbers from 1 to 5, but we have to substract 1 to use python lists that
    # start on zero.
    row_number = int(row) - 1

    board[row_number][column_number] = 'X'

    # Show the board, one row at a time
    for row in board:
        print(row)
```
