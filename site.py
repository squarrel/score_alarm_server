# -*- coding: utf-8 -*-

import os.path
import cherrypy
from jinja2 import Environment, FileSystemLoader
import db_tools

env = Environment(loader=FileSystemLoader('templates'))

class ScoreAlarm:

	@cherrypy.expose
	def index(self):
		template = env.get_template('index.html')
		games = db_tools.all_games()
		players = db_tools.all_players()
		teams = db_tools.all_teams()
		args = {
			'games': games,
			'players': players,
			'teams': teams}
		return template.render(args)

	@cherrypy.expose
	def game(self, pk):
		template = env.get_template('game.html')
		game = db_tools.get_game(pk)
		host = db_tools.get_team(game[5])[1]
		guest = db_tools.get_team(game[6])[1]
		args = {'game': game, 'host': host, 'guest': guest}
		return template.render(args)

	@cherrypy.expose
	def team(self, pk):
		template = env.get_template('team.html')
		team = db_tools.get_team(pk)
		args = {'team': team}
		return template.render(args)

	@cherrypy.expose
	def player(self, pk):
		template = env.get_template('player.html')
		player = db_tools.get_player(pk)
		print('player', player)
		args = {'player': player}
		return template.render(args)

	@cherrypy.expose
	def add_game(self):
		template = env.get_template('add_game.html')
		teams = db_tools.all_teams()
		return template.render({'teams': teams})

	@cherrypy.expose
	def add_game_post(self, host=None, guest=None, start_time=None):
		data = {
			'host': host,
			'guest': guest,
			'start_time': start_time}
		print('data', data)
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
	def add_player(self):
		template = env.get_template('add_player.html')
		return template.render()

	@cherrypy.expose
	def add_player_post(self, first_name=None, last_name=None):
		data = {
			'first_name': first_name,
			'last_name': last_name}
		db_tools.add_player(data)
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
