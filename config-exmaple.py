import markerfilters

worlds['world'] = 'Minecraft-Overviewer-Addons/exmaple'

outputdir = '/var/www/minecraft/exmaple'

filters = [
	dict(name = 'Labels',  filterFunction = markerfilters.labelsign),
	dict(name = 'Signs',   filterFunction = markerfilters.normalsign),
	dict(name = 'Players', filterFunction = markerfilters.playericons)]

renders['UL'] = {
	'world': 'world',
	'title': 'Upper Left',
	'rendermode': 'normal',
	'dimension': 'overworld',
	'northdirection': 'upper-left',
	'markers': filters,
	'poititle': 'Markers'
}
renders['UR'] = {
	'world': 'world',
	'title': 'Upper Right',
	'rendermode': 'normal',
	'dimension': 'overworld',
	'northdirection': 'upper-right',
	'markers': filters,
	'poititle': 'Markers'
}
renders['LL'] = {
	'world': 'world',
	'title': 'Lower Left',
	'rendermode': 'normal',
	'dimension': 'overworld',
	'northdirection': 'lower-left',
	'markers': filters,
	'poititle': 'Markers'
}
renders['LR'] = {
	'world': 'world',
	'title': 'Lower Right',
	'rendermode': 'normal',
	'dimension': 'overworld',
	'northdirection': 'lower-right',
	'markers': filters,
	'poititle': 'Markers'
}

imgformat = 'jpg'
imgquality = 50
processes = 3
