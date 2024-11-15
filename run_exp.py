import argparse
import subprocess


def run_script(script_name):
    """Run the specified Python script."""
    subprocess.run(["python", script_name])


def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Run a specific experiment script.")

    # Define the argument for the script selection
    parser.add_argument(
        "-e", "--experiment",
        choices=["CSB", "CSE", "FCSB", "FCSE", "FBC", "FBCF", "FEC", "FECF"],
        default="CSB",  # Default value set to "CSB"
        # required=True,
        help="Specify the experiment to run: CSB, CSE, FCSB, FCSE, FBC, FBCF, FEC, or FECF."
    )

    # Parse the arguments
    args = parser.parse_args()

    # Map the experiment code to the respective Python script
    experiment_map = {
        "CSB": "Experiment_index_cost_SIMPLE_BTC.py",
        "CSE": "Experiment_index_cost_SIMPLE_ETH.py",
        "FCSB": "Experiment_index_cost_Fuzzy_BTC.py",
        "FCSE": "Experiment_index_cost_Fuzzy_ETH.py",
        "FBC": "Experiment_index_cost_TIME_BTC.py",
        "FBCF": "Experiment_index_cost_TIME_BTC_FISCO.py",
        "FEC": "Experiment_index_cost_TIME_ETH.py",
        "FECF": "Experiment_index_cost_TIME_ETH_FISCO.py"
    }

    # Get the script name based on the input experiment code
    script_name = experiment_map[args.experiment]

    # Run the selected script
    run_script(script_name)


if __name__ == "__main__":
    main()
