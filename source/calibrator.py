from Melodie import Calibrator

from source.model import CovidModel


class CovidCalibrator(Calibrator):
    def setup(self):
        self.add_scenario_calibrating_property("infection_prob")
        self.add_environment_property("s0")

    def distance(self, model: "CovidModel") -> float:
        environment = model.environment
        return (environment.s0 / environment.scenario.agent_num - 0.5) ** 2
