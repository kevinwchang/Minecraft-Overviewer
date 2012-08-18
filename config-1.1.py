import markerfilters

worlds['world'] = '../world-1.1'

outputdir = '/var/www/minecraft/map-1.1'
base = 'http://tiles.iprefermuffins.com:8042/minecraft/map-1.1/'

filters = [
	dict(name = 'Labels',  filterFunction = markerfilters.labelsign, checked = True),
	dict(name = 'Signs',   filterFunction = markerfilters.normalsign),
	dict(name = 'Players', filterFunction = markerfilters.playericons)]

renders['day'] = {
	'world': 'world',
	'title': 'Day',
	'rendermode': 'smooth_lighting',
	'dimension': 'overworld',
	'northdirection': 'upper-right',
	'markers': filters,
	'poititle': 'Markers'
}

renders['night'] = {
	'world': 'world',
	'title': 'Night',
	'rendermode': 'smooth_night',
	'dimension': 'overworld',
	'northdirection': 'upper-right',
	'markers': filters,
	'poititle': 'Markers'
}

imgformat = 'jpg'
imgquality = 50
processes = 3
