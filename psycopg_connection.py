import psycopg2
import psycopg2.extras
import psycopg2.extensions

connection = psycopg2.connect(
    host='localhost', database='dbname', user='username', password='password'
)
connection.set_isolation_level(
    psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
)
cursor = connection.cursor(
    cursor_factory=psycopg2.extras.DictCursor
)

cursor.execute(
    'INSERT INTO item (category_id, title, price) VALUES (%s, %s, %s) RETURNING id',
    (1, 'Yotafone', 99.99)
)

cursor.execute('SELECT * FROM "item"')

items = cursor.fetchall()
