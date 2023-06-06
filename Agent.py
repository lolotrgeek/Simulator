from Messaging import Pusher, Puller
from uuid import uuid4

class Agent():
    def __init__(self) -> None:
        self.id = uuid4()
        self.action_space = None
        self.observation_space = None
        self.observer = Puller()
        self.performer = Pusher()
        #TODO: self.env will connect to a simulator
    
    def observe(self):
        observation = self.observer.pull()
        return observation

    def perform(self, action):
        action = self.performer.push({"action": action, "agent": str(self.id)})
        return action

    def spin(self):
        pass