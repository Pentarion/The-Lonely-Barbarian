import os
import shutil
import pygame  # type: ignore
import sys
import time
import textwrap

# Initialize pygame mixer early in the script
pygame.mixer.init()

# Function to clear the screen
def clear_screen(lines_after_clear=5):
    """
    Clears the terminal screen and optionally adds blank lines after clearing.
    """
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac
        os.system('clear')

    # Add blank lines only after clearing
    if lines_after_clear > 0:
        print("\n" * lines_after_clear, end="")



# Function to center text
def center_text(text):
    try:
        width = shutil.get_terminal_size().columns
    except OSError:
        width = 80  # Default width if terminal size cannot be determined
    return text.center(width)

# Function to initialize and play background music
def play_music():
    try:
        # Update the path to handle PyInstaller's bundle environment
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        music_path = os.path.join(base_path, "1.mp3")
        pygame.mixer.music.load(music_path) 
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)  # Loop the music indefinitely
    except Exception as e:
        print(f"Error loading or playing music: {e}")


# Function to slow text down while playing
def slow_print(text, delay=0.055, width=30):
    """Print text slowly with wrapping and consistent centering for all lines."""
    try:
        terminal_width = shutil.get_terminal_size().columns
    except OSError:
        terminal_width = width  # Default width if terminal size cannot be determined

    # Wrap the text to fit within the terminal width
    wrapped_text = textwrap.fill(text.strip(), width=terminal_width - 2)

    # Process each wrapped line and center it properly
    for line in wrapped_text.splitlines():
        centered_line = line.center(terminal_width)  # Center each wrapped line individually
        for char in centered_line:
            if char.strip():  # Only slow print visible characters
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(delay)
            else:
                sys.stdout.write(char)  # Print spaces instantly
        print()  # Ensure a new line after each wrapped and centered line




# Function to format location for grammatical correctness
def format_location_sentence(location):
    if location.startswith("the "):
        location = location[4:]  # Remove leading "the " for smoother sentence flow
    if location.endswith("."):
        location = location[:-1]  # Remove trailing period for cleaner integration
    return location

# Function to force valid input
def get_valid_input(prompt, valid_options):
    """
    Prompt the user for input and validate against a list of valid options.
    If the input is invalid, prompt again until a valid option is provided.
    """
    while True:
        choice = input(prompt)
        if choice in valid_options:
            return choice
        print("\nInvalid choice. Please try again.")

# Password prompt
def password_prompt():
    clear_screen(lines_after_clear=0)
    while True:
        print("Please enter the password to begin:")
        password = input()
        if password.lower() == "carnival":
            play_music()  # Start playing background music
            break
        else:
            clear_screen(lines_after_clear=5)
            slow_print("Incorrect password. Try again.", delay=0.05)

def title_screen():
    clear_screen(lines_after_clear=5)
    title_box = [
        "**************************************",
        "*                                    *",
        "*       THE LONELY BARBARIAN         *",
        "*                                    *",
        "*    A Mark_the_great production     *",
        "**************************************"
    ]
    # Center each line of the title box
    for line in title_box:
        print(center_text(line))

    ascii_art = [
        "           ,,,,,,,,,,                    ",
        "        ,;;;;;;;;;;;;;;,                 ",
        "      ,;;;;;;;;;;;)));;(((,,;;;,,_       ",
        "     ,;;;;;;;;;;'      |)))))))))))\\    ",
        "     ;;;;;;/ )''    - /,)))((((((((((   ",
        "      ;;;;' \\       ~|\\   )))))))))))  ",
        "      /     /..       \\     (((((((((((  ",
        "    /'      \\....._/~'     ')|()))))))  ",
        "  /'         \\.../>      o_/)))((((((   ",
        " /          /' ~~(____ /  ())))))))))   ",
        "|     ---,   \\        \\     ((((((((((   ",
        "          \\   \\~-_____|      )))))))))   ",
        "            \\  |      |_.---.  (((((((      "
    ]
    # Center each line of ASCII art
    for line in ascii_art:
        print(center_text(line))
    
    input(center_text("\nPress Enter to begin your adventure..."))

# Conquest counter
conquests = 0

# Adventure framework
def story():
    clear_screen(lines_after_clear=5)
    slow_print("You are a fierce, sexy barbarian woman with eyes of honeyed hazel,") 
    slow_print("hair of rich acorn brown and muscles of hardened steel.")
    slow_print("You live in a small, snowy village") 
    slow_print("filled with boring people going about their boring lives.")
    slow_print("While you are respected by your fellow villagers") 
    slow_print("for your beauty, honesty, and strength, you long for something more.\n")
    print()
    slow_print("Something... spicy.", delay=0.15)
    print()
    slow_print("The nights are long and cold, and you feel") 
    slow_print("a burning desire for someone to fill your void.")
    slow_print("Today, you decide to leave your quiet life behind in search of adventure.\n")
    print()
    slow_print("Where will your journey begin?\n", delay=0.1)
    print("1. The tall, hard mountains.")
    print("2. The darkly attractive forest.")
    print("3. The hot and sweaty city.")
    choice = input("Choose your adventure (1/2/3): ")
    if choice == "1":
        path_text = "the snowy mountains, where icy winds howl and rugged, handsome peaks loom in the distance."
    elif choice == "2":
        path_text = "the mysterious forest, where ancient trees whisper sexy secrets, and magic lingers in the air."
    elif choice == "3":
        path_text = "the bustling city, where the sounds of life being created echo in narrow streets and the scent of spice fills the air."
    elif choice == "8":  # Secret option
        clear_screen(lines_after_clear=5)
        slow_print("Yahaha! You found me.", delay=0.1)
        print()
        ascii_art = [
            "    ^    ",
            "   ^ ^   ",
            "  ^^^^^  ",
            " ^  ^  ^ ",
            "^^^^^^^^^ ",
        ]
        for line in ascii_art:
            print(center_text(line))
        input("\nPress Enter to exit...")
        sys.exit()  # Exit the game entirely
    else:
        clear_screen(lines_after_clear=5)
        slow_print("Invalid choice. Starting over...\n")
        input("Press Enter to try again.")
        story()
        return

    journey(path_text)

# Don't look at me
def secret():
    """
    Secret flow when the player chooses the hidden option.
    """
    clear_screen(lines_after_clear=5)
    slow_print("Congratulations, adventurer!")
    slow_print("You've completed the secret scavenger hunt hidden within The Lonely Barbarian.")
    print()
    slow_print("This is a reward reserved for the sharpest minds and most curious souls.")
    print()
    slow_print("To claim your prize, tell the creator the passphrase:")
    slow_print("\"You love me more.\"")
    print()
    slow_print("Thank you for playing and uncovering the hidden path!")
    input("\nPress Enter to return to the main story...")
    story()  # Return to the main story flow


def journey(path_text):
    clear_screen(lines_after_clear=5)
    slow_print(f"You set out toward {path_text}")
    slow_print("Your heart races with the thrill of potential adventure.\n") 
    print()
    slow_print("And potential penis...\n", delay=0.2)
    input("Press Enter to continue...")
    encounter_1(path_text)

# Encounter functions
def encounter_1(path_text):
    global conquests
    clear_screen(lines_after_clear=5)
    location = format_location_sentence(path_text)
    slow_print(f"Along the way in the {location},") 
    slow_print("you meet a rugged hunter named Rorik.")
    slow_print("His muscles bulge the perfect amount,") 
    slow_print("his forearms are thick and only mildly vascular.")
    slow_print("He sits by a campfire, sharpening his axe, and offers to share his camp.")
    slow_print("His piercing, penetrating, stormy blue eyes") 
    slow_print("penetrate and pierce you, and suggest he might be offering more than just warmth.\n")
    print()
    print("\n1. Spend the night with Rorik.")
    print("2. Thank him for the fire and move on.")
    choice = get_valid_input("\nChoose (1/2): ", ["1", "2"])
    if choice == "1":
        clear_screen(lines_after_clear=5)
        slow_print("At the hint of acquiescence in your eyes," )
        slow_print("he grabs your arm, spinning you around. You give a token struggle,") 
        slow_print("but you long for him to dominate you.") 
        slow_print("His leg sweeps yours out from underneath you,")
        slow_print("but he catches you so you don't fall too quickly.")
        print()
        slow_print("Rorik pins you down with his entire body and you involuntarily gasp.") 
        slow_print("You rarely allow a man to best you in such a way.") 
        slow_print("His mouth roughly meets yours and soon he rides you until you see stars.\n")
        print()
        slow_print("\nThe fire wasn't the only thing hot.", delay=0.1)
        print()
        conquests += 1
    else:
        clear_screen(lines_after_clear=5)
        slow_print("You thank Rorik and continue on. The wind is cold") 
        slow_print("and your nether regions colder.")
        print()
    input("\nPress Enter to continue...")
    encounter_2(path_text)

def encounter_2(path_text):
    global conquests
    clear_screen(lines_after_clear=5)
    location = format_location_sentence(path_text)
    slow_print(f"Continuing your journey through the {location},") 
    slow_print("you encounter a mystical druid named Hugh.")
    slow_print("As you approach, you see that he is gently tending to an injured deer,") 
    slow_print("his large hands incredibly gentle despite their size.") 
    slow_print("You can't help wondering if the rest of him is proportionally sized.")
    print()
    slow_print("He turns to glance at you and your heart starts pounding.")
    slow_print("His eyes are an unnatural shade of green,") 
    slow_print("like a vibrant moss growing on an ancient rock.") 
    slow_print("They don't just sparkle - they smolder,") 
    slow_print("as though their sole purpose in life is to ignite") 
    slow_print("the hearts of lonely romance readers.")
    print()
    slow_print("Hugh raises one eyebrow, and with a deep but gentle voice") 
    slow_print("he offers to teach you ancient wisdom...\n")
    print()
    print("1. Accept Hugh's offer.")
    print("2. Politely decline and continue on.")
    choice = get_valid_input("\nChoose (1/2): ", ["1", "2"])
    if choice == "1":
        clear_screen(lines_after_clear=5)
        slow_print("Hugh teaches you more than just ancient secrets.") 
        slow_print("Your heart isn't the only thing pounding.")
        print()
        slow_print("As you both simultaneously reach the peak of pure passion,") 
        slow_print("the sounds you make are more animal than person...") 
        slow_print("but with Hugh that seems appropriate.")
        print()
        conquests += 1
    else:
        clear_screen(lines_after_clear=5)
        slow_print("You thank Hugh and leave, his gaze lingering") 
        slow_print("on your 10/10 butt as you vanish into the distance.\n")
        print()
    input("\nPress Enter to continue...")
    encounter_3(path_text)

def encounter_3(path_text):
    global conquests
    clear_screen(lines_after_clear=5)
    location = format_location_sentence(path_text)
    slow_print(f"As you continue your journey through the {location},") 
    slow_print("you meet a charming rogue named Kael.")
    slow_print("Despite his slim, toned frame, his voice is deep.") 
    slow_print("Everything he says comes out in a gravelly growl.")
    print()
    slow_print("He offers to show you hidden treasures,") 
    slow_print("his smirk hinting at more than just some gold and jewels.")
    slow_print("Kael's charisma is undeniable, but the choice is yours.\n")
    print()
    print("1. Spend the night with Kael.")
    print("2. Decline his offer and continue on your way.")
    choice = get_valid_input("\nChoose (1/2): ", ["1", "2"])
    if choice == "1":
        clear_screen(lines_after_clear=5)
        slow_print("Kael growls and then smirks. He knows what you want,") 
        slow_print("and is very quick to disrobe. He tears off your primitive fur and cloth,") 
        slow_print("and steps back to take in your savage beauty. He smiles.")
        print()
        slow_print("His smile isn't just dazzling; it is an *event*.") 
        slow_print("The kind of smile that causes horse-and-carriage accidents,") 
        slow_print("breaks up long-term relationships, and is probably insured for millions of gold.") 
        slow_print("It shines like he spends every morning gargling liquid diamonds.")
        print()
        slow_print("Tonight, though, his overdescribed mouth will be placed somewhere much dirtier.") 
        print()
        slow_print("(In a sexual sense of course, as you bathe frequently)", delay=0.1)
        print()
        slow_print("You leave him the next morning with a spring in your step.")
        print()
        conquests += 1
    else:
        clear_screen(lines_after_clear=5)
        slow_print("You decline, determined to follow your own, sexually frustrated path.")
        print()
    input("\nPress Enter to continue...")
    encounter_4(path_text)

def encounter_4(path_text):
    global conquests
    clear_screen(lines_after_clear=5)
    location = format_location_sentence(path_text)
    slow_print(f"In the final leg of your journey through the {location},") 
    slow_print("you meet a bard named Ewan McGregor.")
    slow_print("He sings songs that stir your loins as well as your soul,") 
    slow_print("and offers to compose a ballad just for you.")
    print()
    slow_print("His piercing, penetrating gaze and surprisingly well-groomed beard") 
    slow_print("hold a promise of something far more personal.\n")
    print()
    print("1. Spend the night with Ewan.")
    print("2. Politely decline and move on.")
    choice = get_valid_input("\nChoose (1/2): ", ["1", "2"])
    if choice == "1":
        clear_screen(lines_after_clear=5)
        slow_print("Sex happens.", delay=0.25) 
        slow_print("Lots and lots of sex.", delay=0.25)
        print()
        conquests += 1
    else:
        clear_screen(lines_after_clear=5)
        slow_print("You thank Ewan and sadly leave his ballad, and penis, unfinished.")
    input("\nPress Enter to continue...")
    ending(path_text)

# Ending
def ending(path_text):
    global conquests
    clear_screen(lines_after_clear=5)
    location = format_location_sentence(path_text)
    slow_print(f"Your adventure through the {location}") 
    slow_print("has come to an end. You return to your village, forever changed.")
    print()
    slow_print("\nAs you reflect on your journey, you think back on your conquests:")
    print()
    slow_print(f"You had {conquests} {'conquest' if conquests == 1 else 'conquests'} during your travels.\n")
    
    # Humorous messages based on the number of conquests
    if conquests == 0:
        slow_print("The lonely barbarian remains lonely.") 
        slow_print("If only this magical land had invented vibrators. Perhaps next time?")
    elif conquests == 1:
        slow_print("A single conquest! Quality over quantity, eh? You still feel very unsatisfied.")
    elif conquests == 2:
        slow_print("Two conquests! Your legend grows (long and hard).") 
        slow_print("You've still got more work to do though.")
    elif conquests == 3:
        slow_print("Three conquests! The world will sing of your... charisma.") 
        slow_print("You feel a less lonely, but didn't quite get where you needed to.")
    else:
        slow_print("Four conquests! The gods themselves weep in envy of your nocturnal prowess.") 
        slow_print("They reverently send a divine message to you:\n")
        print()
        slow_print("\nSpin and spray, a chore each night,")
        slow_print("Turning grime to gleaming white.")
        slow_print("Hidden cycles, waters churn,")
        slow_print("\nFind me and a secret you'll learn!\n")
        print()
        print()

    # Prompt for playing again if conquests are 0-3
    if conquests <= 3:
        while True:
            play_again = input("\nWould you like to play again? (Y/N): ").strip().lower()
            if play_again == 'y':
                # Reset conquests and start the story again
                conquests = 0
                story()
                return
            elif play_again == 'n':
                break
            else:
                slow_print("Invalid input. Please enter 'Y' or 'N'.")

    # End the game
    slow_print("\nThank you for playing The Lonely Barbarian!")
    input("\nPress Enter to exit.")


# Main function
def main():
    clear_screen()
    password_prompt()
    title_screen()
    story()

if __name__ == "__main__":
    main()