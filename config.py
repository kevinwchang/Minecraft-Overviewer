import os
import markerfilters
from optimizeimages import optipng

worlds['world'] = 'world'

outputdir = 'output/map'
base = 'http://tiles.iprefermuffins.com:8080/map/'

imgformat = 'jpg'
imgquality = 50
processes = 7

end_ambient_smooth_lighting = [Base(), EdgeLines(), SmoothLighting(strength=0.8)]
nether_ambient_smooth_lighting = [Base(), EdgeLines(), Nether(), SmoothLighting(strength=0.8)]

filters = [
  dict(name = 'Labels',     filterFunction = markerfilters.label_sign_filter, checked = True),
  dict(name = 'Signs',      filterFunction = markerfilters.normal_sign_filter),
  dict(name = 'Players',    filterFunction = markerfilters.player_filter),
  dict(name = 'Named mobs', filterFunction = markerfilters.named_mob_filter)]

texturepath='~/.minecraft/versions/' + os.getenv('VERSION') + '/' + os.getenv('VERSION') + '.jar'

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

renders['biomeover'] = {
  'world': 'world',
  'title': 'Biomes',
  'rendermode': [ClearBase(), BiomeOverlay()],
  'dimension': 'overworld',
  'northdirection': 'upper-right',
  'overlay': ['day', 'night'],
  'imgformat': 'png',
  'optimizeimg': [optipng()]
}

renders['end'] = {
  'world': 'world',
  'title': 'End',
  'rendermode': end_ambient_smooth_lighting,
  'dimension': 'end',
  'northdirection': 'upper-right',
  'markers': filters,
  'poititle': 'Markers'
}

renders['nether'] = {
  'world': 'world',
  'title': 'Nether',
  'rendermode': nether_ambient_smooth_lighting,
  'dimension': 'nether',
  'northdirection': 'upper-right',
  'markers': filters,
  'poititle': 'Markers'
}
