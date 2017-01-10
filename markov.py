from random import choice
import sys


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and returns
    the file's contents as one string of text.
    """

    open_file = open(file_path)
    text_string = open_file.read()
    open_file.close()

    return text_string


def make_chains(text_string, input_n):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}
    words = text_string.split()
    for i in range(len(words) - (input_n - 1)):
        n_gram = tuple(words[i:i+input_n])
        try:
            if n_gram in chains:
                chains[n_gram].append(words[i+input_n])
            else:
                chains[n_gram] = [words[i+input_n]]

            # ??? chains.setdefault(bigram, default=[words[i+2]])
        except:
            pass

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""
    text_list = []

    rand_key_tuple = choice(chains.keys())
    text_list.extend(rand_key_tuple)

    while rand_key_tuple in chains:
        rand_value = choice(chains[rand_key_tuple])
        text_list.append(rand_value)

        # listify key, remove first value, add new value, retuplefy key
        rand_key_list = list(rand_key_tuple)
        del rand_key_list[0]
        rand_key_list.append(rand_value)
        rand_key_tuple = tuple(rand_key_list)

    text = " ".join(text_list)

    return text


input_path = sys.argv[1]
input_n = int(sys.argv[2])

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, input_n)

# Produce random text
random_text = make_text(chains)

print random_text
