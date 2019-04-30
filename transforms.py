import sympy
from sympy import *

init_printing()
DR, L1, L2, L3, theta1, theta2, theta3 = symbols('DR L1 L2 L3 theta1, theta2, theta3')
print(DR)

#u_T_r   = Matrix([[1, 0, DR],[0, 1, 0],[0, 0, 1]])
#r_T_j0  = Matrix([[0, -1, 0],[1, 0, 0],[0, 0, 1]]) # Rotate -90 
#j0_T_j1 = Matrix([[1, 0, L1],[0, 1, 0],[0, 0, 1]]) 
#j1_T_j2 = Matrix([[1, 0, L2],[0, 1, 0],[0, 0, 1]])
#j2_T_j3 = Matrix([[0, -1, 0],[1, 0, 0],[0, 0, 1]])
#j3_T_h = Matrix([[1, 0, L3],[0, 1, 0],[0, 0, 1]])

u_T_r   = Matrix([[1, 0, DR],[0, 1, 0],[0, 0, 1]])
r_T_j0  = Matrix([[cos(theta1), sin(theta1), 0],[-sin(theta1), cos(theta1), 0],[0, 0, 1]]) # Rotate -90 
j0_T_j1 = Matrix([[cos(theta2), sin(theta2), L1],[-sin(theta2), cos(theta2), 0],[0, 0, 1]]) 
j1_T_j2 = Matrix([[cos(theta3), sin(theta3), L2],[-sin(theta3), cos(theta3), 0],[0, 0, 1]])
j2_T_h  = Matrix([[1, 0, L3],[0, 1, 0],[0, 0, 1]])


u_T_h  = u_T_r * r_T_j0 * j0_T_j1 * j1_T_j2 * j2_T_h


l1 = latex(u_T_r)
l2 = latex(r_T_j0)
l3 = latex(j0_T_j1)
l4 = latex(j1_T_j2)
l5 = latex(j2_T_h)
l6 = latex(u_T_h) 

latex_list = [l1, l2, l3, l4, l5, l6]
with open("out.tex", "w") as f:
    for l in latex_list:
        f.write(l + "\n\n\n")

    

#l7 = latex(u_T_h.subs([(theta1, -pi/2),(theta2, 0), (theta3, -pi/2)]).evalf()) 
#print(latex(u_T_h.subs([(theta1, -pi/2),(theta2, 0), (theta3, -pi/2)]).evalf()))
