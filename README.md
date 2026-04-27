<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=13&duration=3000&pause=1000&color=F5C518&center=true&vCenter=true&width=500&lines=Terminal-based+movie+rental+store+%F0%9F%8E%AC;Built+entirely+in+Python+%F0%9F%90%8D;Browse+%E2%80%A2+Rent+%E2%80%A2+Return+%E2%80%A2+Order+Food" alt="Typing SVG" />

<br/>

# 🍿 Popcorn Palace Rentals

<p>
  <img src="https://img.shields.io/badge/Python-3.10+-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" />
  <img src="https://img.shields.io/badge/Version-Alpha%201.9-F5C518?style=for-the-badge&logo=github&logoColor=white" />
  <img src="https://img.shields.io/badge/Libraries-Standard%20Only-4CAF50?style=for-the-badge&logo=checkmarx&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" />
</p>

<p><em>My first Python project — a fully functional movie rental store running right in your terminal.</em></p>

</div>

---

## 🎬 What is this?

**Popcorn Palace Rentals** is a terminal-based movie rental store built from scratch in Python. You can browse a catalog of 151 films, rent them, return them, order food, manage your profile, and much more — all from the command line.

Built to practice Python fundamentals: **functions, classes, lists, dictionaries, control flow, and modular file organization.**

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🎬 Movies
- **151 titles** across 11 genres
- Filter by genre, rating or award 🏆
- Partial name search — `"dark"` finds `"The Dark Knight"`
- **Surprise Me** 🎲 — random pick
- Favorite with `fav`, reserve with `res`
- Real per-title stock control 📦

</td>
<td width="50%">

### 🛒 Renting & Returning
- Select by number or partial name
- Confirmation screen before every rental
- Balance system — rentals deduct from account
- Transaction animation ✅ / ❌
- Return by number or partial name
- Stock auto-restored on return

</td>
</tr>
<tr>
<td width="50%">

### 🍔 Foods & Drinks
- **45 items** — burgers, pizza, ramen, desserts...
- Each item has a price
- Balance checked before every purchase
- Order by name or index

</td>
<td width="50%">

### 👤 User Profile
- Current rentals inventory
- Full order & rental history with timestamps
- Favorites and reservations lists
- Account overview: balance, stats, history count

</td>
</tr>
</table>

---

## 🗂️ Project Structure

```
🍿 popcorn-palace-rentals/
│
├── 📄 store.py            # Main loop — entry point of the app
├── 📄 defs.py             # All functions, classes and UI logic
├── 📄 movies_storage.py   # Movie catalog (151 titles)
└── 📄 foods_storage.py    # Food & drinks menu (45 items)
```

---

## 🚀 How to Run

> **Requirements:** Python 3.10 or higher — the app uses `match/case` syntax.

```bash
# 1. Clone the repository
git clone https://github.com/japcodex/popcorn-palace-rentals.git

# 2. Navigate to the project folder
cd popcorn-palace-rentals

# 3. Run
python store.py
```

**No installations needed.** Uses only Python's standard library — `os`, `time`, `random`, `json`, `datetime`.

---

## 🎮 How to Use

Navigate using the letter keys shown on screen at all times:

```
╔══════════════════════════════════════╗
║       🍿 POPCORN PALACE RENTALS      ║
╠══════════════════════════════════════╣
║  [a] Available movies                ║
║  [b] Return a movie                  ║
║  [c] View rented movies              ║
║  [d] Foods & Drink                   ║
║  [e] User                            ║
║  [f] Exit & Save                     ║
╚══════════════════════════════════════╝
```

**Inside the movie browser `[a]`:**

```
[a] View all movies
[b] Recommended   ⭐⭐⭐
[c] Surprise me   🎲         
[d] Hall of fame  🏆
[e] Search by name    🔍
[f] Search by genre   🎭
[g] Filter by rating  📊
[h] Favorites         ❤️
[i] Back             🔙                         
```

**Quick reference:**

| Action | What to type |
|:---|:---|
| Rent movie #5 | `5` |
| Rent by name | `inception` |
| Favorite movie #5 | `5 fav` |
| Unfavorite | `5 fav` again |
| Reserve movie #5 | `5 res` |
| Unreserve | `5 res` again |
| Go back | `E` or `i` |

---

## 🎥 Movie Catalog

<div align="center">

| Genre | Titles | | Genre | Titles |
|:---|:---:|---|:---|:---:|
| Drama 🎭 | 30 | | Thriller 😱 | 14 |
| Horror 👻 | 22 | | Comedy 😂 | 9 |
| Action 🧭 | 21 | | Romance 💕 | 9 |
| Animation 🎨 | 17 | | Fantasy 🧙 | 8 |
| Sci-Fi 🚀 | 15 | | Adventure 🧭 | 5 |

</div>

Includes **34 award-winning titles** 🏆 — The Dark Knight, Interstellar, Inception, Titanic, The Lord of the Rings, and many more.

---

## 🧱 Built With

<p>
  <img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" />
  <img src="https://img.shields.io/badge/match%2Fcase-Navigation-F5C518?style=for-the-badge" />
  <img src="https://img.shields.io/badge/OOP-User%20Class-3670A0?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Modular-4%20Files-4CAF50?style=for-the-badge" />
</p>

- **`match/case`** — Python 3.10+ structural pattern matching for menu navigation
- **Classes** — `User` object manages state (rentals, balance, history, favorites)
- **Modular structure** — logic, data, and entry point in separate files
- **Standard library only** — zero external dependencies

---

## 👨‍💻 Author

<div align="center">

**Julio André** · [@japcodex](https://github.com/japcodex)

Sistemas de Informação · UTFPR · Paraná, Brasil

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/julioandrecimarosti/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/japcodex)

<br/>

*Feel free to open issues, suggest features, or just explore the code!*

</div>
