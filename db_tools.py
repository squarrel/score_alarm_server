import cherrypy
import psycopg2
import psycopg2.extensions as pg_extensions

pg_extensions.register_type(pg_extensions.UNICODE)
pg_extensions.register_type(pg_extensions.UNICODEARRAY)

def connect():
	try:
		connection = psycopg2.connect(database='scorealarm', user='m', password='')
		return connection
	except Exception as e:
		cherrypy.log('Error connecting to the database', e)

def get_data(pk, table):
	with connect() as c:
		r = c.execute("SELECT * FROM %s WHERE id=%s", (table, pk,))
		return r.fetchone()

def edit_game(pk, data):
	with connect() as c:
		c.execute("UPDATE game SET (host, guest, host_score, guest_score) = (%s, %s, %s, %s) WHERE id=%s", (data['host'], data['guest'], data['host_score'], data['guest_score'],))

def delete(pk, table):
	with connect() as c:
		c.execute("DELETE FROM %s WHERE id=%s", (table, pk,))

def add_game(data):
	print('---', data)
	with connect() as connection:
		cursor = connection.cursor()
		cursor.execute("INSERT INTO game (host, guest, start_time) VALUES (%s, %s, %s)", (data['host'], data['guest'], data['start_time'],))
		connection.commit()
