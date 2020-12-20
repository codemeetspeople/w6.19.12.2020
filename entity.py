from db import (
    get_connection_pool,
    ALL_STMT, ONE_STMT, INSERT_STMT
)
from psycopg2.extras import RealDictCursor
import psycopg2.extensions

class Entity:
    connection_pool = get_connection_pool()
    fields = []

    def __init__(self, _id=None):
        self._id = None
        self._changed = False

        if _id:
            self.__load(_id)

    @property
    def id(self):
        return self._id

    def __str__(self):
        return f'{self.__class__.table_name()}({self.id})'

    def __repr__(self):
        return f'{self.__class__.table_name()}({self.id})'

    def __load(self, _id):
        cursor = self.get_cursor()
        cursor.execute(
            ONE_STMT.format(tablename=self.table_name()),
            (_id,)
        )
        object_dict = cursor.fetchone()
        for field in self.fields:
            setattr(self, f'_{field}', object_dict[field])

    def __save(self):
        clean_fields = self.clean_fields()
        cursor = self.get_cursor()

        if not self.id:
            stmt = INSERT_STMT.format(
                tablename=self.table_name(),
                fields = ','.join(clean_fields),
                values = ('%s,'*len(clean_fields))[:-1]
            )
            attrs = [getattr(self, f) for f in clean_fields]
            cursor.execute(stmt, attrs)
            result = cursor.fetchone()
            self._id = result['id']
        else:
            pass

        self._changed = False

    def save(self):
        if not self._changed:
            return

        self.__save()

    @classmethod
    def clean_fields(cls):
        return [f for f in cls.fields if f != 'id']

    @classmethod
    def table_name(cls):
        return cls.__name__.lower()

    @classmethod
    def get_cursor(cls):
        connection = cls.connection_pool.getconn()
        connection.set_isolation_level(
            psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
        )
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

    @classmethod
    def get(cls, _id):
        cursor = cls.get_cursor()
        cursor.execute(
            ONE_STMT.format(tablename=cls.table_name()),
            (_id,)
        )
        return cls.__from_dict(cursor.fetchone())
