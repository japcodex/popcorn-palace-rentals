#Import library
from movies_storage import movies;
from foods_storage import *
from defs import *

loading("Processing")
clean();
welcome_message("💁", f"Welcome to {company_name}! \nWhat would you like to do today?");

while True:
    selec = input("\nPlease choose an option: \n➤ ").lower();

    match selec:
        case "a":
            clean()
            title("🎬", "Movies")
            storage(movies, "name")
            print("💁 -Perfect, choose any movie! \nYou can type the movie title or index.")
            new_selec = input("\nType the movie title or number: \n➤ ").upper()

            if new_selec.isdigit():
                index = int(new_selec) - 1

                if 0 <= index < len(movies):
                    movie = movies[index]

                    if movie["stock"] > 0:
                        movie["stock"] -= 1
                        user.movies.append(movie)
                        user.history.append(movie)

                        clean()
                        attendant_message("💁", "success")
                    else:
                        clean()
                        attendant_message("🙍", "empty")
                else:
                    clean()
                    attendant_message("🙍", "error")

            else:
                found = False

                for movie in movies:
                    if movie["name"].upper() == new_selec:
                        found = True

                        if movie["stock"] > 0:
                            movie["stock"] -= 1
                            user.movies.append(movie)
                            user.history.append(movie)

                            clean()
                            attendant_message("💁", "success")
                        else:
                            clean()
                            attendant_message("🙍", "empty")

                        break

                if not found:
                    clean()
                    attendant_message("🙍", "error")

        
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
            view_and_search_movies(movies);

        case "d":
            if (len(user.movies) <=0):
                clean();
                attendant_message("🙍", "error");
            elif (len(user.movies) >0):
                clean()
                title("🎥", "Your Rented Movies");
                movies_storage_table(user.movies);

        case "e":
            clean();
            title("🍽️", "Foods & Drinks");
            storage(foods, "name");

            print("💁 -Select the food or drink you wish to return. \nYou can type the name or index.")
                
            new_selec = input("\nType the name or number: \n➤ ").upper();
                
            if (new_selec.isdigit()):
                index = int(new_selec) -1;
                if (0 <= index < len(foods)):
                    user.foods.append(foods[index]);
                    #del(foods[index]);
                    clean();
                    attendant_message("💁", "success");
                else:
                    clean();
                    attendant_message("🙍", "error");
            
            elif (new_selec.isalpha()):
                for food in foods:
                    if (food["name"].upper() == new_selec):
                        user.foods.append(food);
                        #foods.remove(food);
                    
                else:
                    clean();
                    attendant_message("🙍", "error");
            
            else:
                clean();
        
        case "f":
            clean();
            user_config();
        
        case "g":
            clean();
            print("🙋 -Ok, see you soon")
            break;

        case _:
            clean();
            attendant_message("🙍", "error");