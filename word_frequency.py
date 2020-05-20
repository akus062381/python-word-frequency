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
    
    for character in text:
        if character not in punctuation:
            nopunc = nopunc + character
    lower_text = nopunc.lower()
    # print(lower_text)
    no_whitespace = lower_text.split()
    # print(no_whitespace)

    for word in no_whitespace:
        if word not in stop_words:
            found_words.append(word)
    # print(found_words)
    sort_words = sorted(found_words)
    # print(sort_words)
    duplicate_words = dict()

    for word in sort_words:
        if word in duplicate_words:
            duplicate_words[word] += 1
        else:
            duplicate_words[word] = 1
    duplicate_words = { key:value for key, value in duplicate_words.items() if value >= 1}

    for key, value in duplicate_words.items():
        print(key , ' | ', value, value * ("*"))

    
    

        

        

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
