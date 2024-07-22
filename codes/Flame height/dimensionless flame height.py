import numpy as np


import numpy as np

def calculate_froude_number(uj, gdj, S, rho_i, rho_inf, Delta_Tf, T_inf):
    """
    Calculate the Froude number based on the given formula.

    Parameters:
    uj (float): Velocity at jet exit.
    gdj (float): g*dj, where g is gravitational acceleration and dj is the characteristic length.
    S (float): Strouhal number.
    rho_i (float): Density of the gas at the inlet.
    rho_inf (float): Ambient density.
    Delta_Tf (float): Temperature difference at the flame.
    T_inf (float): Ambient temperature.

    Returns:
    float: Froude number Frf.
    """
    numerator = uj
    denominator = (gdj**0.5) * ((S + 1)**1.5) * ((rho_i / rho_inf)**0.25) * ((Delta_Tf / T_inf)**0.5)
    Frf = numerator / denominator
    return Frf

# Example usage
uj = 20.0  # Velocity at jet exit (m/s)
gdj = 9.81 * 0.5  # g*dj, gravitational acceleration * characteristic length (m^2/s)
S = 0.3  # Strouhal number
rho_i = 1.2  # Density of the gas at the inlet (kg/m^3)
rho_inf = 1.0  # Ambient density (kg/m^3)
Delta_Tf = 100  # Temperature difference at the flame (K)
T_inf = 300  # Ambient temperature (K)

froude_number = calculate_froude_number(uj, gdj, S, rho_i, rho_inf, Delta_Tf, T_inf)
print(f"Froude Number: {froude_number}")


def calculate_normalized_flame_height(Hf, dj, S, rho_i, rho_inf):
    """
    Calculate the normalized flame height.

    Parameters:
    Hf (float): Actual flame height.
    dj (float): Diameter at the jet exit.
    S (float): Strouhal number.
    rho_i (float): Density of the gas at the inlet.
    rho_inf (float): Ambient density.

    Returns:
    float: Normalized flame height H*.
    """
    H_star = Hf / (dj * (S + 1) * (rho_i / rho_inf)**0.5)
    return H_star

# Example usage
Hf = 10.0  # Actual flame height
dj = 0.5   # Diameter at the jet exit
S = 0.2    # Strouhal number
rho_i = 1.2  # Density of the gas at the inlet
rho_inf = 1.0  # Ambient density

normalized_height = calculate_normalized_flame_height(Hf, dj, S, rho_i, rho_inf)
print(f"Normalized Flame Height: {normalized_height}")
