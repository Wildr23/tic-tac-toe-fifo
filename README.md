# Tic Tac Toe 🎮 - Independent FIFO Edition

A unique version where **X and O each have their own 3-mark limit**! When a player places their 4th mark, the oldest mark of THAT SAME TYPE is removed.

## Files Included

- `index.html` - Main HTML file for the web version
- `styles.css` - Beautiful gradient styling with animations  
- `script.js` - JavaScript game logic with independent FIFO mode
- `tic_tac_toe.py` - Python console-based independent FIFO version
- `README.md` - This file

---

## 🎮 How It Works (Independent FIFO Rules)

### Key Concept: INDEPENDENT QUEUES PER PLAYER!

| Feature | Description |
|---------|-------------|
| **X's Limit** | X can have up to 3 **X marks** on the board |
| **O's Limit** | O can have up to 3 **O marks** on the board |
| **When X plays with 3 X's** | Oldest **X** mark is removed (FIFO) |
| **When O plays with 3 O's** | Oldest **O** mark is removed (FIFO) |

### Total Marks Possible:

- Max **6 marks total** on board at once (3 X + 3 O)
- Each player has their own independent queue!

### The Independent FIFO Mechanism:

```
Move 1: X plays → [X]        (X count: 1)
Move 2: O plays → [X, O]     (X count: 1, O count: 1)
Move 3: X plays → [X, O, X]  (X count: 2, O count: 1)
Move 4: X plays → [O, X, X]  ← Oldest X at pos 1 removed! (X count: 3, O count: 1)
Move 5: O plays → [O, X, X, O] (X count: 2, O count: 2)
Move 6: O plays → [_, X, X, O] ← Oldest O at pos 4 removed! Wait... still 3 max
```

### 🏆 How to Win:

You win when your symbol (X or O) occupies **ALL THREE positions** in a row/column/diagonal!

---

## 🌐 Web Version

This modern version runs in any browser.

### How to Run:

1. Open `index.html` in your web browser
2. Click on cells to place X or O
3. Watch marks appear and disappear (Independent FIFO!)

### Game Flow Example:

```
Start → X at 5 → [X]         (X count: 1, O count: 0)
O at 4 → [X, O]              (X count: 1, O count: 1)  
X at 3 → [X, O, X]           (X count: 2, O count: 1)
X at 1 → [_, O, X] ← Oldest X removed! (X count: 2, O count: 1)
O at 7 → [_, O, X, O]        (X count: 2, O count: 2)
O at 9 → [_, O, X, _, _] ← Oldest O removed! (X count: 2, O count: 2)
```

### Features:
- ✅ **Independent FIFO** - X and O have separate 3-mark limits
- ✅ Max 6 marks total (3 X + 3 O) on board
- ✅ Smooth animations and visual feedback
- ✅ Score tracking (X, O, draws)
- ✅ Restart button resets everything
- ✅ Winning cell highlighting

---

## 💻 Python Console Version

A terminal-based version for command-line players.

### Requirements:
- Python 3.x installed

### How to Run:

```bash
python tic_tac_toe.py
```

### Example Session:

```
==================================================
TIC TAC TOE - INDEPENDENT FIFO MODE
==================================================
Positions: 1 | 2 | 3
           4 | 5 | 6
           7 | 8 | 9
--------------------------------------------------
RULES:
- X can have up to 3 X marks on the board!
- O can have up to 3 O marks on the board!
- When a player places their 4th mark, THE OLDEST MARK
  OF THE SAME TYPE vanishes (FIFO)!
- First player to get all 3 in a row/column/diagonal WINS!
==================================================

  _ | _ | _  

  ---------
  X | O | _  

  ---------
  _ | _ | _  

Board state: 1 X(s) | 1 O(s)

Player X, enter your position (1-9): 

  _ | _ | _  

  ---------
  X | O | _  

  ---------
  _ | X | _  

Board state: 2 X(s) | 1 O(s)

⚠️ X has max marks (3)! Placing new mark will remove oldest X...
→ FIFO! Removing oldest X at position 1 (X)...

  _ | O | _  

  ---------
  _ | X | _  

  ---------
  _ | X | _  

Board state: 2 X(s) | 1 O(s)

Player O, enter your position (1-9): 

🎉 PLAYER X WINS! 🎉
All 3 marks were in a line!
(Board has 3 X's and 1 O's)
```

### Features:
- ✅ Independent FIFO - X and O tracked separately
- ✅ Clear visual board display
- ⚠️ Warning when player has max marks
- ✅ Shows which mark gets removed
- ✅ Play again option after each game
- ✅ Status messages guide you

---

## 📝 Game Rules Summary

1. **Two players**: X and O
2. **X's limit**: Up to 3 **X marks** on the board
3. **O's limit**: Up to 3 **O marks** on the board
4. **FIFO per player**: When a player places their 4th mark, oldest mark of SAME type is removed
5. **Max total marks**: 6 (3 X + 3 O)
6. **Winning condition**: Own ALL THREE positions in any row, column, or diagonal!

### Winning Lines:
```
Row 1: [ ][ ][ ]      Column 1:  [ ][ ][ ]
Row 2: [ ][ ][ ]       Column 2:   |[ ][ ][ ]
Row 3: [ ][ ][ ]       Column 3:   [ ][ ][ ]
Diag 1: [ ][ ][ ]     
Diag 2: [ ][ ][ ]      
```

### Example Win Scenarios:

**X wins with row 2 (has exactly 3 X's):**
```
  _ | _ | O  
---------
  X | X | X ← ALL THREE ARE X! 🎉
---------
  _ | _ | O  
```

---

## 💡 Tips for Playing

1. **Think strategically**: Where should you place marks to create a winning line?
2. **Watch your count**: Keep track of how many marks YOU have on the board (not total!)
3. **When you have 3 marks**: Your next move will remove your oldest mark - consider if it's worth moving!
4. **Block opponents**: If they have 2 marks in a line, try to break it by placing your mark on one of those spots
5. **Corner advantage**: Corners (1, 3, 7, 9) create multiple winning possibilities

---

## 🎨 Web Version Controls

- **Click** on any empty cell to place your mark
- **Independent FIFO kicks in**: When X has 3 marks, oldest X is removed; when O has 3 marks, oldest O is removed
- **Restart Game** button resets the entire game

---

## 🚀 Quick Start

### For Browser:
```bash
# Just open the file!
index.html
```

### For Console:
```bash
cd B:\Project
python tic_tac_toe.py
```

Enjoy the unique Independent FIFO challenge! 🎯