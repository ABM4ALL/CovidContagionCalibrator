import os
from typing import Dict

import matplotlib.pyplot as plt
import numpy as np

from Melodie import Config
from Melodie import db


class CovidAnalyzer:

    def __init__(self, config: "Config"):
        self.fig_folder = config.output_folder
        self.db = db.create_db_conn(config)

    def plot_health_state_share(self, id_scenario: int = 0, id_run: int = 0):
        df = self.db.read_dataframe("environment_result")
        df = df.loc[(df["id_scenario"] == id_scenario) & (df["id_run"] == id_run)]
        values_dict = {
            "Not-infected": df["s0"],
            "Infected": df["s1"],
            "Recovered": df["s2"],
            "Dead": df["s3"],
        }
        figure = plt.figure(figsize=(12, 6))
        ax = figure.add_axes((0.1, 0.1, 0.8, 0.8))
        ax.set_ylim(0, 1000)
        ax.set_xlabel("Period", fontsize=15)
        ax.set_ylabel("Count", fontsize=15)
        x = [i for i in range(0, len(list(values_dict.values())[0]))]
        bottom = np.zeros(len(x))
        for key, values in values_dict.items():
            ax.bar(
                x,
                values,
                bottom=bottom,
                label=key,
            )
            bottom += values
        ax.legend(fontsize=12)
        self.save_fig(figure, f"PopulationInfection_S{id_scenario}R{id_run}")

    def plot_calibration_process(
            self,
            id_calibrator_scenario: int = 0,
            id_calibrator_params_scenario: int = 0,
    ):
        calibrator_params_scenarios = self.db.read_dataframe("calibrator_params_scenarios")
        path_num = calibrator_params_scenarios.at[id_calibrator_scenario, "path_num"]
        df = self.db.read_dataframe("environment_calibrator_result_cov")
        df = df.loc[(df["id_calibrator_scenario"] == id_calibrator_scenario) &
                    (df["id_calibrator_params_scenario"] == id_calibrator_params_scenario)]
        s0_paths = {}
        infection_prob_paths = {}
        for id_path in range(0, path_num):
            df_path = df.loc[df["id_path"] == id_path]
            s0_paths[f"path_{id_path + 1}"] = df_path["s0_mean"].to_numpy()
            infection_prob_paths[f"path_{id_path + 1}"] = df_path["infection_prob_mean"].to_numpy()

        self.plot_paths(
            paths=s0_paths,
            fig_name=f"S0Calibration_CS{id_calibrator_scenario}PS{id_calibrator_params_scenario}",
            y_label="Count",
            y_limit=(0, 600)
        )
        self.plot_paths(
            paths=infection_prob_paths,
            fig_name=f"InfectionProbCalibration_CS{id_calibrator_scenario}PS{id_calibrator_params_scenario}",
            y_label="Infection Probability",
            y_limit=(0, 0.6)
        )

    def plot_paths(self, paths: Dict[str, np.ndarray], fig_name: str, y_label: str = None, y_limit: tuple = None):
        figure = plt.figure(figsize=(12, 6))
        ax = figure.add_axes((0.1, 0.1, 0.8, 0.8))
        if y_limit:
            ax.set_ylim(y_limit)
        ax.set_xlabel("Generation", fontsize=15)
        if y_label:
            ax.set_ylabel(y_label, fontsize=15)
        x = [i for i in range(0, len(list(paths.values())[0]))]
        for id_path, values in paths.items():
            ax.plot(x, values, label=id_path)
        ax.legend(fontsize=12)
        self.save_fig(figure, fig_name)

    def save_fig(self, fig, fig_name):
        fig.savefig(
            os.path.join(self.fig_folder, fig_name + ".png"),
            dpi=200,
            format="PNG",
        )
        plt.close(fig)









