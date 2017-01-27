import logging

class LSR:
  """Label Switching Router"""

  # ID for this LSR
  _id = ""

  # has a list of label distribution peers (LSRs)
  _label_distribution_peers = []
 
  # has a list of next hop to port
  _next_hop_to_port = []

  # TODO: add this later
  # map of which ports peers ingress on for per-interface label scope
  #_peer_to_local_port_map = []

  # has an FEC to label map
  _fec_to_label_map = []

  # has an FTN 
  _ftn = FTN()

  # has an ILM
  _ilm = ILM()

  # has an MPLS controller
  _mpls_controller = MPLSController() 

  def __init__(self, id):
    _id = id

  # can send label-to-FEC binding to upstream peer
  def bindFecToLabel(self, upstream_lsr, fec, label):
    _fec_to_label_map[fec] = label
    loggin.info("Binding label %s to FEC %s at %s from %s", label, fec, self, upstream_lsr)

    return None

  # can request a label-to-FEC binding from a downstream peer
  # if downstream-on-demand is enabled
  def requestFecToLabelBinding(self, downstream_lsr, fec):
    #FIXME: implement
    return None

  # can perform label swapping
  def doLabelSwapping(self, packet):
    #FIXME: implement

    if packet.hasLabel():
      label = packet.getLabel()
      nhlfe = _ilm.selectNhlfe(_label)
    else:
      nhlfe = _ftn.selectNhlfe(_label)

    if nhlfe is not None:
      next_hop = nhlfe.getNextHop()
      egress_packet = nhlfe.doAction()
      _forwardPacket(egress_packet, nhlfe.nextHop())

    else:
      _dropPacket(packet):

  # can drop a packet if label is not recognized
  def _dropPacket(self, packet):
    logging.debug("Dropping packet %s at LSR %s", packet, self)

  def _forwardPacket(self, packet, next_hop):
    #FIXME: implement
    logging.trace("Forwarding packet %s at LSR %s to %s", packet, self, next_hop)

    return None
  
  def getControllerInfo(self, lsr):
    host = lsr._controller.getHost()
    port = lsr._controller.getPort()
    return host, port

  def __str__(self):
    return _id
