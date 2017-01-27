class ILM:
  """Incoming Label Map"""

  # FIXME: this structure is needs to be thread safe
  # has map of label-to-set-of-NHLFEs
  # currently a list of deques
  _nhlfe_list = []

  # ==== Methods for selecting an NHLFE given an input label ====
  # Driven by data plane ingress

  # Can choose an NHLFE fromt he set of NHLFEs (however deem fit)
  def selectNhlfe(self, label):
    """select an NHLFE based on the label"""
    if _nhlfe_list[label] not None:
      #FIXME allow for choosing a selection algorithm
      return _selectRandomNhlfe(label)

  def _selectFirstNhlfe(self, label):
    """always select the first NHLFE in the list"""
    return _nhlfe_list[label][0]

  def _selectRandomNhlfe(self, label):
    """select a random NHLFE from the list"""
    _index = random.randint(0, (nhlfe_list[label].len() - 1))
    return _nhlfe_list[label][_index]

  def _selectLruNhlfe(self, label):
    """select the least recently used NHLFE from the list"""
    _nhlfe = _nhlfe_list[label].popleft()
    _nhlfe_list[label].append(_nhlfe)
    return _nhlfe

  # Used if selection of NHLFE needs to happen at a different layer
  # such as using an OpenFlow group
  def getNhlfeList(self, label):
    """Gets a clone of the NHLFE list for a label in list format"""
    return list(_nhlfe_list[label])

  # ==== Methods for managing mapping of labels to NHLFEs ====
  # (these are largely driven by events on the control plane)

  def addMapping(self, label, nhlfe):
    """add NHFLE to the set of NHLFEs associated with the label"""
    if _nhlfe_list[label] is None:
      _nhlfe_list[label] = deque()

    _nhlfe_list[label].append(nhlfe)

  def delMapping(self, label, nhlfe):
    """delete NHFLE to the set of NHLFEs associated with the label"""
    if _nhlfe_list[label] is None:
      # FIXME: throw exception
      return None 

    _nhlfe_list[label].remove(nhlfe)
  
  def delLabel(self, label):
    """remove a label and all of its associated mappings from the ILM"""
    _nhlfe_list.remove(label)
