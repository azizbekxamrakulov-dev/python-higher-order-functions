sentence = "Functional programming in Python is very powerful and elegant"

words = sentence.split()
top3_longest = sorted(words, key=lambda w: len(w), reverse=True)[:3]

print(top3_longest)