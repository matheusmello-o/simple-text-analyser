from analyser.tx_analyser import App
import tkinter as tk 

def main():
    root = tk.Tk()
    root.title('Text Analyser')
    root.geometry('500x400')
    App(master=root)
    root.mainloop()

if __name__ == '__main__':
    main()