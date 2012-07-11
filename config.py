import markerfilters

worlds['world'] = 'world'

outputdir = '/var/www/minecraft/map'
base = 'http://tiles.iprefermuffins.com:8042/minecraft/map/'

filters = [
	dict(name = 'Labels',  filterFunction = markerfilters.labelsign),
	dict(name = 'Signs',   filterFunction = markerfilters.normalsign),
	dict(name = 'Players', filterFunction = markerfilters.playericons)]

renders['day'] = {
	'world': 'world',
	'title': 'Day',
	'rendermode': 'smooth_lighting',
	'dimension': 'overworld',
	'northdirection': 'upper-right',
	'markers': filters
}

renders['night'] = {
	'world': 'world',
	'title': 'Night',
	'rendermode': 'smooth_night',
	'dimension': 'overworld',
	'northdirection': 'upper-right',
	'markers': filters
}

imgformat = 'jpg'
imgquality = 50
processes = 3
