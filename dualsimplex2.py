from scipy.optimize import linprog
import numpy
import streamlit as st
st.title("Linear Programming Problem - Dual Simplex Method")

st.markdown('''
Enter the constraints by converting them to `<=` format

Example:

    8x1 + 8x2 <= 80 is entered as 8,8 where as
    8x1 + 8x2 >= 80 is entered as -8,-8
''')

st.write("Check this box for maximization problems")
maxi = st.checkbox("Maximization")

c = st.text_input("Enter the objective function", value="12,16").split(',')

for i in range(len(c)):
    c[i] = int(c[i])
 
c = numpy.array(c)
if maxi:
    c *= -1 # negate the objective coefficients
else:
    c = c

eq1 = st.text_input("Enter the eqn2 : ", value="10,20").split(',')
eq2 = st.text_input("Enter the eqn2 : ", value="8,8").split(',')
A = [eq1, eq2]

sol = st.text_input("Enter the sol : ", value="120,80").split(',')
b = sol

x0_bnds = (0, None)
x1_bnds = (0, None)
res = linprog(c, A, b, bounds=(x0_bnds, x1_bnds), method='highs-ds')

if maxi:
    st.write("Objective = {}".format(res.get('fun') * -1)) # don't forget to retransform your objective back!
else:
    st.write("Objective = {}".format(res.get('fun') * -1)) # don't forget to retransform your objective back!
st.write("Optimal Solution = {}".format(res.get('x')))
# st.write(res['message'])
# st.write(res)
