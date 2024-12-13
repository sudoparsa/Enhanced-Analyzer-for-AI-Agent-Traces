# This file illustrates the usage of the COUNT operator

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
  },
  {
    "role": "assistant",
    "content": "verify_identity"
  }
]

trace5 = [
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
      "name": "verify_identity",
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


class PolicyViolation(LookupError):
    '''raise this when there's a lookup error'''

action = "verify_identity"
max_number = 2

# check trace for policy violations. It must raise a PolicyViolation.
if COUNT(action, max_number, trace5):
  raise PolicyViolation('The action ' + str(action) + ' appears more than '+str(max_number)+' times!')