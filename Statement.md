Car Racing Game – Project Statement

1. Problem Statement

The Car Racing Game is a simple, text-based game developed in Python. The player controls a car on a road with three lanes and must avoid an enemy vehicle that appears randomly in one of the lanes.

The game also checks whether the player tries to cross the left or right road boundary. The game ends when a collision or boundary violation occurs, or when the player chooses to quit.

---

2. Scope of the Project

The project focuses on developing a basic interactive game using fundamental Python programming concepts.

It includes:

- Initializing the player's car position and score.
- Generating a random enemy position in one of the three lanes.
- Displaying the road, enemy position, and player's car position.
- Accepting movement commands from the player.
- Supporting left and right movement, along with the "AA" and "DD" shortcut commands.
- Detecting collisions and road-boundary violations.
- Displaying the final score when the game ends.

The current version is a console-based game. It does not include graphics, saved high scores, or a database.

---

3. Target Users

- Students learning Python and basic programming concepts.
- Beginners interested in simple, command-line games.
- Users who want to practice logical thinking and decision-making through a small interactive game.

---

4. High-Level Features

- Three-lane road: The player can move across lanes 1, 2, and 3.
- Random enemy generation: The enemy's lane is selected randomly in each round.
- Player controls: "A" moves left, "D" moves right, "DD" moves from lane 1 to lane 3, and "AA" moves from lane 3 to lane 1.
- Collision detection: The game ends if the enemy and player's car occupy the same lane at the collision check.
- Boundary detection: Attempting to move left from lane 1 or right from lane 3 ends the game.
- Quit option: The player can enter "Q" to end the game.
- Score display: The score is shown when the game ends.
