# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] The game's purpose is to create a guessing game where the user has to guess a specific number in a range within a certain number of guesses. However, the game has a lot of bugs and issues that mess with the game logic. Therefore, you have to fix these bugs to make the game work properly.
- [ ] First, I found a bug with the difficulty levels where the ranges and number of attempts are inconsistent. Also, the hint after each guess does not work and the new game button also does not work. The score also is calculated incorrectly.
- [ ] I applied fixes to the difficulty ranges, the new game button, and the hints after each guess. I made the ranges consistent (easy: 1-20, normal: 1-50, hard: 1-100). I made the new game button correctly restart the game. Finally, the hints actually work properly and tell the user to guess higher or lower based on the secret number and their previous guess.

## 📸 Demo

- [ ] ![Demo Screenshot](https://i.imgur.com/IzO8UKf.png)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
