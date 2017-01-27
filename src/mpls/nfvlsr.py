class SDNLSR(LSR):
  """A logic for managing a software defined Label Switching Router"""

  def doLabelSwapping(self, packet):
    dec = SDNForwardingDecision()
    match = SDNMatch()
    actions = SDNActions()

    if packet.hasLabel():
      label = packet.getLabel()
      nhlfe = _ilm.selectNhlfe(_label)

      # Set match with ingress label
      match.setMPLSLabelMatch(label)

    else:
      nhlfe = _ftn.selectNhlfe(_label)

      if nhlfe is not None:
        # Set match based on ftn info
        match.setMatchByFilter(nhlfe.getFilter(), packet)
      else:
        _dropPacket(packet)

    if nhlfe is not None:
      next_hop = nhlfe.getNextHop()
      next_port = _next_hop_to_port[next_hop]

      # Set actions based on NHLFE
      if nhlfe.isReplace():
        actions.addReplaceMPLSLabel(nhlfe.getLabel())
        actions.addForwardToPorts(next_port)
        dec.commit(match, actions)
      elif nhlfe.isPush():
        actions.addPushMPLSLabel(nhlfe.getLabel())
        actions.addForwardToPorts(next_port)
        dec.commit(match, actions)
      elif nhlfe.isPop():
        actions.addPopMPLSLabel()
        actions.addForwardToPorts(next_port)
        dec.commit(match, actions)
      else:
        logging.warn("NHLFE %s on LSR %s has undefined action", nhlfe, self)

    else:
      _dropPacket(packet):

  # can drop a packet if label is not recognized
  def _dropPacket(self, packet):
    logging.debug("Dropping packet %s at LSR %s", packet, self)
    # FIXME: Install drop rule with short hard timeout
