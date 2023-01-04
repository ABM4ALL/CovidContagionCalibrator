from Melodie import Calibrator

from source.model import CovidModel


class CovidCalibrator(Calibrator):

    def setup(self):
        self.add_scenario_calibrating_property("infection_prob")
        self.add_environment_property("s0")

    def distance(self, model: "CovidModel") -> float:
        return (model.environment.s0 / model.environment.scenario.agent_num - 0.25) ** 2
