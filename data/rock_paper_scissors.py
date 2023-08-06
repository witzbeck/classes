from dataclasses import dataclass, field
from random import choice


@dataclass
class Score:
    user_score: int = 0
    comp_score: int = 0
    win_score: int = 3

    def add_point(
            self,
            user: bool = False,
            comp: bool = False,
    ):
        if user:
            self.user_score += 1
        elif comp:
            self.comp_score += 1
        else:
            raise ValueError

    def __repr__(self):
        u = self.user_score
        c = self.comp_score
        return f"Score = User: {u} | Computer: {c}"

    @property
    def istied(self):
        self.comp_score == self.user_score

    @property
    def iscompwinning(self):
        self.comp_score > self.user_score

    @property
    def isuserwinning(self):
        self.comp_score < self.user_score

    @property
    def userwon(self):
        self.user_score == self.win_score

    @property
    def compwon(self):
        self.comp_score == self.win_score

    @staticmethod
    def eval_hand(comp_hand: str, user_hand: str):
        tie = comp_hand == user_hand
        c, u = comp_hand, user_hand
        cr, cp, cs = c == "r", c == "p", c == "s"
        ur, up, us = u == "r", u == "p", u == "s"
        uwin = ((cr and us) or (cp and ur) or (cs and up))

        if (cr and ur):
            print("Both contestants chose rock!")
        elif (cp and up):
            print("Both contestants chose paper!")
        elif (cs and us):
            print("Both contestants chose scissors!")
        elif ((cs and up) or (cp and us)):
            print("Scissors beats paper!")
        elif ((cr and up) or (cp and ur)):
            print("Paper beats rock!")
        else:
            print("Rock beats scissors!")

        if tie:
            ret = "tie"
        elif uwin:
            ret = "user"
        else:
            ret = "comp"
        return ret

    def score_round(self, comp_hand: str, user_hand: str):
        c, u = comp_hand, user_hand
        val = Score.eval_hand(c, u)
        if val == "user":
            self.add_point(user=True)
        elif val == "comp":
            self.add_point(comp=True)
        return val


@dataclass
class Game:
    score: Score = field(default_factory=Score)
    msgs: dict[str] = field(default_factory=dict,
                            repr=False
                            )
    choices: list[str] = field(default_factory=list, repr=False)
    userquit: bool = False

    def __post_init__(self):
        self.msgs.update({
            "win": "Congratulations, you win!",
            "lose": "You lost, but it's just a game!",
            "tie": "",
            "update_lost": "Round lost!",
            "update_won": "Round won!"})
        self.choices = self.choices + ["r", "p", "s"]

    def printmsg(self, key: str):
        print("\n".join([
            self.msgs[key],
            str(self.score),
            ""
        ]))

    def get_input(self, *args):
        return input(*args)

    def play_again(self, msg: str = "Play again? (y/n)"):
        return self.get_input(msg)

    def user_hand(self, msg: str = "Show hand: (r/p/s/quit)"):
        res = self.get_input(msg)
        if res == "quit":
            self.userquit = True
            raise StopIteration
        elif res not in self.choices:
            print("Please give valid input.")
            res = self.user_hand()
        return res

    @staticmethod
    def get_comp_hand(choices: list[str]):
        return choice(choices)

    def round(self):
        if self.score.userwon:
            self.printmsg("win")
            raise StopIteration
        elif self.score.compwon:
            self.printmsg("lose")
            raise StopIteration
        c = Game.get_comp_hand(self.choices)
        u = self.user_hand()
        res = self.score.score_round(c, u)
        uround = res == "user"
        cround = res == "comp"
        if uround:
            self.printmsg("update_won")
        elif cround:
            self.printmsg("update_lost")
        else:
            self.printmsg("tie")

    @classmethod
    def play(cls):
        game = cls()
        while True:
            if (game.score.userwon or game.score.compwon):
                break
            try:
                game.round()
            except StopIteration:
                break
        if game.userquit:
            pass
        elif game.play_again() == "y":
            cls.play()


if __name__ == '__main__':
    Game.play()
