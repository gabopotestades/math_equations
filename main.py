from information_theory import shannon_entropy

if __name__ == "__main__":

    input_string = input("Enter a string: ")
    entropy = shannon_entropy(input_string)

    print(f'\nThe Shannon Entropy is: {entropy}')
