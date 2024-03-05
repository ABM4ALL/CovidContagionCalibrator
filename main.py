import os

from Melodie import Config
from Melodie import Simulator

from source.calibrator import CovidCalibrator
from source.model import CovidModel
from source.scenario import CovidScenario


def run_calibrator(cfg):
    calibrator = CovidCalibrator(
        config=cfg,
        model_cls=CovidModel,
        scenario_cls=CovidScenario,
        processors=8,
    )
    calibrator.run()


def run_simulator(cfg):
    simulator = Simulator(
        config=cfg,
        model_cls=CovidModel,
        scenario_cls=CovidScenario
    )
    simulator.run()


if __name__ == "__main__":

    config = Config(
        project_name="CovidContagionCalibrator",
        project_root=os.path.dirname(__file__),
        input_folder="data/input",
        output_folder="data/output",
        input_cache=True
    )

    run_simulator(config)
    run_calibrator(config)
