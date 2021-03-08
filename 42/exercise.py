# https://codechalleng.es/bites/42/
import random

MAX_GUESSES = 5
START, END = 1, 20


def get_random_number():
    """Get a random number between START and END, returns int"""
    return random.randint(START, END)


class Game:
    """Number guess class, make it callable to initiate game"""

    def __init__(self):
        """Init _guesses, _answer, _win to set(), get_random_number(), False"""
        self._guesses = set()
        self._answer = get_random_number()
        self._win = False
        self._start = START
        self._end = END

    def _raise_w_message(self, message):
        """This is a very simple helper that prints out the specific
        problem and then raise an error
        """
        print(message)
        raise ValueError

    def guess(self):
        """Ask user for input, convert to int, raise ValueError outputting
        the following errors when applicable:
        'Please enter a number'
        'Should be a number'
        'Number not in range'
        'Already guessed'
        If all good, return the int"""
        # get the user input
        input_msg = f"Guess a number between {self._start} and {self._end}: "
        user_input = input(input_msg)
        # test if input is empty
        if user_input == "" or user_input is None:
            self._raise_w_message("Please enter a number")
        # test if it's a number
        # this is tricky because the test will provide both str and int
        elif isinstance(user_input, str) and not user_input.isdigit():
            self._raise_w_message("Should be a number")
        # at this point we are reasonably sure that we are
        # dealing with a number, time to convert user_input
        user_guess = int(user_input)
        # test if it's in range
        if not (user_guess in range(self._start, self._end + 1)):
            self._raise_w_message("Number not in range")
        # and finally test if it's in the list of previous attempts
        elif user_guess in self._guesses:
            self._raise_w_message("Already guessed")
        # if we made it here input must be valid
        else:
            self._guesses.add(user_guess)
            return user_guess

    def _validate_guess(self, guess):
        """Verify if guess is correct, print the following when applicable:
        {guess} is correct!
        {guess} is too low
        {guess} is too high
        Return a boolean"""
        if guess == self._answer:
            print(f"{guess} is correct!")
            self._win = True
        else:
            _message = "low" if guess < self._answer else "high"
            print(f"{guess} is too {_message}")
            self._win = False
        return self._win

    def __call__(self):
        """Entry point / game loop, use a loop break/continue,
        see the tests for the exact win/lose messaging"""
        counter = 1
        while counter <= 5:
            try:
                this_guess = self.guess()
            except ValueError:
                continue
            if self._validate_guess(this_guess):
                print(f"It took you {counter} guesses")
                return True
            else:
                counter += 1
        # if we reached this point we maxed the attempts
        print(f"Guessed 5 times, answer was {self._answer}")


if __name__ == "__main__":
    game = Game()
    game()
