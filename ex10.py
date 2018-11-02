words = raw_input()

words2 = words.upper().split(' ')

setOfWords = set(words2)

print " ".join(sorted(list(setOfWords)))
