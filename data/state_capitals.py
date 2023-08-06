from random import randint

capdict = {
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne"
}


class StateCapitals:
    @property
    def states(self) -> list[str]:
        return list(self._dict.keys())

    @property
    def capitals(self) -> list[str]:
        return list(self._dict.values())

    def __init__(self, capdict=capdict):
        self._dict = capdict
        self.states_left = self.states

    @property
    def nstates_left(self) -> int:
        return len(self.states_left)

    def pop_idx(self, idx: int) -> str:
        return self.states_left.pop(idx)

    def pop_state(self, state: str) -> str:
        return self.pop_idx(self.states_left.index(state))

    def get_rand_idx(self) -> int:
        return randint(0, self.nstates_left - 1)

    def pop_rand(self):
        return self.pop_idx(self.get_rand_idx())

    def mk_sentence(self, state: str):
        cap = self._dict[state]
        return f"The capital of {state} is {cap}."


def main(
        caps: StateCapitals = StateCapitals(),
        get_options: str = "<state_name>/random/show remaining",
        state: str = None
) -> None:
    print("Which state capital would you like to know??\n")

    while caps.nstates_left > 0:
        pick = input(f"{get_options}\n")
        if pick in ["show remaining", "show", "s"]:
            print(caps.states_left)
        elif pick in ["r", "rand", "random"]:
            state = caps.pop_rand()
        elif pick in caps.states_left:
            state = caps.pop_state(pick)
        elif pick in caps.states:
            print(f"{pick} has already been shown.")
        else:
            raise ValueError("input not recognized")

        if state is not None:
            print(f"{caps.mk_sentence(state)}\n")
            state = None

        choice = input("Wanna know another?? (y/n)\n")
        if caps.nstates_left == 0:
            print("That's all of them!")
        elif choice.lower() in ["y", "yes"]:
            continue
        elif choice.lower() in ["n", "no"]:
            print("\nIt was nice while it lasted.\n")
            break


if __name__ == "__main__":
    main()
