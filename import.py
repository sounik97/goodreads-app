import csv
from db import db


def main():
    with open("./books.csv", "r") as books_csv:
        # read the csv file in csv_reader variable via csv.reader method
        csv_reader = csv.reader(books_csv)

        # jumps to second row as first row is the column name
        next(csv_reader)

        # truncate the table before re-executing

        db.execute('TRUNCATE TABLE books CASCADE')

        data = []

        # insert the data from csv to 'books' table on postgresql by bulk insert

        for isbn, title, author, year in csv_reader:
            title = title.replace("'", "''")
            author = author.replace("'", "''")
            data.append(f"('{isbn}', '{title}', '{author}', '{year}')")
            # print(data)

        db.execute(f'''
            INSERT INTO books(isbn, title, author, year)
            VALUES {', '.join(data)}
        ''')
        
        print('Data stored on Postgre!')
        db.commit()


if __name__ == "__main__":
    main()
    
