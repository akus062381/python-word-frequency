stop_words = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
"""Read in `file` and print out the frequency of words in that file."""

import string
punctuation = string.punctuation

def print_word_freq(file):
    file = open(file)
    text = file.read()
    found_words = []
    nopunc = ""
    
    for punc in text:
        if punc not in punctuation:
            nopunc = nopunc + punc
    lower_text = nopunc.lower()
    # print(lower_text)
    strings = lower_text.split(" ")
    # print(strings)

    for word in strings:
        if word not in stop_words:
            found_words.append(word)
    # print(found_words)
    sort_words = sorted(found_words)
    # print(sort_words)
    duplicate_words = dict()

    for dups in sort_words:
        if dups in duplicate_words:
            duplicate_words[dups] += 1
        else:
            duplicate_words[dups] = 1
    duplicate_words = { key:value for key, value in duplicate_words.items() if value > 1}

    for key, value in duplicate_words.items():
        print(key , ' | ', value)

    
    

        

        

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
