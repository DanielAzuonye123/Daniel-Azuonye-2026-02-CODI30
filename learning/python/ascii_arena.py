import random
import time

# ANSI COLORS
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RESET = "\033[0m"

print(BLUE + r"""
   █████╗ ██████╗  ██████╗ ██╗   ██╗███████╗██╗
  ██╔══██╗██╔══██╗██╔═══██╗██║   ██║██╔════╝██║
  ███████║██████╔╝██║   ██║██║   ██║█████╗  ██║
  ██╔══██║██╔══██╗██║   ██║╚██╗ ██╔╝██╔══╝  ██║
  ██║  ██║██║  ██║╚██████╔╝ ╚████╔╝ ███████╗███████╗
  ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝   ╚═══╝  ╚══════╝╚══════╝
""" + RESET)

print(YELLOW + "🔥 Welcome to ASCII Battle Arena 🔥" + RESET)

# Player setup
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"\nWelcome {name}! Get ready to fight!\n")

health = 100
score = 0

# Game loop
for round_num in range(1, 6):
    print(f"\n--- Round {round_num} ---")
    enemy = random.randint(10, 30)

    print(f"Enemy appears with {enemy} HP 💀")

    action = input("Choose: attack ⚔️ / defend 🛡️ / heal ❤️ : ").lower()

    if action == "attack":
        damage = random.randint(15, 35)
        enemy -= damage
        score += damage
        print(GREEN + f"You hit for {damage} damage!" + RESET)

    elif action == "defend":
        block = random.randint(5, 20)
        health += block
        print(BLUE + f"You block and gain {block} HP!" + RESET)

    elif action == "heal":
        heal = random.randint(10, 25)
        health += heal
        print(YELLOW + f"You heal for {heal} HP ❤️" + RESET)

    else:
        print(RED + "You froze! No action taken 😭" + RESET)
        health -= 10

    # enemy counterattack
    if enemy > 0:
        damage = random.randint(5, 20)
        health -= damage
        print(RED + f"Enemy hits you for {damage} damage!" + RESET)

    print(f"Health: {health} | Score: {score}")

    if health <= 0:
        print(RED + "\nYou were defeated 💀" + RESET)
        break

# Save score
print("\nGame Over!")
print(f"Final Score: {score}")

with open("learning/scores.txt", "a") as file:
    file.write(f"{name},{age},{score}\n")

print(GREEN + "Score saved to leaderboard 🏆" + RESET)
