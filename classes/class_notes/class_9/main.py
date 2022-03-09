import argparse
import os
import sys
from authors_comp import author

if __name__ == '__main__':
    # Instantiate parser
    print(f"Python version: {'.'.join(str(v) for v in sys.version_info[:3])}")
    parser = argparse.ArgumentParser()
    # Add arguments
    parser.add_argument('--home_dir', help='The root directory for this project')
    parser.add_argument('--author_id',
                        help='The author that we are going to process',
                        type=int)
    # Get arguments
    args = parser.parse_args()
    home_dir = args.home_dir
    author_id = args.author_id

    # Instantiate author
    auth_1 = author(home_dir=home_dir, author_id=author_id)
    print(auth_1.get_books_urls(n_books=10))
    auth_1.get_books()


