class FTN:
"""FEC to NHLFE mapping"""

  # FIXME: this structure is needs to be thread safe
  # has map of FEC-to-set-of-NHLFEs
  # currently a list of deques
  _nhlfe_list = []

  # ==== Methods for selecting an NHLFE given an FEC ====
  # Driven by data plane ingress

  # Can choose an NHLFE fromt he set of NHLFEs (however deem fit)
  def selectNhlfe(self, fec):
    """select an NHLFE based on the FEC"""
    if _nhlfe_list[fec] not None:
      #FIXME allow for choosing a selection algorithm
      return _selectRandomNhlfe(fec)

  def _selectFirstNhlfe(self, fec):
    """always select the first NHLFE in the list"""
    return _nhlfe_list[fec][0]

  def _selectRandomNhlfe(self, fec):
    """select a random NHLFE from the list"""
    _index = random.randint(0, (nhlfe_list[fec].len() - 1))
    return _nhlfe_list[fec][_index]

  def _selectLruNhlfe(self, fec):
    """select the least recently used NHLFE from the list"""
    _nhlfe = _nhlfe_list[fec].popleft()
    _nhlfe_list[fec].append(_nhlfe)
    return _nhlfe

  # Used if selection of NHLFE needs to happen at a different layer
  # such as using an OpenFlow group
  def getNhlfeList(self, fec):
    """Gets a clone of the NHLFE list for a FEC in list format"""
    return list(_nhlfe_list[fec])

  # ==== Methods for managing mapping of FECs to NHLFEs ====
  # (these are largely driven by events on the management plane)

  def addMapping(self, fec, nhlfe):
    """add NHFLE to the set of NHLFEs associated with the FEC"""
    if _nhlfe_list[fec] is None:
      _nhlfe_list[fec] = deque()

    _nhlfe_list[fec].append(nhlfe)

  def delMapping(self, fec, nhlfe):
    """delete NHFLE to the set of NHLFEs associated with the FEC"""
    if _nhlfe_list[fec] is None:
      # FIXME: throw exception
      return None 

    _nhlfe_list[fec].remove(nhlfe)
  
  def delFec(self, fec):
    """remove a FEC and all of its associated mappings from the FTN"""
    _nhlfe_list.remove(fec)
