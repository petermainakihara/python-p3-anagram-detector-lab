
class Anagram:
    def __init__(self, word):
        self.word = word.lower()   # store the original word in lowercase
        self.sorted_word = sorted(self.word)  # precompute sorted letters for efficiency

    def match(self, words):
        matches = []
        for candidate in words:
            # make sure we don't count the word itself
            if candidate.lower() != self.word and sorted(candidate.lower()) == self.sorted_word:
                matches.append(candidate)
        return matches
