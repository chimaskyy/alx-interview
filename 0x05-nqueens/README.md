# N Queens

The “0x05. N queens” project is a classic problem in computer science and mathematics, known for its application of the backtracking algorithm to place N non-attacking queens on an N×N chessboard. To successfully complete this project, you will need to understand several key concepts and have access to resources that will help you grasp the necessary algorithms and techniques.

## Concepts Needed:
### Backtracking Algorithms:

* Understanding how backtracking algorithms work to explore all potential solutions to a problem and backtrack when a solution cannot be completed.
* [Backtracking Introduction](https://www.geeksforgeeks.org/introduction-to-backtracking-data-structure-and-algorithm-tutorials/)

### Recursion:

* Using recursive functions to implement backtracking algorithms.
* [Recursion in Python](https://realpython.com/python-thinking-recursively/)

### List Manipulations in Python:

* Creating and manipulating lists, especially to store the positions of queens on the board.
* [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)

### Python Command Line Arguments:

* Handling command-line arguments with the sys module.
* [Command Line Arguments in Python](https://docs.python.org/3.3/library/sys.html#sys.argv)

By studying these concepts and utilizing the resources provided, you will be equipped with the knowledge required to implement an efficient solution to the N queens problem using Python. This project not only tests programming and problem-solving skills but also offers an excellent opportunity to learn about algorithmic thinking and optimization techniques.

### Additional Resources
* [Mock Interview](https://www.youtube.com/watch?v=GneS80iYa7I)

## Question
The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

Usage: nqueens N<br>
If the user called the program with the wrong number of arguments, print Usage: nqueens N, followed by a new line, and exit with the status 1<br>
where N must be an integer greater or equal to 4<br>
If N is not an integer, print N must be a number, followed by a new line, and exit with the status 1<br>
If N is smaller than 4, print N must be at least 4, followed by a new line, and exit with the status 1<br>
The program should print every possible solution to the problem<br>
One solution per line<br>
Format: see example<br>
You don’t have to print the solutions in a specific order<br>
You are only allowed to import the sys module<br>
Read: [Queen](https://en.wikipedia.org/wiki/Queen_%28chess%29), [Backtracking](https://en.wikipedia.org/wiki/Backtracking)