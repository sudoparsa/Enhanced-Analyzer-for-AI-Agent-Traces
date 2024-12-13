# This file illustrates the usage of the WITHIN operator
# The timestamp system used by OpenAI is the UNIX timestamp system: https://www.unixtimestamp.com/
# We'll assume that every Message event has a timestamp indicated on the "created_at" with time measured in seconds.

from logical_operators import *

trace = [
  {
    "created_at": 1702212600,
    "role": "user",
    "content": "Can you show me my transactions?"
  },
    {
    "created_at": 1702212603,
    "role": "assistant",
    "content": "Sure! Here there are..."
  },
    {
    "created_at": 1702212608,
    "role": "user",
    "content": "Great! Also, can you tell me the last time I paid for my groceries?"
  },
    {
    "created_at": 1702212609,
    "role": "assistant",
    "content": "Sure! It was 5 days ago."
  },
]




class PolicyViolation(LookupError):
    '''raise this when there's a lookup error'''

action1 = "Can you show me my transactions?"
action2 = "Sure! Here there are..."
time = 3

# check trace trace for policy violations. It must raise a PolicyViolation.
if WITHIN(action1, action2, time, trace):
  raise PolicyViolation('"'+str(action1) + '" and "'+str(action2)+'" are executed within ' + str(time)+' seconds!')
