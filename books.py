import sys
import argparse
import os

# add optional arguments here
parser = argparse.ArgumentParser(description="Display list of books from different files")
parser.add_argument('--filter', help="show a subset of books, looks for the argument as a substring of any of the fields")
parser.add_argument('--year', action='store_true', help="sort the books by year, ascending instead of default sort")
parser.add_argument('--reverse', action='store_true',help="reverse sort")
args = parser.parse_args()

# empty array that will hold book dictionary objects
book_obj = []
# array of file types and their respective delimiter
file_types=[
        ('csv', ', '),
        ('pipe', ' | '),
        ('slash', '/')
        ]

# order of how each file orders their title, lastname, first name, year
file_order={
    'csv':[0,1,2,3],
    'pipe':[2,1,0,3],
    'slash':[3,2,1,0]
}

# parse each file and assign them to a dictionary object
# loop through each file type and add each book to the book_obj array
def parsefiles():
    for ftype in file_types:
        orderarr = file_order[ftype[0]]
        with open(ftype[0]) as bookfile:
            for b in bookfile:
                arr = b.rstrip('\n').split(ftype[1])
                book_obj.append({
                    'title':arr[orderarr[0]],
                    'last':arr[orderarr[1]],
                    'first':arr[orderarr[2]],
                    'pub_date':arr[orderarr[3]]
                })


# take populated book_obj and filter/reverse here
def filter_and_reverse():
    global book_obj
    order = 'last'
    if args.year:
        order = 'pub_date'
    if args.filter:
        book_obj = list(filter(contains_filter_string, book_obj))

    # sort book_obj array here
    book_obj.sort(key=lambda x: x[order], reverse=args.reverse)


# look through dictionary values and check if values contain filter argument
def contains_filter_string(obj):
    for key, value in obj.items():
        if args.filter in value:
            return True

    return False

def main():
    # first parse files and populate book_obj with dictionary objects of each books
    # filter and reverse book_obj list based on optional arguments
    parsefiles()
    filter_and_reverse()
    for b in book_obj:
        print('{}, {}, {}, {}'.format(b['last'], b['first'], b['title'], b['pub_date']))
        # print(b['last'], b['first'], b['title'], b['pub_date'])

if __name__ == "__main__":
    main()

# argument parser
# read and parse files
# filter via any optional arguments
# print
