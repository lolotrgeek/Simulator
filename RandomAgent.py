from Agent import Agent
from random import sample, randint

class RandomAgent(Agent):
    def __init__(self) -> None:
        super().__init__()
        self.action_space = [0,1,2,3,4,5,6,7,8,9,10,11]
        self.actions = []
        self.episode = 0
        self.episodes = 1000

    def sample_action(self):
        return self.action_space[sample(range(0, len(self.action_space)), 1)[0]]
        
    def decide(self):
        return randint(self.action_space[1],self.action_space[-1])    

    def spin(self):
        while True:
            self.episode += 1
            # print(self.episode)
            if(self.episode >= self.episodes):
                print(self.id, self.actions)
                break
            observation = self.observe()
            # print("observation", observation)
            if observation is None or observation == {}:
                continue
            if(observation["action"] < self.decide()):
                action = self.sample_action()
                # print("performing action", action)
                self.perform(action)
                self.actions.append(action)
            else:
                # print("not performing action") 
                continue      
