import tkinter as tk

class App:
    def __init__(self, master = None):
        self.master = master
        self.window_creation()
        
    def window_creation(self):
        self.text_entry_widget = tk.Entry(self.master)
        self.text_entry_widget.pack(side = 'left')

        self.button_statistics_calculation = tk.Button(self.master,
                                                       text = 'Statistics Calculation',
                                                       command = self.statistics_calculation)
        self.button_statistics_calculation.pack(side = 'left')

        self.label_results = tk.Label(self.master, text='')
        self.label_results.pack(side="bottom")
    
    def text_capture(self):
        return self.text_entry_widget.get() # catching text that were create in window_creation() methoded
        
    def statistics_calculation(self):
        text = self.text_capture()
        text_analyser = Text_Analyser()
        
        text_analysed = text_analyser.analyse_text(text)
        
        self.label_results.config(text = text_analysed)

class Text_Analyser:
    def __init__(self):
        pass

    def count_words(self, text):
        return len(text.split())

    def count_letters(self, text):
        return len(text.replace(' ', ''))

    def count_blank_space(self, text):
        return text.count(' ')
    
    def words(self, text):
        return text.split()
    
    def mean_letters_per_words(self, text):
        mean = self.count_letters(text) / self.count_words(text)
        return mean
    
    def top_most_frequent_words(self, text, only_more_than_3_letters = False):
        from collections import Counter
        from itertools import islice

        if only_more_than_3_letters is True:
            filtered_words_more_3_letters = [word for word in self.words(text) if len(word) > 3]
            words_rank = Counter(filtered_words_more_3_letters)
            words_rank = dict(sorted(words_rank.items(), key=lambda item: item[1], reverse = True))
            top5 = dict(islice(words_rank.items(), 5))
            return top5
        else:
            words_rank = Counter(self.words(text))
            words_rank = dict(sorted(words_rank.items(), key=lambda item: item[1], reverse = True))
            top5 = dict(islice(words_rank.items(), 5))
            return top5
    
    def analyse_text(self, text):
        count_words = self.count_words(text)
        count_letters = self.count_letters(text)
        top_words = self.top_most_frequent_words(text)

        string_results = f'''
            count of words: {count_words}
            count of letters: {count_letters}
            top 5 words: {top_words}
        '''

        return string_results