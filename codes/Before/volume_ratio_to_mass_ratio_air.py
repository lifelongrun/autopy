# do the calculation for transforming from volume ratio to mass ratio.


# prerequisites (density unit kg/m3 at condition of 1 atm, 298.15 K)
# -----用来转换空气体积至质量分数

density_o2 = 1.292
density_n2 = 0.694
volume_ratio_o2 = 0.21
volume_ratio_n2 = 0.79

# calculation

o2_in_mass_frac = density_o2*volume_ratio_o2/(density_o2*volume_ratio_o2+density_n2*volume_ratio_n2)

n2_in_mass_frac = 1 - o2_in_mass_frac

print(f"The transformed results is :\n"
      f"{o2_in_mass_frac:.4f} (O2 in mass fraction);{n2_in_mass_frac:.4f} (N2 in mass fraction)\n"
      )