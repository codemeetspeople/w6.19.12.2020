import psycopg2
from psycopg2 import pool


ALL_STMT = 'select * from {tablename}'


connection_pool = None
def get_connection_pool():
    global connection_pool

    if not connection_pool:
        connection_pool = psycopg2.pool.SimpleConnectionPool(
            1, 20,
            user = "shop",
            password = "shop",
            host = "127.0.0.1",
            port = "5432",
            database = "shop"
        )

    return connection_pool
