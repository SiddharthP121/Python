# count unique words in a sentence

sent = 'I have a cat who have a ball'
new = sent.split(' ')

unique = set(new)

print(unique)

print(len(unique))

