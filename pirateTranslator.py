pirate = {}
pirate['English'] = 'Pirate'
pirate['sir'] = 'matey'
pirate['hotel'] = 'fleabag inn'
pirate['student'] = 'swabbie'
pirate['boy'] = 'matey'
pirate['restaurant'] = 'galley'
pirate['professor'] = 'foul blaggart'
pirate['man'] = 'matey'
pirate['is'] = 'be'
pirate['hello'] = 'avast'
pirate['my'] = 'me'
pirate['restroom'] = 'head'
pirate['the'] = 'th’'
pirate['lawyer'] = 'snake'
pirate['are'] = 'be'
pirate['students'] = 'swabbies'
pirate['excuse'] = 'arr'
pirate['your'] = 'yer'
# and so on

sentence = input("Please enter a sentence in English")

psentence = []
words = sentence.split()
for aword in words:
    if aword in pirate:
        psentence.append(pirate[aword])
    else:
        psentence.append(aword)

print(" ".join(psentence))
