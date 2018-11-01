prompt = '> '

print(f"Please enter your name")
name = input(prompt)

print(f"Please insert any nationality")
nationality = input(prompt)

print(f"Please enter 4 adjectives")
adjective1 = input(prompt)
adjective2 = input(prompt)
adjective3 = input(prompt)
adjective4 = input(prompt)

print(f"Now input 3 nouns")
noun1 = input(prompt)
noun2 = input(prompt)
noun3 = input(prompt)

print(f"Now enter a plural noun")
pluralnoun = input(prompt)

print(f"Enter two types of foods")
food1 = input(prompt)
food2 = input(prompt)

print(f"Please enter 2 sets of numbers")
number1 = input(prompt)
number2 = input(prompt)

print(f"Finally, input any kind of shapes")
shapes = input(prompt)

print(f"""Pizza was invented by a {adjective1} {nationality} chef named {name}.
To make a pizza, you need to take a lump of {noun1}, and make a thin, round {adjective2} {noun2}.
Then you cover it with {adjective3} sauce, {adjective4} cheese, and fresh chopped {pluralnoun}.
Next you have to bake it in a very hot {noun3}.
When it is done, cut it into {number1} {shapes}.
Some kids like {food1} pizza the best, but my favorite is the {food2} pizza.
If I could, I would eat pizza {number2} times a day!
""")
