# Tic Tac Toe

😂 I was just bored so I coded something waiting for my flight ✈️

## Features:
- Terminal Tic Tac Toe
- Terminal Score Board with history
- Player vs Player
- Player vs Random Computer
- Player vs Hard computer

## Goal of the exercise
- use of Class inheritance 
- use of different Array/Dict manipulations
- use of asserts
- use of pytest
- Folder/File architecture

## Design
#### Menu Game
```
==========================================
    👾 Welcome to the Tic Tac Toe Board  👾
==========================================
    [1] For Single Player (vs Computer)
    [2] For Single Player (Very HARD)
    [3] For 2 Players

    [4] Show score board

    [0] to Exit Game
```
#### The starting board
```
————————————————————
|   | 1  |  2 |  3 |
————————————————————
| A | 🔲 | 🔲 | 🔲 |
————————————————————
| B | 🔲 | 🔲 | 🔲 |
————————————————————
| C | 🔲 | 🔲 | 🔲 |
————————————————————

```
#### In Game
```
————————————————————
|   | 1  |  2 |  3 |
————————————————————
| A | ❌ | ❌ | ⭕️ |
————————————————————
| B | ⭕️ | 🔲 | ❌ |
————————————————————
| C | 🔲 | ⭕️ | 🔲 |
————————————————————
```
#### Winner
```
————————————————————
|   | 1  |  2 |  3 |
————————————————————
| A | ❌ | ❌ | ⭕️ |
————————————————————
| B | ⭕️ | ❌ | ⭕️ |
————————————————————
| C | 🔲 | ⭕️ | ❌ |
————————————————————
```
#### Choice selection
```
🤔 PLAYER it is your Turn [TICTOE]
Select one of the following choices
Choices  👉: ALL_CHOICE
____________________
```

#### Winner Screen
```
=====================================================================
  🏆 Congrats! The winner is PLAYER in 0 steps with a score of 999
=====================================================================
```

#### Draw Screen
```
=====================================================================
                       🥶 Draw! No winner ! 
=====================================================================
```

#### Score Board
```
==========================================
            🎖️ Score Board 🎖️
==========================================
    RANK    |   USERNAME    |   SCORE
    
    #🥇            SKA          34
    #🥈            BOU          143
    #🥉                            
    #4                            
    #5                            
```