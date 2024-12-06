import sqlite3
import logging

from AbstractDbClient import AbstractDbClient
from ..decorator.singletone import singleton


@singleton
class SQLiteClient(AbstractDbClient):
    def __init__(self, db_name=":memory:") -> None:
        self.db_name = db_name
        self._connection = None
        self.log = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(className)s %(message)s')

    def init_connection(self):
        self._connect()

    def close_connection(self):
        if self._connection:
            self._connection.close()
            self._connection = None

    def _connect(self):
        if not self._connection:
            self._connection = sqlite3.connect(self.db_name)
        self._connection.row_factory = sqlite3.Row
        return self._connection

    @property
    def cursor(self):
        return self._connect().cursor()

    def _execute(self, query: str, params=()):
        cursor = self.cursor
        cursor.execute(query, params)
        if 'INSERT' or 'UPDATE' or 'DELETE' in query:
            self._connection.commit()
        return cursor

    def fetch_all(self, query: str):
        cursor = self._execute(query)
        return cursor.fetchall()

    def fetch_one(self, query: str):
        cursor = self._execute(query)
        return cursor.fetchone()

    def create_table(self, table_name: str, schema: dict):
        columns = ', '.join(f'{col} {d_type}' for col, d_type in schema.items())
        query = f'CREATE TABLE {table_name} ({columns})'
        self._execute(query)

    def insert(self, table_name: str, data: dict):
        columns = ', '.join(data.keys())
        parameters = ', '.join("?" for i in data)
        query = f'INSERT INTO {table_name} ({columns}) VALUES ({parameters})'
        self._execute(query, tuple(data.values()))

    def update(self, table_name: str, data: dict, condition: str):
        update_params = ', '.join(f'{k} = ?' for k in data.keys())
        query = f'UPDATE {table_name} SET {update_params} WHERE {condition}'
        self._execute(query, tuple(data.values()))

    def delete(self, table_name: str, condition: str):
        query = f'DELETE FROM {table_name} WHERE {condition}'
        self._execute(query)
