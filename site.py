import os.path
import cherrypy
from jinja2 import Environment, FileSystemLoader
import db_tools

env = Environment(loader=FileSystemLoader('templates'))

class ScoreAlarm:

	@cherrypy.expose
	def index(self):
		template = env.get_template('index.html')
		return template.render()

	@cherrypy.expose
	def add_game(self):
		template = env.get_template('add_game.html')
		teams = ''
		return template.render({'teams': teams})

	@cherrypy.expose
	def add_game_post(self, host=None, guest=None, start_time=None):
		data = {
			'host': host,
			'guest': guest,
			'start_time': start_time}
		db_tools.add_game(data)
		raise cherrypy.HTTPRedirect('/')

	@cherrypy.expose
	def add_team(self):
		template = env.get_template('add_team.html')
		cities = ''
		countries = ''
		return template.render({
			'cities': cities,
			'countries': countries})

	@cherrypy.expose
	def add_team_post(self, title=None, city=None, country=None):
		data = {
			'title': title,
			'city': city,
			'country': country}
		db_tools.add_team(data)
		raise cherrypy.HTTPRedirect('/')

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
