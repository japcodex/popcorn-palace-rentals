#Import library
import os;

#Creating Variables
company_name = "Popcorn Palace Rentals";
inventory = [
    {"name": "Z", "genres": "Drama 🎭", "rating": "1"},
]
width = 60;


#Creating defs
def title(emoji, text):
    print("\n" + "=" * width);
    print(f"{emoji} {text.center(width - 6).upper()}");
    print("=" * width);

def clean():
    os.system('cls' if os.name == 'nt' else 'clear')

def attendant_message(emoji, message):
    print("=" * width);
    print(f"🍿{company_name.center(width - 6).upper()}🍿")
    print("=" * width);
    print(f"{emoji} -{message}")
    print("""
[a] Rent a movie
[b] Return a movie
[c] View available movies
[d] Search for a movie
[e] View rented movies
[f] Exit""");

def storage(storage, name):
    for index, i in enumerate(storage, start=1):
        print(f"{index}.", i[f"{name}"]);
    print("=" * width);

def storage_table(storage):
    print(f"{'NAME':<30} {'GENRES':<16} {'RATING'}")
    print("-" * width)
    
    for index, i in enumerate(storage, start=1):
        stars = "⭐" * int(i["rating"])
        print(f"{index:<3}. {i['name']:<25} {i['genres']:<15} {stars:<5}")
    
    print("=" * width)