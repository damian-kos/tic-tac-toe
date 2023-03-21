# TicTacToe

## Features
TicTacToe game between two human players.

## Installation
- Install Python: If you haven't installed Python already, download the latest version of Python from the official website (https://www.python.org/downloads/), and install it on your system.
- Open Command Prompt: Press the Windows key + R to open the Run dialog box. Type "cmd" and press Enter to open the Command Prompt.
- Navigate to the directory containing your Python script: Use the "cd" command to navigate to the directory where your Python script is saved. For example, if your script is saved on the desktop, type "cd C:\Users<username>\Desktop" and press Enter.
- Run the Python script: Once you are in the directory where your script is saved, type "python <filename>.py" and press Enter. Replace <filename> with the name of your Python script. Your script will run, and the output will be displayed in the Command Prompt.

## Usage
- At first game will create an empty board.
```
| | | |
--+-+--
| | | |
--+-+--
| | | |
--+-+--
```
- All fields has their corresponding numbers, which looks as follows.
```
|1|2|3|
--+-+--
|4|5|6|
--+-+--
|7|8|9|
--+-+--
```
- And ask for first player input. It starts with X.
```
Where do you want to put your X. Range(1-9): 1
```
- Putting so, we will get.
```
|X| | |
--+-+--
| | | |
--+-+--
| | | |
--+-+--
```
And so on.

## Result
Once any of players will get their signs in a row, it will determine a winner. Or a draw if such scenario happened.

## Logic behing
If any of players has at least 3 signs on board, script will start to check if any of player's combination collected exactly 15 points. Players collect points by putting their signs on board.
This is how points are distribiuted across the board.
```
|2|7|6|
--+-+--
|9|5|1|
--+-+--
|4|3|8|
--+-+--
```
  
