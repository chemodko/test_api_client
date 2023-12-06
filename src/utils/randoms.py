from random import choice, randint
from string import ascii_letters, digits
import random


def random_number(start: int = 100, end: int = 1000) -> int:
    return randint(start, end)


def random_string(start: int = 9, end: int = 15) -> str:
    return ''.join(choice(ascii_letters + digits) for _ in range(randint(start, end)))


def random_list_of_strings(start: int = 9, end: int = 15) -> list[str]:
    return [random_string() for _ in range(randint(1, 5))]


def random_bool() -> bool:
    return bool(random.getrandbits(1))


def random_float(start: float = 1.0, end: float = 100.0) -> float:
    return round(random.uniform(start, end), 2)


if __name__ == "__main__":
    print(random_string())
    print(random_string())
    print(bool(random.getrandbits(1)))
    print(random_float())

