import tkinter as tk

class App(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.text_analyser = Text_Analyser()
        self.window_creation()

    def text_capture(self):
        self.text_entry = tk.Entry(self)
        self.text_entry.pack(side = 'left')
        
    def window_creation(self):
        self.text_capture()

        self.button_statistics_calculation = tk.Button(self,
                                                       text = 'Statistics Calculation',
                                                       command = self.text_analyser.statistics_calculation)
        self.button_statistics_calculation.pack(side = 'left')

        self.label_results = tk.Label(self, text='')
        self.label_results.pack(side="bottom")

class Text_Analyser(App):
    def __init__(self):
        self.text = App.text_capture()

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
    
    def statistics_calculation(self):
        count_words = self.count_words()
        count_letters = self.count_letters()
        top_words = self.top_most_frequent_words()

        string_results = f'''
            count of words: {count_words}
            count of letters: {count_letters}
            top 5 words: {top_words}
        '''
        self.label_results.config(text = string_results) # label created in App class