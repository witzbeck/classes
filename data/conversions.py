from dataclasses import dataclass, field
from random import randint


@dataclass
class Distance:
    miles: float = field(default=None)
    km: float = field(default=None)
    ratio: float = field(
        default=1.60934,
        repr=False,
        )

    @classmethod
    def from_km(cls, km: float):
        dist = cls(km=km)
        dist.miles = dist.km / dist.ratio
        return dist

    @classmethod
    def from_miles(cls, miles: float):
        dist = cls(miles=miles)
        dist.km = dist.miles * dist.ratio
        return dist


@dataclass
class Person:
    _height: float
    _weight: float
    roundto: int = field(
        default=1,
    )
    ratiofactor: float = field(
        default=351.5,
    )
    hunits: str = field(
        default="in",
    )
    wunits: str = field(
        default="lb",
    )

    @property
    def height(self) -> str:
        return self._height

    @height.setter
    def height(self, val: str) -> None:
        self._height = float(val)

    @property
    def weight(self) -> str:
        return self._weight

    @weight.setter
    def weight(self, val: str) -> None:
        self._weight = float(val)

    @property
    def bmi(self):
        val = (self.weight / self.height) * self.ratiofactor
        return str(round(val, self.roundto))

    @property
    def hrepr(self):
        h = round(self.height, self.roundto)
        return f"{str(h)}{self.hunits}"

    @property
    def wrepr(self):
        w = round(self.weight, self.roundto)
        return f"{str(w)}{self.wunits}"

    def __repr__(self):
        return f"For {self.hrepr} & {self.wrepr}, BMI = {self.bmi}"

    def __post_init__(self):
        self.weight = self._weight
        self.height = self._height


def getbmi(
        height: float = None,
        weight: float = None,
        round_digits: int = 1
) -> float:
    if height is None:
        height = input("\nHeight (in):")
    if weight is None:
        weight = input("\nWeight (lb):")
    print(Person(height, weight))


@dataclass
class Time:
    _seconds: int = field(repr=False)

    @staticmethod
    def get_mod(val: int | float, factor: int = 60):
        return val % factor

    @staticmethod
    def get_whole(val: int | float, factor: int = 60):
        return val // factor

    @property
    def seconds(self):
        return Time.get_mod(int(self._seconds))

    @property
    def whole_min(self):
        return Time.get_whole(int(self._seconds))

    @property
    def minutes(self):
        return Time.get_mod(self.whole_min)

    @property
    def hours(self):
        return Time.get_whole(self.whole_min)

    def __repr__(self):
        return " ".join([
            f"{self._seconds} seconds",
            "is equal to",
            f"{str(self.hours)} hours,",
            f"{str(self.minutes)} minutes,",
            f"& {str(self.seconds)} seconds.",
        ])

    @classmethod
    def from_seconds(cls, s: int):
        print(cls(s))

    @classmethod
    def from_rand_sec(cls, _min: int = 1000, _max: int = 1_000_000):
        cls.from_seconds(randint(_min, _max))


@dataclass
class Smores:
    crackers: int
    marshmallows: int
    chocolate: int
    crack_marsh_ratio: int = field(
        default=2,
        repr=False,
    )
    choc_marsh_ratio: int = field(
        default=3,
        repr=False,
    )

    @property
    def prop_crack(self):
        return self.crackers // self.crack_marsh_ratio

    @property
    def prop_choc(self):
        return self.chocolate // self.choc_marsh_ratio

    @property
    def nmax(self):
        return min(
            self.prop_choc,
            self.prop_crack,
            self.marshmallows
        )

    @classmethod
    def from_rand(cls, _min: int = 10, _max: int = 1000):
        return cls(
            randint(_min, _max),
            randint(_min, _max),
            randint(_min, _max),
        )


if __name__ == '__main__':
    s = Smores.from_rand()
    print(s, s.nmax)
