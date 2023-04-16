"""
Word Occurrences
Estimate: 20 minutes
Actual:45 minutes
"""
word_counts = {}
text = input("Text: ")
words_list = text.split()
for word in words_list:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1
vocabulary_list = list(word_counts.keys())
vocabulary_list.sort()

longest_length = max(len(word) for word in words_list)
for word in vocabulary_list:
    print(f"{word:{longest_length}} = {word_counts[word]}")
