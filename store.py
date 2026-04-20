#Import library
from movies_storage import movies;
from foods_storage import *
from defs import *


attendant_message("💁", f"Welcome to {company_name}! \nWhat would you like to do today?");

while True:
    selec = input("\nPlease choose an option: \n➤ ").lower();

    match selec:
        case "a":
            clean();
            title("🎬", "Movies");
            storage(movies, "name");
            print("💁 -Perfect, choose any movie! \nYou can type the movie title or index.")

            new_selec = input("\nType the movie title or number: \n➤ ").upper();

            if (new_selec.isdigit()):
                index = int(new_selec) -1;
                if (0 <= index < len(movies)):
                    User.movies.append(movies[index]);
                    del(movies[index]);
                    clean();
                    attendant_message("💁", "Thank you for your purchase. \nWhat would you like?");
                else:
                    clean();
                    attendant_message("🙍", "Sorry, but we don´t have this movie. \nTry again, please!");
            
            elif (new_selec.isalpha()):
                for movie in movies:
                    if (movie["name"].upper() == new_selec):
                        User.movies.append(movie);
                        movies.remove(movie);

                        clean();
                        attendant_message("💁", "Thank you for your purchase. \nWhat would you like?");
                        break;
                        
                else:
                    clean();
                    attendant_message("🙍", "Sorry, but we don´t have this movie. \nTry again, please!");
            
            else:
                clean();
                attendant_message("🙍", "Sorry, but we don´t have this movie. \nTry again, please!");


        
        case "b":
            if (len(User.movies) <=0):
                clean();
                attendant_message("🙍", "Sorry, but you don´t have any movies");
            elif (len(User.movies) >0):
                clean()
                title("🎒", "Your Inventory");
                storage(User.movies, "name");
                print("💁 -Select the movie you wish to return. \nYou can type the movie title or index.")
                
                new_selec = input("\nType the movie title or number: \n➤ ").upper();
                
                if (new_selec.isdigit()):
                    index = int(new_selec) -1;
                    if (0 <= index < len(User.movies)):
                        movies.append(User.movies[index]);
                        del(User.movies[index]);
                        clean();
                        attendant_message("💁", "Thank you for your return. \nWhat would you like?");
                    else:
                        clean();
                        attendant_message("🙍", "Sorry, but you don´t have this movie. \nTry again, please!");
            
                elif (new_selec.isalpha()):
                    for inv in User.movies:
                        if (inv["name"].upper() == new_selec):
                            movies.append(inv);
                            User.movies.remove(inv);
                    
                    else:
                        clean();
                        attendant_message("🙍", "Sorry, but you don´t have this movie. \nTry again, please!");
            
                else:
                    clean();
                    attendant_message("🙍", "Sorry, but you don´t have this movie. \nTry again, please!");

        case "c":
            clean();
            title("📦", "Our Storage");
            movies_storage_table(movies);
            print("💁 -Do you wanna any movie?")
            print("[a] Yes \n[b] No");

            new_selec = input("\nPlease choose an option: \n➤ ").lower();

            if new_selec == "a":
                print("💁 -Okay, you can type the movie title or index.");

            if new_selec == "b":
                clean();
                attendant_message("🙋", "Okay, What would you like?");

        case "d":
            clean();
            title("🔍", "Search");
            print("[a] Search by Name \n[b] Search by Genre \n[c] Search by Rating \n[d] Back");
            print("=" * width);

            new_selec = input("\nPlease choose an option: \n➤ ").lower();

            if (new_selec == "a"):
                ...;
            elif (new_selec == "b"):
                ...;
            elif (new_selec == "c"):
                ...;
            elif (new_selec == "d"):
                clean();
                attendant_message("🙋", "Okay, What would you like?");
            else:
                clean();
                attendant_message("🙍", "Sorry, I don´t urdestand your message. \nTry again, please!");

        case "e":
            if (len(User.movies) <=0):
                clean();
                attendant_message("🙍", "Sorry, but you don´t have any rented movie");
            elif (len(User.movies) >0):
                clean()
                title("🎥", "Your Rented Movies");
                movies_storage_table(User.movies);
        
        case "f":
            clean();
            title("🍽️", "Foods & Drinks");
            storage(foods, "name");

            print("💁 -Select the food or drink you wish to return. \nYou can type the name or index.")
                
            new_selec = input("\nType the name or number: \n➤ ").upper();
                
            if (new_selec.isdigit()):
                index = int(new_selec) -1;
                if (0 <= index < len(foods)):
                    User.foods.append(foods[index]);
                    #del(foods[index]);
                    clean();
                    attendant_message("💁", "Thank you. \nWhat would you like?");
                else:
                    clean();
                    attendant_message("🙍", "Sorry, but you don´t have this food. \nTry again, please!");
            
            elif (new_selec.isalpha()):
                for food in foods:
                    if (food["name"].upper() == new_selec):
                        User.foods.append(food);
                        #foods.remove(food);
                    
                else:
                    clean();
                    attendant_message("🙍", "Sorry, but you don´t have this food. \nTry again, please!");
            
            else:
                clean();
            
        
        case "g":
            clean();
            title("🎞️", "Movies");
            storage(User.movies, "name");
            title("🥗", "Foods");
            storage(User.foods, "name");

            exit();

        case "h":
            clean();
            print("🙋 -Ok, see you soon")
            break;

        case _:
            clean();
            attendant_message("🙍", "Sorry, I don´t urdestand your message. \nTry again, please!");