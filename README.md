# 🍿 Popcorn Palace Rentals

> A terminal-based movie rental store built entirely in Python — browse, rent, return, and order food, all from the command line.

This is my first Python project, built from scratch to practice core concepts like functions, classes, lists, dictionaries, control flow, and modular code organization.

---

## 📋 Features

### 🎬 Movies
- Browse the full catalog of **151 movies** across **11 genres**
- Filter by genre, rating (⭐ / ⭐⭐ / ⭐⭐⭐), or award-winning titles 🏆
- Search by name (partial match supported — type `"dark"` to find `"The Dark Knight"`)
- **Surprise Me** — get a random movie picked for you
- Favorite movies with `fav` and reserve them with `res`
- Real stock control — each title has limited copies

### 🛒 Renting
- Select movies by index or by typing part of the name
- Confirmation screen before renting — shows genre, rating, stock, price and balance
- Balance system — each rental deducts from your account
- Transaction loading animation ✅ / ❌

### 📦 Returning
- Return by index or partial name
- Stock is automatically restored on return

### 🍔 Foods & Drinks
- Order from a menu of **45 items** (burgers, pizza, ramen, desserts and more)
- Each item has a price — balance is checked before purchase
- Order by name or index

### 👤 User Profile
- View your current rentals and order history
- Favorites list and reservations
- Account overview: balance, total rentals, food orders

---

## 🗂️ Project Structure

```
popcorn-palace-rentals/
│
├── store.py           # Main loop — entry point of the app
├── defs.py            # All functions, classes and UI logic
├── movies_storage.py  # Movie catalog (151 titles)
└── foods_storage.py   # Food & drinks menu (45 items)
```

---

## 🚀 How to Run

**Requirements:** Python 3.10 or higher (uses `match/case`)

```bash
# Clone the repository
git clone https://github.com/your-username/popcorn-palace-rentals.git

# Navigate to the project folder
cd popcorn-palace-rentals

# Run the app
python store.py
```

No external libraries needed — only Python's standard library (`os`, `time`, `random`, `json`, `datetime`).

---

## 🎮 How to Use

Once running, navigate using the letter keys shown in the menu:

```
[a] Available movies    → browse and rent
[b] Return a movie      → return by name or number
[c] View rented movies  → see your current rentals
[d] Foods & Drink       → order snacks
[e] User                → profile, history, favorites
[f] Exit & Save
```

**Inside the movie browser:**
```
[a] View all movies
[b] Recommended ⭐⭐⭐
[c] Surprise me 🎲
[d] Hall of fame 🏆
[e] Search by name
[f] Search by genre
[g] Filter by rating
[h] Favorites ❤️
```

**Renting tips:**
- Type a number to select: `5`
- Type part of the name: `inception`
- Add `fav` to favorite: `5 fav`
- Add `res` to reserve: `5 res`

---

## 🎥 Movie Catalog

| Genre | Titles |
|---|---|
| Drama 🎭 | 30 |
| Horror 👻 | 22 |
| Action 🧭 | 21 |
| Animation 🎨 | 17 |
| Sci-Fi 🚀 | 15 |
| Thriller 😱 | 14 |
| Comedy 😂 | 9 |
| Romance 💕 | 9 |
| Fantasy 🧙 | 8 |
| Adventure 🧭 | 5 |
| Documentary 🎥 | 1 |

Includes **34 award-winning titles** such as The Dark Knight, Interstellar, Inception, Titanic, and The Lord of the Rings.

---

## 🧱 Built With

- **Python 3.10+**
- `match/case` for menu navigation
- Classes (`User`) for state management
- Modular structure across multiple files
- Standard library only — no pip installs

---

## 👨‍💻 Author

Built by Julio André.

Feel free to open issues, suggest features, or just explore the code!
