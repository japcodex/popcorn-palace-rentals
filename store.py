#Import library
from movies_storage import movies;
from defs import *


attendant_message("💁", f"Welcome to {company_name}! \nWhat would you like to do today?");

while True:
    selec = input("\nPlease choose an option: \n➤ ").lower();

    match selec:
        case "a":
            clean();
            title("🎬", "Movies");
            storage(movies, "name");
            print("💁 -Perfect, choose any movie!")

        
        case "b":
            if (len(inventory) <=0):
                clean();
                attendant_message("🙍", "Sorry, but you don´t have any movies");
            elif (len(inventory) >0):
                clean()
                title("🎒", "Your Inventory");
                storage(inventory, "name");
                print("💁 -Select the movie you wish to return. \nYou can type the movie title or index.")
                new_selec = input("\nType the movie title or number: \n➤ ").lower();

        case "c":
            clean();
            title("📦", "Our Storage");
            storage_table(movies);
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
            attendant_message("🙍", "Sorry, I don´t urdestand your message, try again please!");