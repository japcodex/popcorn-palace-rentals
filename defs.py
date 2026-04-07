#Import library
import os;


#Creating defs
def title(emoji, text):
    print("\n" + "=" * 40);
    print(f"{emoji} {text.center(36).upper()}");
    print("=" * 40);

def clean():
    os.system('cls' if os.name == 'nt' else 'clear')

def default_message():
    print("""
===========================
🍿POPCORN PALACE RENTALS🍿
===========================

🙋- OK, What would you like?

[a] Rent a movie
[b] Return a movie
[c] View available movies
[d] Search for a movie
[e] View rented movies
[f] Exit""");