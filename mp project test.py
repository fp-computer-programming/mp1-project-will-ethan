
def xinput(prompt):
    try:
        seen = xinput.seen
    except AttributeError:
        seen = xinput.seen = set()

    while True:
        response = input(prompt)
        if response in seen:
            print(f'You already entered "{response}". Enter again')
        else:
            seen.add(response)
            return response

b1 = xinput('Enter an adjective: ')
b2 = xinput('Enter a noun: ')
b3 = xinput('Enter a verb: ')
b4 = xinput("Noun(place): ")
b5 = xinput("Verb: ")
b6 = xinput("Adjective: ")
b7 = xinput("Noun(place): ")
b8 = xinput("Noun(person): ")
b9 = xinput("Noun(object): ")
b10 = xinput("Noun(exclamation): ")
b11 = xinput("Verb: ")
b12 = xinput("Verb(sense): ")
b13 = xinput("Noun(feeling): ")
b14 = xinput("Noun(object): ")
b15 = xinput("Verb(emotion): ")
b16 = xinput("Verb(emotion): ")
b17 = xinput("Verb: ")
b18 = xinput("Pronoun: ")
b19 = xinput("Adjective(emotion): ")
b20 = xinput("Verb(action): ")
b21 = xinput("Adjective(emotion): ")
b22 = xinput("Noun(quote): ")
b23 = xinput("Verb: ")
b24 = xinput("Verb: ")
b25 = xinput("Verb: ")
b26 = xinput("Noun(Jesuit figure): ")
b27 = xinput("Noun(quote): ")
b28 = xinput("Noun(question): ")
b29 = xinput("Noun(answer question): ")
b30 = xinput("Adjective(emotion): ")
b31 = xinput("Noun(question): ")
b32 = xinput("Noun(thought): ")
b33 = xinput("Noun(question): ")
b34 = xinput("Verb: ")
b35 = xinput("Noun(opinion): ")
b36 = xinput("Verb: ")
b37 = xinput("Noun(time): ")
b38 = xinput("Verb: ")
b39 = xinput("Verb: ")
b40 = xinput("Noun(opinion): ")
b41 = xinput("Adjective(emotion): ")
b42 = xinput("Noun(someone): ")
b43 = xinput("Noun(thing): ")
b44 = xinput("Verb(rude action): ")
b45 = xinput("Verb(action): ")
b46 = xinput("Verb(action): ")
b47 = xinput("Verb(imperfect action): ")
b48 = xinput("Noun(group of people): ")
b49 = xinput("Verb(action): ")
b50 = xinput("Verb(action): ")
b51 = xinput("Noun(lesson): ")
b52 = xinput("Noun(thing): ")

print(f'''It was a {b1} and {b2} night. 
Ignatius was found {b3} in the {b4}. 
The locals couldn't help but {b5}in{b6}.
They knew that he needed to be taken to the {b7}. 
After taking him there, they told the {b8} that they think he was hit by a {b9}.
\"{b10}\", Ignatius exclaimed as he {b11}.
The locals who brought him there had {b12} that he was in {b13}, so they brought him {b14}.
Upon receiving the gift, he was {b15} to {b16}.
He told them he was {b17} towards them and wanted them to {b18}.
The people were {b19} by his reaction, and left after saying {b20} to him.
Ignatius was now alone and had time to {b21} but didn’t want to {b22} the people who brought him the gift.
He decided to {b23} until the next morning. 
When he woke up, {b24} was in his room.
Ignatius yelled in surprise saying \"{b25}!\" The Jesuit figure asked him \"{b26}?\". 
To which Ignatius replied \"{b27}\". {b28} with this response, then asked \"{b29}?\". 
Ignatius didn’t answer and acted like he was {b30}, although he also wondered {b31} too. 
The Jesuit tried to ask him \"{b32}\" but was interrupted by Ignatius asking him to {b33}, and he complied.
Though Ignatius acted like he {b34} about what the man had to say, he {b35} about it later. 
In the following {b36}, Ignatius decided that he would {b37} the peoples gifts. 
Once he started {b38}, he found that he {b38}(Opinion) doing it, and felt {b39} towards the people.
He realized what {b24} was trying to tell him. 
He got right to sending {b40} and {b24} a {b41}, wanting to apologize for {b42} them.
Upon receiving these, {b40} and {b24} decided to {b43}.
To show that he wanted to {b44}, Ignatius {b45}. 
The {b46} forgave Ignatius by {b47}, and told him {b48} in the future. 
Ignatius learned {b49}, and gained {b50} in the process.
''')