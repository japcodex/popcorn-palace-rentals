#Import library
from movies_storage import movies;
from defs import *


print("""
===========================
🍿POPCORN PALACE RENTALS🍿
===========================

🙋 -Welcome to Popcorn Palace!
What would you like to do today?

[a] Rent a movie
[b] Return a movie
[c] View available movies
[d] Search for a movie
[e] View rented movies
[f] Exit""");

while True:
    selec = input("\nPlease choose an option: \n➤ ").lower();

    match selec:
        case "a":
            ...;

        
        case "b":
            ...;

        case "c":
            clean();
            title("📦", "Our Storage");
            for m in movies:
                print(m["name"]);
            
            print("=" * 40, "\n💁 -Do you wanna any movie?")
            print("[a] Yes \n[b] No");

            if selec == "a":
                print("💁 -What´s the movie? ");

            if selec == "b":
                clean();
                default_message();

        case "d":
            clean();
            title("🔍", "Search");
            print(*movies, sep="\n");
            print("=" * 40);

        case "e":
            ...
        
        case "f":
            clean();
            print("🙋 -Ok, see you soon")
            break;

        case _:
            clean();
            print("""
===========================
🍿POPCORN PALACE RENTALS🍿
===========================

🙍 -Sorry, I don´t urdestand your message, try again please!

[a] Rent a movie
[b] Return a movie
[c] View available movies
[d] Search for a movie
[e] View rented movies
[f] Exit""");