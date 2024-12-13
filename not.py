# This file illustrates the usage of the NOT operator

from logical_operators import *

# example of trace that don't have identity verification
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

# example of trace that have identity verification in a Message event
trace2 = [
  {
    "role": "user",
    "content": "Show my transactions"
  },
  {
    "role": "assistant",
    "content": "verify_identity"
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

# example of trace that have identity verification in a ToolCall event
trace3 = [
  {
    "role": "user",
    "content": "Show my transactions"
  },
  {
    "role": "assistant",
    "content": ""
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
      "name": "verify_identity",
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
  },
  {
    "role": "assistant",
    "content": "verify_identity"
  }
]


# define a policy that illustrates the NOT operator:
class PolicyViolation(LookupError):
    '''raise this when there's a lookup error'''

required_action = "verify_identity"

# check trace1 trace for policy violations. It must raise a PolicyViolation.
if NOT(required_action, trace1):
  raise PolicyViolation('The following required action is missing: ' + str(required_action))

"""
# check trace2 trace for policy violations. It must not raise a PolicyViolation.
if NOT(required_action, trace2):
  raise PolicyViolation('The following required action is missing: ' + str(required_action))

# check trace3 trace for policy violations. It must not raise a PolicyViolation.
if NOT(required_action, trace3):
  raise PolicyViolation('The following required action is missing: ' + str(required_action))

# check trace4 trace for policy violations. It must not raise a PolicyViolation.
if NOT(required_action, trace4):
  raise PolicyViolation('The following required action is missing: ' + str(required_action))

"""