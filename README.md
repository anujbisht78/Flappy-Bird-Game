# Flappy Bird Game
Flappy Bird is a classic side-scrolling mobile game where the player controls a bird, guiding it through a series of obstacles made up of pipes. The objective is to navigate the bird through the gaps between the pipes without touching them. The bird automatically moves forward, and the player can make it flap its wings to gain altitude and avoid crashing into the pipes. The game is known for its simple mechanics, addictive gameplay, and challenging difficulty. Players aim to achieve the highest score possible by flying through as many pipes as they can without colliding.

### Gameplay: [Link](https://www.linkedin.com/posts/anujbisht78_python-pythonprogramming-flappybird-activity-7170703629971116032-HjEg?utm_source=share&utm_medium=member_desktop)
## Some Images:
<img width="450px;" src="https://github.com/anujbisht78/Flappy-Bird-Game/blob/main/sprites/raw/main.png"/>
<img width="450px;" src="https://github.com/anujbisht78/Flappy-Bird-Game/blob/main/sprites/raw/game.png"/>
<img width="450px;" src="https://github.com/anujbisht78/Flappy-Bird-Game/blob/main/sprites/raw/game1.png"/>

## Table of Contents
- [Import Statements](#import-statements)
- [Global Variables](#global-variables)
- [Main Function](#main-function)
- [Welcome Screen Function](#welcome-screen-function)
- [Main Game Function](#main-game-function)
- [isCollide Function](#iscollide-function)
- [getRandomPipe Function](#getrandompipe-function)
- [run_game Function](#run-game-function)

## Import Statements
- Imports necessary modules and libraries for the game, including random, sys, pygame, and asyncio.
  
## Global Variables
- Defines global variables used in the game, such as frame rate, screen width and height, game sprites, game sounds, and file paths for various resources.

## Main Function
- Defines the main coroutine function of the game using asyncio. Initializes Pygame, sets the game's window caption, loads game sprites and sounds, and runs the welcome screen and main game loop asynchronously.

## Welcome Screen Function
- Displays the welcome screen to the user and waits for a key press to start the game. It shows the game logo, player character, message, and base.

## Main Game Function
- Contains the main game loop. Handles user input, updates game state, detects collisions, calculates score, and blits game sprites to the screen. This function controls the flow of the game.

## isCollide Function
- Checks for collisions between the player character and the pipes or ground. It returns True if a collision is detected, indicating the end of the game.

## getRandomPipe Function
- Generates positions for two pipes (one upper and one lower) to be displayed on the screen. The pipes are randomly positioned within the screen boundaries.

## run_game Function
- Calls the main() coroutine function using asyncio.run() to start the game.
