# 11SE Task 2 2025 - Text-Based Adventure
### By Anthony Revel

# Sprint 1
## Requirements Definition
### Functional Requirements
* The user needs to be able to view their collection of items and must be capable of viewing the statistics of them as well
* The user must be capable of retrieving data about their 'item' collection and be capable of using these in the game to battle enemies.
* The user must be capable of saving their data (via json)
* The user must be capable of "crafting" items upon meeting requirements
### Non-Functional Requirements
* The system must be capable of executing most functions in under a second.
* The system must not fail while running and data should not be lost.
* The system should be easily navigable with minimal instructions required to understand the major functions of the system.

## Determining Specifications
### Functional Specifications
* The user must be capable of interacting with the system via a GUI interface
* The user must be capable of playing the game with no runtime errors
* The program must be capable of handling invalid inputs as well as users attempting to break the program (attempting to edit save data)
* The program must be capable of:
  * Rolling with rng
  * Increasing luck or other aspects with items
  * Saving data
  * View their collection
  * Battling using items from their collection
* The program should have an 'admin' panel as to make it reasonable to mark the program
### Non-Functional Specifications
* The program must be capable of running most functions in under a second (with an exception to those that intentionally force waiting)
* The program should be efficient minimising redundant code with loops and functions
* The UI should be easy to understand and not complex to allow for ease of use, hard to see colours should not be used and text should be reasonably sized
* Everything within the program should work as intended, menu navigation should function as intended and data should not become corrupted (unless the user attempts to edit the save data themselves, then it is their fault)
### Use Case

*Viewing Collection*
![Use Case 1](Use_1.png)
*Actually playing the main game*
![Use Case 2](Use_2.png)
*Saving after playing for a bit*
![Use Case 3](Use_3.png)
*Crafting an item and selecting it after meeting requirements*
![Use Case 4](Use_4.png)
## Design
*Storyboard*
![Storyboard](Storyboard.png)
*Level 0 DFD*
![Data Flow Diagram](DFD0.png)
*Level 1 DFD*
![More Complex Data Flow Diagram](DFD1.png)
*Gantt Chart*
![Gantt Chart](Agile_Gantt.jpeg)
## Build and Test
```Python

```

## Review

1. The system is entirely successful in meeting all specified functional and non-functional requirements and also meets many further unnessecary requirements (that realistically should've been implemented in future sprints), it is capable of saving and loading data via json, accessing the collection and allowing the user to view it, it is capable of "crafting" upon meeting requirements, there is currently little to no delay in the functionality of anything and the system encounter no runtime errors with it being relatively easy to naviagate.
2. The system handles inputs and outputs almost exactly as planned, although one use case has yet to have been made (planned for next sprint) all other use cases have been recreated in a similar fashion to what was originally planned for the system.
3. The functions, variables and docstrings/comments ensure that the code is easily readable and understandable with everything being rather clear if you have a fundemental level of understanding of the modules already being used. The system as a whole is very organised with designated sections seperated by strings to increase clarity.
4. The next sprint is intended to include the main feature of the game among various other smaller features for the game to have, including an auto-roll for normal players, for gears and a way to increase rolling speed, a roll cooldown, biomes and many other minor features to increase the complexity of the game.

# Sprint 2

## Design
Add storyboard and data flow diagram

## Build and Test
```Python

```

## Review

# Sprint 3

## Design
Add storyboard and data flow diagram

## Build and Test
Add code block

## Review

# Sprint 4

## Design
Add storyboard and data flow diagram

## Build and Test
Add code block

## Review

## System Evaluations