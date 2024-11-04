# Гончаров Александр Сергеевич 474267

import csv
import random

DATASET_PATH = "books-en.csv"
OUT_PATH = "bibliography.txt"
data_list = ["ISBN", "Book-Title", "Book-Author", "Year-Of-Publication", "Publisher", "Downloads", "Price"]


# Задание 1

def count_title_length():
    with open(DATASET_PATH) as r_file:
        reader = csv.reader(r_file, delimiter=";")
        count = 0
        for row in reader:
            if len(list(row)[1]) > 30:
                count += 1
    print(f"Колличество книг, у которых название длиннее 30 символов: {count}")
        
if __name__ == '__main__':
    count_title_length()
    print()


# Задание 2

def search_book_by_author(author_name):

    books_found = []

    with open(DATASET_PATH) as r_file:
        reader = csv.reader(r_file, delimiter=";")
        next(reader)

        for row in reader:
            book_title = row[1]
            book_author = row[2]
            year_of_publication = (row[3])
            
            if book_author.lower() == author_name.lower() and 1991 <= int(year_of_publication) <= 1995:
                books_found.append(book_title)
    return books_found

if __name__ == '__main__':
    author_input = input("Enter author's name: ")
    books = search_book_by_author(author_input)

    if books:
        print(f"Книги автора '{author_input}' (1991-1995):")
        for book in books:
            print(f"- {book}")
    else:
        print(f"Книги автора '{author_input}' в диапазоне 1991-1995 не найдены.")
    print()


# Задание 3

def generate_bibliography(DATASET_PATH, OUT_PATH, num_entries=20):

    entries = []

    with open(DATASET_PATH) as r_file:
        reader = csv.reader(r_file, delimiter=';')
        next(reader)

        for row in reader:
            book_author = row[2]
            book_title = row[1]
            year_of_publication = row[3]
            entry = f"{book_author}. {book_title} - {year_of_publication}"
            entries.append(entry)
    
    selected_entries = random.sample(entries, min(num_entries, len(entries)))
    
    with open(OUT_PATH, mode='w', encoding='utf-8') as output_file:
        for i, entry in enumerate(selected_entries, start=1):
            output_file.write(f"{i}. {entry}\n")
    
    print(f"Библиографические ссылки успешно сохранены в {OUT_PATH}.")

if __name__ == '__main__':
    generate_bibliography(DATASET_PATH, OUT_PATH)
    print()


# Задание 4

def parsing():
    import xml.dom.minidom as minidom

    xml_file = open('currency.xml', 'r')
    xml_data = xml_file.read()

    dom = minidom.parseString(xml_data)
    dom.normalize()

    valutes = dom.getElementsByTagName('Valute')
    char_codes = []

    for valute in valutes:
        nominal = valute.getElementsByTagName('Nominal')[0].firstChild.data
        if nominal in {'10', '100'}:
            char_code = valute.getElementsByTagName('CharCode')[0].firstChild.data
            char_codes.append(char_code)
    
    print(char_codes)
    print()

if __name__ == "__main__":
    parsing()


# допзадание

def list_of_publishers():

    publishers = []

    with open(DATASET_PATH) as r_file:
        reader = csv.reader(r_file, delimiter=";")
        next(reader)
        for row in reader:
            publishers.append(row[4])

    print(set(publishers))


if __name__ == "__main__":
    list_of_publishers()
        
def top_20_books():

    topbooks = []

    with open(DATASET_PATH) as r_file:
        reader = csv.reader(r_file, delimiter=";")
        next(reader)
        for row in reader:
            book_title = row[1]
            downloads = row[5]
            topbooks.append((book_title, downloads))
            topbooks = sorted(topbooks, key=lambda x: int(x[1]), reverse = True)[:20]
    
    for i in topbooks:
        print(i[0])

if __name__ == "__main__":
    print('Top 20 books:')
    print()
    top_20_books()
