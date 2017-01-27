class NHLFE:
  """Next Hop Label Forwarding Entity"""

  # TODO: this may need to be modified to allow for pushing more than one label
  # has packet's next hop (can be self)
  _next_hop = None

  # the action for this NHLFE
  _action = None

  # TODO: Allow for pushing more than one label
  # the label for the action
  _label = []

  _NHLFE_PUSH = 1
  _NHLFE_POP = 2
  _NHLFE_REPLACE = 3

  # may have data link encapsulation

  # may have way to encode label stack

  # RFC 3031 3.10 2.f, can contain other other info

  def __init__(self, next_hop):
    _next_hop = next_hop

  def setToReplace(self):
    _action = _NHLFE_REPLACE 

  def setToPop(self):
    _action = _NHLFE_PUSH

  def setToPush(self):
    _action = _NHLFE_POP

  def isPush(self):
    return action == _NHLFE_PUSH

  def isPop(self):
    return action == _NHLFE_POP

  def isReplace(self):
    return action == _NHLFE_REPLACE

  def getNextHop(self):
    return _next_hop

  def doAction(self, packet):
    if _action == _NHLFE_REPLACE:
      _replaceLabel(_label, packet)
    elif _action == _NHLFE_PUSH:
      _pushLabel(_label, packet)
    elif _action == _NHLFE_POP:
      _popLabel(_label, packet)
    else:
      # FIXME: throw exception
      return None


  # can replace label at top of stack
  def _replaceLabel(self, label, packet):
    packet.replaceLabel()

    return None

  # can pop label stack
  def _popLabel(self, label=None, packet):
    packet.popLabel()

    if label not None:
      replaceLabel(label)

    return None

  def _pushLabel(self, label, packet):
    if not packet.hasLabel():
      packet.setBosBit()

    packet.pushLabel(label)

    return implement

  # TODO: allow this function to be called
  # Can replace label at top of stack AND push one or more new labels
  def _pushLabels(self, label_queue, packet):
    if len(labelQueue) == 0:
      #FIXME throw exception, must at least replace top of stack
      return None

    self._replaceLabel(label_queue[0], packet)

    for label in labelQueue[1:]:
      self._pushLabel(label, packet)

    return None
