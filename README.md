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



# DOMAIN MODEL

Is a visual (Graphic) representation of:
   1. The relevant concepts (they are called conceptual classes) present within the DOMAIN where the problem has been defined
   2. The relationships that, physically or conceptually, interconnect these classes / concepts.

Represents as a UML Class Diagram without any indication of methods, which model:

   a) CONCEPTS / OBJECTS in the domain of the problem AS CLASSES

   b) Properties of OBJECTS / CONCEPTS as attributes

   c) Conceptual or physical connections betwwen OBJECTS / CONCEPTS as reelationships:
      -Inheritance(generalization) (IS - A)
      -Association
      -Dependency

The domain model will be the seed for a design phase artifact: the design class diagram (DCD). 

The DCD: 
   1. Will likely transform the conceptual classes of the domain model in classes.
   2. Will incorporate additional classes not corresponding to any of the conceptual classes in the DM.
   3. Will likely appear the relationships that appeared in the DM.
   4. Will appear new relationships between:
        - Classes corresponding to conceptual classes in the DM and new classes
        - New classes
   5. Attributes and methods signatures for all the classes.

Techniques for building the Domain Model.
   1. Techniques for IDENTIFYING concpets / objects.
   2. Techniques for IDENTIFYING relationships.
   3. Techniques for IDENTIFYING attributes or objects / concepts.

1. Identifying objects / concepts in the domain.

   3 Methods:
      1. For begginers: Textual analysis of List of requirements / use cases.
      2. Derivation from conceptual class category lists.
      3. Study: Learn from experts.
  
Text analysis of req list and use cases:
   1. Take any noun that appears in the req list / use cases as a potential object concpet to be represented in the domain model.
   2. Discard
        - Redundant nouns.
        - Ambiguous / vague nouns.
        - Non relevant concets / objects.
        - Names of attributes. (colour, lenght, size, width, age, ... )
        - Names of structures
 



IDENTIFYING RELATIONSHIPS
Two Methods:
   1.Text analysis of Req List/Use cases (BEGINNERS)
   2Associations categories list + generalization relationship.


1)Text analysis:
1. Take every VERB that connects two concepts objects identified and keep in the task of identifying OBJECTS/CONCEPTS as a potential relationship between these two concepts/objects
2. DISCARD -Nonrelevant verbs
           -ACTIONS
3. Identifying th type of relationship inheritance (IS-A_SPECIFIC_TYPE-OF) association or dependency.
4. For each association:
     a)Indicate MULTIPLICITY
     b)Indicat roles

   POSAR FOTOs

Implementation of relationship in code:
Inheritance:
Clas B(A): -->Python                  
public class B extends A --> Java

Association are implemneted by  ATTRIBUTES
public class A ~associated~ one to many B 

**Relationships**

Inheritance --> IS-A-TYPE-OF. Strongest relationship

Dpendency --> Class A has a dependency relationship with class B if:
   - An instance of B is a local variable of some method of A.
   - An instance of B is an argument of a method of A.
   - An instance of B is the return value of a method.

     Desing goal:
     -   To keep dependencies (Couplings) as low as possible.

Association --> Any relationship that is neither an inheritance nor a dependency.
   - Discovered by text analysis: verbs that connect nouns that are relevant concepts/objects in the domain (different than IS-A)

Particular types of associations

Associations that are established between an object/concept which is a whole and an object/concept which is a part of this whole.


In aggregations. If the whole disappears, its parts can still exists

In composition. If the whole disappears, the parts also disappear.

Appear during the design process
   . When specifies the arguments of the methods or the return values of the methods.   

Implementation of associations
   1. Associations are implemented with attributes.
Because an association somehow implies that you have to provide to an object whose class is involved in the association, the capability of going to another object of the other class involved in the assossition

![](https://github.com/Eudald1601/RevisitingPolymorphism/blob/main/carperson.drawio.png)

- Given a certain person, the system must be able to present to the user the details of the car owned by that person.
- How can the system go from an object vlass Person to the object of class Car that is owned by that person.

  Cardinality:

  In association between A and B. Cardianlity of A is the number of objects of B that may be associated with one object of  the cardinality of A is represented next to B.

   Symbols:
     -  One object B is associated with B objects A
     -  Absence of any indication of cardinality means 1
     -  One object B is associated with 1, 2, or 3 objects A
 
Implementation of associations

Arrow means: capability of arrive to an object of the class pointed by the arrow from an object of the other class in the association


*** FROM DOMAIN MODEL TO FIRST DESIGN ***
The DM is the seed of the DCB

DCD: UML class diagram showing ALL the classes, with all their attributes and all their methods signatures, as well as their relationships

REMARK 1: In general NO all the dependencies are shown.

How to go from DM to first DCD?

1. If no navegability indicaation in associations add them
2. Identify abstractions
   - If we can identify some attribute --> abstract class
   - Else --> interface

Candidates to absractions: Classes that appear in a hierarchy and have subclasses.


*** LAYERING ***

Distribution of code in several layers.

![](https://github.com/Eudald1601/RevisitingPolymorphism/blob/main/img/layering.png)

PROPERTY:

Anything placed in a certain layer is more stable than anthing placed in outer layers and is less stable than anthing in inner layers.

Stable: related to the likelihood of change.

Rule in Software Systems: Make our software to depend as much as possible on stable classes/tools

Dependency / Couplings:

Mesurement of how strongly one element is connected to, has knowledge of, or relies on other elements.

One software design goal:
To reduce as mush as possible the compling with non-stable elements!!

There is nothing wrong on coupling with stable elements.

- Subclasses and superclasses
- Associated classes
- Classes with dependency relationship
   - Arguments
   - Local variables
   - Return values
How to use clean architecture?? Make that elements in one layer do not depend on elements that appear in outer layers.    


***COUPLING /DIP Final Words***
1. Identifying breaks of DIP naming packages
   -Include in the names of the packages name of the layer.

2. Define more complex methods for reducing coupling.

**Single Responsibility Principle (SRP)**

Cohesion: Measurement of how strongly related and focused the responsibility of an element are.

Element can be classes or packages.

Goals of design

Reducing as much as possible coupling increasing cohesion.

Formulation 1:
   - A class should have only one reason to change. A program usually must satisly requirements coming from differnet sources.
      - Human resources
      - Econmics
      - Academic

But requirements Change. Therefore, there will be change requests design should be such as a change request from one source. Must not interact with code that satisfies needs of sources different than the one that has made the CR.
         
Formulation 2: Gather together things that change for the same reason. Separate them from things that change by different reasons . SEPARATION OF CONCERS.

**OVERVIEW OF DESIGN**
1. Take DM and build first version of D[]
2. Identify ALL THE METHODS required for solving the problem, and specify them USE CASE
3. Assign to each method to a class in a way that:
   1. Keeps coupling as low as possible and in the right direction
   2. Keep cohesion as high as possible(SRP)

GRASP: Geral Responsibility Assigment Software Patterns.

Rules that we will follow for assigning one method to ne class for keeping high cohesion and low coupling.

Almost any program will:
1. Interact with users for receiving requests or return results
2. Create objects
3. Put objects to interact with other objects invoking thir methods.

Controller (GRASP)

Question(PROBLEM): What objects (beyond the UI) receives the requests from user, and coordinates (controls) the software system operations?

Answer: Assign this responsibility to A class (controller) that represents either. The whole system, or a whole subsystem or a use case scenario

Controller: delegates in other classe the execution of the tasts required for satisfying the user's requests.

2) CREATE OBJECTS:
Queston(PROBLEM): Whow should be responsible (what class) of creating objects of one class(B).
Answer: Assign it to a class A if one of the following situations is TRUE.

a) A creator contains or aggregates B
b) A records B
c) A closely uses B
d) A has the initializating data for B

Hwo whould be responsible forcrating ChessCell? CHEESBOARD

**GRASP EXPORT**

QUESTION: What is a general principle for answering responsibilities to objects?

ANSWER: Assign the responsibility the class that has the information required to fulfill the responsibility. As long as this decision keeps high cohesion and low coupling.

CONTRAINDICATIONS:

Sometimes it leads to low cohesion:
   - Do not save yourself
   - Do not print yourself

DISCUSSION:

What if the information is distributed in more than one class?

To study these classes, and eventually assign the responsibility to one of them (respecting the SRP and Low Coupling), and make it a kind of "task controller")

REMAINING PROBLEM:

What if assigning the responsibility to one of the classes identified break the SRP or pramatically increases coupling?

PUREFABRICATION:

Question: What if assigning the responsibility to one of the classes identified break the SRP or pramatically increases coupling?

Answer: Assign the responsability to an "artificail" convenience class, which does not represent any domain object/concept what is highly cohesine and as low coupled as possible.

NAMING OF PURE FABRICATION CLASSES:

The names must include NOUNS. Not verbs. (Saver, Printer...)

POLIYMORPHISM

Question: How to assign a certain responsability when the behaviour depends on type?
 
Answer: Assign the responsability to a inheritance hierarchy using polimorphic method, so that each behaviour is assigned to onw of the subclasses.

If there is a behaviour by default => behaviour in superclass.

If not, superclass is abstract.
 
ODD: GENERAL STRATEGY (PROCESS)

Starting poing: use cases

1) Select one use case: The most rellevant:
     -  Case study: PlayChessTurn
  
2) If the use case contains different potential starting points assimilate each one to one method.
3) For each operation (as identified in step 2) Collect all the scenarios
4) For each step in the scenarios (in alternative scenarios - extensions) Start with trigger envents.
     - Identify the action described in the step (orTE) -> Assign a method to it or break it in smaller actions (assigning one method to each action)
     - Assign a name to the methods should contains a verb and indicate what the method will be in charge of
     - Identify what objecs (data the method will require for performing it's job -> candidates for arguments)
     - Identify:
          - Whatever the method has to return a value or not
          - If it has to return a value identify it's type / class
          - Identify exceptional situations
          - If any -> include an exception class in your design.
      
5) Specify what the method has to do
6) Identify the class where this method has to be places (Assignment of responibility- apply GRASP/SOLID) Identify class that invokes the method.

Example: PlayChessTurn

a) Player proposes to move

b) Player proposes to temporally stop

c) Player proposes requests draw

Assimilate a) to a method

Name: MovePiece

Arguments: Chessboard, rO, cO, rD, cD.

2a) System noticies that either there is not any piece in origin cell or there is a piece o the opponent:
   - Exception situation:
     Exception: OriginExcepion
   - getPieceColorInCell(rO, cO, ChessBoard)


**SOFTWARE DESIGN PATTERNS**
Touple formed by:

1) A well-known and recurrent design problem IDENTIFICATION
2) A formalized solution for this problem, including:
   - STRUCTURE (Classes and relationships -UML class diagram)
   - PARTICIPANTS (Roles for the classes)
   - COLLABORATIONS between the objects for solving the problem)
  
3) Discussion on the problem and solution including: consequences advantages, disadvantages and trade-offs...

- They are RECIPES.
- They capture and preserve important design experience.
- They build a design vocabulary


GoF: gang of four


**VISITOR PATTERN**
To be used in evaluation of POSTFIX expression!!!

CONTEXT and PROBLEM:
- We have a structure of elements of different types.

STRUCTURE:
- list, graph, tree ...

PROLEM: Traveise the structure ( visit all us elements) and while visiting each element, perform a task which dpends on the type of the element

I have toperform a traversal1 on this structre on ElementA objects, this traversal1 will does certain task on ElementB traversal1 will perform a different task. The problem is to whom I hae to assign traversal1? GRASP Pattern: Polymorphism specify abstract method on Element, and program different implementations in ElementA and ElementB.

Imagine that my project has to implement, not one traversal, but P traversals. 
