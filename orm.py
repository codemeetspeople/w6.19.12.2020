from db import (
    get_connection_pool,
    ALL_STMT
)
from psycopg2.extras import RealDictCursor

class Entity:
    connection_pool = get_connection_pool()
    fields = []

    def __init__(self):
        self._id = None
        self._changed = False

    @property
    def id(self):
        return self._id

    def __str__(self):
        return f'{self.__class__.table_name()}({self.id})'

    def __repr__(self):
        return f'{self.__class__.table_name()}({self.id})'

    @classmethod
    def table_name(cls):
        return cls.__name__.lower()

    @classmethod
    def get_cursor(cls):
        connection = cls.connection_pool.getconn()
        return connection.cursor(cursor_factory=RealDictCursor)

    @classmethod
    def __from_dict(cls, dict):
        obj = cls()
        for field in cls.fields:
            setattr(obj, f'_{field}', dict[field])
        return obj

    @classmethod
    def all(cls):
        cursor = cls.get_cursor()
        cursor.execute(ALL_STMT.format(tablename=cls.table_name()))
        obj_list = []
        for obj in cursor.fetchall():
            obj_list.append(cls.__from_dict(obj))
        return obj_list


class Category(Entity):
    fields = ['id', 'title']

    def __init__(self, _id = None):
        super().__init__()
        self._title = None

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self.title = value


class Item(Entity):
    fields = ['id', 'title', 'price', 'category_id']

    def __init__(self, _id = None):
        super().__init__()
        self._title = None

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self.title = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self.price = value

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, value):
        self.category_id = value
