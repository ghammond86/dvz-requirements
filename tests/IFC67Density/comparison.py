import h5py
import numpy as np

A0 = 6.824687741e3
A1 = -5.422063673e2
A2 = -2.096666205e4
A3 = 3.941286787e4
A4 = -6.733277739e4
A5 = 9.902381028e4
A6 = -1.093911774e5
A7 = 8.590841667e4
A8 = -4.511168742e4
A9  = 1.418138926e4
A10 = -2.017271113e3
A11 = 7.982692717e0
A12 = -2.616571843e-2
A13 = 1.522411790e-3
A14 = 2.284279054e-2
A15 = 2.421647003e2
A16 = 1.269716088e-10
A17 = 2.074838328e-7
A18 = 2.174020350e-8
A19 = 1.105710498e-9
A20 = 1.293441934e1
A21 = 1.308119072e-5
A22 = 6.047626338e-14

a1 = 8.438375405e-1
a2 = 5.362162162e-4
a3 = 1.720000000e0
a4 = 7.342278489e-2
a5 = 4.975858870e-2
a6 = 6.537154300e-1
a7 = 1.150000000e-6
a8 = 1.510800000e-5
a9 = 1.418800000e-1
a10 = 7.002753165e0
a11 = 2.995284926e-4
a12 = 2.040000000e-1

AlistDocSTOMP = np.array ([A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16, 
            A17, A18, A19, A20, A21, A22])
AlistCodePFLO = np.array([6.824687741e3, -5.422063673e2, -2.096666205e4, 3.941286787e4, -6.733277739e4,
        9.902381028e4, -1.093911774e5, 8.590841667e4, -4.511168742e4, 1.418138926e4, -2.017271113e3,
        7.982692717e0, -2.616571843e-2, 1.522411790e-3, 2.284279054e-2, 2.421647003e2, 1.269716088e-10,
        2.074838328e-7, 2.174020350e-8, 1.105710498e-9, 1.293441934e1, 1.308119072e-5, 6.047626338e-14])
diffA = AlistCodePFLO - AlistDocSTOMP
print(diffA)

alistDocSTOMP = np.array ([a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12])
alistCodePFLO = np.array([ 8.438375405e-1, 5.362162162e-4, 1.720000000, 7.342278489e-2,
                        4.975858870e-2, 6.537154300e-1, 1.150000000e-6, 1.510800000e-5,
                        1.418800000e-1, 7.002753165, 2.995284926e-4, 2.040000000e-1])
diffa = alistCodePFLO - alistDocSTOMP
print(diffa)

# vcwSTOMP = 57.1075
# WTMW = 18.015

vcw = 0.00317
TABS = 273.15
TCRW = 647.3  # same as PFLOTRAN

T = np.array([10, 15, 25, 35, 55])
T = (T + TABS) / TCRW

PCRW = 22.064e6 # same as PFLOTRAN; STOMP: 221.2e5  # 22.064e6
P = np.array([101325, 5e5, 1e6, 2e6, 5e6])
P = P/PCRW

FMWH2O = 18.01534

rho = np.zeros(len(T) * len(P))
rhoPFLO = np.zeros(len(T) * len(P))
count = 0

for Prw in P:
    for Trw in T:
        Y = 1 - a1 * Trw ** 2. - a2 * Trw ** -6.
        zterm = a3* Y ** 2. - 2. * a4 * Trw + 2. * a5 * Prw
        Z = Y + zterm ** (1./2.)

        yy = 1 - a1*Trw ** 2. - a2 * Trw ** (-6.)
        xx = (a3*yy*yy - 2.0 * (a4*Trw-a5*Prw)) ** (1./2.)
        zz = xx + yy

        line1 = A11 * a5 * Z ** (-5./17.) + A12 + A13 * Trw + A14 * Trw ** 2.
        line2 = A15 * (a6 - Trw) ** 10. + A16 * (a7 + Trw ** 19) ** -1.
        line3 = (a8 + Trw ** 11) ** -1. * (A17 + 2. * A18 * Prw + 3. * A19 * Prw ** 2)
        line4 = A20 * Trw ** 18 * (a9 + Trw ** 2.) * (-3. * (a10 + Prw) ** -4 + a11)
        line5 = 3 * A21 * (a12 - Trw) * Prw ** 2. + 4. * A22 * Trw ** -20. * Prw **3 

        vr = line1 + line2 -line3 - line4 + line5
        rho[count] = 1. / (vcw * vr)


        vrPFLO = A11 * a5 * zz ** (-5./17.) \
            + A12 + Trw * (A13 + A14 * Trw) \
        + A15 * (a6-Trw) ** 9. *(a6-Trw) \
        + A16 * 1./(a7 + Trw ** 19.) \
        - 1 /(a8 +Trw ** 11.) * (A17 +(2. * A18+ 3. * A19 * Prw) * Prw) \
        - (a11-3*((a10+Prw)**(-4.))) * (A20 * Trw ** 18. *(a9 + Trw ** 2.)) \
        + (3 * A21 * (a12-Trw) + 4 * A22 * Prw / Trw ** 20.)* Prw ** 2.

        # vr = u1+aa(12)+theta*(aa(13)+aa(14)*theta)+u8*(a6-theta) &
        # +aa(16)*u4-u2*u3-u6*u7+(three*aa(21)*(a12-theta) &
        # +four*aa(22)*beta/theta20)*beta2x

        rhoPFLO[count] = 1. / (vrPFLO * vcw)

        count += 1
    
filename = "test-eos67.h5"

def printname(name):
    print(name)

with h5py.File(filename, "r+") as f:
    # f.visit(printname)
    index_string = 'Time:  0.00000E+00 d/Liquid_Density [kg_m^3]'
    pflotranDensity = np.array(f[index_string], '=f8')

pflotranDensityLine = np.reshape(pflotranDensity, (25,), 'F')

# print("coded in STOMP: ")
# print(rho)
# print("PFLOTRAN run: ")
print(pflotranDensityLine)
# print("PFLOTRAN coded: ")
# print(rhoPFLO)

# relErrorPFLO = abs(rhoPFLO - pflotranDensityLine)/rhoPFLO
# print("print rel error PFLO")
# print(relErrorPFLO)

relError = abs(rho - pflotranDensityLine)/rho
print("print rel error coded Stomp vs. PFLO run")
print(relError)

# relErrorCoded = abs(rho - rhoPFLO)/rho
# print("print rel error Stomp vs. PFLO coded")
# print(relErrorCoded)

tol = 1e-6
if any (e > tol for e in relError):
    print("Failed")
else:
    print("Passed")