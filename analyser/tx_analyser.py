class Text_Analyser():
    def __init__(self, text = None):
        self.text = text

    def count_words(self):
        return len(self.text.split())

    def count_letters(self):
        return len(self.text.replace(' ', ''))

    def count_blank_space(self):
        return self.text.count(' ')
    
    def words(self):
        return self.text.split()
    
    def mean_letters_per_words(self):
        mean = self.count_letters() / self.count_words()
        return mean
    
    def top_most_frequent_words(self, only_more_than_3_letters = False):
        from collections import Counter
        from itertools import islice

        if only_more_than_3_letters is True:
            filtered_words_more_3_letters = [word for word in self.words() if len(word) > 3]
            words_rank = Counter(filtered_words_more_3_letters)
            words_rank = dict(sorted(words_rank.items(), key=lambda item: item[1], reverse = True))
            top5 = dict(islice(words_rank.items(), 5))
            return top5
        else:
            words_rank = Counter(self.words())
            words_rank = dict(sorted(words_rank.items(), key=lambda item: item[1], reverse = True))
            top5 = dict(islice(words_rank.items(), 5))
            return top5