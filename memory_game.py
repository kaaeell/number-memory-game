import random
import time
import os


def clear_screen():
    """
    Clears the terminal screen.
    Works on Windows and macOS/Linux.
    """
    os.system("cls" if os.name == "nt" else "clear")


def generate_number(length):
    """
    Generates a random number with the given length.
    """
    return "".join(str(random.randint(0, 9)) for _ in range(length))


def play_game():
    print("🎲 Welcome to the Number Memory Game!")
    print("Test your memory. Each level gets harder.\n")

    level = 1
    number_length = 3  # starting difficulty
    display_time = 3   # seconds the number is shown

    while True:
        print(f"\n🔹 Level {level}")
        number = generate_number(number_length)

        print("Memorize this number:")
        print(f"\n   {number}\n")

        time.sleep(display_time)
        clear_screen()

        user_input = input("Enter the number: ")

        if user_input == number:
            print("✅ Correct! Well done.")
            level += 1
            number_length += 1  # increase difficulty
            display_time = max(1, display_time - 0.3)  # slightly faster each round
        else:
            print("❌ Wrong answer.")
            print(f"The correct number was: {number}")
            print(f"You reached Level {level}.")
            break

    print("\nThanks for playing! 🧠")


if __name__ == "__main__":
    play_game()