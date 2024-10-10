sentence = "hello world, how are you?"

capital_sentence = ""

words = sentence.split()

for word in words:
    sentence = word[0].upper() + word[1:].lower()
    capital_sentence += sentence + " "

capital_sentence = capital_sentence.strip()

print(capital_sentence)