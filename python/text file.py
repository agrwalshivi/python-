def get_unique_words(file_path):
    unique_words = set()
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                # Removing punctuation marks from words
                word = word.strip('.,!?;:()[]{}\'"')
                unique_words.add(word)
    return unique_words

def main():
    file_path = input("Enter the path of the text file: ")
    unique_words = get_unique_words(file_path)
    print("Unique words in the file:")
    for word in unique_words:
        print(word)

if __name__ == "__main__":
    main()
