# do the calculation for transforming from volume ratio to mole ratio .

# prerequisites (density unit kg/m3 at condition of 1 atm, 298.15 K)
density_ch4 = 0.65
density_h2 = 0.09
molecular_mass_ch4 = 16
molecular_mass_h2 = 2


v_ch4 = float(input("Please input the fuel of CH4 in vol.% \n(eg: CH4 volume in percent = 50%, please input '0.5'):\n>"))



# calculation
n_ch4_per_cent = (density_ch4*v_ch4/molecular_mass_ch4*v_ch4)/(
        (density_ch4*v_ch4/molecular_mass_ch4*v_ch4)+(density_h2/molecular_mass_h2*(1-v_ch4)
                                                      )
)

m_ch4_per_cent = (density_ch4*v_ch4)/((density_ch4*v_ch4)+(density_h2*(1-v_ch4)))

print(f"The transformed results is :\n"
      f"{n_ch4_per_cent:.4f} (CH4 in mole fraction);{1-n_ch4_per_cent:.4f} (H2 in mole fraction)\n"
      f"{m_ch4_per_cent:.4f} (CH4 in mavolume_ratio_to_mole_ratio.pyss fraction);{1-m_ch4_per_cent:.4f} (H2 in mass fraction) ")