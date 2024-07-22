import fmpy
import matplotlib.pyplot as plt


def install_fmpy():
    import subprocess
    subprocess.run(["pip", "install", "fmpy"], check=True)


def load_fmu(fmu_path):
    """Load the FMU and return the model description."""
    model_description = fmpy.read_model_description(fmu_path)
    fmpy.dump(model_description)
    return model_description


def simulate_fmu(fmu_path, parameters=None, start_time=0, stop_time=10, step_size=0.1):
    """Simulate the FMU and return the results."""
    input_settings = {'start_time': start_time, 'stop_time': stop_time, 'step_size': step_size}
    if parameters:
        input_settings['parameters'] = parameters
    result = fmpy.simulate_fmu(fmu_path, **input_settings)
    return result


def plot_results(results, variable_name):
    """Plot the simulation results."""
    plt.figure(figsize=(10, 5))
    plt.plot(results['time'], results[variable_name], label=variable_name)
    plt.xlabel('Time [s]')
    plt.ylabel(variable_name)
    plt.title('Simulation Results')
    plt.legend()
    plt.show()


def cleanup_fmus():
    """Cleanup extracted FMUs to free resources."""
    fmpy.remove_extracted_fmus()


# Usage example:
if __name__ == "__main__":
    # Install FMPy if not installed (uncomment the following line)
    # install_fmpy()

    fmu_path = f"E:\OneDrive\2_full_time_job\24_tool\Digital twins\Help file-digital twins\TwinBuilder_GetStarted_2022R1_Student\Module 12 - Static ROM\WS12.4\test_model.fmu"
    model_description = load_fmu(fmu_path)

    # Define parameters if necessary
    parameters = {'parameter1': 100, 'parameter2': 200}

    # Simulate the FMU
    results = simulate_fmu(fmu_path, parameters=parameters)

    # Plot the results
    plot_results(results, 'variableName')  # Replace 'variableName' with your actual variable name

    # Cleanup
    cleanup_fmus()

# TwinBuilder_SendingPeriod