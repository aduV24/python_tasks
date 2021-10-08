# This python program displays random jokes usinmg the random module
# Learnt howe to use the random module here:
# https://www.w3schools.com/python/ref_random_randint.asp

import random
i = random.randint(0, 9)

jokes = ["I’d like to start with the chimney jokes – I’ve got a stack of "
         "them. The first one is on the house.",
         "The best time to add insult to injury is when you’re signing "
         "somebody’s cast.",
         "Years ago I used to supply Filofaxes for the mafia. I was "
         "involved in very organised crime.",
         "Years ago I used to supply Filofaxes for the mafia. I was "
         "involved in very organised crime.",
         "I waited and stayed up all night and tried to figure out where "
         "the sun was. Then it dawned on me.",
         "I saw this bloke chatting-up a cheetah. I thought: ‘He’s trying "
         "to pull a fast one.",
         "This policeman came up to me with a pencil and a piece of very "
         "thin paper. He said, ‘I want you to trace someone for me.",
         "My New Year’s resolution is to get in shape. I choose round.",
         "My wife – it’s difficult to say what she does. She sells "
         "seashells on the seashore.",
         "Toughest job I ever had? Selling doors, door-to-door."]

print("Generating random jokes..............")
print()
print(jokes[i])
