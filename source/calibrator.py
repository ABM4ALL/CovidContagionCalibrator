from Melodie import Calibrator

from source.environment import CovidEnvironment


class CovidCalibrator(Calibrator):

    def setup(self):
        self.add_scenario_calibrating_property("infection_prob")
        self.add_environment_property("accumulated_infection")

    def distance(self, environment: "CovidEnvironment") -> float:
        return (environment.s0 / environment.scenario.agent_num - 0.25) ** 2


