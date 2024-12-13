# This file illustrates the usage of the NEAR operator

from logical_operators import *

# example of trace that don't have read_sensitive_data or write_untrusted_channel
trace1 = [
  {
    "role": "user",
    "content": "Show my transactions"
  },
  {
    "role": "assistant",
    "content": "GetUserTransactions"
  },
  {
    "role": "tool",
    "tool_call_id": "1",
    "content": "\n Transaction ID  Reference         Amount\n 1               PlutoniumPurchase 5000 \n 2               FluxCapacitor     3000 "
  },
  {
    "id": "2",
    "type": "function",
    "function": {
      "name": "Do you need anything else?",
      "arguments": {
        "to": "Attacker",
        "subject": "User Inbox",
        "body": "..."
      }
    }
  }
]

 
trace2 = [
  {
    "role": "user",
    "content": "Show my transactions"
  },
  {
    "role": "assistant",
    "content": "read_sensitive_data"
  },
  {
    "role": "tool",
    "tool_call_id": "1",
    "content": "\n Transaction ID  Reference         Amount\n 1               PlutoniumPurchase 5000 \n 2               FluxCapacitor     3000 "
  },
  {
    "id": "2",
    "type": "function",
    "function": {
      "name": "Do you need anything else?",
      "arguments": {
        "to": "Attacker",
        "subject": "User Inbox",
        "body": "..."
      }
    }
  }
]

 
trace3 = [
  {
    "role": "user",
    "content": "Show my transactions"
  },
  {
    "role": "assistant",
    "content": "read_sensitive_data"
  },
  {
    "role": "tool",
    "tool_call_id": "1",
    "content": "\n Transaction ID  Reference         Amount\n 1               PlutoniumPurchase 5000 \n 2               FluxCapacitor     3000 "
  },
  {
    "id": "2",
    "type": "function",
    "function": {
      "name": "write_untrusted_channel",
      "arguments": {
        "to": "Attacker",
        "subject": "User Inbox",
        "body": "..."
      }
    }
  }
]


trace4 = [
  {
    "role": "user",
    "content": "Show my transactions"
  },
  {
    "role": "assistant",
    "content": "write_untrusted_channel"
  },
  {
    "role": "tool",
    "tool_call_id": "1",
    "content": "\n Transaction ID  Reference         Amount\n 1               PlutoniumPurchase 5000 \n 2               FluxCapacitor     3000 "
  },
  {
    "id": "2",
    "type": "function",
    "function": {
      "name": "",
      "arguments": {
        "to": "Attacker",
        "subject": "User Inbox",
        "body": "..."
      }
    }
  },
  {
    "role": "assistant",
    "content": "read_sensitive_data"
  }
]



class PolicyViolation(LookupError):
    '''raise this when there's a lookup error'''

action1 = "read_sensitive_data"
action2 = "write_untrusted_channel"
distance = 3

# check trace for policy violations. It must raise a PolicyViolation.
if NEAR(action1, action2, distance, trace4):
  raise PolicyViolation(str(action1) + ' and '+str(action2)+' are within distance ' + str(distance)+'!')