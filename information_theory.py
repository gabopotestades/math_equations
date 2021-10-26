def shannon_entropy(str):

    import math

    shannon = 0
    string_length = len(str)
    characters_dict = {}
    probabilities_dict = {}

    for char in str:
        if char not in characters_dict.keys():
            characters_dict[char] = 1
        else:
            characters_dict[char] = characters_dict[char] + 1

    for key in characters_dict.keys():
        probabilities_dict[key] = characters_dict[key] / string_length

    for key in probabilities_dict.keys():
        shannon += probabilities_dict[key] * math.log2(probabilities_dict[key])

    return shannon if shannon == 0 else (shannon * -1)
