# Greed
This a game where you try and collect as much gems(*) as possible while earning points and at the same time, avoid rocks(0) 
that will affect your score. There is no target points you should reach so the game will go on and on until you close it. 
Enjoy not getting hit by rocks!

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine.
You can install Raylib Python CFFI by opening a terminal and running the following command.
Apple M1 Max chip users create a Rosetta based terminal and work withing that terminal.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

```
python3 greed 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- greed               (source code for game)
  +-- data              (data files for game)
  +-- game              (specific game classes)
  +-- __main__.py       (entry point for program)
+-- README.md           (general info)
```
## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7
* Rosetta Terminal for macOS M1 users
     If your macOS is using an Apple M1 Max chip, you should create a Rosetta based terminal and work within that terminal by following these steps below [ONLY FOR macOS M1].
     - Uninstall all the raylib related packages you previously had installed by executing `python3 -m pip uninstall [package]`
     - Locate the Terminal application within the Utilities folder (Finder > Go menu > Utilities)
     - Select Terminal.app and right-click on it, then choose “Duplicate”.
     - Rename the duplicated Terminal app something obvious and distinct, like ‘Rosetta Terminal’.
     - Now select the freshly renamed ‘Rosetta Terminal’ app and right-click and choose “Get Info” (or hit Command+i)
     - Check the box for “Open using Rosetta”, then close the Get Info window.
     - Run the “Rosetta Terminal” as usual, which will fully support Homebrew and other x86 command line apps.
     - In the “Rosetta Terminal”, first ensure pip is upgraded `python3 -m pip install --upgrade pip` and then install raylib `python3 -m pip install raylib`
     - Then you should be able to run your raylib based python game.

## Authors
---
* Gibran Castillo (cas21045@byui.edu)
* Clyve Kokotiko (kok21002@byui.edu)
* Isiakpona Chuks (juliusrlnd@gmail.com)
* Patrick Ochen (patrickochen97@gmail.com)
* Roguin Peña (ro.guin31@gmail.com)
* Zibanani Nkomo (nko21005@byui.edu)