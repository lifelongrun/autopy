def btu_per_lb_to_kj_per_kg(btu_per_lb):
    # Conversion factors
    btu_to_kj = 1.055055
    lb_to_kg = 0.453592

    # Convert Btu/lb to kJ/kg
    kj_per_kg = btu_per_lb * btu_to_kj / lb_to_kg

    return kj_per_kg


# Example: Convert 200 Btu/lb to kJ/kg
btu_value = 22900.0 # 62050.0 for H2
kj_value = btu_per_lb_to_kj_per_kg(btu_value)

print(f"{btu_value} Btu/lb is equal to {kj_value:.2f} kJ/kg")

# the heat of hydrogen/H2 combustion: 144328.30 kJ/kg
# the heat of methane/CH4 combustion: 53265.40 kJ/kg