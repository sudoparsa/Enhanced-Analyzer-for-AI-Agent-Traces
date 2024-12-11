from invariant import Policy
from scenarios import *
import sys

class PolicyViolation(LookupError):
    '''raise this when there's a lookup error'''


class Enhanced_Policy():
    def __init__(self, string):
        self.policy_not = ''
        self.policy_count = ''
        self.policy_near = ''
        self.policy_within = ''
        if 'NOT' in string:
            self.policy_not = string[string.index('NOT'):].split('\n')[0]
            string = ''.join(string.split(self.policy_not))
        if 'COUNT' in string:
            self.policy_count = string[string.index('COUNT'):].split('\n')[0]
            string = ''.join(string.split(self.policy_count))
        if 'NEAR' in string:
            self.policy_near = string[string.index('NEAR'):].split('\n')[0]
            string = ''.join(string.split(self.policy_near))
        if 'WITHIN' in string:
            self.policy_within = string[string.index('WITHIN'):].split('\n')[0]
            string = ''.join(string.split(self.policy_within))
        
        self.policy = Policy.from_string(string)
    
    def NOT(self, msgs):
        if not self.policy_not:
            return False
        action = self.policy_not.strip().split('NOT')[1].strip()
        message = str(msgs)
        if action in message:
            return False
        return True
    
    def COUNT(self, msgs):
        if not self.policy_count:
            return False
        action = self.policy_count.strip().split('COUNT')[1].split()[0]
        max_number = int(self.policy_count.strip().split('COUNT')[1].split()[1])
        message = str(msgs)
        number_of_appearances = message.count(action)
        if number_of_appearances > max_number:
            return True
        return False
    # Auxiliary function for NEAR operator. Given two lists A and B of integers, return minimun difference between A and B.
    def findSmallestDifference(self, A, B):
        A.sort()
        B.sort()
        a = 0
        b = 0
        result = sys.maxsize
        m = len(A)
        n = len(B)
    
        while (a < m and b < n):
            if (abs(A[a] - B[b]) < result):
                result = abs(A[a] - B[b])
            if (A[a] < B[b]):
                a += 1
            else:
                b += 1
        return result 


    def NEAR(self, message):
        if not self.policy_near:
            return False
        action1 = self.policy_near.strip().split('NEAR')[1].split()[0]
        action2 = self.policy_near.strip().split('NEAR')[1].split()[1]
        distance = int(self.policy_near.strip().split('NEAR')[1].split()[2])

        message_as_string = str(message)
        if (action1 in message_as_string) and (action2 in message_as_string):

            list_of_indices_action1_in_message = []
            list_of_indices_action2_in_message = []

            for event in message:
                event_as_string = str(event)
                if action1 in event_as_string:
                    list_of_indices_action1_in_message.append(message.index(event))
                if action2 in event_as_string:
                    list_of_indices_action2_in_message.append(message.index(event))

            minimum_distance = self.findSmallestDifference(list_of_indices_action1_in_message, list_of_indices_action2_in_message)
            if minimum_distance <= distance:
                return True                           
            return False
        return False
    
    def analyze(self, msgs):
        analysis = self.policy.analyze(msgs)

        if self.NOT(msgs):
            action = self.policy_not.strip().split('NOT')[1].strip()
            analysis.errors.append(PolicyViolation('The following required action is missing: ' + str(action)))
        
        if self.COUNT(msgs):
            action = self.policy_count.strip().split('COUNT')[1].split()[0]
            max_number = int(self.policy_count.strip().split('COUNT')[1].split()[1])
            analysis.errors.append(PolicyViolation('The action ' + str(action) + ' appears more than '+str(max_number)+' times!'))
        
        if self.NEAR(msgs):
            action1 = self.policy_near.strip().split('NEAR')[1].split()[0]
            action2 = self.policy_near.strip().split('NEAR')[1].split()[1]
            distance = int(self.policy_near.strip().split('NEAR')[1].split()[2])
            analysis.errors.append(PolicyViolation(str(action1) + ' and '+str(action2)+' are within distance ' + str(distance)+'!'))
        
        return analysis
        





if __name__ == '__main__':
    print('### Scenario 1 ###')
    policy = Enhanced_Policy(POLICY1)
    print(policy.analyze(TRACE1))

    print('### Scenario 2 ###')
    policy = Enhanced_Policy(POLICY2)
    print(policy.analyze(TRACE2))

    print('### Scenario 3 ###')
    policy = Enhanced_Policy(POLICY3)
    print(policy.analyze(TRACE3))

    print('### Scenario 4 ###')
    policy = Enhanced_Policy(POLICY4)
    print(policy.analyze(TRACE4))

