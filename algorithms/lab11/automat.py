class FSM:
    def __init__(self, alphabet, states, startState, finiteState, transitions):
        self.alphabet = alphabet
        self.states = states
        self.startState = startState
        self.finiteState = finiteState
        self.transitions = transitions
        self.currentState = None
        self.states = []
        self.answer = []

    def __check_is_in_alphabet(self, symbol):
        return True if (symbol in self.alphabet) else False

    def __change_state(self, symbol):
        if self.transitions[self.currentState] and self.transitions[self.currentState][symbol]:
            self.currentState = self.transitions[self.currentState][symbol]
        else:
            raise Exception("Нет переходов(((" % (self.currentState, symbol))

    def find(self, value):
        self.currentState = self.startState
        for symbol in value:
            if self.__check_is_in_alphabet(symbol):
                self.__change_state(symbol)
                self.states.append(self.currentState)
            else:
                self.currentState = self.startState
                self.states.append(self.currentState)

            if self.currentState in self.finiteState:
                print(self.states)
                self.answer.append(len(self.states) - 3)
        return self.answer


if __name__ == '__main__':
    alphabet = "abc"
    states = ["0", "1", "2", "3"]
    startState = "0"
    finiteState = ["3"]
    transitions = {
        "0": {"a": "1", "b": "0", "c": "0"},
        "1": {"a": "0", "b": "2", "c": "0"},
        "2": {"a": "0", "b": "0", "c": "3"},
        "3": {"a": "0", "b": "0", "c": "0"},
    }
    with open("input.txt", "r") as f:
        string = f.readline()
        fsm = FSM(alphabet, states, startState, finiteState, transitions)

    print(string)
    ans = fsm.find(string.lower())
    print(ans)
