import re
import time

# helpers

def fulltext(poi):
  raw = '\n'.join([poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']])
  decoded = raw.replace(u'\uf700', '').replace(u'\uf701', '').decode('unicode-escape')
  return raw, decoded

label_re = re.compile('^\s*##\d')

def islabelsign(text):
  return label_re.search(text) is not None

fakeplayer_re = re.compile('(bot|cam)$', re.I)

def isrealplayer(poi):
  return fakeplayer_re.search(poi['EntityId']) is None

# filters

def labelsign(poi):
  if poi['id'] == 'Sign':
    raw, decoded = fulltext(poi)
    if islabelsign(decoded):
      print 'Label: ' + decoded.replace('\n', ' ') + ' (raw: ' + repr(raw) + ')'
      return decoded

def normalsign(poi):
  if poi['id'] == 'Sign':
    raw, decoded = fulltext(poi)
    if not islabelsign(decoded) and not decoded.strip() == '':
      print 'Sign: ' + decoded.replace('\n', ' ') + ' (raw: ' + repr(raw) + ')'
      return decoded

def playericons(poi):
  if poi['id'] == 'Player' and isrealplayer(poi):
    print 'Player: ' + poi['EntityId']
    poi['icon'] = 'https://minotar.net/body/{0}/16'.format(poi['EntityId'])
    poi['image'] = 'https://minotar.net/body/{0}/64'.format(poi['EntityId'])
    return 'Last known location for {0}\n{1}'.format(poi['EntityId'], time.strftime('%A, %B %d, %Y\n%H:%M:%S %Z', poi['time']))
