prompt = '> '

print(f"Please insert 2 verbs")
verb1 = input(prompt)
verb2 = input(prompt)

print(f"Please enter 2 adjectives")
adjective1 = input(prompt)
adjective2 = input(prompt)

print(f"Now enter a verb ending with -ed")
verbed = input(prompt)

print(f"Now enter another verb ending with -ing")
verbing = input(prompt)

print(f"Now enter a type of liquid ")
liquid = input(prompt)

print(f"Now input 3 nouns")
noun1 = input(prompt)
noun2 = input(prompt)
noun3 = input(prompt)

print(f"""
Jack and Jill went up the {noun1},
To {verb1} a pail of {liquid};
Jack {verbed} down, and broke his {noun2},
And Jill came {verbing} after.

Then up Jack got and off did {verb2},
As {adjective1} as he could caper,
To old Dame Dob, who patched his {noun2}
With {noun3} and {adjective2} paper.
""")
