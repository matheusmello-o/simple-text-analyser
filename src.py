#import sys
#sys.path.append('analyser/')
from analyser.tx_analyser import Text_Analyser
import tkinter as tk 

def creating_window():
    window = tk.Tk()
    window.title('Text Analyser')
    window.geometry('600x400')
    
    text_box = tk.Entry(window)
    text_box.pack(pady = 50)

    window.mainloop()


def main():
    text = 'testing the most pica das galaxias'
    analyser = Text_Analyser(text)
    
    creating_window()


if __name__ == '__main__':
    main()