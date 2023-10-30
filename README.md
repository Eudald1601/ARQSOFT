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

  ------- Conditions that are met befare starting the use case they must not be tested in the use case. -----
  
PRECONDITIONS:
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

1.c Player requests draw

(AS 1.a but in case that the opponent accecpt it, the system ends with stop by draw)

2.a System detects that either there is NOT any piece or there is a piece of the opponent in origin cell.

   1. System notifies this situation and ask new action to player.
   2. Go to step 1 of basic flow.

2.b System detects that there is a piece of the player at destination cell.

   1. Same as 2.a.1
   2. Same as 2.a.1

2.c System detects that the movement requested DOES NOT CORRESPOND to the piece in origin cell.
  
   1. Same as 2.a.1
   2. Same as 2.a.1

2.d System detects that the movement would leave Player's King is threatened by some piece of player's opponent.
   1. Same as 2.a.1
   2. Same as 2.a.1

2.e System detects that the path is NOT free

Name: movementOFBishopOK

Number: 3

ACTORS: 

PRECONDITIONS:
   - Player has reported movement.
   - Origin cell has a piece a bishop of the player.
   - In destination cell there is no piece or there is a piece of the opponent.

BASIC FLOW:

1. System detects that the movement is in diagonal.
2. System ends with movement ok.

**EXTENSIONS**

1.a System detects that movement is NOT diagonal

   1. System ends with movement KO

Name: BishopPathFree

Number: 4

ACTORS:

PRECONDITIONS:
   - Player has requested movement
   - Origin cell has a Bishop of the player.
   - Destination cell: No piece of the Opponent
   - Movement requested is movement of Bishop

BASIC FLOW:
1. System ends with path FREE

**EXTENSIONS** 

   1.a System detects that in diagonal from origin cell to dest-cell on the board there is second piece
      1. System ends with path NO FREE.

Name: KingIsThreatened

Number: 5

PRECONDITIONS:
   - Path from origin to destination is free

BASIC FLOW:

1. System takes a piece
2. System notices that movement to king's opponent is a movement of the piece
3. System notices that the path is NOT free

Repeat 1 to 3 while there are pieces left

4. System returns king NOT threatened

**EXTENSIONS**

1.a System notices movement does not correspond to piece

   1. Go to Step 1 of basic flow.

2.a System notiece that the path is FREE.

   1. System ends use case with king threatened

![](https://github.com/Eudald1601/RevisitingPolymorphism/blob/main/img/example.drawio.png)

Execution paths of the system we use the sentence: "when this use case is executed" on "then use case X is executed".

Executing a use case <--> talking about the system executing the steps in one of the scenarios of a use case.

The execution of the use cases must take place in a certain proper order. And this order is defined by PRECONDITIONS and POST CONDITIONS of the use cases.

Name: createGame

Number: x

PRE-CONDITION: 
   1. User has requested to create the game

POST-CONDITIONS:
   1. Game framework created: user added as player to the created game

BASIC FLOW:
   1. System creates the game framework
   2. System adds user as players

Name: BuildFrameworkChess

PRE-CONDITIONS: 
   1. user has requested to create ChessGame

POST-CONDITIONS:
   1. Framework for chess created.
      - Board
      - Cells

BASIC FLOW:
   1. System creates the chess board.
   2. System creates all the chess cells in the ChessBoard.

NAME: AddPlayerChess 

PRECONDITIONS:
   1. The chess framework has been created

BASIC FLOW:
   1. System creates the pieces.
   2. System gives pieces to player.
   3. System places the pieces on the board.

NAME: BuildFrameworkMonopoly

PRECONDITIONS: 

POSTCONDITIONS: 
   1. Monopoly Board, Cells, {TOKENS: Money, Cards, house, hotels}

BASICFLOW:
   1. System creates MonopolyBoard.
   2. System creates cells.
   3. System creates bank (third party)
   4. System creates tokens (money, houses, cards, hotels)

NAME: BuildFramework

PRECONDITIONS:
   1. User has requested to the play game

POSTCONDITIONS:
   1. Board, Cells, Tokens and third party

BASIC FLOW:
   1. System creates Board
   2. System creates cells
   3. System creates tokens
   4. System creates third party

**EXTENSIONS** 

   3.a There are no tokens
   
      - Go to step 4 of B.F
   
   4.a Tehre are no third party
   
      - End use case
      
