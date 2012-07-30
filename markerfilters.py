import re

# helpers

def fulltext(poi):
	return '\n'.join([poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']])

label_re = re.compile('^\s*#')

def islabelsign(poi):
	return label_re.search(fulltext(poi)) is not None

# filters

def labelsign(poi):
	if poi['id'] == 'Sign' and islabelsign(poi):
		return fulltext(poi)

def normalsign(poi):
	if poi['id'] == 'Sign' and not islabelsign(poi) and not fulltext(poi).strip() == '':
		return fulltext(poi)

def playericons(poi):
	if poi['id'] == 'Player':
		poi['icon'] = "http://overviewer.org/avatar/%s" % poi['EntityId']
		return "Last known location for %s" % poi['EntityId']
