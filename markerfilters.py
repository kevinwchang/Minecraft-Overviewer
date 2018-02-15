import re
import time


### helpers ###

def full_text(poi):
  raw = '\n'.join([poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']])
  decoded = raw #.replace(u'\uf700', '').replace(u'\uf701', '').decode('unicode-escape')
  return raw, decoded

LABEL_RE = re.compile('^\s*##\d')

def is_label_sign(text):
  return LABEL_RE.search(text) is not None

FAKE_PLAYER_RE = re.compile('(bot|cam)$', re.I)

def is_real_player(poi):
  return FAKE_PLAYER_RE.search(poi['EntityId']) is None

MOB_NAME_REPLACEMENTS = {'evocation_illager': 'Evoker', 'vindication_illager': 'Vindicator', 'illusion_illager': 'Illusioner', 'snowman': 'Snow golem', 'villager_golem': 'Iron golem'}

def mob_type(poi):
  id = re.sub('^minecraft:', '', poi['id'])
  if id in MOB_NAME_REPLACEMENTS.keys():
    return MOB_NAME_REPLACEMENTS[id]
  else:
    return re.sub('_', ' ', id).lower().capitalize() # replace underscores, then convert to sentence case
  

### filters ###

def label_sign_filter(poi):
  if poi['id'] == 'minecraft:sign':
    raw, decoded = full_text(poi)
    if is_label_sign(decoded):
      print 'Label: ' + decoded.replace('\n', ' ') + ' (raw: ' + repr(raw) + ')'
      return decoded

def normal_sign_filter(poi):
  if poi['id'] == 'minecraft:sign':
    raw, decoded = full_text(poi)
    if not is_label_sign(decoded) and not decoded.strip() == '':
      print 'Sign: ' + decoded.replace('\n', ' ') + ' (raw: ' + repr(raw) + ')'
      return decoded

def player_filter(poi):
  if poi['id'] == 'Player' and is_real_player(poi):
    print 'Player: ' + poi['EntityId']
    poi['icon'] = 'https://mc-heads.net/player/{0}/16'.format(poi['uuid'])
    poi['image'] = 'https://mc-heads.net/body/{0}/64'.format(poi['uuid'])
    return 'Last known location for {0}\n{1}'.format(poi['EntityId'], time.strftime('%A, %B %d, %Y\n%H:%M:%S %Z', poi['time']))

def named_mob_filter(poi):
  if 'CustomName' in poi.keys() and poi['CustomName'] is not None and 'Health' in poi.keys():
    mtype = mob_type(poi)
    text = '{0} ({1})'.format(poi['CustomName'], mtype) 
    print 'Custom name: ' + text
    poi['icon'] = 'icons/mobs/{0}.png'.format(mtype.replace(' ', '').lower()) # remove spaces and lowercase
    return text
