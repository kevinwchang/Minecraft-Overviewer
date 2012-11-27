import markerfilters

worlds['world'] = 'world'

outputdir = '/var/www/minecraft/map'
base = 'http://tiles.iprefermuffins.com:8042/minecraft/map/'

imgformat = 'jpg'
imgquality = 50
processes = 3

end_rendermode = [Base(), EdgeLines(), SmoothLighting(strength=0.8)]

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

renders['end'] = {
	'world': 'world',
	'title': 'End',
	'rendermode': end_rendermode,
	'dimension': 'end',
	'northdirection': 'upper-right',
	'markers': filters,
	'poititle': 'Markers'
}