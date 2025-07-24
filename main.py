from stats import count_words, count_char, char_report
import sys

def get_book_text(filepath: str):
    with open(f'{filepath}') as f:
        file_contents = f.read()
    
    return file_contents
    
def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    filepath = sys.argv[1]
    file_contents = get_book_text(filepath)

    char_report(file_contents)

    # print(f'{num_words} words found in the document')

try:
    main()
except Exception as e:
    print(f'Error encountered: {e}')