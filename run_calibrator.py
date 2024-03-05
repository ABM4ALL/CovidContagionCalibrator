from config import config
from source.calibrator import CovidCalibrator
from source.model import CovidModel
from source.scenario import CovidScenario

if __name__ == "__main__":
    calibrator = CovidCalibrator(
        config=config,
        model_cls=CovidModel,
        scenario_cls=CovidScenario,
        processors=8,
    )
    calibrator.run()
