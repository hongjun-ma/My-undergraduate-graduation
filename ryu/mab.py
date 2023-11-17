import math
import numpy as np

# MAB superclass
class MAB(object):
    def __init__(self, actions, action_num):
        self.actions = actions
        self.action_num = action_num

class Action(object):
    def __init__(self, id):
        self.id = id
        self.mean = 0
        self.N = 0
    
    def update(self, reward):
        self.N += 1
        self.mean = 1.0 * reward / self.N + (1 - 1.0/self.N) * self.mean 
        
    def __repr__(self):
        return "id:" + str(self.id) + " ChoosenTime:" + str(self.N) + " MeanReward:" + str(self.mean)
    
# epsilon-greedy class
class egreedy(MAB):
    def __init__(self, actions, action_num, eps):
        super(egreedy, self).__init__(actions, action_num)
        self.eps = eps

    def choose_action(self):
        p = np.random.random()
        if p < self.eps:
            j = np.random.choice(self.action_num)
        else:
            j = np.argmax([action.mean for action in self.actions])
        x = self.actions[j]
        return x

# softmax class
class softmax(MAB):
    def __init__(self, actions, action_num, tau):
        super(softmax, self).__init__(actions, action_num)
        self.tau = tau

    def choose_action(self):
        z = sum([math.exp(a.mean / self.tau) for a in self.actions])
        probs = [math.exp(a.mean / self.tau) / z for a in self.actions]

        p = np.random.random()
        cumm_prob = 0.0
        for i in range(len(self.actions)):
            cumm_prob += probs[i]
            if cumm_prob > p:
                return self.actions[i]
        return self.actions[-1]

#UCB class
class UCB(MAB):
    def __init__(self, actions, action_num):
        super(UCB1, self).__init__(actions, action_num)
    
    def choose_action(self):
        timestep = sum([a.N for a in self.actions]) + 1
        indexs = [a.mean + math.sqrt(2 * math.log10(timestep) / a.N) for a in self.actions]
        choosen = np.argmax(indexs)
        return self.actions[choosen]
