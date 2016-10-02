import math

def moment_calc(Type):
    Type = Type.lower()

    if Type == "Bending moment of Beam with only UDL" or Type == "1" or Type == "UDL":
        bending_moment1()
        deflection1()

    elif Type == "Bending Moment of Beam with UDL and Point Load" or Type == "2" or Type == "UDL + Point":
        bending_moment2()
        print("The Deflection calculation is below: ")
        deflection2()

    else:
        print("Enter UDL or UDL + Point Load")

def bending_moment1():

    UDL_Load = float(input("Enter the distributed load on beam: "))
    Beam_Length = float(input("Enter the length of the beam: "))
    Beam_UDL = ((UDL_Load) * (Beam_Length ** 2)) / 8

    print ("The Bending Moment of the Beam is {}kN.m ".format(Beam_UDL))

def bending_moment2() : #Calculation for beam with a UDL and Point Load.

    UDL_Load = float(input("Enter the distributed load on beam: "))
    Beam_Length = float(input("Enter the length of the beam: "))
    Point_Load = float(input("Enter the point Load applied to beam: "))
    Beam_UDL_PointLoad = ((UDL_Load) * (Beam_Length ** 2)) / 8 + (((Point_Load * Beam_Length)) / 4)

    print("The Bending Moment of the Beam is {}kN.m ".format(Beam_UDL_PointLoad))

def deflection1():

    UDL_Load = float(input("Enter the distributed load on beam "))
    Beam_Length = float(input("Enter the length of the beam in mm: "))
    mof = float(input("Enter Moment of Inertia of beam in cm^4: "))
    e = float(input("Enter Modulus of Elasticity of beam in N/mm^2: "))
    beam_deflec  = (5 * UDL_Load * Beam_Length **4)/(e*mof*384*10000)
    print("The deflection of the Beam is {}mm ".format(beam_deflec))

def deflection2():
    UDL_Load = float(input("Enter the distributed load on beam: "))
    Point_load = float(input("Enter Point Load on beam: "))
    Beam_Length = float(input("Enter the length of the beam in mm: "))
    mof = float(input("Enter Moment of Inertia of beam in cm^4: "))
    e = float(input("Enter Modulus of Elasticity of beam in N/mm^2: "))
    beam_deflection = (5 * UDL_Load * Beam_Length ** 4) / (e * mof * 384 * 10000) + (Point_load *1000* Beam_Length ** 3) / (e * mof * 48 * 10000)
    print("The deflection of the Beam is {}mm ".format(beam_deflection))

def main():

    calculation_type = input("Calculate Bending Moment and Deflection of Beam with UDL only(Type 1) or UDL + Point Load(Type 2): ")
    moment_calc(calculation_type)




main()