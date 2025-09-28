import tkinter as tk
import math
import random

SWEDISH = ["å", "ä", "ö", "Å", "Ä", "Ö"]  # Swedish letters

OPPONENTS = ["Rocky", "Random", "Reinhard"]
ROCK = "Rock"
PAPER = "Paper"
SCISSORS = "Scissors"

OPTIONS = [ROCK, PAPER, SCISSORS]

DRAW = 2
WIN = 1
LOSS = 0

RESULT = ["LOSS", "WIN", "DRAW"]


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

        self.opponent = None
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

    def switch_opponent(self, opponent):
        self.opponent = opponent


class MainMenu(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="Main menu").pack(
            side="top", fill="x", pady=10
        )
        self._parent = parent

        self.opponent_selection = tk.StringVar(value=OPPONENTS[0])

        opponent_selection_label = tk.Label(self, text="Select an opponent")
        opponent_selection_label.pack(pady=10)
        opponent_selection_menu = tk.OptionMenu(
            self, self.opponent_selection, *OPPONENTS
        )
        opponent_selection_menu.pack(pady=10)

        self.start_game = tk.Button(
            self,
            command=lambda: self.play_game(),
            text="Play",
        ).pack(side="top", fill="x", pady=10)
        self.quit = tk.Button(self, text="Exit", command=lambda: parent.quit()).pack(
            side="top", fill="x", pady=10
        )

    def play_game(self):
        self._parent.opponent = self.opponent_selection.get()
        self._parent.switch_frame(Game)


class Game(tk.Frame):
    def game_rule(self, selection, opponent_selection):
        """
        The basic rules of rock paper scissors
        Rock beats Scissors
        Paper beats Rock
        Scissors beat Paper
        """
        if selection == opponent_selection:
            return DRAW
        elif (
            selection == ROCK
            and opponent_selection == SCISSORS
            or selection == PAPER
            and opponent_selection == ROCK
            or selection == SCISSORS
            and opponent_selection == PAPER
        ):
            return WIN
        return LOSS

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="Game").pack(side="top", fill="x", pady=10)
        self.opponent = parent.opponent
        self.results = [0, 0, 0]

        self.rock_button = tk.button = tk.Button(
            self, text=ROCK, command=lambda: self.play(ROCK)
        ).pack(side="top", fill="x", pady=10)
        self.paper_button = tk.button = tk.Button(
            self, text=PAPER, command=lambda: self.play(PAPER)
        ).pack(side="top", fill="x", pady=10)
        self.scissor_button = tk.button = tk.Button(
            self,
            text=SCISSORS,
            command=lambda: self.play(SCISSORS),
        ).pack(side="top", fill="x", pady=10)

        self.goto_main_menu = tk.button = tk.Button(
            self, text="Give up", command=lambda: parent.switch_frame(MainMenu)
        ).pack(side="top", fill="x", pady=10)

    def play(self, played):
        print("You have played", played)
        opponents_selection = self.opponent_turn(played)
        print("Your opponent has played: ", opponents_selection)
        result = self.game_rule(played, opponents_selection)
        print("Result:", RESULT[result])
        self.results[result] += 1
        print(
            "Number of wins: ",
            self.results[WIN],
            "Number of draws: ",
            self.results[DRAW],
            "Number of losses: ",
            self.results[LOSS],
        )

    def opponent_turn(self, played):
        if self.opponent == "Rocky":
            return ROCK
            print("Your opponent has played: ", ROCK)
        if self.opponent == "Random":
            select = random.uniform(0, 3)
            option = OPTIONS[math.floor(select)]
            return option
        if self.opponent == "Reinhard":
            select = random.uniform(0, 3)
            option = OPTIONS[math.floor(select)]
            cheat = self.game_rule(played, option)
            if cheat == WIN:
                select = random.uniform(0, 3)
                option = OPTIONS[math.floor(select)]
            return option


if __name__ == "__main__":
    game = RockPaperScissorGame()
    game.mainloop()
