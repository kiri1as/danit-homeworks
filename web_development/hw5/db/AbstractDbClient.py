from abc import ABC, abstractmethod


class AbstractDbClient(ABC):
    @abstractmethod
    def init_connection(self):
        pass

    @abstractmethod
    def close_connection(self):
        pass

    @abstractmethod
    def create_table(self, table_name: str, schema: dict):
        pass

    @abstractmethod
    def insert(self, table_name: str, data: dict):
        pass

    @abstractmethod
    def update(self, table_name: str, data: dict, condition: str):
        pass

    @abstractmethod
    def delete(self, table_name: str, condition: str):
        pass
