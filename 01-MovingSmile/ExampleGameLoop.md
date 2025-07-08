---
layout: page
---


<!-- vim-markdown-toc GFM -->

* [Introduction: ExampleGameLoop](#introduction-examplegameloop)
  * [Setup](#setup)
* [Step 0: The prelude](#step-0-the-prelude)
* [Step 1: The initialization phase](#step-1-the-initialization-phase)
* [Step 2: The game loop](#step-2-the-game-loop)
  * [While loops](#while-loops)
  * [Indentation](#indentation)
  * [For loops](#for-loops)
  * [Printing](#printing)
  * [Conditionals and exiting](#conditionals-and-exiting)
  * [Screen updates](#screen-updates)

<!-- vim-markdown-toc -->

# Introduction: ExampleGameLoop

In this small exercise, we will write our first python program that displays an
empty screen with a title. We will see how to tell pygame the size of our
screen, and then check how pygame captures every event on the screen.

## Setup

In pycharm, open up the file `ExampleGameLoop.py` in your repository, it is
under the `00-MovingSmile` directory.


# Step 0: The prelude

Our example code starts with the following two lines:
```python
import pygame
import sys
```
This of these two lines as being the tools needed for our recipe.  When we bake
a cake, we first need to make sure that we have the right set of tools (e.g., a
stand mixer, a spatula, etc.). In our case, we need two tools (or modules, or
libraries), the first being `pygame` while the second is `sys`.

`pygame` is a box that contains numerous tools that the instructions in our
recipe are going to require. We will spend most of our time dealing with the
content of `pygame` to make games and capture events. 

`sys` on the other hand is another tool box that allows python to communicate
with the part of your computer that actually runs python, i.e., the operating
system.

# Step 1: The initialization phase

Next, we will need to initialize our python environment to use pygame and set a
few configuration options, which is why we need the following lines of code
```python
pygame.init()
pygame.display.set_caption("Hello World")
```

The first line, `pygame.init()`, sets up pygame for us to use. Alternatively,
you can think of this as turning on your game console before you start any game.

The second line, `pygame.display.set_caption("Hello World")`, accesses the
`display` tool in the pygame toolbox, and asks it to set the caption of our game
to be `Hello World`. Note that the phrase `Hello World` is placed between
quotes, why is that? It is because `Hello World` is actually a __string__, i.e.,
a non code piece of text. Generally, any set of characters surrounded with
quotes (single or double) form a string.

Then, we create our universe, the game screen! To do that, we use the following
line of code
```python
screen = pygame.display.set_mode((640, 480))
```
What does this do? I am glad you asked. It first accesses the `display` tool
from the pygame toolbox and asks to create a screen for us with height 640
pixels and width 480 pixels. What are pixels you may ask? You can think about
them as the smallest unit of measurement on a computer screen. 

But wait, what's with all those parentheses? There are two things that we should
be aware of:
1. First, `set_mode` is a __function__ that we are __calling__, thus we refer to
   this statement as a _function call_. Everytime we call a function, we must
   open and close a pair of parentheses. 
2. Okay, but what about the second pair? The second pair of parentheses actually
   creates a tuple off of the numbers 640 and 480. In other words, the numbers
   640 (for the height) and 480 (for the width) are grouped together in a single
   tuple and then used as input to the function `set_mode`. 
   
Question: How many arguments (inputs) are we providing to the function
`set_mode` when we called it from our code?

# Step 2: The game loop

Next up is our game loop, that's where the bulk of what we will be doing is
going to happen. So let's dissect this loop line by line.

## While loops

```python
while True:
```

This piece of code tells python to keep running the succeeding lines of code
forever. Semantically speaking, python will keeping executing the code __while__
`True` is true (huh?! In other words, python will keep looping while the truth
is true, and it will only stop when the truth is false, which is never going to
happen). 

In general, we write `while condition` to make python loop while the
`condition` is satisfied, and stop looping when the condition becomes false. But
since `True` is always true, we will never stop our loop. 

## Indentation

In python programming, indentation is of crucial importance. Every time you
indent your code, you are telling python the code belongs __inside__ of the
previous block of code. 

So if I want to execute some python statements __inside__ of a loop, I will have
to make sure that those lines of code are indent one level more than the loop.
This way, python will interpret those statements as part of the loop and will
run them as long as the loop condition is true. 

## For loops

```python
    for event in pygame.event.get():
```
This next line creates a __for__ loop, which is very similar to a `while` loop,
however you can specify __iterative__ conditions for the loop. For example, the
above statement iterates over all events in pygame and executes some code on
each event. Implementing this using a `for` loop is easier than implementing it
using a `while` loop. 

Note how this loop is indented with respect to the `while` loop, which means
that now this `for` loop will execute inside of the `while`. So we now have two
__nested__ loops. Hurray!!

## Printing

```python
    for event in pygame.event.get():
        print(event)
```

Next you see that we are using `print`, but where did that come from? Luckily,
python is packaged with a bunch of very helpful __functions__ that we can use
and call. `print` is the name of the function that python provides and `event`
is an __argument__ to that function. The statement `print(event)` is referred to
as a function call. When python sees that we are calling the `print` function,
it will go and print our message (the event) to the screen. 

## Conditionals and exiting

Next, let's look at the following statement:
```python
if event.type == pygame.QUIT:
    sys.exit()
```

This statement is referred to as a conditional statement, and it typically has
the form
```python
if condition:
    code
else:
    other_code
```
  
Conditional statements are very powerful if you want different code to execute
depending on some condition. In our case, we are checking the condition
```python
event.type == pygame.QUIT
```

But what's with that `==` symbol? Glad you asked, this symbol means that we are
comparing the value of the `event.type` variable to that of `pygame.QUIT`. The
condition will return `True` if the values are equal, and `False` otherwise. 

`pygame.QUIT` is generated when the user (you or the player) clicks on the 'X'
button in the window and would like to close things off. 

```python
sys.exit()
```
Finally, when the user wants to exit, we simple call another function that
python provides for us, which is the `exit` function contained within the `sys`
box of commands (i.e., package). This function call will close everything and
completely exit the program.

## Screen updates

The last line of code `pygame.display.update()` simply tells pygame to update
the screen (we will see later what we need to update). If we had drawn anything
on the screen, pygame would update those and draw them up. 

