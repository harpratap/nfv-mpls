class SDNForwardingDecision():

  _id = None

  _controller = None

  _match = None

  _actions = None

  def __init__(self, match, actions, controller):
    _match = match
    _actions = actions

  def commit(self):
    #FIXME: implement
    return None

  def setIngressPacketHandler(self, method):
    #FIXME: implement
    return None

  def setEgressPacketHandler(self, method):
    #FIXME: implement
    return None

  def _sendForwardingDecision():
    #FIXME: implement
    return None

  def _removeForwardingDecision():
    #FIXME: implement
    return None
