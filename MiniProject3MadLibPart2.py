#MiniProject1

Words1 = ["noun", "2nd noun", "3rd noun", "verb","2nd verb", "liquid", "verb ending with -ed",
"verb ending with -ing", "adjective", "2nd adjective"]

Dictonary = {}

for Word in Words1:
    Wording = input(f"""Please insert a/an {Word}
    > """)
    Dictonary[Word] = Wording

print(f"""
Jack and Jill went up the {Dictonary['noun']},
To {Dictonary['verb']} a pail of {Dictonary['liquid']};
Jack {Dictonary['verb ending with -ed']} down, and broke his {Dictonary['2nd noun']},
And Jill came {Dictonary['verb ending with -ing']} after.

Then up Jack got and off did {Dictonary['2nd verb']},
As {Dictonary['adjective']} as he could caper,
To old Dame Dob, who patched his {Dictonary['2nd noun']}
With {Dictonary['3rd noun']} and {Dictonary['2nd adjective']} paper.
""")


#MiniProject2

Words2 = ["adjective", "2nd adjective", "3rd adjective", "4th adjective",
"5th adjective","6th adjective", "plural noun", "number", "2nd number", "place" ]

for Word in Words2:
    Wording = input(f"""Please insert a/an {Word}
    > """)
    Dictonary[Word] = Wording

print(f"""I'm a {Dictonary['adjective']}, {Dictonary['adjective']} man, I'm {Dictonary['2nd adjective']} and I'm in my prime
I'm a {Dictonary['adjective']}, {Dictonary['adjective']} man, I'm {Dictonary['2nd adjective']} and I'm in my prime
I don't pick my {Dictonary['plural noun']}, I'm ready for any ol' kind
Yes, I'm a real {Dictonary['2nd adjective']} man, a brand new {Dictonary['number']}
Yes, I'm a real {Dictonary['2nd adjective']} man, a brand new {Dictonary['number']}
Well, I'm {Dictonary['3rd adjective']}, I'm {Dictonary['4th adjective']}, I'm practically much alive
Well, I'm {Dictonary['2nd number']} feet tall, I ain't no hand me down
Yes, I'm {Dictonary['2nd number']} feet tall and I ain't no hand me down
Well, I got a gal in {Dictonary['place']} who calls me {Dictonary['5th adjective']} {Dictonary['6th adjective']} Brown
""")

# MiniProject3

Words3 = ["name", "nationality", "adjective", "2nd adjective", "3rd adjective",
"4th adjective", "noun", "2nd noun", "3rd noun", "plural noun", "food item", "another food item",
"number", "2nd number", "shapes"]

for Word in Words3:
    Wording = input(f"""Please insert a/an {Word}
    > """)
    Dictonary[Word] = Wording

print(f"""Pizza was invented by a {Dictonary['adjective']} {Dictonary['nationality']} chef named {Dictonary['name']}.
To make a pizza, you need to take a lump of {Dictonary['noun']}, and make a thin, round {Dictonary['2nd adjective']} {Dictonary['2nd noun']}.
Then you cover it with {Dictonary['3rd adjective']} sauce, {Dictonary['4th adjective']} cheese, and fresh chopped {Dictonary['plural noun']}.
Next you have to bake it in a very hot {Dictonary['3rd noun']}.
When it is done, cut it into {Dictonary['number']} {Dictonary['shapes']}.
Some kids like {Dictonary['food item']} pizza the best, but my favorite is the {Dictonary['another food item']} pizza.
If I could, I would eat pizza {Dictonary['2nd number']} times a day!
""")

#MiniProject4

Words4 = ["color", "adjective", "2nd adjective", "3rd adjective", "4th adjective",
"noun", "body part", "2nd body part", "animal"]

for Word in Words4:
    Wording = input(f"""Please insert a/an {Word}
    > """)
    Dictonary[Word] = Wording

print(f"""The {Dictonary['color']} Dragon has {Dictonary['adjective']} {Dictonary['body part']} and a {Dictonary['2nd body part']} shaped like a {Dictonary['noun']}.
It loves to eat {Dictonary['animal']}, although it will feast on nearly anything. It is {Dictonary['2nd adjective']} and {Dictonary['3rd adjective']}.
You must be {Dictonary['4th adjective']} around it, or you may end up as it's meal!
""")


#MiniProject5

Words5 = ["place", "adjective", "2nd adjective", "noun", "2nd noun", "plural noun",
"2nd plural noun", "verb", "2nd verb", "number", "body part"]

for Word in Words5:
    Wording = input(f"""Please insert a/an {Word}
    > """)
    Dictonary[Word] = Wording

print(f"""Two {Dictonary['plural noun']}, both alike in dignity,
In fair {Dictonary['place']}, where we lay our scene,
From ancient {Dictonary['noun']} break to new mutiny,
Where civil blood makes civil hands unclean.
From forth the fatal loins of these two foes
A pair of star-cross`d {Dictonary['2nd plural noun']} take their life;
Whole misadventured piteous overthrows
Do with their {Dictonary['2nd noun']} bury their parents` strife.
The fearful passage of their {Dictonary['adjective']} love,
And the continuance of their parents` rage,
Which, but their children`s end, nought could {Dictonary['verb']} ,
Is now the {Dictonary['number']} hours` traffic of our stage;
The which if you with {Dictonary['2nd adjective']} {Dictonary['body part']} attend,
What here shall {Dictonary['2nd verb']}, our toil shall strive to mend.
""")


#MiniProject6

Words6 = ["female name", "place", "color", "adjective", "2nd adjective", "noun",
"2nd noun", "3rd noun", "4th noun", "plural noun", "2nd plural noun", "3rd plural noun",
"4th plural noun", "food item", "2nd food item", "verb", "2nd verb", "3rd verb", "4th verb",
"5th verb", "verb ending with -s", "adverb", "body part", "article of clothing" ]

for Word in Words6:
    Wording = input(f"""Please insert a/an {Word}
    > """)
    Dictonary[Word] = Wording

print(f"""Picture yourself in a {Dictonary['noun']} on a river,
With {Dictonary['food item']} trees and {Dictonary['2nd food item']} skies
Somebody calls you, you {Dictonary['verb']} quite {"adverb"},
A girl with {Dictonary['adjective']} eyes.

Cellophane {Dictonary['plural noun']} of {Dictonary['color']} and green,
{Dictonary['2nd verb']} over your head.
{Dictonary['3rd verb']} for the girl with the {Dictonary['2nd noun']} in her eyes,
And she`s gone.

{Dictonary['female name']} in the sky with {Dictonary['2nd plural noun']}...
{Dictonary['female name']} in the sky with {Dictonary['2nd plural noun']}...
{Dictonary['female name']} in the sky with {Dictonary['2nd plural noun']}...

Follow her down to a {Dictonary['3rd noun']} by a fountain
Where rocking horse {Dictonary['3rd plural noun']} eat {Dictonary['4th noun']} pies,
Everyone {"verb ending with -s"} as you {Dictonary['4th verb']} past the flowers,
That {Dictonary['5th verb']} so incredibly high.

Newspaper {Dictonary['4th plural noun']} appear on the shore,
Waiting to take you away.
Climb in the back with your {Dictonary['body part']} in the clouds,
And you`re gone.

Picture yourself on a train in a {Dictonary['place']},
With {Dictonary['2nd adjective']} porters with looking glass {Dictonary['article of clothing']},
Suddenly someone is there at the turnstile,
The girl with {Dictonary['adjective']} eyes.

{Dictonary['female name']} in the sky with {Dictonary['2nd plural noun']}...
{Dictonary['female name']} in the sky with {Dictonary['2nd plural noun']}...
{Dictonary['female name']} in the sky with {Dictonary['2nd plural noun']}...
""")

#MiniProject7

Words7 = ["name","famous person", "2nd famous person" ,"nationality", "adjective", "2nd adjective",
"plural noun", "2nd plural noun", "3rd plural noun", "noun", "2nd noun", "verb", "occupation",
"liquid", "number", "place"]

for Word in Words7:
    Wording = input(f"""Please insert a/an {Word}
    > """)
    Dictonary[Word] = Wording

print(f"""
I enjoy long, {Dictonary['adjective']} walks on the beach, getting {Dictonary['verb']} in the rain and serendipitous encounters with {Dictonary['plural noun']}.
I really like piña coladas mixed with {Dictonary['liquid']}, and romantic, candle-lit {Dictonary['2nd plural noun']}.
I am well-read from Dr. Seuss to {Dictonary['famous person']}.
I travel frequently, especially to {Dictonary['place']}, when I am not busy with work. (I am a {Dictonary['occupation']}.)
I am looking for {Dictonary['noun']} and beauty in the form of a {Dictonary['nationality']} goddess.
She should have the physique of {Dictonary['2nd famous person']} and the {Dictonary['2nd noun']} of {Dictonary['name']}.
I would prefer if she knew how to cook, clean, and wash my {Dictonary['3rd plural noun']}.
I know I’m not very attractive in my picture, but it was taken {Dictonary['number']} days ago, and I have since become more {Dictonary['2nd adjective']}.
""")

#MiniProject8

Words8 = ["verb", "2nd verb", "3rd verb", "4th verb", "5th verb", "noun", "2nd noun",
"adjective", "feeling", "body part"]

for Word in Words8:
    Wording = input(f"""Please insert a/an {Word}
    > """)
    Dictonary[Word] = Wording

print(f"""
What would you think if I {Dictonary['verb']} out of tune?
Would you {Dictonary['2nd verb']} up and {Dictonary['3rd verb']} out on me?
Lend me your {Dictonary['body part']} and I'll {Dictonary['4th verb']} you a song
And I'll try not to {Dictonary['4th verb']} out of key
Oh, I get by with a {Dictonary['adjective']} help from my {Dictonary['noun']}
Mm, I get high with a {Dictonary['adjective']} help from my {Dictonary['noun']}
Mm, gonna try with a {Dictonary['adjective']} help from my {Dictonary['noun']}
What do I do when my {Dictonary['2nd noun']} is away?
Does it worry you to be alone?
How do I feel by the end of the day?
Are you {Dictonary['feeling']} because you're on your own?
No, I get by with a {Dictonary['adjective']} help from my {Dictonary['noun']}
Mm, get high with a {Dictonary['adjective']} help from my {Dictonary['noun']}
Mm, gonna try with a {Dictonary['adjective']} help from my {Dictonary['noun']}
Do you need anybody?
I need somebody to {Dictonary['5th verb']}
Could it be anybody?
I want somebody to {Dictonary['5th verb']}.
""")


#MiniProject9

Words9 = ["noun", "2nd noun", "3rd noun", "4th noun", "5th noun", "plural noun",
"2nd plural noun", "3rd plural noun", "4th plural noun", "adjective", "2nd adjective",
"3rd adjective", "verb", "food item"]

for Word in Words9:
    Wording = input(f"""Please insert a/an {Word}
    > """)
    Dictonary[Word] = Wording

print(f"""
If you like to talk to {Dictonary['plural noun']}
If a {Dictonary['noun']} can make you {Dictonary['verb']}
If you like to waltz with {Dictonary['2nd plural noun']}
Up and down the produce {Dictonary['2nd noun']}...
Have we got a {Dictonary['3rd noun']} for you!

{Dictonary['food item']}Tales, {Dictonary['food item']}Tales, {Dictonary['food item']}Tales, {Dictonary['food item']}Tales,
{Dictonary['food item']}Tales, {Dictonary['food item']}Tales, {Dictonary['food item']}Tales, {Dictonary['food item']}Tales!

Broccoli! {Dictonary['3rd plural noun']}! Gotta be
{Dictonary['food item']}Tales!

{Dictonary['adjective']} beans! Collard {Dictonary['4th plural noun']}! {Dictonary['2nd adjective']} {Dictonary['4th noun']}!
{Dictonary['food item']}Tales!

Cauliflower! {Dictonary['3rd adjective']} and sour! Half an hour!
{Dictonary['food item']}Tales!

There`s never-ever-ever-ever-ever been a {Dictonary['3rd noun']} like {Dictonary['food item']}Tales!
There`s never-ever-ever-ever-ever been a {Dictonary['3rd noun']} like {Dictonary['food item']}Tales!
It`s {Dictonary['5th noun']} for {Dictonary['food item']}Tales!
""")

#MiniProject10

Words10 = ["noun", "2nd noun", "3rd noun", "4th noun", "5th noun", "adjective",
"2nd adjective", "3rd adjective", "plural noun", "2nd plural noun", "3rd plural noun",
"verb", "verb ending with -ing", "occupation", "2nd occupation", "subject", "2nd subject", "body part"]

for Word in Words10:
    Wording = input(f"""Please insert a/an {Word}
    > """)
    Dictonary[Word] = Wording

print(f"""
The following has been quotes by Albert Einstein himself:
(Don't look this up online trust us this is 100% factual and real.)

"Any intelligent fool can make things {Dictonary['adjective']}, more {Dictonary['2nd adjective']}, and more violent.
It takes a touch of genius -- and a lot of {Dictonary['plural noun']} -- to move in the opposite {Dictonary['noun']}."

"Reality is merely a {Dictonary['2nd noun']}, albeit a very {Dictonary['3rd adjective']} one."

"Great {Dictonary['2nd plural noun']} have often encountered violent opposition from weak {Dictonary['3rd plural noun']}."

"Technological progress is like a {Dictonary['3rd noun']} in the hands of a pathological {Dictonary['occupation']}."

"No, this {Dictonary['4th noun']} won`t work... How on earth are you ever going to {Dictonary['verb']} in terms
of {Dictonary['subject']} and {Dictonary['2nd subject']} so important a biological phenomenon as {Dictonary['3rd adjective']} love?"

"The release of {Dictonary['5th noun']} power has changed everything except our way
of {Dictonary['verb ending with -ing']}... the solution to this problem lies in the {Dictonary['body part']} of mankind.
If only I had known, I should have become a {Dictonary['2nd occupation']}."
""")
