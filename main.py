import tkinter as tk

HEIGHT = 400
WIDTH = 400
WINDOW_SIZE = str(HEIGHT) + "x" + str(WIDTH)

if __name__ == "__main__":
    rootWindow = tk.Tk()
    rootWindow.title("Game")
    rootWindow.geometry(WINDOW_SIZE)

    label = tk.Label(rootWindow, text="hello")
    label.pack(pady=100)

    rootWindow.mainloop()
