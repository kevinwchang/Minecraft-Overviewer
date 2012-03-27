import re

def fulltext(poi):
	return poi['Text1'] + poi['Text2'] + poi['Text3'] + poi['Text4']

label_re = re.compile('^\s*#')

def islabelsign(poi):
	return label_re.search(fulltext(poi)) is not None

def labelsign(poi):
	"Labels"
	return poi['id'] == 'Sign' and islabelsign(poi)

def normalsign(poi):
	"Signs"
	return poi['id'] == 'Sign' and not islabelsign(poi) and not fulltext(poi).strip() == ''

