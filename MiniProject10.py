prompt = '> '

print(f"Please insert 5 nouns")
noun1 = input(prompt)
noun2 = input(prompt)
noun3 = input(prompt)
noun4 = input(prompt)
noun5 = input(prompt)

print(f"Please enter 3 adjectives")
adjective1 = input(prompt)
adjective2 = input(prompt)
adjective3 = input(prompt)

print(f"Now input 3 plural nouns")
pluralnoun1 = input(prompt)
pluralnoun2 = input(prompt)
pluralnoun3 = input(prompt)

print(f"Now insert a verb")
verb1 = input(prompt)

print(f"Now insert another verb but ending with -ing")
verbing = input(prompt)

print(f"Now input 2 occupations")
occ1 = input(prompt)
occ2 = input(prompt)

print(f"Now insert 2 school subjects")
subject1 = input(prompt)
subject2 = input(prompt)

print(f"Finally, enter any part of the body")
body = input(prompt)

print(f"""
The following has been quotes by Albert Einstein himself:
(Don't look this up online trust us this is 100% factual and real.)

"Any intelligent fool can make things {adjective1}, more {adjective2}, and more violent.
It takes a touch of genius -- and a lot of {pluralnoun1} -- to move in the opposite {noun1}."

"Reality is merely a {noun2}, albeit a very {adjective3} one."

"Great {pluralnoun2} have often encountered violent opposition from weak {pluralnoun3}."

"Technological progress is like a {noun3} in the hands of a pathological {occ1}."

"No, this {noun4} won`t work... How on earth are you ever going to {verb1} in terms
of {subject1} and {subject2} so important a biological phenomenon as {adjective3} love?"

"The release of {noun5} power has changed everything except our way
of {verbing}... the solution to this problem lies in the {body} of mankind.
If only I had known, I should have become a {occ2}."
""")
