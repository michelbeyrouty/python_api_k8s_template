import sqlite3

from typing import Any, Tuple


class BaseRepository:

    con: None
    cur = None

    def __init__(self):
        self.con = sqlite3.connect('template.db')
        self.cur = self.con.cursor()

    def fetch_one(self, query: str) -> Tuple[Any]:
        """
        Fetch one result from the datastore
        :param query: SQL statement to execute
        :return: tuple of the row
        """

        res = self.cur.execute(query)
        return res.fetchone()

    def insert(self, query: str) -> None:
        """
        Insert row in the database

        :param query: query to insert
        :return: None
        """

        self.cur.execute(query)
        self.con.commit()

    def delete(self, query: str) -> None:
        """
        Delete row from the database

        :param query: query to execute
        :return: None
        """

        self.cur.execute(query)
        self.con.commit()
