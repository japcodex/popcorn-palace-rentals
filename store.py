#Import library
from movies_storage import movies
from foods_storage import *
from defs import *

loading("Processing")
clean()
attendant_message("💁", custom_text = f"Welcome to {company_name}! \nWhat would you like to do today?")

while True:
    selec = input("\nPlease choose an option: \n➤ ").lower()

    match selec:
        case "a":
            view_and_search_movies(movies)

        
        case "b":
            if not user.movies:
                clean()
                attendant_message("🙍", "empty")

            else:
                clean()
                title("🎒", "Your Inventory")
                storage(user.movies, "name")
                print("💁 -Select the movie you wish to return.\nYou can type the movie title or index.")
                new_selec = input("\nType the movie title or number: \n➤ ").upper()

                if new_selec.isdigit():
                    index = int(new_selec) - 1

                    if 0 <= index < len(user.movies):
                        movie = user.movies[index]
                        movie["stock"] += 1
                        user.movies.remove(movie)
                        clean()
                        attendant_message("💁", "success")
                    else:
                        clean()
                        attendant_message("🙍", "error")

                else:
                    found = False
                    for movie in user.movies:
                        if movie["name"].upper() == new_selec:
                            found = True
                            movie["stock"] += 1
                            user.movies.remove(movie)
                            clean()
                            attendant_message("💁", "success")
                            break
                    if not found:
                        clean()
                        attendant_message("🙍", "error")

        case "c":
            if not user.movies:
                clean()
                attendant_message("🙍", "error")
            else:
                clean()
                title("🎥", "Your Rented Movies")
                movies_storage_table(user.movies)
                input("\nPress Enter to continue...")
                clean()
                attendant_message("💁", "attendant")

        case "d":
            clean()
            title("🍽️", "Foods & Drinks")
            storage(foods, "name")
            print("💁 -Select the food or drink you wish to return.")
            print("You can type the name or index.")
            print("[E] For exit!")
            new_selec = input("\nType the name or number: \n➤ ").upper()

            if new_selec == "E":
                clean()
                attendant_message("💁", "attendant")

            elif new_selec.isdigit():
                index = int(new_selec) - 1
                if 0 <= index < len(foods):
                    food = foods[index]
                    user.foods.append(food)
                    user.history.append({**food, 'type': 'food'})
                    clean()
                    attendant_message("💁", "success")
                else:
                    clean()
                    attendant_message("🙍", "error")

            else:
                found = False
                for food in foods:
                    if new_selec in food['name'].upper():
                        user.foods.append(food)
                        user.history.append({**food, 'type': 'food'})
                        found = True
                        clean()
                        attendant_message("💁", "success")
                        break

                if not found:
                    clean()
                    attendant_message("🙍", "error")

        case "e":
            clean()
            user_config()
        
        case "f":
            clean()
            print("🙋 -Ok, see you soon")
            break

        case _:
            clean()
            attendant_message("🙍", "error")