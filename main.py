"""


Dict values should be summarized in case of identical keys.

Example:
dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

combine_dicts(dict_1, dict_2)
Result: {'a': 300, 'b': 200, 'c': 300}

combine_dicts(dict_1, dict_2, dict_3)
Result: {'a': 600, 'b': 200, 'c': 300, 'd': 100}
"""


def combine_dicts(*args: dict) -> dict:
    """
    function receives a changeable number of dictionaries (keys - letters, values - integers)
    and combines them into one dictionary.

    """
    result = {}
    for dictionary in args:  # iterate through tuple elements
        for key in dictionary:  # iterate through keys in dictionaries
            if not (key.isalpha() and len(key) == 1 and key.islower()):
                raise KeyError
            if not isinstance(dictionary[key], int):
                raise ValueError
            if key in result:
                result[key] += dictionary[key]
            else:
                result.update({key: dictionary[key]})
    return result


if __name__ == '__main__':
    pass
