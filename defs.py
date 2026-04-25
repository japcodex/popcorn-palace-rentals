#Import library
import os;
import time;
import random;
from movies_storage import movies;

#Creating Variables
company_name = "Popcorn Palace Rentals";
default_width = 80;
width = default_width;
class User:
    def __init__(self):
        self.name = "Guest"
        self.movies = []
        self.foods = []
        self.favorites = []
        self.reserved = []
        self.history = []

user = User()

#Creating defs
def loading(text="Loading"):
    print(text, end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.3)
    print()

def title(emoji, text):
    print("\n" + "=" * width);
    print(f"{emoji} {text.center(width - 6).upper()}");
    print("=" * width);

def clean():
    os.system('cls' if os.name == 'nt' else 'clear')

def exit():
    exit_comand = input("\nPress anything to exit: \n➤ ");
    clean()
    attendant_message("💁", "attendant");

def random_message(tipo):
    mensagens = {
        "success": [
            "Nice choice! Enjoy your movie",
            "Great pick! You're gonna love this one",
            "Done! Anything else?",
            "All set! Enjoy the show",
            "Perfect choice, have fun!",
            "You're all good to go!",
            "That’s a solid pick",
            "Enjoy! Let me know if you need anything else",
            "Boom! Movie night sorted ",
            "Everything’s ready, have a great time!"
        ],
        "error": [
            "Hmm... that doesn’t seem right\nTry again, please!",
            "Oops! Something went wrong\nGive it another try!",
            "I couldn't find that \nPlease try again!",
            "Something went wrong\nLet’s try that once more!",
            "Uh oh... can you check that again?\nTry again, please!",
            "That didn’t work as expected\nGive it another shot!",
            "Error there!\nLet’s try again!",
            "I’m having trouble with that request\nPlease try again!",
            "No luck finding that \nTry again!",
            "That input looks off\nGive it another try!"
        ],
        "attendant": [
            "Alright, what would you like to do next?",
            "What can I help you with now?",
            "Ready for the next step?",
            "What would you like to explore?",
            "Let’s keep going — what’s next?",
            "Anything else you’d like to check?",
            "Your move! What do you want to do?",
            "What are you in the mood for now?",
            "Let me know what you'd like next",
            "Where do we go from here?",
        ],
        "empty": [
            "Nothing available right now\nTry again, please!",
            "Looks like there’s nothing here at the moment\nGive it another try!",
            "No items found \nPlease try again!",
            "There’s nothing to show right now\nTry again, please!",
            "Hmm... seems empty here\nGive it another shot!",
            "No results available at the moment\nPlease try again!",
            "Nothing showed up this time\nTry again, please!",
            "It looks like there’s nothing here yet\nGive it another try!",
            "No luck finding anything \nPlease try again!",
            "This section is empty for now\nTry again, please!"
        ],
    }
    return random.choice(mensagens[tipo])

def welcome_message(emoji, text):
    print("=" * width);
    print(f"🍿{company_name.center(width - 6).upper()}🍿")
    print("=" * width);

    print(f"{emoji} -{text}")
    print("""
[a] Rent a movie
[b] Return a movie
[c] Available movies
[d] View rented movies
[e] Foods & Drinks
[f] User
[g] Exit""");

def attendant_message(emoji, type="welcome", custom_text=None):
    print("=" * width);
    print(f"🍿{company_name.center(width - 6).upper()}🍿")
    print("=" * width);

    if custom_text:
        text = custom_text
    else:
        text = random_message(type)

    print(f"{emoji} -{text}")

    print("""
[a] Rent a movie
[b] Return a movie
[c] Available movies
[d] View rented movies
[e] Foods & Drinks
[f] User
[g] Exit""");

def storage(storage, name):
    for index, i in enumerate(storage, start=1):
        print(f"{index}.", i[f"{name}"]);
    print("=" * width);

def movies_storage_table(storage):
    print(f"{'NAME':<45} {'GENRES':<16} {'RATING':<10} {'STOCK':<10}")
    print("-" * width)
    
    for index, i in enumerate(storage, start=1):
        stars = "⭐" * i["rating"]
        empty = "  " * (3 - i["rating"])  # 2 espaços por estrela faltante
        stars_display = stars + empty

        stock_bar = "📦" * i["stock"]
        empty_stock = "❌" * (i["total_stock"] - i["stock"])
        stock_display = stock_bar + empty_stock

        print(f"{index:<3}. {i['name']:<40} {i['genres']:<15} {stars_display}  {stock_display}")
    print("=" * width)

def view_and_search_movies(movies):
    while True:
        clean();
        title("🎬", "Movies")
        print("[a] View all movies")
        print("[b] Recommended        ⭐⭐⭐")
        print("[c] Surprise me        🎲")
        print("[d] Top rated          🏆")
        print("[e] Award-winning      🏅")
        print("[f] Search by name     🔍")
        print("[g] Search by genre    🎭")
        print("[h] Filter by rating   📊")
        print("[i] Back               🔙")
        print("=" * width)

        new_selec = input("\nPlease choose an option: \n➤ ").lower()

        if new_selec == "a":
            clean()
            title("🎬", "All Movies")
            movies_storage_table(movies)
            input("\nPress Enter to continue...")

        elif new_selec == "b":
            clean()
            title("⭐", "Recommended")
            recommended = [m for m in movies if int(m["rating"]) >= 3]
            if recommended:
                movies_storage_table(recommended)
            else:
                print("No recommended movies available.")
            input("\nPress Enter to continue...")

        elif new_selec == "c":
            clean()
            title("🎲", "Surprise Me!")
            surprise = random.choice(movies)
            movies_storage_table([surprise])
            input("\nPress Enter to continue...")

        elif new_selec == "d":
            clean()
            title("🏆", "Top Rated")
            sorted_movies = sorted(movies, key=lambda m: int(m["rating"]), reverse=True)
            movies_storage_table(sorted_movies)
            input("\nPress Enter to continue...")

        elif new_selec == "e":
            clean()
            awarded = [m for m in movies if int(m["rating"]) == 3]
            title("🏅", "Award-Winning")
            if awarded:
                movies_storage_table(awarded)
            else:
                print("No award-winning movies found.")
                input("\nPress Enter to continue...")

        elif new_selec == "f":
            clean()
            title("🔍", "Search by Name")
            query = input("Type part of the movie name: \n➤ ").upper()
            results = [m for m in movies if query in m["name"].upper()]
            if results:
                movies_storage_table(results)
            else:
                print("❌ No movies found.")
            input("\nPress Enter to continue...")

        elif new_selec == "g":
            clean()
            title("🎭", "Search by Genre")
            genres = sorted(set(m["genres"] for m in movies))
            for i, g in enumerate(genres, 1):
                print(f"[{i}] {g}")
            print("=" * width)

            choice = input("Choose a genre number: \n➤ ")
            if choice.isdigit() and 1 <= int(choice) <= len(genres):
                chosen = genres[int(choice) - 1]
                results = [m for m in movies if m["genres"] == chosen]
                clean()
                title("🎭", chosen)
                movies_storage_table(results)
            else:
                print("❌ Invalid option.")
            input("\nPress Enter to continue...")

        elif new_selec == "h":
            clean()
            title("📊", "Filter by Rating")
            print("[1] ⭐ (bad)")
            print("[2] ⭐⭐ (average)")
            print("[3] ⭐⭐⭐ (great)")
            print("=" * width)

            choice = input("Choose a rating: \n➤ ")
            if choice in ["1", "2", "3"]:
                results = [m for m in movies if int(m["rating"]) == int(choice)]
                clean()
                title("📊", f"Rating: {'⭐' * int(choice)}")
                if results:
                    movies_storage_table(results)
                else:
                    print("No movies with this rating.")
            else:
                print("❌ Invalid option.")
            input("\nPress Enter to continue...")

        elif new_selec == "i":
            clean()
            attendant_message("🙋", "attendant")
            break;

        else:
            clean()
            attendant_message("🙍", "error")

def user_config():
    while True:
        clean()
        title("👤", "User")
        print("[a] Reserved movies")
        print("[b] Favorites")
        print("[c] Inventory")
        print("[d] History")
        print("[e] Account")
        print("[f] Back")
        print("=" * width)

        selec = input("\nPlease choose an option: \n➤ ").lower()

        if selec == "a":
            clean()
            title("📅", "Reserved Movies")
            if not user.reserved:
                print("  You have no reserved movies.")
            else:
                movies_storage_table(user.reserved)
            input("\nPress Enter to continue...")

        elif selec == "b":
            clean()
            title("❤️", "Favorites")
            if not user.favorites:
                print("  You have no favorite movies yet.")
            else:
                movies_storage_table(user.favorites)
            print("\n[a] Add a favorite")
            print("[b] Remove a favorite")
            print("[c] Back")
            print("=" * width)
            sub = input("\nPlease choose an option: \n➤ ").lower()

            if sub == "a":
                all_movies = movies + user.movies
                clean()
                title("🎬", "Add to Favorites")
                storage(all_movies, "name")
                choice = input("\nType the movie title or number: \n➤ ").upper()
                found = None
                if choice.isdigit():
                    index = int(choice) - 1
                    if 0 <= index < len(all_movies):
                        found = all_movies[index]
                else:
                    for m in all_movies:
                        if m["name"].upper() == choice:
                            found = m
                            break
                if found:
                    if found not in user.favorites:
                        user.favorites.append(found)
                        clean()
                        attendant_message("success")
                    else:
                        clean()
                        attendant_message("🙍", "success")
                else:
                    clean()
                    attendant_message("🙍", "error")

            elif sub == "b":
                if not user.favorites:
                    clean()
                    attendant_message("🙍", "error")
                else:
                    clean()
                    title("💔", "Remove Favorite")
                    storage(user.favorites, "name")
                    choice = input("\nType the movie title or number: \n➤ ").upper()
                    if choice.isdigit():
                        index = int(choice) - 1
                        if 0 <= index < len(user.favorites):
                            removed = user.favorites.pop(index)
                            clean()
                            attendant_message("💁", "success")
                        else:
                            clean()
                            attendant_message("🙍", "error")
                    else:
                        for fav in user.favorites:
                            if fav["name"].upper() == choice:
                                user.favorites.remove(fav)
                                clean()
                                attendant_message("💁", "success")
                                break
                        else:
                            clean()
                            attendant_message("🙍", "error")

        elif selec == "c":
            clean()
            title("🎞️", "Movies")
            if user.movies:
                storage(user.movies, "name")
            else:
                print("  No rented movies.")
                print("=" * width)
            title("🥗", "Foods")
            if user.foods:
                storage(user.foods, "name")
            else:
                print("  No foods ordered.")
                print("=" * width)
            input("\nPress Enter to continue...")

        elif selec == "d":
            clean()
            title("📜", "Rental History")
            if not user.history:
                print("  You haven't rented any movies yet.")
                print("=" * width)
            else:
                print(f"  Total rentals: {len(user.history)}")
                print("-" * width)
                movies_storage_table(user.history)
            input("\nPress Enter to continue...")

        elif selec == "e":
            clean()
            title("👤", "Account")
            print(f"  Rented now  : {len(user.movies)} movies")
            print(f"  Favorites   : {len(user.favorites)} movies")
            print(f"  History     : {len(user.history)} rentals")
            print(f"  Foods saved : {len(user.foods)} items")
            print("=" * width)
            input("\nPress Enter to continue...")

        elif selec == "f":
            clean()
            attendant_message("🙋", "attendant")
            break

        else:
            clean()
            attendant_message("🙍", "error")