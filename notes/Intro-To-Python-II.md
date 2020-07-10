# Intro To Python II

## Lambda’s Problem Solving Framework

Throughout the Computer Science curriculum, we will reference and use the Lambda Problem Solving Framework, sometimes referred to as UPER. This framework is a step-by-step process:

Understand
Plan
Execute
Reflect

**Understand**

The most crucial thing to do before you do anything else is to understand all of the details of what the problem is asking you to do. One helpful starting point is to transcribe the description of the problem from the page into your own words.

### Questions

Here is a list of starter questions that might come up during this step:

1. What are the inputs your code receives?
2. What is the range of input?
3. How big can the input be (how much data)?
4. What are the outputs your code produces?
5. What is the range of output?
6. How big can the output be (how much data)?
7. How performant must the code be?
8. What is missing from the task description?
9. Are there third-party stakeholders who we should consult?
10. What assumptions are you making?
11. Does anyone else on the team need to validate these assumptions?

### Actions

- The most important thing you can do during this stage of the process is to ask questions!

  - Be as specific as you can when you are asking questions.
  - Be clear and concise with your questions by using unambiguous language and only including necessary details.

- Do not fear this part of the process—enjoy it!

  - Try to have a mindset where you see the problem as a curiosity to be explored, not something there to antagonize you.
  - Feeling antagonized and afraid won’t help you at work or in an interview. Remember, problem solving is the fun part so enjoy it!

- Identify the smaller components that make up the larger problem.

  - If you get stuck in understanding, break the larger problem into smaller sub-problems.
  - Then, apply this framework against each of the smaller sub-problems until you solve the larger problem.

- Try to digest the problem and comprehend it by rewriting the problem in your own words.

  - If you had to describe the problem to someone else, how would you do so?

- Diagram how the data flows through the problem.

  - Think about each stage of the journey for the data and what will happen to it as it travels through your program.

- Think like a villain.

  - What inputs would break your program?

- Where is the description of the problem incomplete?
  - If you aren’t able to get answers on something that’s unclear in the specifications, make an educated guess and document your assumptions and your decision.

You are done with this step when you could explain this problem to someone who has never seen it. Your explanation should be thorough enough for the person to skip the Understand step themselves and start to plan right away.

### Plan

This is where you will ask what steps will I take to solve the problem? You will take your description of the problem and transform it into a complete, actionable plan to solve that problem. If you find shortcomings in your understanding of the problem while you’re planning, drop back to Step 1 until you resolve the ambiguity. If you have not yet completed Step 1, you will end up planning to solve the wrong problem! When interviewing, it’s very important that you do this step aloud!

Remember, you aren’t coding during this step, unless it’s small pieces of throwaway code to test a hypothesis. You should write pseudocode during this step, however.

_Questions_

- Do you know the answer to a similar problem that has similar inputs and outputs?
  - What does this problem remind you of?
  - Can you bring that knowledge to bear here?
- Does my plan meet the performance requirements?
  - What’s the time complexity?
  - What’s the space complexity?
  - How big can my input data be?
- Can sorting the input data ahead of time lead to any improvements in time complexity?
  - Does recursion help?
  - Is the problem made up of identical subproblems?
  - Can you state the problem with itself in its own definition?
- Think like a villain. Does your plan cover the edge cases?

_Actions_

- Solve the problem like a human.
  - If you’re sorting something, imagine your task as a pile of blocks in front of you that need to be sorted.
- Break down the steps you take into small enough pieces for a computer to understand.
- Approach the problem from many angles.
- Get a brute-force solution as quickly as possible, even if it’s not performant enough.
  - It can lead you toward better solutions.
- Come up with as many plans of attack as you can.
  - Choose the best one that satisfies performance needs.
- Try to solve a simpler version of the problem.
  - If the input is a 2D array, can you solve it for a 1D array?
  - If you need to count the number of ways to eat cookies 1, 2, or 3 at a time, first try to solve it for the number of ways you could eat two at a time or even one at a time.
  - The solution to the simpler problem can lead to insights on the more complex problem.
- List the nouns and verbs in the problem description.
  - Map each one to an algorithm, process, data structure, object, method, function, etc.
- Perfect can be the enemy of good.
  - Even if your initial workable solution isn’t performant enough, you can iterate later.
  - “Premature optimization is the root of all evil.”

You know that you completed this step when you have pseudocode that’s detailed enough to convert to real code. You should also be convinced the pseudocode represents a legitimate, working solution.

### Execute

This is where you take your plan and convert it to actual, working code. This step isn’t easy, but it’s much easier if you’ve done a good job with Steps 1 and 2 above. If you find shortcomings in your plan while you’re implementing the solution, drop back to Step 2 until you resolve the ambiguity. If you have not yet completed Step 2, you will spend far longer on this step than you have to.

_Questions_

- Think like a villain. Does your implementation handle all inputs?
- What language is best to solve this problem?
  - Best technically?
  - Best for the company?
- What is the best way to split this code into functional modules?
- Are any of the modules reusable for later projects?
- Does this functionality already exist?

  - Are there built-in libraries I can leverage?
  - Are there third-party libraries I can leverage?
    - Are the licenses on those third-party libraries compatible with our needs?

_Actions_

- Start a source code control repo (e.g. a git repo) if one doesn’t already exist.
- Convert your pseudocode and outlines into actual code.
- Don’t Repeat Yourself (DRY): Remove redundant code as you write it.
- Document code as you write it.
  - Header blocks that contain usage information.
  - Comments where necessary.
- Write code clearly enough that comments aren’t necessary.
  - If comments help clarify or summarize a piece of code to a reader, definitely add comments.
- If you write code that’s hackish or kludgy, fix it.
  - If you don’t have time to fix it, comment it with:
  - Why you couldn’t do it the Right Way (time constraints, etc.)
    - What do you need to do to make it Right.
- Follow the style guide for the company.
  - If no style guide is available, follow the style of the existing codebase.
  - If there is no existing style guide or codebase, choose the best one you can find.
- Write unit tests as required.
- Write end-to-end tests as required.

You know this step is complete when:

- The program works on good data.
- The program doesn’t fail on bad data or edge cases.
- The program passes all tests.

### Reflect

Is this implementation as good as I can make it? Would I be proud to show my code to another programmer?

_Questions_

- Does your solution work in all cases?
  - Main case?
  - Edge cases?
- Is the solution performant enough?
- Is the code documented?
- In retrospect, what would you do differently? What will you do differently next time?

  - What went right?
  - What went wrong?

_Actions_

- Document or implement any changes that you still need to make to the code.
- Document or remove any redundant code that you should refactor.
- Remove unused code.
- Document future shortcomings that you will need to address in the medium or long term.
- Identify and document algorithms that you should replace with algorithms with better time complexity.
- Identify and document or remove redundant computation.
- Document any embarrassing code that you need to fix.
  - Why you couldn’t do it the Right Way (time constraints, etc.)
  - What you need to do to make it Right.

You know that this step is complete when you cannot think of anything else to reflect upon.

### Hypothetical Rock-Paper-Scissors Game

_Requirements_

- There will be 2 players:
  - One player will be a human user.
  - The second player will a computer player that the human user is competing against.
- Each player has three choices:
  - rock
  - paper
  - scissors
- There are three results after both the human and the computer make one of their choices:
  - win
  - lose
  - tie
- The rules for figuring out who wins and who loses are:
  - rock beats scissors
  - paper beats rock
  - scissors beats paper
- A tie occurs if both users choose the same option.

_Understand_

- What happens at the start of the game?
  - _We should print out a welcome message to the user after they initialize the game._
- What is the first thing the user will see when starting the game?
  - _They will see the welcome message and historical win/loss data._
- How are points being tracked?
  - _We will track points in memory during a game and print out current score after each round. When the game ends we will save data to our data store._
- At what point does the game end?
  - _The game will only end when the user quits the game._
- Will the computer user merely make random choices or will we program in some strategy based on user behavior?
  - _For this first implementation of the game, let’s just have the computer make a random choice and not try to program in any strategy._
- Should we have some persistent data that stores previous results or a running win/loss count?
  - _We will save our win/loss data to a text file that we will read from at the start of a new game and save to at the end of each game._
- If we save the data, where should we save it and when should we update the storage.
  - _We will save to a text file and update the file at the end of each game._
- When do we load the historical data?
  - _We will load the historical data from the text file at the start of a new game._
- How does the user quit or end the current game session?
  - _The user will have the option to quit after each round of the game_
- Will we use the keyboard for input or will there be an interface for using a mouse?
  - _We will use keyboard input because this will be a Python terminal game._

### Plan

```python
### necessary variables
welcome_message
historical_data_message
quit_message
win_message
loss_message
tie_message

wins
ties
losses

choice_options

computer_choice
user_choice
```

For now, we will just leave these as pseudocode, but next let’s think about the functionality of the game.

```python
### procedures
1. display welcome_message
2. load historical_data and populate variables with data
3. display historical_data_message with historical data
4. prompt user to make a choice between rock, paper, scissors, or quit
  1. if quit, update text file with current wins, ties, losses data and exit game
  2. if not quit, move on to step 5
5. computer makes a choice between rock, paper, and scissors
6. compare user choice and computer choice
7. display message based on result of comparison
8. update wins, ties, losses appropriately
9. return to step 4
```

### Overview

Now, we need to write the simple Python terminal game. We will use the pseudo-code that we wrote during the previous objective:

```python
### necessary variables
welcome_message
historical_data_message
quit_message
win_message
loss_message
tie_message

wins
ties
losses

choice_options

computer_choice
user_choice

### procedures
1. display welcome_message
2. load historical_data and populate variables with data
3. display historical_data_message with historical data
4. prompt user to make a choice between rock, paper, scissors, or quit
  1. if quit, update text file with current wins, ties, losses data and exit game
  2. if not quit, move on to step 5
5. computer makes a choice between rock, paper, and scissors
6. compare user choice and computer choice
7. display message based on result of comparison
8. update wins, ties, and losses
9. return to step 4
```

We will start by declaring all of our variables and assigning values to them:

```python
import random


score =  {
    “wins”: 0,
    “ties”: 0,
    “losses”: 0
}

welcome_message = “Welcome to Rock, Paper, Scissors!”
historical_data_message = “Wins: %s, Ties: %s, Losses: %s”
quit_message = “Thanks for playing Rock, Paper, Scissors!”
win_message = “Congratulations, you won!”
loss_message = “Sorry, you lost!”
tie_message = “It was a tie.”

historical_data = # TODO: will need a function for loading historical data
score[“wins”] = historical_data[“wins”]
score[“ties”] = historical_data[“ties”]
score[“losses”] = historical_data[“losses”]

choice_options = {
    1: “rock”,
    2: “paper”,
    3: “scissors”,
    9: “quit”
}

computer_choice = random.randint(1, 3) # use the random module imported above
user_choice = None
```

Now, we need to write out our procedural code by transforming our pseudo-code to actual Python code. We will look at our list of necessary procedures and logic and try to contain logical groupings into separate functions.

```python
import random


score =  {
    “wins”: 0,
    “ties”: 0,
    “losses”: 0
}

welcome_message = “Welcome to Rock, Paper, Scissors!”
historical_data_message = “Wins: %s, Ties: %s, Losses: %s”
quit_message = “Thanks for playing Rock, Paper, Scissors!”
win_message = “Congratulations, you won!”
loss_message = “Sorry, you lost!”
tie_message = “It was a tie.”

historical_data = get_historical_data()
score[“wins”] = historical_data[“wins”]
score[“ties”] = historical_data[“ties”]
score[“losses”] = historical_data[“losses”]

choice_options = {
    1: “rock”,
    2: “paper”,
    3: “scissors”,
    9: “quit”
}

computer_choice = random.randint(1, 3)
user_choice = None

### procedures
### 1. display welcome_message
### 2. load historical_data and populate variables with data
### 3. display historical_data_message with historical data
### 4. prompt user to make a choice between rock, paper, scissors, or quit
    # 4.1. if quit, update text file with current wins, ties, losses data and exit game
    # 4.2. if not quit, move on to step 5
### 5. computer makes a choice between rock, paper, and scissors
### 6. compare user choice and computer choice
### 7. display message based on result of comparison
### 8. update wins, ties, and losses
### 9. return to step 4

### 1. display welcome_message
def show_welcome_message():
    welcome_message = “Welcome to Rock, Paper, Scissors!”
    print(welcome_message)

### 2. load historical_data and populate variables with data
def get_historical_data():
    text_file = open(“history.txt”, “r”)
    text_data = text_file.read().split(“,”)
    text_file.close()
    return {
        “wins”: int(text_data[0]),
        “ties”: int(text_data[1]),
        “losses”: int(text_data[2])
    }

### 3. display historical_data_message with historical data
def show_historical_data_message():
    print(historical_data_message %
          (score[“wins”], score[“ties”], score[“losses”]))

### 4. prompt user to make a choice between rock, paper, scissors, or quit
def get_user_choice():
    choice = input(“[1] rock   [2] paper   [3] scissors    [9] quit\n”)
    return choice_options[int(choice)]

### 4.1. if quit, update text file with current wins, ties, losses data and exit game
def quit_game(wins, ties, losses):
    text_file = open(“history.txt”, “w”)
    text_file.write(str(wins) + “,” + str(ties) + “,” + str(losses))
    text_file.close()

### 6. compare user choice and computer choice
def compare_choices_and_get_result(user, computer):
    if user == computer:
        return “tie”
    elif (user == “rock” and computer == “scissors”) or (user == “paper” and computer == “rock”) or (user == “scissors” and computer == “paper”):
        return “win”
    else:
        return “loss”

### 7. display message based on result of comparison
### 8. update wins, ties, and losses
def display_result_message_and_update_score(result):
    if result == “tie”:
        print(tie_message)
        score[“ties”] += 1
    elif result == “win”:
        print(win_message)
        score[“wins”] += 1
    else:
        print(loss_message)
        score[“losses”] += 1
```

We have all the individual pieces of our code. But, our code is a mess. And, we never figured out how we will loop through our game logic or quit when necessary. Now that we have all of this code there in front of us, it can be much easier to refactor. Let’s do that together.

Note: we need to create a “history.txt” file with 0,0,0 as it’s only contents.

The first thing we should do is move all the function definitions to the top of the file.

```python
import random


def show_welcome_message():
    welcome_message = “Welcome to Rock, Paper, Scissors!”
    print(welcome_message)


def get_historical_data():
    text_file = open(“history.txt”, “r”)
    text_data = text_file.read().split(“,”)
    text_file.close()
    return {
        “wins”: int(text_data[0]),
        “ties”: int(text_data[1]),
        “losses”: int(text_data[2])
    }


def show_historical_data_message():
    print(historical_data_message %
          (score[“wins”], score[“ties”], score[“losses”]))


def get_user_choice():
    choice = input(“[1] rock   [2] paper   [3] scissors    [9] quit\n”)
    return choice_options[int(choice)]


def quit_game(wins, ties, losses):
    text_file = open(“history.txt”, “w”)
    text_file.write(str(wins) + “,” + str(ties) + “,” + str(losses))
    text_file.close()


def compare_choices_and_get_result(user, computer):
    if user == computer:
        return “tie”
    elif (user == “rock” and computer == “scissors”) or (user == “paper” and computer == “rock”) or (user == “scissors” and computer == “paper”):
        return “win”
    else:
        return “loss”


def display_result_message_and_update_score(result):
    if result == “tie”:
        print(tie_message)
        score[“ties”] += 1
    elif result == “win”:
        print(win_message)
        score[“wins”] += 1
    else:
        print(loss_message)
        score[“losses”] += 1

score =  {
    “wins”: 0,
    “ties”: 0,
    “losses”: 0
}

welcome_message = “Welcome to Rock, Paper, Scissors!”
historical_data_message = “Wins: %s, Ties: %s, Losses: %s”
quit_message = “Thanks for playing Rock, Paper, Scissors!”
win_message = “Congratulations, you won!”
loss_message = “Sorry, you lost!”
tie_message = “It was a tie.”

historical_data = get_historical_data()
score[“wins”] = historical_data[“wins”]
score[“ties”] = historical_data[“ties”]
score[“losses”] = historical_data[“losses”]

choice_options = {
    1: “rock”,
    2: “paper”,
    3: “scissors”,
    9: “quit”
}

computer_choice = random.randint(1, 3)
user_choice = None
```

So, now we have all of our function definitions and variable declarations at the top of our file. But, we haven’t used our functions and variables to write out the game loop for our game. This is a perfect scenario for the use of a while loop. We want to keep looping through our game logic unless the user has quit.

Let’s change our code again:

```python
def show_welcome_message():
    welcome_message = “Welcome to Rock, Paper, Scissors!”
    print(welcome_message)


def get_historical_data():
    text_file = open(“history.txt”, “r”)
    text_data = text_file.read().split(“,”)
    text_file.close()
    return {
        “wins”: int(text_data[0]),
        “ties”: int(text_data[1]),
        “losses”: int(text_data[2])
    }


def show_historical_data_message():
    print(historical_data_message %
          (score[“wins”], score[“ties”], score[“losses”]))


def get_user_choice():
    choice = input(“[1] rock   [2] paper   [3] scissors    [9] quit\n”)
    return choice_options[int(choice)]


def quit_game(wins, ties, losses):
    text_file = open(“history.txt”, “w”)
    text_file.write(str(wins) + “,” + str(ties) + “,” + str(losses))
    text_file.close()


def compare_choices_and_get_result(user, computer):
    if user == computer:
        return “tie”
    elif (user == “rock” and computer == “scissors”) or (user == “paper” and computer == “rock”) or (user == “scissors” and computer == “paper”):
        return “win”
    else:
        return “loss”


def display_result_message_and_update_score(result):
    if result == “tie”:
        print(tie_message)
        score[“ties”] += 1
    elif result == “win”:
        print(win_message)
        score[“wins”] += 1
    else:
        print(loss_message)
        score[“losses”] += 1

score =  {
    “wins”: 0,
    “ties”: 0,
    “losses”: 0
}

welcome_message = “Welcome to Rock, Paper, Scissors!”
historical_data_message = “Wins: %s, Ties: %s, Losses: %s”
quit_message = “Thanks for playing Rock, Paper, Scissors!”
win_message = “Congratulations, you won!”
loss_message = “Sorry, you lost!”
tie_message = “It was a tie.”

historical_data = get_historical_data()
score[“wins”] = historical_data[“wins”]
score[“ties”] = historical_data[“ties”]
score[“losses”] = historical_data[“losses”]

choice_options = {
    1: “rock”,
    2: “paper”,
    3: “scissors”,
    9: “quit”
}

### Start of Game
show_welcome_message()
show_historical_data_message()

### First user choice
user_choice = get_user_choice()

### Game Loop
while user_choice != “quit”:
    computer_choice = choice_options[random.randint(1, 3)]
    result = compare_choices_and_get_result(user_choice, computer_choice)
    display_result_message_and_update_score(result)
    user_choice = get_user_choice()

### Quit game if user exits game loop
quit_game(score[“wins”], score[“ties”], score[“losses”])
```

Now, we have a functioning Rock, Paper, Scissors game!
