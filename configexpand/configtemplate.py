'''
This file is part of configexpand.py script.
It contains data to be put into the config.
This is to separate data and code, as config listings are often quite extensive.


'''

# example config generates dial-peers for Cisco VoIP gateways:
CONFIG_TEMPLATE_ITERATIVE = """dial-peer voice {sequence} voip
 description {description}
 preference 1
 destination-pattern {pattern}
 session protocol sipv2
 session target ipv4:{ip}
 dtmf-relay rtp-nte
 codec g711alaw
 no vad
"""

CONFIG_TEMPLATE_COUNTER = dict(offset = 42 )# offset, if needed

# 
# this way any static data can be added if needed:
CONFIG_TEMPLATE_STATIC = dict(ip='192.0.2.42') # TEST-NET-1 per RFC5737 https://tools.ietf.org/html/rfc5737 


CONFIG_TEMPLATE_ADD_BEFORE = ""

CONFIG_TEMPLATE_ADD_AFTER = ""