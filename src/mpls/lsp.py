class LSP:
  """Label Switched Path"""

  # has a depth
  _depth = 0

  # has a sequence of LSRs
  _lsr_sequence = None

  # can do penultimate hop popping based on config
