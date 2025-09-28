import tkinter as tk
import math
import random

SWEDISH = ["å", "ä", "ö", "Å", "Ä", "Ö"]  # Swedish letters

OPPONENTS = ["Rocky", "Random", "Reinhard"]


class RockPaperScissorGame(tk.Tk):
    HEIGHT = 400
    WIDTH = 400
    WINDOW_SIZE = str(HEIGHT) + "x" + str(WIDTH)

    def __init__(self, *args, **kwargs):
        """
        Init the main window to the game
        Main window starts at the MainMenu
        """
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry(self.WINDOW_SIZE)
        self.title("Sten sax påse")

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

        self.start_game = tk.Button(
            self, text="Play", command=lambda: parent.switch_frame(Game)
        ).pack(side="top", fill="x", pady=10)
        self.quit = tk.Button(self, text="Exit", command=lambda: parent.quit()).pack(
            side="top", fill="x", pady=10
        )


class Game(tk.Frame):
    ROCK = "Rock"
    PAPER = "Paper"
    SCISSORS = "Scissors"

    OPTIONS = [ROCK, PAPER, SCISSORS]

    DRAW = 2
    WIN = 1
    LOSS = 0

    RESULT = ["LOSS", "WIN", "DRAW"]

    def game_rule(self, selection, opponent_selection):
        """
        The basic rules of rock paper scissors
        Rock beats Scissors
        Paper beats Rock
        Scissors beat Paper
        """
        if selection == opponent_selection:
            return self.DRAW
        elif (
            selection == self.ROCK
            and opponent_selection == self.SCISSORS
            or selection == self.PAPER
            and opponent_selection == self.ROCK
            or selection == self.SCISSORS
            and opponent_selection == self.PAPER
        ):
            return self.WIN
        return self.LOSS

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="Game").pack(side="top", fill="x", pady=10)

        self.OPPONENT = OPPONENTS[0]

        self.rock_button = tk.button = tk.Button(
            self, text=self.ROCK, command=lambda: self.play(self.ROCK)
        ).pack(side="top", fill="x", pady=10)
        self.paper_button = tk.button = tk.Button(
            self, text=self.PAPER, command=lambda: self.play(self.PAPER)
        ).pack(side="top", fill="x", pady=10)
        self.scissor_button = tk.button = tk.Button(
            self,
            text=self.SCISSORS,
            command=lambda: self.play(self.SCISSORS),
        ).pack(side="top", fill="x", pady=10)

        self.goto_main_menu = tk.button = tk.Button(
            self, text="Give up", command=lambda: parent.switch_frame(MainMenu)
        ).pack(side="top", fill="x", pady=10)

    def play(self, played):
        print("You have played", played)
        opponents_selection = self.opponent_turn(played)
        print("Your opponent has played: ", opponents_selection)
        result = self.game_rule(played, opponents_selection)
        print("Result:", self.RESULT[result])

    def opponent_turn(self, played):
        if self.OPPONENT == "Rocky":
            return self.ROCK
            print("Your opponent has played: ", self.ROCK)
        if self.OPPONENT == "Random":
            select = random.uniform(0, 3)
            option = self.OPTIONS[math.floor(select)]
            return option
        if self.OPPONENT == "Reinhard":
            select = random.uniform(0, 3)
            option = self.OPTIONS[math.floor(select)]
            cheat = self.game_rule(played, option)
            if cheat == self.WIN:
                select = random.uniform(0, 3)
                option = self.OPTIONS[math.floor(select)]
            return option


if __name__ == "__main__":
    game = RockPaperScissorGame()
    game.mainloop()
