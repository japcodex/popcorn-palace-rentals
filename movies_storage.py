#Movies genres:
# Comedy 😂
# Drama 🎭
# Horror 👻
# Sci-Fi 🚀
# Romance 💕
# Thriller 😱
# Adventure 🧭
# Animation 🎨
# Fantasy 🧙
# Documentary 🎥

#Ratings:
# ⭐ stars
# 🏆 awards

#Creating my storage
movies = [
    {"name": "The Dark Knight", "genres": "Drama 🎭", "rating": 3, "total_stock": 5, "stock": 5}, # 🏆
    {"name": "Interstellar", "genres": "Sci-Fi 🚀", "rating": 3, "total_stock": 5, "stock": 5}, # 🏆
    {"name": "Titanic", "genres": "Romance 💕", "rating": 3, "total_stock": 5, "stock": 5}, # 🏆
    {"name": "The Room", "genres": "Drama 🎭", "rating": 1, "total_stock": 5, "stock": 5},
    {"name": "The Conjuring", "genres": "Horror 👻", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Cats", "genres": "Fantasy 🧙", "rating": 1, "total_stock": 5, "stock": 5},
    {"name": "Inception", "genres": "Sci-Fi 🚀", "rating": 3, "total_stock": 5, "stock": 5}, # 🏆
    {"name": "Toy Story", "genres": "Animation 🎨", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "The Emoji Movie", "genres": "Animation 🎨", "rating": 1, "total_stock": 5, "stock": 5},
    {"name": "The Lord of the Rings", "genres": "Fantasy 🧙", "rating": 3, "total_stock": 5, "stock": 5}, # 🏆
    {"name": "Joker", "genres": "Drama 🎭", "rating": 3, "total_stock": 5, "stock": 5}, # 🏆
    {"name": "Parasite", "genres": "Thriller 😱", "rating": 3, "total_stock": 5, "stock": 5}, # 🏆
    {"name": "Get Out", "genres": "Horror 👻", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "The Social Dilemma", "genres": "Documentary 🎥", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "Avengers: Endgame", "genres": "Adventure 🧭", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Morbius", "genres": "Action 🧭", "rating": 1, "total_stock": 5, "stock": 5},
    {"name": "La La Land", "genres": "Romance 💕", "rating": 3, "total_stock": 5, "stock": 5}, # 🏆
    {"name": "Shrek", "genres": "Animation 🎨", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Mad Max: Fury Road", "genres": "Action 🧭", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Gladiator", "genres": "Drama 🎭", "rating": 3, "total_stock": 5, "stock": 5}, # 🏆
    {"name": "The Matrix", "genres": "Sci-Fi 🚀", "rating": 3, "total_stock": 5, "stock": 5}, # 🏆
    {"name": "It", "genres": "Horror 👻", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "Frozen", "genres": "Animation 🎨", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "The Notebook", "genres": "Romance 💕", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "Se7en", "genres": "Thriller 😱", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Up", "genres": "Animation 🎨", "rating": 3, "total_stock": 5, "stock": 5}, # 🏆
    {"name": "Superbad", "genres": "Comedy 😂", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "Batman & Robin", "genres": "Action 🧭", "rating": 1, "total_stock": 5, "stock": 5},
    {"name": "The Godfather", "genres": "Drama 🎭", "rating": 3, "total_stock": 5, "stock": 5}, # 🏆
    {"name": "Pulp Fiction", "genres": "Drama 🎭", "rating": 3, "total_stock": 5, "stock": 5}, # 🏆
    {"name": "Fight Club", "genres": "Drama 🎭", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "The Hangover", "genres": "Comedy 😂", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "Scary Movie", "genres": "Comedy 😂", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "Hereditary", "genres": "Horror 👻", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Insidious", "genres": "Horror 👻", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "The Nun", "genres": "Horror 👻", "rating": 1, "total_stock": 5, "stock": 5},
    {"name": "Twilight", "genres": "Romance 💕", "rating": 1, "total_stock": 5, "stock": 5},
    {"name": "John Wick", "genres": "Action 🧭", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Transformers", "genres": "Sci-Fi 🚀", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "Minions", "genres": "Animation 🎨", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "Black Swan", "genres": "Drama 🎭", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "The Grand Budapest Hotel", "genres": "Comedy 😂", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "1917", "genres": "Drama 🎭", "rating": 3, "total_stock": 5, "stock": 5}, # 🏆
    {"name": "Tenet", "genres": "Sci-Fi 🚀", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "The Batman", "genres": "Action 🧭", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Logan", "genres": "Action 🧭", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Jaws", "genres": "Horror 👻", "rating": 3, "total_stock": 5, "stock": 5}, # 🏆
    {"name": "Alien", "genres": "Horror 👻", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Aliens", "genres": "Action 🧭", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "The Thing", "genres": "Horror 👻", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Casablanca", "genres": "Romance 💕", "rating": 3, "total_stock": 5, "stock": 5}, # 🏆
    {"name": "The Truman Show", "genres": "Drama 🎭", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Catch Me If You Can", "genres": "Drama 🎭", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "The Departed", "genres": "Thriller 😱", "rating": 3, "total_stock": 5, "stock": 5}, # 🏆
    {"name": "Goodfellas", "genres": "Drama 🎭", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Scarface", "genres": "Drama 🎭", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "The Big Lebowski", "genres": "Comedy 😂", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "The Mask", "genres": "Comedy 😂", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "Bruce Almighty", "genres": "Comedy 😂", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "Ace Ventura", "genres": "Comedy 😂", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "Doctor Strange", "genres": "Fantasy 🧙", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Thor", "genres": "Fantasy 🧙", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "Iron Man", "genres": "Action 🧭", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Captain America: Civil War", "genres": "Action 🧭", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Black Panther", "genres": "Action 🧭", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Cars", "genres": "Animation 🎨", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "Monsters Inc.", "genres": "Animation 🎨", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "The Incredibles", "genres": "Animation 🎨", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Despicable Me", "genres": "Animation 🎨", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "Kung Fu Panda", "genres": "Animation 🎨", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "World War Z", "genres": "Horror 👻", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "I Am Legend", "genres": "Sci-Fi 🚀", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "28 Days Later", "genres": "Horror 👻", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Train to Busan", "genres": "Horror 👻", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "The Ring", "genres": "Horror 👻", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "The Hunger Games", "genres": "Adventure 🧭", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Divergent", "genres": "Sci-Fi 🚀", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "Maze Runner", "genres": "Sci-Fi 🚀", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "Ready Player One", "genres": "Sci-Fi 🚀", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "The Curious Case of Benjamin Button", "genres": "Drama 🎭", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Slumdog Millionaire", "genres": "Drama 🎭", "rating": 3, "total_stock": 5, "stock": 5}, # 🏆
    {"name": "Life of Pi", "genres": "Adventure 🧭", "rating": 3, "total_stock": 5, "stock": 5}, # 🏆
    {"name": "Cast Away", "genres": "Adventure 🧭", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "The Terminal", "genres": "Comedy 😂", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "Shutter Island", "genres": "Thriller 😱", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "The Sixth Sense", "genres": "Thriller 😱", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Split", "genres": "Thriller 😱", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Glass", "genres": "Thriller 😱", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "300", "genres": "Action 🧭", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Troy", "genres": "Action 🧭", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Kingdom of Heaven", "genres": "Action 🧭", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Enchanted", "genres": "Fantasy 🧙", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "Maleficent", "genres": "Fantasy 🧙", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "Snow White and the Huntsman", "genres": "Fantasy 🧙", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "The Lego Movie", "genres": "Animation 🎨", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Spider-Man: Into the Spider-Verse", "genres": "Animation 🎨", "rating": 3, "total_stock": 5, "stock": 5}, # 🏆
    {"name": "Soul", "genres": "Animation 🎨", "rating": 3, "total_stock": 5, "stock": 5}, # 🏆
    {"name": "Turning Red", "genres": "Animation 🎨", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "Fast & Furious", "genres": "Action 🧭", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "Hobbs & Shaw", "genres": "Action 🧭", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "Madagascar", "genres": "Animation 🎨", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "The Fault in Our Stars", "genres": "Romance 💕", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "Love Actually", "genres": "Romance 💕", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Notting Hill", "genres": "Romance 💕", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Bohemian Rhapsody", "genres": "Drama 🎭", "rating": 3, "total_stock": 5, "stock": 5}, # 🏆
    {"name": "Rocketman", "genres": "Drama 🎭", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Elvis", "genres": "Drama 🎭", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "The Avengers", "genres": "Action 🧭", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Guardians of the Galaxy", "genres": "Action 🧭", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Doctor Sleep", "genres": "Horror 👻", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "Coraline", "genres": "Animation 🎨", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "ParaNorman", "genres": "Animation 🎨", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "The Lighthouse", "genres": "Horror 👻", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Midsommar", "genres": "Horror 👻", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Knives Out", "genres": "Thriller 😱", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Glass Onion", "genres": "Thriller 😱", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "The Menu", "genres": "Thriller 😱", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Barbarian", "genres": "Horror 👻", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Nope", "genres": "Horror 👻", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Us", "genres": "Horror 👻", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "The Flash", "genres": "Action 🧭", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "Aquaman", "genres": "Action 🧭", "rating": 2, "total_stock": 5, "stock": 5},
    {"name": "The Whale", "genres": "Drama 🎭", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Marriage Story", "genres": "Drama 🎭", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "The Northman", "genres": "Action 🧭", "rating": 3, "total_stock": 5, "stock": 5},
    {"name": "Everything Everywhere All at Once", "genres": "Sci-Fi 🚀", "rating": 3, "total_stock": 5, "stock": 5}, # 🏆
]