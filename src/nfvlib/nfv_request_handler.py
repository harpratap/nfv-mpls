from flask import Flask, url_for

class SDNRequestHandler():

  app = Flask(__name__)

  ####### Controllable Network Devices #######

  @app.route("/networkdevice/openflow/json", methods=["GET", "POST", "DELETE"])
  def handleOpenFlowSwitchRequest():

    # Get a formatted list of known switches
    if request.method == "GET":
      switches = getOpenFlowSwitches()
      return formatList(switches)

    # Add a switch to the list of known switches
    elif request.method == "POST":
      if request.args['id']:
        result = addOpenFlowSwitch(request.args['id'])
      else:
        result = "Failed: no switch ID specified"

      return formatResult(result)

    # Remove a switch from the list of known switches
    elif request.method == "DELETE":
      if request.args['id']:
        result = removeOpenFlowSwitch(request.args['id'])
      else:
        result = "Failed: no switch ID specified"

      return formatResult(result)

    # Verb not understood
    else:
      result = "Unable to understand request"
      return formatResult(result)


  ####### Links #######

  @app.route("/link/openflow/json", methods=["GET", "POST", "DELETE"])
  def handleOpenFlowLinkRequest():

    # Get a formatted list of known links
    if request.method == "GET":
      links = getOpenFlowLinks()
      formatted_links = []

      for link in links:
        formatted_links.add(formatLink(link))

      return formatList(formatted_links)

    # Add a link to the list of known links
    elif request.method == "POST":
      if request.args['switch1'] and request.args['switch2']:
        result = addOpenFlowLink(request.args['switch1'], request.args['switch2'])
      else:
        result = "Failed: either switch1 or switch2 not defined"

      return formatResult(result)

    # Remove a link from the list of known links
    elif request.method == "DELETE":
      if request.args['switch1'] and request.args['switch2']:
        result = removeOpenFlowLink(request.args['switch1'], request.args['switch2'])
      else:
        result = "Failed: either switch1 or switch2 not defined"

      return formatResult(result)

    # Verb not understood
    else:
      result = "Unable to understand request"
      return formatResult(result)

  ####### Received Packet Events #######


