import random
from sort import constants


def get_random_list(size, limit=constants.MAX_VALUE):
    """
    Generates a list of random integers.
    """
    return [random.randint(0, limit) for _ in range(size)]
