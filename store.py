#Import library
from movies_storage import movies;


# print(*movies, sep="\n");

print("""
===========================
🍿POPCORN PALACE RENTALS🍿
===========================

🙋- Welcome to Popcorn Palace!
What would you like to do today?

[a] Rent a movie
[b] Return a movie
[c] View available movies
[d] Search for a movie
[e] View rented movies
[f] Exit

Please choose an option:""");
selec = input().lower();
print(selec);