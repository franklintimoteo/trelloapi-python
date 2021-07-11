class Label:
  def __init__(self, id, type, name, color):
    self.id = id
    self.type = type
    self.name = name
    self.color = color

class Board:
  def __init__(self, id, name, shortLink):
    self.id = id
    self.name = name
    self.shortLink = shortLink

class Card:
  def __init__(self, type, id, shortLink, text):
    self.type = type
    self.id = id
    self.shortLink = shortLink
    self.text = text

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

class Display:
  def __init__(self, translationKey, entities):
    self.translationKey = translationKey
    self.entities = entities # type: dict

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
    action = {
      'id': actdata['id'],
      'idMemberCreator': actdata['idMemberCreator'],
      'data': actdata['data'],
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
