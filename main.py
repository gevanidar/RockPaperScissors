import tkinter as tk

HEIGHT = 400
WIDTH = 400
WINDOW_SIZE = str(HEIGHT) + "x" + str(WIDTH)


class RockPaperScissorGame(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self._frame = None
        self.switch_frame(MainMenu)

    def switch_frame(self, frame_class):
        """
        Destroy the previous frame and all of its children.
        Create a new frame with new frame in its place.
        """
        new_frame = frame_class(self)
        if self._frame is not None:
            for widget in self._frame.winfo_children():
                widget.destroy()
            self._frame.destroy()
        self._frame = new_frame
        new_frame.pack()


class MainMenu(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="Main menu").pack(
            side="top", fill="x", pady=10
        )
        self.quit_button = tk.Button(
            self, text="Start", command=lambda: parent.switch_frame(Game)
        ).pack(side="top", fill="x", pady=10)


class Game(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="Game").pack(side="top", fill="x", pady=10)
        self.game_button = tk.button = tk.Button(
            self, text="Quit", command=lambda: parent.switch_frame(MainMenu)
        )
        self.game_button.pack(side="top", fill="x", pady=10)


if __name__ == "__main__":
    game = RockPaperScissorGame()
    game.mainloop()
