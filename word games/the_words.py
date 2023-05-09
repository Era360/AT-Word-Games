import random

en_words = [
    "banana",
    "camera",
    "dinner",
    "elephant",
    "father",
    "garden",
    "hockey",
    "jungle",
    "kitten",
    "laptop",
    "mother",
    "orange",
    "puzzle",
    "rocket",
    "school",
    "turtle",
    "umbrella",
    "violin",
    "window",
    "yellow",
    "animal",
    "butter",
    "candle",
    "donkey",
    "eskimo",
    "fossil",
    "guitar",
    "hamster",
    "island",
    "jacket",
    "kangaroo",
    "lizard"
    "muffin",
    "noodle",
    "octopus",
    "penguin",
    "quality",
    "rainbow",
    "sunshine",
    "trumpet",
    "vampire",
    "waffle",
    "xylophone",
    "yoghurt",
    "acquire",
    "balloon",
    "cabbage",
    "diamond"
]


def select_items(num_items):
    """
    Selects a specified number of items randomly from a list of items.

    Args:
    num_items (int): The number of items to select.
    items_list (list): The list of items to choose from.

    Returns:
    A list of randomly selected items.
    """
    if num_items > len(en_words):
        raise ValueError(
            "The number of items to select is greater than the number of items in the list.")
    return random.sample(en_words, num_items)

# def get_words(no):
#     for i in en_words:

#     return en_words
