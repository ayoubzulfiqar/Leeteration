import re

def preprocess_sentence(sentence):
    sentence = sentence.lower()
    sentence = re.sub(r'[^a-z0-9\s]', '', sentence)
    words = [word for word in sentence.split() if word]
    return set(words)

def calculate_jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    if union == 0:
        return 1.0
    return intersection / union

def are_sentences_similar(sentence1, sentence2, threshold=0.5):
    if not isinstance(sentence1, str) or not isinstance(sentence2, str):
        raise TypeError("Both inputs must be strings.")
    if not (0.0 <= threshold <= 1.0):
        raise ValueError("Threshold must be between 0.0 and 1.0.")

    words1 = preprocess_sentence(sentence1)
    words2 = preprocess_sentence(sentence2)

    similarity = calculate_jaccard_similarity(words1, words2)

    return similarity >= threshold, similarity