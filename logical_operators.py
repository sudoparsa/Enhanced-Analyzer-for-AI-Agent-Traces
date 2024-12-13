# This file contains the implementations of the logical operators (NOT, COUNT, NEAR, WITHIN).
# These implementations currently work independently of the DSL (run NOT.py, COUNT.py, NEAR.py, and WITHIN.py to understand and test these implementations).
# main.py incorporate these implementations into the DSL with a parser.  
# Each operator returns a boolean value, where True corresponds with a PolicyError (False does not raise any PolicyError).
# Their inputs can be are actions, traces and integers (these inputs depend on each operator). An action is a string, and a trace is a list of dictionaries.


# NOT operator: Returns True iff an action is NOT in a trace.
def NOT(action, trace):
    trace = str(trace)
    if action in trace:
        return False
    return True


# COUNT operator: Returns True iff an action appears more than a given number of times in a trace.
def COUNT(action, max_number, trace):
    trace = str(trace)
    number_of_appearances = trace.count(action)
    if number_of_appearances > max_number:
        return True
    return False


import sys
# Auxiliary function for NEAR and WITHIN operators. Given two lists A and B of integers, return minimun difference between A and B.
# Time complexity:  O(m log m + n log n), where m = len A and n = len B.
def findSmallestDifference(A, B):
 
    # Sort both lists 
    # using sort function
    A.sort()
    B.sort()
 
    a = 0
    b = 0
 
    # Initialize result as max value
    result = sys.maxsize

    m = len(A)
    n = len(B)
 
    # Scan Both lists upto
    # sizeof of the lists
    while (a < m and b < n):
     
        if (abs(A[a] - B[b]) < result):
            result = abs(A[a] - B[b])
 
        # Move Smaller Value
        if (A[a] < B[b]):
            a += 1
 
        else:
            b += 1
    # return final sma result
    return result 


# NEAR operator: Returns True iff action1 and action2 are close within a given distance in a trace.
# This implementation is useful when action1 and action2 are distinct (otherwise it always returns True).
def NEAR(action1, action2, distance, trace):
    trace_as_string = str(trace)
    if (action1 in trace_as_string) and (action2 in trace_as_string):

        # First we create two arrays. One will contain the indices of the trace where action1 appears. Same for action2.
        list_of_indices_action1_in_trace = []
        list_of_indices_action2_in_trace = []

        for event in trace:
            event_as_string = str(event)
            if action1 in event_as_string:
                list_of_indices_action1_in_trace.append(trace.index(event))
            if action2 in event_as_string:
                list_of_indices_action2_in_trace.append(trace.index(event))

        # Now we compute the minimum distance between action1 and action2
        minimum_distance = findSmallestDifference(list_of_indices_action1_in_trace, list_of_indices_action2_in_trace)

        if minimum_distance <= distance:
            return True                           
        return False

    return False


# WITHIN operator: Returns True iff action1 and action2 are executed within a given time in a trace.
# This implementation is useful when action1 and action2 are distinct (otherwise it always returns True).
# We assume that action1 and action2 have timestamps in the dictionary trace indicated by the key "created_at"
def WITHIN(action1, action2, time, trace):
    trace_as_string = str(trace)
    if (action1 in trace_as_string) and (action2 in trace_as_string):

        # First we create two arrays. One will contain the times where action1 is executed in trace. Same for action2.
        list_of_times_action1_in_trace = []
        list_of_times_action2_in_trace = []

        for event in trace:
            event_as_string = str(event)
            if action1 in event_as_string:
                list_of_times_action1_in_trace.append(event["created_at"])
            if action2 in event_as_string:
                list_of_times_action2_in_trace.append(event["created_at"])

        # Now we compute the minimum time between action1 and action2
        minimum_time = findSmallestDifference(list_of_times_action1_in_trace, list_of_times_action2_in_trace)

        if minimum_time <= time:
            return True                           
        return False

    return False
