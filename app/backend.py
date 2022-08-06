import sqlite3


class Backend:
    """
    Provide functionality to manage registers.
    """

    def __init__(self, database_name: str) -> None:
        """
        Parameters
        ----------
        database_name : str
            Path where database will be stored.
        """
        self.database_name = database_name
        with sqlite3.connect(self.database_name) as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS book (
                id INTEGER PRIMARY KEY, 
                title TEXT,
                author TEXT, 
                year INTEGER default 0, 
                isbn TEXT 
            )"""
            )

    def insert(self, title: str, author: str, year: int, isbn: str) -> None:
        """
        Insert a new register.

        Parameters
        ----------
        title : str
            book title.

        author : str
            book author.

        year : int
            book year.

        isbn : str
            book isbn.
        """
        with sqlite3.connect(self.database_name) as connection:
            connection.execute(
                'INSERT INTO book VALUES(NULL,?,?,?,?)',
                (title, author, year, isbn),
            )

    def view(self) -> None:
        """
        Get all registers.

        Returns
        -------
        list
            All registers stored.
        """
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.execute('SELECT * FROM book')
            rows = cursor.fetchall()

        return rows

    def search(
        self, title: str = '', author: str = '', year: int = 0, isbn: str = ''
    ) -> None:
        """
        Search for a specific book.

        Parameters
        ----------
        title : str
            book title.

        author : str
            book author.

        year : str
            book year.

        isbn : str
            book isbn.

        Returns
        -------
        list
            All registers finded.
        """
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.execute(
                'SELECT * FROM book WHERE title like ? and author like ? and year like ? and isbn like ?',
                (title + '%', author + '%', year + '%', isbn + '%'),
            )
            rows = cursor.fetchall()

        return rows

    def delete(self, primary_key: int) -> None:
        """
        Delete a specific register.

        Parameters
        ----------
        primary_key : int
            Register id.
        """
        with sqlite3.connect(self.database_name) as connection:
            connection.execute('DELETE FROM book WHERE id = ?', (primary_key,))

    def update(
        self, primary_key: int, title: str, author: str, year: int, isbn: str
    ) -> None:
        """
        Update a specific register.

        Parameters
        ----------
        primary_key : int
            Register id.

        title : str
            new book title.

        author : str
            new book author.

        year : str
            new book year.

        isbn : str
            new book isbn.

        """
        with sqlite3.connect(self.database_name) as connection:
            connection.execute(
                'UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?',
                (title, author, year, isbn, primary_key),
            )
