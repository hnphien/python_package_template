# Project: Main
# File Created: 2023-10-01
from src.bigdata_cole_framework import ColeAlgorithms


def run():
    # Find max value in a list
    algorithm = ColeAlgorithms()
    numbers = [1, 2, 3, 4, 5]
    max_value = algorithm.get_max_number(numbers)
    print(f"The maximum value in the list is: {max_value}")


if __name__ == "__main__":
    run()
