from Agent import Agent

class NothingAgent(Agent):
    def __init__(self) -> None:
        super().__init__()
        self.episode = 0
        self.episodes = 1000

    def spin(self):
        while True:
            observation = self.observe()
            print("observation", observation)
