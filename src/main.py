import time
import os

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
wait = time.sleep

print("Welcome to the Dungeon Crawler!")
input("Press Enter to start your adventure...")
clear()
wait(2)
print("1: 4")
wait(0.05)
clear()
input("Press Enter to continue...")
print("2: 8")
wait(0.05)
clear()

code = input("Enter the secret code to unlock the next level: ")
if code == "48":
    print("Code accepted! You may proceed to the next level.")
else:
    print("Incorrect code. Please try again later.")
input("Press Enter to exit the game...")