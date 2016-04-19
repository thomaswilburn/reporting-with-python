"""
This is a simple script intended to test your comprehension--I don't expect you to write it, so it does use some features that we haven't talked about in class, but you should be able to read it and figure out what's going on.

Please annotate it with comments for each line (comments are lines starting with a # character) that explain what the script is doing. When in doubt, err on the side of verbosity.

Note: this script is actually broken in a non-obvious way! It will run, but it will end up with incorrect results. Can you figure out why? If you can figure out the error, either fix it in place or leave a comment at the end describing the bug.
"""

import random

player_one = 0
player_two = 0

choices = ["rock", "paper", "scissors"]

while player_one + player_two < 3:
    p1 = random.choice(choices)
    p2 = random.choice(choices)
    print("Player one chose:" + p1)
    print("Player two chose:" + p2)
    if (p1 == "rock" and p2 == "scissors") or (p1 == "paper" and p2 == "rock") or (p1 == "scissors" and p2 == "paper"):
        print("Player one scores a point.")
        player_one = player_one + 1
    else:
        print("Player two scores a point.")
        player_two = player_two + 1
    print("Current score: " + str(player_one) + " vs " + str(player_two))

if player_one > player_two:
    print("Player one wins!")
else:
    print("Player two wins!")