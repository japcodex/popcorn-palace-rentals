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
    {"name": "The Dark Knight", "genres": "Drama 🎭", "rating": 3}, # 🏆
    {"name": "Interstellar", "genres": "Sci-Fi 🚀", "rating": 3}, # 🏆
    {"name": "Titanic", "genres": "Romance 💕", "rating": 3}, # 🏆
    {"name": "The Room", "genres": "Drama 🎭", "rating": 1},
    {"name": "The Conjuring", "genres": "Horror 👻", "rating": 3},
    {"name": "Cats", "genres": "Fantasy 🧙", "rating": 1},
    {"name": "Inception", "genres": "Sci-Fi 🚀", "rating": 3}, # 🏆
    {"name": "Toy Story", "genres": "Animation 🎨", "rating": 3},
    {"name": "The Emoji Movie", "genres": "Animation 🎨", "rating": 1},
    {"name": "The Lord of the Rings", "genres": "Fantasy 🧙", "rating": 3}, # 🏆
    {"name": "Joker", "genres": "Drama 🎭", "rating": 3}, # 🏆
    {"name": "Parasite", "genres": "Thriller 😱", "rating": 3}, # 🏆
    {"name": "Get Out", "genres": "Horror 👻", "rating": 3},
    {"name": "The Social Dilemma", "genres": "Documentary 🎥", "rating": 2},
    {"name": "Avengers: Endgame", "genres": "Adventure 🧭", "rating": 3},
    {"name": "Morbius", "genres": "Action 🧭", "rating": 1},
    {"name": "La La Land", "genres": "Romance 💕", "rating": 3}, # 🏆
    {"name": "Shrek", "genres": "Animation 🎨", "rating": 3},
    {"name": "Mad Max: Fury Road", "genres": "Action 🧭", "rating": 3},
    {"name": "Gladiator", "genres": "Drama 🎭", "rating": 3}, # 🏆
    {"name": "The Matrix", "genres": "Sci-Fi 🚀", "rating": 3}, # 🏆
    {"name": "It", "genres": "Horror 👻", "rating": 2},
    {"name": "Frozen", "genres": "Animation 🎨", "rating": 3},
    {"name": "The Notebook", "genres": "Romance 💕", "rating": 2},
    {"name": "Se7en", "genres": "Thriller 😱", "rating": 3},
    {"name": "Up", "genres": "Animation 🎨", "rating": 3}, # 🏆
    {"name": "Superbad", "genres": "Comedy 😂", "rating": 2},
    {"name": "Batman & Robin", "genres": "Action 🧭", "rating": 1},
    {"name": "The Godfather", "genres": "Drama 🎭", "rating": 3}, # 🏆
    {"name": "Pulp Fiction", "genres": "Drama 🎭", "rating": 3}, # 🏆
    {"name": "Fight Club", "genres": "Drama 🎭", "rating": 3},
    {"name": "The Hangover", "genres": "Comedy 😂", "rating": 2},
    {"name": "Scary Movie", "genres": "Comedy 😂", "rating": 2},
    {"name": "Hereditary", "genres": "Horror 👻", "rating": 3},
    {"name": "Insidious", "genres": "Horror 👻", "rating": 2},
    {"name": "The Nun", "genres": "Horror 👻", "rating": 1},
    {"name": "Twilight", "genres": "Romance 💕", "rating": 1},
    {"name": "John Wick", "genres": "Action 🧭", "rating": 3},
    {"name": "Transformers", "genres": "Sci-Fi 🚀", "rating": 2},
    {"name": "Minions", "genres": "Animation 🎨", "rating": 2},
    {"name": "Black Swan", "genres": "Drama 🎭", "rating": 3},
    {"name": "The Grand Budapest Hotel", "genres": "Comedy 😂", "rating": 3},
    {"name": "1917", "genres": "Drama 🎭", "rating": 3}, # 🏆
    {"name": "Tenet", "genres": "Sci-Fi 🚀", "rating": 2},
    {"name": "The Batman", "genres": "Action 🧭", "rating": 3},
    {"name": "Logan", "genres": "Action 🧭", "rating": 3},
    {"name": "Jaws", "genres": "Horror 👻", "rating": 3}, # 🏆
    {"name": "Alien", "genres": "Horror 👻", "rating": 3},
    {"name": "Aliens", "genres": "Action 🧭", "rating": 3},
    {"name": "The Thing", "genres": "Horror 👻", "rating": 3},
    {"name": "Casablanca", "genres": "Romance 💕", "rating": 3}, # 🏆
    {"name": "The Truman Show", "genres": "Drama 🎭", "rating": 3},
    {"name": "Catch Me If You Can", "genres": "Drama 🎭", "rating": 3},
    {"name": "The Departed", "genres": "Thriller 😱", "rating": 3}, # 🏆
    {"name": "Goodfellas", "genres": "Drama 🎭", "rating": 3},
    {"name": "Scarface", "genres": "Drama 🎭", "rating": 3},
    {"name": "The Big Lebowski", "genres": "Comedy 😂", "rating": 2},
    {"name": "The Mask", "genres": "Comedy 😂", "rating": 2},
    {"name": "Bruce Almighty", "genres": "Comedy 😂", "rating": 2},
    {"name": "Ace Ventura", "genres": "Comedy 😂", "rating": 2},
    {"name": "Doctor Strange", "genres": "Fantasy 🧙", "rating": 3},
    {"name": "Thor", "genres": "Fantasy 🧙", "rating": 2},
    {"name": "Iron Man", "genres": "Action 🧭", "rating": 3},
    {"name": "Captain America: Civil War", "genres": "Action 🧭", "rating": 3},
    {"name": "Black Panther", "genres": "Action 🧭", "rating": 3},
    {"name": "Cars", "genres": "Animation 🎨", "rating": 2},
    {"name": "Monsters Inc.", "genres": "Animation 🎨", "rating": 3},
    {"name": "The Incredibles", "genres": "Animation 🎨", "rating": 3},
    {"name": "Despicable Me", "genres": "Animation 🎨", "rating": 2},
    {"name": "Kung Fu Panda", "genres": "Animation 🎨", "rating": 3},
    {"name": "World War Z", "genres": "Horror 👻", "rating": 2},
    {"name": "I Am Legend", "genres": "Sci-Fi 🚀", "rating": 3},
    {"name": "28 Days Later", "genres": "Horror 👻", "rating": 3},
    {"name": "Train to Busan", "genres": "Horror 👻", "rating": 3},
    {"name": "The Ring", "genres": "Horror 👻", "rating": 2},
    {"name": "The Hunger Games", "genres": "Adventure 🧭", "rating": 3},
    {"name": "Divergent", "genres": "Sci-Fi 🚀", "rating": 2},
    {"name": "Maze Runner", "genres": "Sci-Fi 🚀", "rating": 2},
    {"name": "Ready Player One", "genres": "Sci-Fi 🚀", "rating": 3},
    {"name": "The Curious Case of Benjamin Button", "genres": "Drama 🎭", "rating": 3},
    {"name": "Slumdog Millionaire", "genres": "Drama 🎭", "rating": 3}, # 🏆
    {"name": "Life of Pi", "genres": "Adventure 🧭", "rating": 3}, # 🏆
    {"name": "Cast Away", "genres": "Adventure 🧭", "rating": 3},
    {"name": "The Terminal", "genres": "Comedy 😂", "rating": 2},
    {"name": "Shutter Island", "genres": "Thriller 😱", "rating": 3},
    {"name": "The Sixth Sense", "genres": "Thriller 😱", "rating": 3},
    {"name": "Split", "genres": "Thriller 😱", "rating": 3},
    {"name": "Glass", "genres": "Thriller 😱", "rating": 2},
    {"name": "300", "genres": "Action 🧭", "rating": 3},
    {"name": "Troy", "genres": "Action 🧭", "rating": 3},
    {"name": "Kingdom of Heaven", "genres": "Action 🧭", "rating": 3},
    {"name": "Enchanted", "genres": "Fantasy 🧙", "rating": 2},
    {"name": "Maleficent", "genres": "Fantasy 🧙", "rating": 2},
    {"name": "Snow White and the Huntsman", "genres": "Fantasy 🧙", "rating": 2},
    {"name": "The Lego Movie", "genres": "Animation 🎨", "rating": 3},
    {"name": "Spider-Man: Into the Spider-Verse", "genres": "Animation 🎨", "rating": 3}, # 🏆
    {"name": "Soul", "genres": "Animation 🎨", "rating": 3}, # 🏆
    {"name": "Turning Red", "genres": "Animation 🎨", "rating": 2},
    {"name": "Fast & Furious", "genres": "Action 🧭", "rating": 2},
    {"name": "Hobbs & Shaw", "genres": "Action 🧭", "rating": 2},
    {"name": "Madagascar", "genres": "Animation 🎨", "rating": 2},
    {"name": "The Fault in Our Stars", "genres": "Romance 💕", "rating": 2},
    {"name": "Love Actually", "genres": "Romance 💕", "rating": 3},
    {"name": "Notting Hill", "genres": "Romance 💕", "rating": 3},
    {"name": "Bohemian Rhapsody", "genres": "Drama 🎭", "rating": 3}, # 🏆
    {"name": "Rocketman", "genres": "Drama 🎭", "rating": 3},
    {"name": "Elvis", "genres": "Drama 🎭", "rating": 3},
    {"name": "The Avengers", "genres": "Action 🧭", "rating": 3},
    {"name": "Guardians of the Galaxy", "genres": "Action 🧭", "rating": 3},
    {"name": "Doctor Sleep", "genres": "Horror 👻", "rating": 2},
    {"name": "Coraline", "genres": "Animation 🎨", "rating": 3},
    {"name": "ParaNorman", "genres": "Animation 🎨", "rating": 2},
    {"name": "The Lighthouse", "genres": "Horror 👻", "rating": 3},
    {"name": "Midsommar", "genres": "Horror 👻", "rating": 3},
    {"name": "Knives Out", "genres": "Thriller 😱", "rating": 3},
    {"name": "Glass Onion", "genres": "Thriller 😱", "rating": 2},
    {"name": "The Menu", "genres": "Thriller 😱", "rating": 3},
    {"name": "Barbarian", "genres": "Horror 👻", "rating": 3},
    {"name": "Nope", "genres": "Horror 👻", "rating": 3},
    {"name": "Us", "genres": "Horror 👻", "rating": 3},
    {"name": "The Flash", "genres": "Action 🧭", "rating": 2},
    {"name": "Aquaman", "genres": "Action 🧭", "rating": 2},
    {"name": "The Whale", "genres": "Drama 🎭", "rating": 3},
    {"name": "Marriage Story", "genres": "Drama 🎭", "rating": 3},
    {"name": "The Northman", "genres": "Action 🧭", "rating": 3},
    {"name": "Everything Everywhere All at Once", "genres": "Sci-Fi 🚀", "rating": 3}, # 🏆
]