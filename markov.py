"""Generate Markov text from text files."""

from random import choice

from sys import argv


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    filename = open(argv[1]).read()
    opened_file = open(file_path).read()

    combined = filename + opened_file

    #print (combined)
    return combined


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    lst = text_string.split()

    for i in range(len(lst)-2):
    	if (lst[i],lst[i+1]) in chains:
    		chains[(lst[i],lst[i+1])].append(lst[i+2])
    	else:
    		chains[(lst[i],lst[i+1])] = [lst[i+2]]

    #print (chains)
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    current_key = choice(list(chains))
    words.extend([current_key[0],current_key[1]])
    while current_key in chains:
    	chosen_word = choice(chains[current_key])
    	words.append(chosen_word)
    	current_key = (current_key[1],chosen_word)

    print (" ".join(words))

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
combined = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(combined)

# Produce random text
random_text = make_text(chains)

#print random_text
