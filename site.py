import os.path
import cherrypy
from jinja2 import Environment, FileSystemLoader
import db_tools

env = Environment(loader=FileSystemLoader('templates'))

class ScoreAlarm:

	@cherrypy.expose
	def index(self):
		template = env.get_template('index.html')
		content = 'Score Alarm application server'
		return template.render({'content': content})

	@cherrypy.expose
	def add_game(self, host=None, guest=None, start_time=None):
		if cherrypy.request.method.upper() == 'POST':
			db_tools.add_game({host, guest, start_time})
		template = env.get_template('add_game.html')
		content = ""
		return template.render({'content': content})

	@cherrypy.expose
	def edit_game(self, pk):
		template = env.get_template('edit_game.html')
		content = 'Input data here:'
		return template.render({'content': content})

	@cherrypy.expose
	def delete_game(self, pk):
		template = env.get_template('delete_game.html')
		content = 'Input data here:'
		return template.render({'content': content})

sa_config = os.path.join(os.path.dirname(__file__), 'score_alarm.conf')

if __name__ == '__main__':
	cherrypy.quickstart(ScoreAlarm(), config=sa_config)
