import os.path
import cherrypy


class ScoreAlarm:

	@cherrypy.expose
	def index(self):
		return 'Score Alarm application server'

sa_config = os.path.join(os.path.dirname(__file__), 'score_alarm.conf')

if __name__ == '__main__':
	cherrypy.quickstart(ScoreAlarm(), config=sa_config)
