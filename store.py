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
            movies_storage(movies, "name");
            print("💁 -Perfect, choose any movie! \nYou can type the movie title or index.")

            new_selec = input("\nType the movie title or number: \n➤ ").upper();

            if (new_selec.isdigit()):
                index = int(new_selec) -1;
                if (0 <= index < len(movies)):
                    inventory.append(movies[index]);
                    del(movies[index]);
                    clean();
                    attendant_message("💁", "Thank you for your purchase. \nWhat would you like?");
                else:
                    clean();
                    attendant_message("🙍", "Sorry, but we don´t have this movie. \nTry again, please!");
            
            elif (new_selec.isalpha()):
                for movie in movies:
                    if (movie["name"].upper() == new_selec):
                        inventory.append(movie);
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
            if (len(inventory) <=0):
                clean();
                attendant_message("🙍", "Sorry, but you don´t have any movies");
            elif (len(inventory) >0):
                clean()
                title("🎒", "Your Inventory");
                movies_storage(inventory, "name");
                print("💁 -Select the movie you wish to return. \nYou can type the movie title or index.")
                
                new_selec = input("\nType the movie title or number: \n➤ ").upper();
                
                if (new_selec.isdigit()):
                    index = int(new_selec) -1;
                    if (0 <= index < len(inventory)):
                        movies.append(inventory[index]);
                        del(inventory[index]);
                        clean();
                        attendant_message("💁", "Thank you for your return. \nWhat would you like?");
                    else:
                        clean();
                        attendant_message("🙍", "Sorry, but you don´t have this movie. \nTry again, please!");
            
                elif (new_selec.isalpha()):
                    for inv in inventory:
                        if (inv["name"].upper() == new_selec):
                            movies.append(inv);
                            inventory.remove(inv);
                    
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
            if (len(inventory) <=0):
                clean();
                attendant_message("🙍", "Sorry, but you don´t have any rented movie");
            elif (len(inventory) >0):
                clean()
                title("🎥", "Your Rented Movies");
                movies_storage_table(inventory);
        
        case "f":
            clean();
            title("🍽️", "Foods & Drinks");
            storage(foods, "name");
            storage(drinks, "name");
            
        
        case "g":
            clean();
            print("🙋 -Ok, see you soon")
            break;

        case _:
            clean();
            attendant_message("🙍", "Sorry, I don´t urdestand your message. \nTry again, please!");