# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game looked like a normal guessing game where the user has to guess a number between 1 and 100 with 8 attempts. Difficult levels decrease or increase the range the number can be in. There are also buttons to start a new game, submit your guess, and show hints.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
First, the "New Game" button does not work correctly. It just takes an attempt and does not reset the game. Second, the hints are incorrect. When the answer is higher, it would say "go lower". Third, the difficulty levels are mixed up. The hard level has a range of 1 to 50 while the normal is 1 to 100.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Copilot for this project.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
I asked Copilot to explain why the ranges across difficult levels were inconsistent. Copilot correctly found that the difficulty ranges were implemented incorrectly and suggested a correction that made sense. I verified the result by first checking logic_utils.py that the refactored code contained the correct logic. Then, I checked the pytest that Copilot generated to make sure it correctly tested the fix. Finally, I ran the app to check if the fix was correcty implemented.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
I asked Copilot to verify that the issues with the difficulty levels were fixed. However, it only fixed the number ranges and not the number of attempts per difficulty level. The number of attempts were also inconsistent, so the AI suggestion was misleading. I verified this by looking through app.py for the issue and running the app and seeing the issue. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I first checked the suggested code fix to see if the logic was fixed properly. Then, I verified that the pytest that Copilot generated actually checked for the fix. Finally, I ran the app to see that the problem was solved and the fix is working properly.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I ran a pytest test that checked that the difficulty level that is selected has a consistent and logical range that the secret number can fall into. It showed me that my code checks difficulty levels easy, normal, and hard against each other to ensure consistency.
- Did AI help you design or understand any tests? How?
Yes, AI helped me design several of my tests. I used ask and plan mode to understand how Copilot was generating the tests and making sure they would actually test if the fix is working properly. Then, I used agent mode to implement the fix as planned.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
