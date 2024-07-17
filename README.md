# Dino-Plus
![intro](/figs/intro.gif)
### Video Demo:  <https://www.youtube.com/watch?v=aRjIwt7jzKA>

## Introduction
This project involves creating the classic Chrome Dino-Plus game using the Pygame library in Python. The game will feature various phases, each with specific requirements and optional enhancements to improve gameplay and user experience.

## Phase 1: Basic Implementation

### Game Start Screen
The game starts with an introductory screen that includes:
- **Game Logo**: Displays the logo of the game prominently.
- **Instructions**: Prompts the user to press any key to start the game.
- **High Score**: Optionally displays the highest score achieved by the player.

### Dinosaur Character
The dinosaur character will have the following behaviors:
- **Running**: The dinosaur will alternate between two images to simulate running.
- **Jumping**: The dinosaur can jump when a specific key is pressed.
- **Ducking**: The dinosaur can duck when another key is pressed.

### Obstacles
The game will include obstacles (cacti) that the dinosaur must avoid by jumping or ducking. Key details include:
- **Variety of Cacti**: Different types and sizes of cacti.
- **Random Generation**: Obstacles are generated at random intervals.

### Scoring System
The game will track the player’s score based on the distance covered. Key points include:
- **Score Increment**: The score increases as the dinosaur runs.
- **Score Reset**: The score resets to zero upon collision with an obstacle.

## Phase 2: Advanced Features

### Night Mode
The game will check the system time and switch to a dark mode theme if it’s nighttime. Additionally, the game will switch between day and night modes every 2000 points.

### Power-Ups
The game will feature various power-ups to enhance gameplay:
1. **Extra Life Potion**: Appears every 1000 points and grants the dinosaur an extra life.
   - **Sound Effect**: Plays a sound when collected.
   - **Visual Indicator**: Displays an icon next to the dinosaur to indicate the extra life.

2. **Temporary Immortality Potion**: Appears every 2700 points, granting the dinosaur 15 seconds of invincibility when activated by pressing 'H'.
   - **Sound Effect**: Plays a special sound when collected.
   - **Visual Indicator**: Displays an icon to indicate the temporary invincibility.

3. **Speed Potion**: Appears every 700 points, randomly doubling or halving the dinosaur’s speed.
   - **Immediate Activation**: Activates immediately upon collection.
   - **Avoidable**: Can be avoided by jumping over it.

### Sound Effects
To enhance the gaming experience, various sound effects will be added:
- **Jumping Sound**: Plays when the dinosaur jumps.
- **Collision Sound**: Plays when the dinosaur hits an obstacle.
- **Power-Up Sounds**: Unique sounds for collecting each type of power-up.

### Pause Functionality
The game will include a pause feature, allowing the player to pause and resume the game by pressing a specific key.

## Conclusion
The Dino T-Rex game project involves creating a fun and engaging game with multiple phases and features. Starting with the basic implementation of the game mechanics and extending to advanced features like night mode, power-ups, and sound effects, this project aims to provide a comprehensive and enjoyable user experience. The use of object-oriented programming principles is mandatory to ensure a well-structured and maintainable codebase.
