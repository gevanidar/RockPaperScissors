import tkinter as tk
import math
import random

SWEDISH = ["å", "ä", "ö", "Å", "Ä", "Ö"]  # Swedish letters

ROCKY = "Rocky (Easy)"
RANDOM = "Random (Medium)"
REINHARD = "ReinHard (Hard)"
OPPONENTS = [ROCKY, RANDOM, REINHARD]

DRAW = 2
WIN = 1
LOSS = 0

RESULT = ["LOSS", "WIN", "DRAW"]


class Game:
    # Game rules
    ROCK = "Rock"
    PAPER = "Paper"
    SCISSOR = "Scissors"
    OPTIONS = [ROCK, PAPER, SCISSOR]

    def __init__(self):
        self.results = [0, 0, 0]
        self.opponent = None

    def set_opponent(self, opponent):
        self.opponent = opponent

    def get_opponent(self):
        return self.opponent

    def play(self, played):
        opponents_selection = self.opponent_turn(played)
        result = self.game_rule(played, opponents_selection)
        self.results[result] += 1

        return f"You have played {played} and you opponent {self.opponent} played {opponents_selection}. Its a {RESULT[result]}"

    def opponent_turn(self, played):
        if self.get_opponent() == ROCKY:
            return self.ROCK
            print("Your opponent has played: ", self.ROCK)
        if self.get_opponent() == RANDOM:
            select = random.uniform(0, 3)
            option = self.OPTIONS[math.floor(select)]
            return option
        if self.get_opponent() == REINHARD:
            select = random.uniform(0, 3)
            option = self.OPTIONS[math.floor(select)]
            cheat = self.game_rule(played, option)
            if cheat == WIN:
                # Reinhard cheats
                select = random.uniform(0, 3)
                option = self.OPTIONS[math.floor(select)]
            return option

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
            selection == self.ROCK
            and opponent_selection == self.SCISSOR
            or selection == self.PAPER
            and opponent_selection == self.ROCK
            or selection == self.SCISSOR
            and opponent_selection == self.PAPER
        ):
            return WIN
        return LOSS


# Main window for game
class RockPaperScissorGame(tk.Tk):
    HEIGHT = 400
    WIDTH = 400
    WINDOW_SIZE = str(HEIGHT) + "x" + str(WIDTH)
    TITLE = "Sten sax påse"

    def __init__(self, *args, **kwargs):
        """
        Init the main window to the game
        Main window starts at the MainMenu
        """
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry(self.WINDOW_SIZE)
        self.title(self.TITLE)

        self.game = Game()
        self._frame = None
        self.switch_frame(MainMenu)

    def switch_frame(self, frame_class):
        """
        Destroys the current frame and all of its children.
        Sets the current frame to the one supplied
        """
        new_frame = frame_class(self)
        self._destroy_current_frame()
        self._set_new_frame(new_frame)

    def _destroy_current_frame(self):
        """
        Destroy current frame and all of its children.
        """
        if self._frame is None:
            return
        for widget in self._frame.winfo_children():
            widget.destroy()
        self._frame.destroy()

    def _set_new_frame(self, new_frame):
        """
        Sets the current frame
        """
        self._frame = new_frame
        new_frame.pack()

    def switch_opponent(self, opponent):
        """
        Switch the current opponent a new one
        """
        self.game.set_opponent(opponent)


class MainMenu(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="Main menu").pack(
            side="top", fill="x", pady=10
        )
        self._parent = parent

        self.opponent_selection = tk.StringVar(value=OPPONENTS[0])
        self.setup_opponent_drop_down_menu()

        self.start_game = tk.Button(
            self,
            command=lambda: self.play_game(),
            text="Play",
        ).pack(side="top", fill="x", pady=10)
        self.quit = tk.Button(self, text="Exit", command=lambda: parent.quit()).pack(
            side="top", fill="x", pady=10
        )

    def setup_opponent_drop_down_menu(self):
        """
        Setup the opponent drop down menu
        """
        opponent_selection_label = tk.Label(self, text="Select an opponent")
        opponent_selection_label.pack(pady=10)
        opponent_selection_menu = tk.OptionMenu(
            self, self.opponent_selection, *OPPONENTS
        )
        opponent_selection_menu.pack(pady=10)

    def play_game(self):
        """
        Set the current opponent and start the game
        """
        self._parent.game.set_opponent(self.opponent_selection.get())
        self._parent.switch_frame(GameFrame)


class GameFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="Game").pack(side="top", fill="x", pady=10)
        self.parent = parent
        game = parent.game

        action_selection = tk.Frame(self)
        action_selection.pack(side="top")

        self.rock_button = tk.Button(
            self, text=game.ROCK, command=lambda: self.play(game.ROCK)
        ).pack(in_=action_selection, side="left", pady=10)
        self.paper_button = tk.Button(
            self,
            text=game.PAPER,
            command=lambda: self.play(game.PAPER),
            # ).pack(side="top", fill="x", pady=10)
        ).pack(in_=action_selection, side="left", pady=10)
        self.scissor_button = tk.Button(
            self,
            text=game.SCISSOR,
            command=lambda: self.play(game.SCISSOR),
        ).pack(in_=action_selection, side="left", pady=10)

        info = tk.Frame(self)
        info.pack(side="top")
        self.info_text = tk.StringVar()
        self.info_text.set("Play either, 'Rock', 'Paper' or 'Scissor'")

        self.label = tk.Label(self, textvariable=self.info_text).pack(
            in_=info, fill="x", pady=10
        )

        extra = tk.Frame(self)
        extra.pack(side="bottom")

        self.statistics_button = tk.Button(
            self, text="Show statistics", command=lambda: self.display_result()
        ).pack(in_=extra, fill="x", pady=10)

        # TODO: Always plays last entry on self.play(option)
        # for option in OPTIONS:
        # tk.Button( self, text=option, command=lambda: self.play(option), ).pack(side="top", fill="x", pady=10)

        self.goto_main_menu = tk.button = tk.Button(
            self, text="Give up", command=lambda: parent.switch_frame(MainMenu)
        ).pack(in_=extra, fill="x", pady=10)

    def play(self, played):
        result = self.parent.game.play(played)
        self.info_text.set(result)

    def display_result(self):
        results = self.parent.game.results
        result_string = f"{results[WIN]}/{results[LOSS]}/{results[DRAW]}"
        self.info_text.set(result_string)


if __name__ == "__main__":
    game = RockPaperScissorGame()
    game.mainloop()
