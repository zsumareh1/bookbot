import sys
from stats import get_num_words, count_charachter, report

#book_path ="/home/zakaria/bookbot/books/frankenstein.txt"

if len(sys.argv) >= 2:
    book_path = sys.argv[1]
    contents = get_num_words(book_path)

    print(f"Found {contents} total words") 

    results = count_charachter(book_path)
    #print(results)

    rep = report(results)

    for item in rep:
        print(f"{item["char"]}: {item["num"]}")
else:
    print("Usage python3 main.py <path_to_book>")
    sys.exit(1)