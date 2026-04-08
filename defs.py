#Import library
import os;

#Creating Variables
company_name = "Popcorn Palace Rentals";
inventory = [
    {"name": "Z", "genres": "Drama 🎭", "rating": "⭐"},
]


#Creating defs
def title(emoji, text):
    print("\n" + "=" * 40);
    print(f"{emoji} {text.center(36).upper()}");
    print("=" * 40);

def clean():
    os.system('cls' if os.name == 'nt' else 'clear')

def attendant_message(emoji, message):
    print("=" * 40);
    print(f"🍿{company_name.center(36).upper()}🍿")
    print("=" * 40);
    print(f"{emoji} -{message}")
    print("""
[a] Rent a movie
[b] Return a movie
[c] View available movies
[d] Search for a movie
[e] View rented movies
[f] Exit""");

def storage(storage, name):
    for i in storage:
        print(i[f"{name}"]);
    print("=" * 40);

def storage_table(storage):
    for i in storage:
        print(f"{i['name']:<10} {i['genres']:<20} {i['rating']}")
    print("=" * 40);