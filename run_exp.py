import argparse
import subprocess


def run_script(script_name):
    """Run the specified Python script."""
    try:
        # Run the script and wait for it to complete
        subprocess.run(["python", script_name], check=True)
        print(f"Successfully ran {script_name}")
    except subprocess.CalledProcessError:
        # If a script fails, print an error but continue with the next script
        print(f"Error occurred while running {script_name}. Continuing with the next script.")
    except Exception as e:
        # Catch other potential errors and continue
        print(f"Unexpected error: {e}. Continuing with the next script.")


def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Run a specific experiment script.")

    # Define the argument for the script selection with a default value
    parser.add_argument(
        "-e", "--experiment",
        choices=["CSB", "CSE", "FCSB", "FCSE", "FTB", "FTBF", "FTE", "FTEF", "ALL"],
        default="FTB",  # Default value set to "CSB"
        help="Specify the experiment to run: CSB, CSE, FCSB, FCSE, FTB, FTBF, FTE, FTEF, or ALL. Default is CSB."
    )

    # Parse the arguments
    args = parser.parse_args()

    # Map the experiment code to the respective Python script
    experiment_map = {
        "CSB": "Exps/Experiment_index_cost_SIMPLE_BTC.py",
        "CSE": "Exps/Experiment_index_cost_SIMPLE_ETH.py",
        "FCSB": "Exps/Experiment_index_cost_Fuzzy_BTC.py",
        "FCSE": "Exps/Experiment_index_cost_Fuzzy_ETH.py",
        "FTB": "Exps/Experiment_index_cost_TIME_BTC.py",
        "FTBF": "Exps/Experiment_index_cost_TIME_BTC_FISCO.py",
        "FTE": "Exps/Experiment_index_cost_TIME_ETH.py",
        "FTEF": "Exps/Experiment_index_cost_TIME_ETH_FISCO.py"
    }

    # If the argument is 'ALL', run all scripts in the map
    if args.experiment == "ALL":
        for script_name in experiment_map.values():
            run_script(script_name)
    else:
        # Get the script name based on the input experiment code
        script_name = experiment_map[args.experiment]
        # Run the selected script
        run_script(script_name)


if __name__ == "__main__":
    main()
