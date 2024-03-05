from Melodie import Simulator
from config import config
from source.model import CovidModel
from source.scenario import CovidScenario

if __name__ == "__main__":
    simulator = Simulator(
        config=config,
        model_cls=CovidModel,
        scenario_cls=CovidScenario
    )
    simulator.run()
