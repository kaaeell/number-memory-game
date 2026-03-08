import random
import time
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def generate_number(length):
    return "".join(str(random.randint(0, 9)) for _ in range(length))

def get_player_name():
    name = input("Enter your name: ").strip()
    return name if name else "Player"

def show_countdown():
    for i in [3, 2, 1]:
        print(f"Get ready... {i}")
        time.sleep(1)
    clear_screen()

def show_stats(level, best_level, streak):
    print(f"📊 Level: {level}  |  🏆 Best: {best_level}  |  🔥 Streak: {streak}")

def play_game():
    print("🧠 Number Memory Game!")
    print("How far can your memory take you?\n")
    name = get_player_name()

    best_level = 1
    play_again = True

    while play_again:
        level = 1
        number_length = 3
        display_time = 3.0
        streak = 0

        clear_screen()
        print(f"\nHey {name}! Let's go. Starting at Level 1...\n")
        time.sleep(1.5)

        while True:
            clear_screen()
            show_stats(level, best_level, streak)
            print(f"\n🔹 Level {level} — {number_length} digits ({display_time:.1f}s to memorize)\n")

            number = generate_number(number_length)
            print("Memorize this number:\n")
            print(f"   👉  {number}\n")
            time.sleep(display_time)
            clear_screen()

            show_countdown()

            try:
                user_input = input("Enter the number: ").strip()
            except KeyboardInterrupt:
                print("\n\nGame interrupted. Goodbye!")
                return

            if user_input == number:
                streak += 1
                level += 1
                number_length += 1
                display_time = max(1.0, display_time - 0.3)

                if streak == 3:
                    print("🔥 3 in a row! You're on fire!")
                elif streak == 5:
                    print("💥 5 streak! Incredible memory!")
                else:
                    print(f"✅ Correct, {name}! Keep going!")

                if level > best_level:
                    best_level = level
                    print("🏆 New personal best!")

                time.sleep(1.5)
            else:
                clear_screen()
                print(f"❌ Wrong! The number was: {number}")
                print(f"\n📊 Final Stats for {name}:")
                print(f"   • Level reached : {level}")
                print(f"   • Best level    : {best_level}")
                print(f"   • Longest streak: {streak}")
                break

        again = input("\nPlay again? (yes/no): ").strip().lower()
        play_again = again == "yes"

    print(f"\nThanks for playing, {name}! Final best: Level {best_level} 👋")

if __name__ == "__main__":
    play_game()
