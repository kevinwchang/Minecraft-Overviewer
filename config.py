def allSignsFilter(poi):
	"Signs"
	return poi['id'] == 'Sign'

worlds['world'] = 'world'

outputdir = '/var/www/minecraft/map'

renders['day'] = {
	'world': 'world',
	'title': 'Day',
	'rendermode': 'smooth_lighting',
	'dimension': 'overworld',
	'northdirection': 'upper-right',
	'markers': [allSignsFilter],
}

renders['night'] = {
	'world': 'world',
	'title': 'Night',
	'rendermode': 'smooth_night',
	'dimension': 'overworld',
	'northdirection': 'upper-right',
	'markers': [allSignsFilter],
}

imgformat = 'jpg'
imgquality = 50
processes = 3
