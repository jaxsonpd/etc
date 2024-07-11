## 
# @file q1-std-atmospheric-cond-calc.py
# @author Jack Duignan (Jdu80@uclive.ac.nz)
# @date 2024-07-11
# @brief This program provides functionality to calculate the standard 
# atmospheric conditions for every 1000 [m] in altitude from 0[m] to 30000 [m] 
# or 100000 [ft] (The temperature in the troposphere and Stratosphere (
# +36000[ft] or + 11000[m]))
# 
# Assumptions:
# Temperature drops linearly in troposphere (T_alt = T_SL - Lh)
# with a lapse rate of L = 3.56^o R / 1000 [ft] = 6.5^o K / 1000 [m]
# 
# Temperature is constant in the lower part of the stratosphere (up to
# 30000 [m])
# 
# Using standard conditions of P_SL = 1.013e5 [Pa] = 2116 [lb]/[ft]^2,
# \rho_SL = 1.23 [kg]/[m]^3 = 0.002378 [sl]/[ft]^3, T_SL = 288^o K 
# = 520^o R, and T_stratosphere = 216.5^o K = 389.99^o R
#
# A universal gas constant of R = 8.314 [J/k mol] = 53.5 [ft-lb/lb R]
#
# Derivation:
# Using the following equations:
# Perfect Gas equation: P = \rho R T
# Hydrostatic equation dP = - \rho g dh
# 
# They can be re-arranged to eliminate density:
# dP / P = - (g/RT) dh
#
# Thus for the troposphere:
# P_alt = ((T_SL - Lh)/T_SL)^(g/LR) P_SL
# \rho_alt = ((T_SL - Lh)/T_SL)^((g-LR)/LR) \rho_SL
#
# and for the stratosphere:
# P_2 / P_1 = \rho_2 / \rho_1 = e^(g(h_1 - h_2)/RT)

from math import exp

g = 9.81 # [m/s^2]

# Constants metric
T_SL_m = 288 # [K]
T_strat_m = 273 - 56.5 # [K]

P_SL_m = 1.013e5 # [Pa]
P_1_strat_m = 22610 # [Pa]

rho_SL_m = 1.23 # [kg/m^3]
rho_1_strat_m = 0.364 # [kg/m^3]

R_m = 287 # [J/K kg]
L_m = 6.5/1000 # [K/m]
K_to_C_m = 273 # [K]

# Max heights of atmospheric layers
h_troposphere_e = 36000 # [ft]
h_stratosphere_e = 100000 # [ft]
h_troposphere_m = 11000 # [m]
h_stratosphere_m = 30000 # [m]

def calc_troposphere(h: int, R: float, L: float, T_SL: float, P_SL: float, rho_SL: float) -> tuple[float, float]:
    """
    Calculate the density and pressure at the given h for the troposphere

    ### Params:
    h : int
        The height to calculate values at
    R : float
        The gas constant for the fluid
    L : float
        The lapse rate
    T_SL : float
        The temperature at sea level
    P_SL : float
        The pressure at sea level
    rho_SL : float
        The density at sea level

    ### Returns:
    out : float
        The pressure at the given altitude
    out : float
        The density at the given altitude
    out : float
        The temperature at the given altitude
    """
    if (h < 0):
        raise Exception("height value out of range")
    
    temp = (T_SL - L * h)
    pressure = (temp/T_SL)**(g/(L*R)) * P_SL
    density = (temp/T_SL)**((g - L*R)/(L*R)) * rho_SL

    return (pressure, density, temp)

def calc_stratosphere(h: int, R: float, T: float, P_1: float, rho_1: float) -> tuple[float, float]:
    """
    Calculate the density and pressure at the given h for the stratosphere

    ### Params:
    h : int
        The height distance from h_1 to h_2 (h_1 - h_2) (will be negative)
    R : float
        The gas constant for the fluid
    T : float
        The temperature at in the lower stratosphere
    P_1 : float
        The pressure at h_1
    rho_1 : float
        The density at h_1

    ### Returns:
    out : float
        The pressure at the given altitude
    out : float
        The density at the given altitude
    """
    if (h > 0):
        raise Exception("height value out of range")

    pressure = exp(g*h/(R*T)) * P_1
    density = exp(g*h/(R*T)) * rho_1

    return (pressure, density)

def calc_std_conditions_metric(h1: int = 0, h2: int = 30000):
    """
    Calculate the standard atmospheric conditions from h1 to h2
    
    ### Params:
    h1 : int = 0
        The initial height
    h2 : int = 30000
        The final height
    """
    if (h1 > h2):
        raise Exception("height 1 is greater than height 2")
    if (h1 < 0):
        raise Exception("Height 1 must be positive")
    
    first_time_tropo = True
    first_time_strato = True

    print(f"Metric Standard Atmospheric")
    print(f"Conditions from {h1} to {h2}")
    print()
    for h in range(h1, h2+1, 1000):
        if (h <= h_troposphere_m):
            if (first_time_tropo):
                print("========= Troposphere ==========")
                print("h [m] T [K] P [kPa] rho [kg/m^3]")
                first_time_tropo = False

            pressure, density, temp = calc_troposphere(h, R_m, L_m, T_SL_m, P_SL_m, rho_SL_m)
            print(f"{h:5.0f} {temp-K_to_C_m:5.1f}  {pressure*10**(-3):6.2f}   {density:6.4f}")

        elif (h <= h_stratosphere_m):
            if (first_time_strato):
                print("========= Stratosphere =========")
                print("h [m] T [C] P [kPa] rho [kg/m^3]")
                first_time_strato = False

            pressure, density = calc_stratosphere(h_troposphere_m - h, R_m, T_strat_m, P_1_strat_m, rho_1_strat_m)
            print(f"{h:5.0f} {T_strat_m-K_to_C_m:5.1f} {pressure*10**(-3):6.2f}    {density:6.4f}")
            

            

            
    
calc_std_conditions_metric()
