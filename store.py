#Import library
from movies_storage import movies;
from foods_storage import *
from defs import *

loading("Processing")
clean();
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
                    user.movies.append(movies[index]);
                    del(movies[index]);
                    user.history.append(movie)
                    clean();
                    attendant_message("💁", "Thank you for your purchase. \nWhat would you like?");
                else:
                    clean();
                    attendant_message("🙍", "Sorry, but we don´t have this movie. \nTry again, please!");
            
            elif (new_selec.isalpha()):
                for movie in movies:
                    if (movie["name"].upper() == new_selec):
                        user.movies.append(movie);
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
            if (len(user.movies) <=0):
                clean();
                attendant_message("🙍", "Sorry, but you don´t have any movies");
            elif (len(user.movies) >0):
                clean()
                title("🎒", "Your Inventory");
                storage(user.movies, "name");
                print("💁 -Select the movie you wish to return. \nYou can type the movie title or index.")
                
                new_selec = input("\nType the movie title or number: \n➤ ").upper();
                
                if (new_selec.isdigit()):
                    index = int(new_selec) -1;
                    if (0 <= index < len(user.movies)):
                        movies.append(user.movies[index]);
                        del(user.movies[index]);
                        clean();
                        attendant_message("💁", "Thank you for your return. \nWhat would you like?");
                    else:
                        clean();
                        attendant_message("🙍", "Sorry, but you don´t have this movie. \nTry again, please!");
            
                elif (new_selec.isalpha()):
                    for inv in user.movies:
                        if (inv["name"].upper() == new_selec):
                            movies.append(inv);
                            user.movies.remove(inv);
                    
                    else:
                        clean();
                        attendant_message("🙍", "Sorry, but you don´t have this movie. \nTry again, please!");
            
                else:
                    clean();
                    attendant_message("🙍", "Sorry, but you don´t have this movie. \nTry again, please!");

        case "c":
            clean();
            view_and_search_movies(movies);

        case "d":
            if (len(user.movies) <=0):
                clean();
                attendant_message("🙍", "Sorry, but you don´t have any rented movie");
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
        
        case "f":
            clean();
            user_config();
        
        case "g":
            clean();
            print("🙋 -Ok, see you soon")
            break;

        case _:
            clean();
            attendant_message("🙍", "Sorry, I don´t urdestand your message. \nTry again, please!");