"""
Permits exploration of EXPRESSIONS, e.g. 3 + (5 * 2) and "hello" + "goodbye",
and NAMES and ASSIGNMENT, e.g.    n = n + 1

Authors: David Mutchler, Sana Ebrahimi, Mohammed Noureddine, Vibha Alangar,
         Matt Boutell, Dave Fisher, their colleagues, and
"""

import random
import math


###############################################################################
# TODO 1: Smile
###############################################################################

###############################################################################
# TODO 2:
#   Write a statement that prints your name
###############################################################################


###############################################################################
# Part 1: Numbers, Arithmetic, and Precedence.
###############################################################################

###############################################################################
# TODO: 3.
#   Uncomment the following and then run the program, paying close attention
#   to what gets printed.
#  _
#   Then type an example of your own for each of:
#        -- subtraction
#        -- division
#   and run the program, checking that what gets printed is what you expect.
###############################################################################

# print()
# print("_TODO 3:")
# print("4 + 8 evaluates to:   ", 4 + 8)
# print("7 * 10 evaluates to:  ", 7 * 10)
# print("1.53 + 8 evaluates to:", 1.53 + 8)

###############################################################################
# TODO: 4.
#   Uncomment the following and then run the program,
#   paying close attention to what gets printed.
###############################################################################

# print()
# print("_TODO 4:")
# print("(4 + 2) * 3 evaluates to:", (4 + 2) * 3)
# print("4 + (2 * 3) evaluates to:", 4 + (2 * 3))
# print("4 + 2 * 3   evaluates to:", 4 + 2 * 3)
# print("(4 - 2) + 3 evaluates to:", (4 - 2) + 3)
# print("4 - (2 + 3) evaluates to:", 4 - (2 + 3))
# print("4 - 2 + 3   evaluates to:", 4 - 2 + 3)

###############################################################################
# TODO: 5.
#   Uncomment the following and then run the program,
#   paying close attention to what gets printed.
###############################################################################

# print()
# print("_TODO 5:")
# print("2 ** 10  evaluates to:", 2 ** 10)
# print("10 ** 2  evaluates to:", 10 ** 2)
# print("2 ** 0.5  evaluates to:", 2 ** 0.5)
# print("10 ** -2  evaluates to:", 10 ** -2)
# print("10 ** -0.5  evaluates to:", 10 ** -0.5, "(do you see why?")

###############################################################################
# TODO: 6.
#   Type some expressions of your own choosing that use combinations of:
#     -- addition, subtraction
#     -- multiplication, division
#     -- exponentiation
#   using parentheses to make clear the order of operations.
#   Then run the program, checking that what gets printed is what you expect.
#  _
###############################################################################

# print()
# print("_TODO 6:")

###############################################################################
# Part 2: Exceptions: Syntax and Run-Time Errors.
###############################################################################

###############################################################################
# TODO: 7.
#   Uncomment the following and then run the program,
#   paying close attention to what gets printed.
#  _
#   Then comment-out the line that causes the syntax error.
#  _
#   Now type some other statement that causes a syntax error,
#   for example a statement that is missing a required parenthesis.
#   Run again to see the error-message from your syntax error,
#   and finally comment-out your statement to continue to the next _TODO.
###############################################################################

# print()
# print("_TODO 7:")
# This is crazy!  Python will make no sense of it!

###############################################################################
# TODO: 8.
#   Uncomment the following and then run the program,
#   paying close attention to what gets printed, especially the last red line.
#   Note that the error-output (in red) may (or may not) appear BEFORE the
#   ordinary output from previously executed PRINT statements.
#  _
#   Then comment-out the line that causes the run-time error.
###############################################################################

# print()
# print("_TODO 8:")
# print("3 + 2 evaluates to:", 3 + 2)
# print("3 / 0 evaluates to:", 3 / 0)

###############################################################################
# TODO: 9.
#   Uncomment the following and then run the program,
#   paying close attention to what gets printed, especially the last red line.
#   Again note that the error-output (in red) may PRECEDE ordinary output.
#  _
#   Then comment-out the first line that causes the run-time error
#   and run the program again to see the result of running the line below it.
###############################################################################

# print()
# print("_TODO 9:")
# print("3 / 'hello' evaluates to:", 3 / 'hello')

###############################################################################
# TODO: 10.
#   Type some expressions of your own choosing that cause error messages.
#   Then run the program, paying close attention to the last line
#   of each error message (in red).
#  _
###############################################################################

# print()
# print("_TODO 10:")

###############################################################################
# Part 3: Objects, Types, and Values.
###############################################################################

###############################################################################
# TODO: 11.
#   READ the following statements and PREDICT what they will produce as output.
#   Then, uncomment them and run the program, checking your predictions
#   and learning from any predictions that you got wrong
###############################################################################

# print()
# print("_TODO 11:")
#
# print("The type of   482      is:", type(482))
# print("The type of   48.203   is:", type(48.203))
# print('The type of   "blah blah blah"      is:', type("blah blah blah"))
# print("The type of   'blah blah blah'      is:", type('blah blah blah'))
# print("The type of   [4, 2, 9]      is:", type([4, 2, 9]))
# print("The type of   (4, 2, 9)      is:", type((4, 2, 9)))
# print("The type of   min     is:", type(min))
# print("The type of   'min'   is:", type('min'))
# print("The type of   min(4, 6, 2, 12, 10)    is:", type(min(4, 6, 2, 12, 10)))
# print("The type of   min(4, 6, 2.0, 12, 10)  is:", type(min(4, 6, 2.0, 12, 10)))


###############################################################################
# TODO: 12.
#   Type an expression that involves addition, subtraction and multiplication
#   (but NOT division, yet), using whole numbers (which are of type int).
#   Then run the program, checking that what gets printed is what you expect.
#  _
#   Next, repeat the above, but making just a single one of the numbers in
#   your expression a float, by appending a decimal point to it, like this:
#       instead of 2 (which is an int), write 2.0 (which is a float).
#  _
#  Finally, try division by uncommenting the following and then run the program,
#  paying close attention to what gets printed.  What do you notice about the
#  type that results from division, even if both arguments are  int  objects?
###############################################################################

# print()
# print("_TODO 12:")
# print("4.2 / 2.0 evaluates to:", 4.2 / 2.0)
# print("4.2 / 2   evaluates to:", 4.2 / 2)
# print("4 / 2     evaluates to:", 4 / 2)
# print("3 / 2     evaluates to:", 3 / 2)

###############################################################################
# TODO: 13.
#   Uncomment the following and then run the program,
#   paying close attention to what gets printed.
#  _
#  Then try more expressions involving the   //   and   %   operators
#  until you understand what those operators do.
###############################################################################

# print()
# print("_TODO 13:")
# print("17 // 5   evaluates to:", 17 // 5)
# print("17 % 5    evaluates to:", 17 % 5)

###############################################################################
# TODO: 14.
#   Uncomment the following and then run the program,
#   paying close attention to what gets printed.
#  _
#  Then try more expressions involving string arithmetic as needed, until you
#  understand what the  +   and   *   operators do when applied to strings.
###############################################################################

# print()
# print("_TODO 14:")
#
# print("hello" + "goodbye girl")
# print("big" * 20)
# print(("hello " + "goodbye ") * 4)

###############################################################################
# TODO: 15.
#   Type a statement that prints:
#     I'm not a bug, that's right!
#   and then run the program, checking that it printed the above sentence
#   (including the punctuation exactly as written above).
#  _
#   Then repeat the above for the sentence:
#     What does "yarborough" mean?
#  _
#   Then repeat the above for the sentence:
#     I'm on "pins and needles" about '"'".
#   Hint: consider using the   +   operator as part of your solution.
#  _
###############################################################################

# print()
# print("_TODO 15:")

###############################################################################
# Part 4: Names, Variables, and Assignment.
###############################################################################

###############################################################################
# TODO: 16.
#   Uncomment the following and then run the program,
#   paying close attention to what gets printed.
#  _
#   Then comment-out the line that causes the run-time error,
#   PREDICT what the subsequent lines will print,
#   and run again to check your predictions.
#  _
#   Finally, practice assignment as suggested by the examples below, that is:
#   choose your own names, given them values by using the assignment (=)
#   operator, and define new names by using expressions that include names
#   that you defined previously.
###############################################################################

# print()
# print("_TODO 16:")
# first_program = "Hello, world!"
# print(first_program)
# print(greeting)
#
# greeting = "Hello, earthlings"
# print(greeting)
# print(first_program + (greeting * 2))
#
# n = 3
# print(first_program * n)
# n = 2 * first_program
# print(n + greeting)

###############################################################################
# TODO: 17.
#   Uncomment the following and then run the program,
#   paying close attention to what gets printed.
#  _
#   Throughout this program, remember that error-output may (or may not)
#   PRECEDE ordinary output from previous PRINT statements.  Be sure to scroll
#   up to see if any error message (in red) appears higher up in the Console.
#  _
#   Then repeatedly:
#     -- comment-out the line that causes a run-time error
#     -- run again to see the output from the statements that follow it.
#   until you see the output from the last statement below,
#   noting its perhaps-surprising output.
#  _
#   Finally, try out your own assignment statements that yield run-time errors.
###############################################################################

# print()
# print("_TODO 17:")
# r = 0
# s = -9
# t = s / r
# y = "oops" + s
# u = math.sqrt(-2)
# v = (-2) ** 0.5
# print(v)

###############################################################################
# TODO: 18.
#   Uncomment the following and then run the program,
#   paying close attention to what gets printed.
#  _
#   Then comment-out the line that causes the run-time error,
#   PREDICT what the subsequent lines will print,
#   and run again to check your predictions.
###############################################################################

# print()
# print("_TODO 18:")
# a = 45
# 45 = a
# b = 10
# c = b + 20
# b = c
# print(a, b, c)

###############################################################################
# TODO: 19.
#   Uncomment the following and PREDICT what will get printed.
#   Then run the program, checking to see whether your prediction is correct.
###############################################################################

# print()
# print("_TODO 19:")
# x = 5
# x = x + 1
# print(x)
#
# x = x + 1
# print(x)
#
# x = x + 1
# print(x)

###############################################################################
# TODO: 20.
#   Uncomment the following and PREDICT what will get printed.
#   (Hint: what gets printed is  NOT  75 10.)
#   Then run the program, checking to see whether your prediction is correct.
###############################################################################

# print()
# print("_TODO 20:")
# x = 10
# y = 75
# x = y
# y = x
# print(x, y)

###############################################################################
# TODO: 21.
#  The statements below make x and y refer to random integers between 1 and 99,
#  then prints the values of x and y.
#  _
#  Challenge: can you write statements below the following that causes the
#    values of x and y to SWAP?  For example, if the values of x and y are set
#    randomly to 40 and 33, so that the given print statement prints:  40 33
#    then your code should print:  33 40
#  _
#  Spend up to 1 minute on this challenge, typing your code and running the
#  program to try out your solution.
#  _
###############################################################################

# print()
# print("_TODO 22:")
# x = random.randint(1, 99)
# y = random.randint(1, 99)
# print(x, y)
