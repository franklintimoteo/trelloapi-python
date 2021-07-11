class Label:
  def __init__(self, id, name, color):
    self.id = id
    self.name = name
    self.color = color
    
  @classmethod
  def deserialize_json(cls, data):
    labeldata = data['label']
    label = {
      'id': labeldata['id'],
      'name': labeldata['name'],
      'color': labeldata['color']
    }
    
    return cls(**label)

class Board:
  def __init__(self, id, name, shortLink):
    self.id = id
    self.name = name
    self.shortLink = shortLink
  
  @classmethod
  def deserialize_json(cls, data):
    boarddata = data['board']
    board = {
      'id': boarddata['id'],
      'name': boarddata['name'],
      'shortLink': boarddata['shortLink']
    }
    
    return cls(**board)


class Card:
  def __init__(self, id, name, idShort, shortLink):
    self.id = id
    self.shortLink = shortLink
    self.name = name
    self.idShort = idShort
  
  @classmethod
  def deserialize_json(cls, data):
    carddata = data['card']
    
    card = {
      'id': carddata['id'],
      'shortLink': carddata['shortLink'],
      'name': carddata['name'],
      'idShort': carddata['idShort']
    }
    
    return cls(**card)
    

class MemberCreator:
  def __init__(self, id, trtype, username, text, activityBlocked, avatarHash, avatarUrl, fullName, initials,nonPublicAvailable,idMemberReferrer=None,  nonPublic={}):

    self.id = id
    self.type = trtype
    self.username = username
    self.text = text
    self.activityBlocked = activityBlocked
    self.avatarHash = avatarHash
    self.avatarUrl = avatarUrl
    self.fullName = fullName
    self.idMemberReferrer = idMemberReferrer
    self.initials = initials
    self.nonPublic = nonPublic # type: dict
    self.nonPublicAvailable = nonPublicAvailable
  
  @classmethod
  def deserialize_json(cls, data):
    mcdata = data['memberCreator']
    memberCreator = {
      'id': mcdata['id'],
      'type' : mcdata['type'],
      'username' : mcdata['username'],
      'text' : mcdata['text'],
      'activityBlocked' : mcdata['activityBlocked'],
      'avatarHash' : mcdata['avatarHash'],
      'fullName' : mcdata['fullName'],
      'idMemberReferrer' : mcdata['idMemberReferrer'],
      'initials' : mcdata['initials'],
      'nonPublic' : mcdata['nonPublic'],
      'nonPublicAvailable' : mcdata['nonPublicAvailable'] 
    }
    return cls(**memberCreator)

class Display:
  def __init__(self, translationKey, entities):
    self.translationKey = translationKey
    self.entities = entities # type: dict
  
  @classmethod
  def deserialize_json(cls, data):
    ddata = data['display']
    display = {
      'translationKey': ddata['translationKey'],
      'entities': ddata['entities']
    }
    return cls(**display)
  
    

class Action:
  def __init__(self, id, idMemberCreator, data, type, date, appCreator, limits, display, memberCreator):
    self.id = id
    self.idMemberCreator = idMemberCreator
    self.data = data # type: dict
    self.type = type
    self.date = date
    self.appCreator = appCreator
    self.limits = limits # type: dict
    self.display = display # type: Display
    self.memberCreator = memberCreator # type: MemberCreator
  
  @classmethod
  def deserialize_json(cls, data):
    actdata = data['action']

    action_data = actdata['data']
    action_payload = {
      'value': action_data.get('value', ''),
      'text': action_data.get('text', ''),
      'data': dict()
    }
    if action_data.get('card'):
      action_payload['data']['card'] = Card.deserialize_json(action_data)
    if action_data.get('board'):
      action_payload['data']['board'] = Board.deserialize_json(action_data)
    if action_data.get('label'):
      action_payload['data']['label'] =  Label.deserialize_json(action_data)
    
    if action_data.get('old'):
      action_payload['data']['old'] = action_data['old']
    if action_data.get('checklist'):
      action_payload['data']['checklist'] = action_data['checklist']
    if action_data.get('checkItem'):
      action_payload['data']['checkItem'] = action_data['checkItem']
    if action_data.get('listBefore'):
      action_payload['data']['listBefore'] = action_data['listBefore']
    if action_data.get('listAfter'):
      action_payload['data']['listAfter'] = action_data['listAfter']
    

    action = {
      'id': actdata['id'],
      'idMemberCreator': actdata['idMemberCreator'],
      'data': action_payload,
      'type': actdata['type'],
      'date': actdata['date'],
      'appCreator': actdata['appCreator'],
      'limits': actdata['limits'],
      'display': actdata['display'],
      'memberCreator': actdata['memberCreator'],
    }
    return cls(**action)


class Model:
  def __init__(self, id, name, desc, descData, closed, idOrganization, idEnterprise, pinned, url, shortUrl, prefs, labelNames):
    self.id = id
    self.name = name
    self.desc = desc
    self.descData = descData
    self.closed = closed
    self.idOrganization = idOrganization
    self.idEnterprise = idEnterprise
    self.pinned = pinned
    self.url = url
    self.shortUrl = shortUrl
    self.prefs = prefs
    self.labelNames = labelNames

  def __repr__(self):
    return "<Model id:%s name:'%s' url:'%s'>" %(self.id, self.name, self.shortUrl.split('/')[-1])
    
  @classmethod
  def deserialize_json(cls, data):
    mdata = data['model']

    model = {
      'id': mdata['id'],
      'name': mdata['name'],
      'desc': mdata['desc'],
      'descData': mdata['descData'],
      'closed': mdata['closed'],
      'idOrganization': mdata['idOrganization'],
      'idEnterprise': mdata['idEnterprise'],
      'pinned': mdata['pinned'],
      'url': mdata['url'],
      'shortUrl': mdata['shortUrl'],
      'prefs': mdata['prefs'],
      'labelNames': mdata['labelNames'],
    }
    return cls(**model)
