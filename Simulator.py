from Messaging import Router
from Agent import Agent

class Simulator():
    def __init__(self) -> None:
        self.state = Router()
        pass


    def run(self):  
        try:
            self.state.route()
        except KeyboardInterrupt:
            pass

