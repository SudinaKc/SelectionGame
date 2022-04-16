from tkinter.messagebox import YES
from turtle import left, right

print("Selection Game")
print("Welcome!!")
name = input("Enter your name: ")
age = int(input("Age: "))
health = 10
if age >= 18:
    print("You are eligble to play this game.")
    wants_to_play = input("Do you want to play (Yes/no)").lower()
    if wants_to_play == "yes":
        print("you are starting with", health, "health")
        print("Lets Start the game!!")
        left_or_right = input("First choice ... (left/right)")
        if left_or_right == "left":
            ans = input(
                "Nice, you follow the path and reach a lake . Do you swim across or go around (across/ around)")
            if ans == "around":
                print("You choose around and reached the other side of the lake.")
            elif ans == "across":
                print("You managed to reach across, but got bitten by a shark.")
                health -= 5
            ans = input(
                "You found Hotel and zip line. Where do you want go (hotel/zip)?")
            if ans == "hotel":
                print("You went to hotel and the owner killed you. ")
                if health <= 0:
                    print("You now have 0 health and you lost the game.")
                else:
                    print("You have survived")
                    print("Congrats!!! You won!!! ")
            else:
                print("You fell from ziplining and lost.")
        else:
            print("You are eaten by tiger on the path and lost the game.")
    else:
        print("Go and study")
else:
    print("You are not eligble to play.")
