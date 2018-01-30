import markerfilters
from optimizeimages import optipng

worlds['world'] = 'Minecraft-Overviewer-Addons/exmaple'

outputdir = 'output/exmaple'

filters = []

renders['day'] = {
	'world': 'world',
	'title': 'Upper Right',
	'rendermode': 'normal',
	'dimension': 'overworld',
	'northdirection': 'upper-right',
	'markers': filters,
	'poititle': 'Markers'
}

renders['spawnover'] = {
  'world': 'world',
  'title': 'Spawn',
  'rendermode': [ClearBase(), SpawnOverlay()],
  'dimension': 'overworld',
  'northdirection': 'upper-right',
  'overlay': ['day'],
  'imgformat': 'png',
  'optimizeimg': [optipng()]
}

imgformat = 'jpg'
imgquality = 50
processes = 3
