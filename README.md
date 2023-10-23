# RevisitingPolymorphism
Lab0 Eudald Brils i Clara Aymerich

# THEORY 
***USE CASES*** 

You will probably hear "user stories" (in scream) Use cases ARE NOT the same as user stories-Papers in Atenea that compare use case and user sotries. These is one, which provides rationale for still wron cases.

Internal definition set of ACTIONS (including the interactions between a user and the software system) that a software systems PERFORMS for ACHIEVING a SPEIFIC GOAL that BRINGS VALUE to the user.

SET OF ACTIONS strongly related with the contents of a use case 
1. ACTION 1
2. ACTION 2
3. ACTION 3

Types of actions:
- Performed by user
- Performed by the software system

Two types of use cases:
1. USER LEVEL use cases.
   - Where both, the user and the system perform some actions __(INTERACT)__
2. SUB-FUNCTION LEVER
   - Where there are ONLY actions __PERFORMED BY THE SYSTEM__

__Another informed definition:__

WRITEN STORIES on how some actor uses the software system under development for ACHIEVING a RELLEVANT GOAL for that actor and, consequenty, getting an ADDED VALUE.

WHAT WE (analyst) have to do with regards to the ue cases?

1. IDENTIFY THE RELEVANT USE CASES FRO THE SOFTWARE SYSTEM under development. Taking into account:
      - Diferent types of users
      - Identify the added values each type wants to get from the system <--> GOALS TO BE ACHIEVED by the system.
      - Name the use cases:
         - Short
         - Include a VERB
        
2. Build all the identified relevant use cases.
      - ORDERING THIS DEVELOPMENT
      - Start with the one thta concentrates the most relevant core goal.
      - While developing a use case, an analyst can identify another use case not previously identified. This means a 'tree' of use cases:
        
        ![](https://github.com/Eudald1601/RevisitingPolymorphism/blob/main/img/img1.drawio.png)

Worked EXAMPLE: CASE STUDY

Identification of use cases

Types of users: 
 - Player
 - Administrator

To identify the relevant interactions that a person who wants to use this system has to perform with that system.

![](https://github.com/Eudald1601/RevisitingPolymorphism/blob/main/img/example.drawio.png)

Name: Play game

Number: 1 

ACTORS:
   - Players: persons that play the game.

PRECONDITIONS:
   - Conditions that are met befare starting the use case they must not be tested in the use case.
   - The game has been created
   - All the players have been added to the game

POSTCONDITIONS:
   - Game ended or suspended.
     
BASIC FLOW: 
1. System gives turn to the right player
2. Player plays the turn
3. System performs actions as required by new state

Repeat 1 to 3 while:

Status is NOT STOP

4. System notifies WINNER to all plaayers
5. System notifies end of game to all players.

**EXTENSIONS**

3.a Player makes a mistake while is playing the turn
   - System notifies player
   - System request player turn again
   - Go to step 2

4.a There is no winner 
   - System notifies stop by the suiteable reason
   - Go to step 5 of basic flow


![](https://github.com/Eudald1601/RevisitingPolymorphism/blob/main/img/diagrama.drawio.png)


Name: PlayTurnChess

Number: 2

ACTORS: Players

PRECONDITIONS:
   - Game selected is chess
   - Chess framework created
   - 2 players aded

POSTCONDITIONS:
   - Player turn completed

BASIC FLOW:
1. Player requests to move a piece from an origin cell to a destination cell of the board.
2. System  moves the pieces as requested by player
3. System ends use case with status go on.

**EXTENSIONS**

1.a Player requests to temporally stop 

   1. System notifies stop requests to the opponent.
   2. Opponent accepts the stop request.
   3. System notifies stop.
   4. System ends use case with status stop temporaily.

      2.a Oponents rejects stop request.
         1. System notifies rejection.
         2. System asks for new action to player with turn.
         3. Go to step 1 of basic flow.
            
1.b Player surrends
   1. System notifies to players
   2. System ends use case with stop by surrending

