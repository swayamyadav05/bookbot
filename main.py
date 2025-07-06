from stats import count_words, count_chars, sorted_dict


def get_book_text(path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        file_content = f.read()

    return file_content


import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    file_path = sys.argv[1]
    print(f"Analyzing book found at {file_path}...")
    contents = get_book_text(file_path)
    print("----------- Word Count ----------")
    words = count_words(contents)
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    chars = count_chars(contents)
    list_of_chars_count = sorted_dict(chars)
    for item in list_of_chars_count:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()
