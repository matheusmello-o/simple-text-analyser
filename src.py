from analyser.tx_analyser import App
import tkinter as tk 

def main():
    root = tk.Tk()
    App(master=root)
    root.mainloop()

if __name__ == '__main__':
    main()