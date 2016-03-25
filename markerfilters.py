import re
import time


### helpers ###

def full_text(poi):
  raw = '\n'.join([poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']])
  decoded = raw.replace(u'\uf700', '').replace(u'\uf701', '').decode('unicode-escape')
  return raw, decoded

LABEL_RE = re.compile('^\s*##\d')

def is_label_sign(text):
  return LABEL_RE.search(text) is not None

FAKE_PLAYER_RE = re.compile('(bot|cam)$', re.I)

def is_real_player(poi):
  return FAKE_PLAYER_RE.search(poi['EntityId']) is None

MOB_NAME_REPLACEMENTS = {'LavaSlime': 'Magma cube', 'MushroomCow': 'Mooshroom', 'Ozelot': 'Ocelot', 'PigZombie': 'Zombie pigman', 'SnowMan': 'Snow golem', 'VillagerGolem': 'Iron golem', 'WitherBoss': 'Wither'}

def mob_type(poi):
  if poi['id'] == 'EntityHorse':
    return ['Horse', 'Donkey', 'Mule', 'Zombie horse', 'Skeleton horse'][poi['Type']]
  elif poi['id'] == 'Guardian':
    return ['Guardian', 'Elder guardian'][poi['Elder']]
  elif poi['id'] == 'Skeleton':
    return ['Skeleton', 'Wither skeleton'][poi['SkeletonType']]
  elif poi['id'] == 'Ozelot':
    return 'Ocelot' if poi['CatType'] == 0 else 'Cat'
  elif poi['id'] == 'Zombie':
    return ['Zombie', 'Zombie villager'][poi['IsVillager'] if 'IsVillager' in poi.keys() else 0]
  elif poi['id'] in MOB_NAME_REPLACEMENTS.keys():
    return MOB_NAME_REPLACEMENTS[poi['id']]
  else:
    return re.sub('(?!^)([A-Z][a-z]+)', ' \g<1>', poi['id']).lower().capitalize() # expand camel case, then convert to sentence case
  

### filters ###

def label_sign_filter(poi):
  if poi['id'] == 'Sign':
    raw, decoded = full_text(poi)
    if is_label_sign(decoded):
      print 'Label: ' + decoded.replace('\n', ' ') + ' (raw: ' + repr(raw) + ')'
      return decoded

def normal_sign_filter(poi):
  if poi['id'] == 'Sign':
    raw, decoded = full_text(poi)
    if not is_label_sign(decoded) and not decoded.strip() == '':
      print 'Sign: ' + decoded.replace('\n', ' ') + ' (raw: ' + repr(raw) + ')'
      return decoded

def player_filter(poi):
  if poi['id'] == 'Player' and is_real_player(poi):
    print 'Player: ' + poi['EntityId']
    poi['icon'] = 'https://minotar.net/body/{0}/16'.format(poi['EntityId'])
    poi['image'] = 'https://minotar.net/body/{0}/64'.format(poi['EntityId'])
    return 'Last known location for {0}\n{1}'.format(poi['EntityId'], time.strftime('%A, %B %d, %Y\n%H:%M:%S %Z', poi['time']))

def named_mob_filter(poi):
  if 'CustomName' in poi.keys() and poi['CustomName'] is not None and 'Health' in poi.keys():
    mtype = mob_type(poi)
    text = '{0} ({1})'.format(poi['CustomName'], mtype) 
    print 'Custom name: ' + text
    poi['icon'] = 'icons/mobs/{0}.png'.format(mtype.replace(' ', '').lower())
    return text
