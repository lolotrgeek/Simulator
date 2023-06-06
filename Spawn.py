from multiprocessing import Process
from RandomAgent import RandomAgent

class Spawn():
    def __init__(self) -> None:
        self.agents = []
        pass

    def spawn(self, agents=5):
        for i in range(0,agents):
            agent_process = Process(target=RandomAgent().spin)
            self.agents.append(agent_process)
            agent_process.start()

    def kill(self):  
        print("attempting to kill agents..." )
        for agent in self.agents:
            agent.terminate()
            agent.join()
        print("agents successfully killed")




