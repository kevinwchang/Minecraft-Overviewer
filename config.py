import markerfilters

worlds['world'] = 'world'

outputdir = '/var/www/minecraft/map'

filters = [markerfilters.labelsign, markerfilters.normalsign]

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
