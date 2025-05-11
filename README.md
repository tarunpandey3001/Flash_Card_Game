# 🇫🇷 Python French Flash Cards 🎴

An interactive **desktop flash card app** built with Python to help users **learn and revise French vocabulary**. The program displays a French word, gives users time to recall the translation, and then reveals the English meaning — all through a friendly GUI.

---

## 🧠 Features

- 🖼️ **Graphical User Interface** with `Tkinter`
- 📖 **CSV Word Bank** powered by `pandas`
- 🔁 **Randomized Flash Cards** using `random`
- ✅ **Track Mastered Words** – Automatically skips known words
- 💾 **Progress Saved** to file

---

## 📂 How It Works

1. French word appears first.
2. After a few seconds, the English meaning is revealed.
3. You can mark the word as *Known* or *Still Learning*.
4. The app adapts by removing mastered words from the pool.

---

## 🛠 Built With

- **Python 3**
- **Tkinter** – GUI rendering
- **pandas** – DataFrame for reading and updating word lists
- **random** – For randomized card shuffling

---

## 🚀 Getting Started

### 🔧 Installation

Make sure you have Python 3 installed.

```bash
git clone https://github.com/tarunpandey3001/Flash_Card_Game.git
cd Flash_Card_Game
pip install pandas
python main.py
