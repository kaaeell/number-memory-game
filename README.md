# 🎲 Number Memory Game – CLI Brain Trainer

A simple terminal-based memory game built with Python.

The goal is simple:
Memorize the number shown on the screen before it disappears.

Each level:
- The number gets longer
- The display time gets shorter
- The challenge increases

---

## 🚀 Why I Built This

I wanted to build a small interactive project that:
- Uses randomness
- Uses time control
- Has increasing difficulty
- Is fun to play

Instead of making another calculator app, I built a mini brain-training game.

---

## 🧠 How It Works

1. The program generates a random number.
2. The number is displayed for a few seconds.
3. The screen clears.
4. You must type the number from memory.
5. If correct → next level.
6. If wrong → game over.

The difficulty increases automatically.

---

## 🛠️ Technologies Used

- Python 3
- `random` module
- `time` module
- `os` module (for clearing terminal)

No external libraries required.

---

## 💻 How to Run

Make sure you have Python 3 installed.

```bash
python memory_game.py
```

---

## 📸 Example Gameplay

```
Level 1
Memorize this number:
482

Enter the number:
> 482

Correct! Moving to Level 2...
```

---

## 🔥 Future Improvements

- Add score system
- Save high score to file
- Add difficulty modes
- Add limited lives
- Add colored terminal output