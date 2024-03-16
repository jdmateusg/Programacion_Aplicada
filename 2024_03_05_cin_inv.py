import math

def cin_inv(x3, y3, z3, a1=1, a2=1, a3=3):
    th1 = math.atan2(y3, x3)  # theta 1
    r1 = math.sqrt(x3**2 + y3**2)
    r2 = z3 - a1
    alp2 = math.atan2(r2, r1)  
    r3 = math.sqrt(r1**2 + r2**2)
    alp1 = math.acos(((a3)**2 - (a2)**2 - (r3)**2)/(-2 * a2 * r3))
    th2 = alp2 - alp1  # theta 2
    alp3 = math.acos(((r3)**2 - (a2)**2 - (a3)**2)/(-2 * a2 * a3))
    th3 = math.degrees(180 - alp3) # theta 3
    
    print(th1,th2,th3) 


