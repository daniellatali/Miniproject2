prompt = '> '

print(f"Please insert a color")
color = input(prompt)

print(f"Please enter 5 adjectives")
adjective1 = input(prompt)
adjective2 = input(prompt)
adjective3 = input(prompt)
adjective4 = input(prompt)

print(f"Now input a noun")
noun = input(prompt)

print(f"Enter a body part in plural form")
body = input(prompt)

print(f"Now enter another body part in singular form")
body2 = input(prompt)

print(f"Now enter an animal in plural form")
animal = input(prompt)

print(f"""The {color} Dragon has {adjective1} {body} and a {body2} shaped like a {noun}.
It loves to eat {animal}, although it will feast on nearly anything. It is {adjective2} and {adjective3}.
You must be {adjective4} around it, or you may end up as it's meal!
""")
