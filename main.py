
from Simulator import Simulator
from RandomAgent import RandomAgent
from multiprocessing import Process
from time import sleep
from NothingAgent import NothingAgent

def simulate():
    try:
        simulator = Simulator()
        simulator.run()
    except Exception as e:
        print(e)
        pass

def spawn_agent():
    try:
        agent = RandomAgent()
        agent.spin()
    except Exception as e:
        print(e)
        pass

def initial_agent():
    try:
        agent = RandomAgent()
        agent.perform(0)
    except Exception as e:
        print(e)
        pass

if __name__ == "__main__":
    try:

        agents = []
        num_agents = 5
        simulator_process = Process(target=simulate)
        simulator_process.start()
        print(simulator_process)
        sleep(1)
        initial_agent()
        sleep(1)
        for i in range(0,num_agents):
            agent_process = Process(target=spawn_agent)
            agents.append(agent_process)
            agent_process.start()

        print(agents)

        while True:
            sleep(.1)

    except KeyboardInterrupt:
        print("attempting to close processes..." )
        for agent in agents:
            agent.terminate()
            agent.join()

        simulator_process.terminate()
        simulator_process.join()
        print("processes successfully closed")

    finally:
        exit(0)        
