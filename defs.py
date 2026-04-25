#Import library
import os
import time
import random
from movies_storage import movies

#Creating Variables
company_name = "Popcorn Palace Rentals"
default_width = 80
width = default_width

class User:
    def __init__(self):
        self.name = "Guest"
        self.movies = []
        self.foods = []
        self.reserved = []
        self.history = []
user = User()

menu = """
[a] Available movies
[b] Return a movie
[c] View rented movies
[d] Foods & Drink
[e] User
[f] Exit"""

#Creating defs
def loading(text="Loading"):
    print(text, end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.3)
    print()

def title(emoji, text):
    print("\n" + "=" * width)
    print(f"{emoji} {text.center(width - 6).upper()}")
    print("=" * width)

def clean():
    os.system('cls' if os.name == 'nt' else 'clear')

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

def attendant_message(emoji, type="welcome", custom_text=None):
    print("=" * width)
    print(f"🍿{company_name.center(width - 6).upper()}🍿")
    print("=" * width)

    if custom_text: text = custom_text
    else: text = random_message(type)

    print(f"{emoji} -{text}")
    print(menu)

def storage(storage, name):
    for index, i in enumerate(storage, start=1):
        print(f"{index}.", i[f"{name}"])
    print("=" * width)

def movies_storage_table(storage):
    print(f"{'NAME':<35} {'GENRES':<16} {'RATING':<10} {'STOCK':<8} {'AWARD'}")
    print("-" * width)
    
    for index, i in enumerate(storage, start=1):
        stars = "⭐" * i["rating"]
        empty = "  " * (3 - i["rating"])  # 2 espaços por estrela faltante
        stars_display = stars + empty

        stock_bar = "📦" * i["stock"]
        empty_stock = "❌" * (i["total_stock"] - i["stock"])
        stock_display = stock_bar + empty_stock

        award_display = "🏆" if i.get("award", False) else " "
        favorited = "♥" if i.get("favorite", False) else ""
        name_display = f"{i['name']} {favorited}"

        print(f"{index:<3}. {name_display:<30} {i['genres']:<15} {stars_display}  {stock_display:<8} {award_display}")
    print("=" * width)

def confirm_rent(movie):
    print(f"\n🎬 {movie['name']}")
    print(f"⭐ {'⭐' * movie['rating']}")
    print(f"📦 Stock: {movie['stock']}")
    
    choice = input("\nAre you sure you want to rent this movie? [y/n]: ").lower()
    return choice == "y"

def select_movie(movie_list):
    print("💁 -Do you want to rent a movie?")
    print("You can type the movie title or index.")
    print("Use 'fav' to favorite/unfavorite (ex: 10 fav)")
    print("[E] For exit!")

    new_selec = input("\nType the movie title or number: \n➤ ").upper().split()

    if not new_selec:
        return

    if new_selec[0] == "E":
        return

    is_fav = "FAV" in new_selec
    value = new_selec[0]

    if value.isdigit():
        index = int(value) - 1

        if 0 <= index < len(movie_list):
            movie = movie_list[index]

            if is_fav:
                movie["favorite"] = not movie.get("favorite", False)
                clean()
                print("❤️   Added to favorites!" if movie["favorite"] else "💔   Removed from favorites!")
                input("\nPress Enter to continue...")
            else:
                if movie["stock"] > 0:
                    if confirm_rent(movie):
                        movie["stock"] -= 1
                        user.movies.append(movie)
                        user.history.append({**movie, 'type': 'movie'})

                        clean()
                        attendant_message("💁", "success")
                    else:
                        clean()
                        attendant_message("🙋", "attendant")
                else:
                    clean()
                    attendant_message("🙍", "empty")
        else:
            clean()
            attendant_message('🙍', 'error')

    else:
        found = False

        for movie in movie_list:
            if value in movie["name"].upper():
                found = True

                if is_fav:
                    movie["favorite"] = not movie.get("favorite", False)
                    clean()
                    print("❤️   Added to favorites!" if movie["favorite"] else "💔   Removed from favorites!")
                    input("\nPress Enter to continue...")
                else:
                    if movie["stock"] > 0:
                        if confirm_rent(movie):
                            movie["stock"] -= 1
                            user.movies.append(movie)
                            user.history.append({**movie, 'type': 'movie'})

                            clean()
                            attendant_message("💁", "success")
                        else:
                            clean()
                            attendant_message("🙋", "attendant")
                    else:
                        clean()
                        attendant_message("🙍", "empty")

                break

        if not found:
            clean()
            attendant_message("🙍", "error")

def view_and_search_movies(movies):
    while True:
        clean()
        title("🎬", "Movies")
        print("[a] View all movies")
        print("[b] Recommended        ⭐⭐⭐")
        print("[c] Surprise me        🎲")
        print("[d] Hall of fame       🏆")
        print("[e] Search by name     🔍")
        print("[f] Search by genre    🎭")
        print("[g] Filter by rating   📊")
        print("[h] Favorites          ❤️")
        print("[i] Back               🔙")
        print("=" * width)

        new_selec = input("\nPlease choose an option: \n➤ ").lower()

        if new_selec == "a":
            clean()
            title("🎬", "All Movies")
            movies_storage_table(movies)
            select_movie(movies)
            break

        elif new_selec == "b":
            clean()
            title("⭐", "Recommended")
            recommended = [m for m in movies if int(m["rating"]) >= 3]
            if recommended:
                movies_storage_table(recommended)
            else:
                print("No recommended movies available.")
            select_movie(recommended)
            break

        elif new_selec == "c":
            clean()
            title("🎲", "Surprise Me!")
            surprise = random.choice(movies)
            movies_storage_table([surprise])
            select_movie(surprise)
            break

        elif new_selec == "d":
            clean()
            title("🏆", "Top Rated")
            award_movies = [m for m in movies if m.get("award", False)]
            movies_storage_table(award_movies)
            select_movie(award_movies)
            break

        elif new_selec == "e":
            clean()
            title("🔍", "Search by Name")
            query = input("Type part of the movie name: \n➤ ").upper()
            results = [m for m in movies if query in m["name"].upper()]
            if results:
                movies_storage_table(results)
                select_movie(results)
                break
            else:
                print("❌ No movies found.")

        elif new_selec == "f":
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
            select_movie(results)
            break

        elif new_selec == "g":
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
            select_movie(results)
            break

        elif new_selec == "h":
            clean()
            title("❤️", "Favorites")

            favorite_movies = [m for m in movies if m.get("favorite", False)]

            if favorite_movies:
                movies_storage_table(favorite_movies)
                select_movie(favorite_movies)
                break
            else:
                print("❌ No favorite movies yet.")
                input("\nPress Enter to continue...")
        
        elif new_selec == "i":
            clean()
            attendant_message("🙋", "attendant")
            break

        else:
            clean()
            attendant_message("🙍", "error")

def user_config():
    while True:
        clean()
        title("👤", "User")
        print("[a] Reserved movies    📌")
        print("[b] Inventory          🎒")
        print("[c] History            🕘")
        print("[d] Account            ⚙️")
        print("[e] Back               🔙")
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

        elif selec == "c":
            clean()
            title("📜", "Rental History")
            if not user.history:
                print("  You haven't rented any movies yet.")
                print("=" * width)
            else:
                print(f"  Total rentals: {len(user.history)}")
                print("-" * width)
                storage(user.history, "name")
            input("\nPress Enter to continue...")

        elif selec == "d":
            clean()
            title("👤", "Account")
            print(f"{' Name':<15}: {user.name}")
            print(f"{' Rented now':<15}: {len(user.movies)} movies")
            print(f"{' Favorites':<15}: {sum(1 for m in movies if m.get('favorite', False))} movies")
            print(f"{' History':<15}: {len(user.history)} rentals")
            print(f"{' Foods saved':<15}: {len(user.foods)} items")
            print("=" * width)
            input("\nPress Enter to continue...")

        elif selec == "e":
            clean()
            attendant_message("🙋", "attendant")
            break

        else:
            ...