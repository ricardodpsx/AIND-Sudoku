# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: With the naked twins technique we introduce a new rule or theorem that allow us to remove potencial values on the different
boxes of the Sudoku in order to reduce the search space. The more we reduce the search space, the faster the DPS will go.

We can think in the Naked Twins as an inferred rule that can be expressed as 
"Given the boxes A != B  in unit U where A = B = (a,b) there is no box c != A != B that contains a or b" (Excuse the lack of mathematical symbols)

So every time we enforce rules and make the the board change, the constraints on some boxes may change, so we need to propagate the constraint changes.

The more rules we find, the more rules we can apply to reduce the search space. That makes me think that if you encode the rules as predicates and you have
an algorithm that generates new theorems based on the initial predicates then you can apply all kind of auto generated constraints to reduce the search space.

The way it is solved in this case is that for every unit we find every possible pair of twins. As soon as a twin is found, the values in the twin ares removed 
   


# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
The sudoku problem is encoded in a clever way with the concepts of Units, and Boxes
We are just trying to find out values that We can put in the boxes that satisfy the constraints in the boxes and in the Units. So basically we have two types of general rules:
  Boxes: You have to put one value between 1 and 9
  Units: You can not use the same number twice
So Units can be whatever we want: diagonals, verticals, boxes, Circles, as long as you follow the rule exposed previously you
 just need to apply the same strategy of reducing the possible values in the Units by applying the rules and propagating the constraints on the boxes, finalizing with a DPS.

In this case I just had to add the two diagonals to the set of Units in lines 28 and 29

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.