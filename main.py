import string

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        count(file_contents)
        countcharacters(file_contents)
        print("--- End report ---")

def count(file):
    words = file.split()
    print(len(words), " words found in the document\n")

def countcharacters(file):
    # Initialize a dictionary with each letter of the alphabet set to 0
    letter_counts = {letter: 0 for letter in string.ascii_lowercase}
    for char in file.lower():
        if char in letter_counts:  # Only count alphabetic characters
            letter_counts[char] += 1
    
    sorted_letter_counts = dict(sorted(letter_counts.items(), key=lambda item: item[1], reverse=True))

    for letter, count in sorted_letter_counts.items():
        print(f"The '{letter}' character was found {count} times")

main()
