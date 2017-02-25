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
tell him if it was a hit or a miss. Bob will start with a blank board (because he doesn't know where Alice's ships are), and after each guess he'll mark an `X` if there was a hit, or a dot (`.`) if there was a miss. For example if his guesses are `D4`, `C3`, `A2`, his board will look like.

![Bob Board](https://raw.githubusercontent.com/dmoisset/battleship-dojo/explanation/board-bob.png)

In a normal game of battleships Bob would also would have his own ships and alice her guessing board, but to make the program shorter we will just make this simple version. A nice project for taking home is to modify this into the full game.
