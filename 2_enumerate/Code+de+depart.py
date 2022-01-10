phrase = 'Phrase en camel case'

# Convertir la phrase ci-dessus dans ce format :
'phraseEnCamelCase'
words = phrase.lower().split()
camelCase_sentence = words[0]

for i, word in enumerate(words):
    if i > 0:
        camelCase_sentence += word.title()

print(camelCase_sentence)
    
    
