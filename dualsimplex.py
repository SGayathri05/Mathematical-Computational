import numpy as np
import scipy as sp
from scipy.optimize import linprog


import streamlit as st
import re
tc = int(st.number_input("Enter no of total constraints"))
sign=st.selectbox("Choose the optimisation problem type",('MAX Z', 'MIN Z'))
#if st.button("enter the data:"):
#collect_numbers = lambda x : [float(i) for i in re.split("[^(-+?0-9\.)]", x) if i != ""]
rx = re.compile(r'-?\d+(?:\.\d+)?')
collect_numbers = lambda x : [float(i) for i in re.split("[^(-?0-9\.)]", x) if i != ""]
obj = st.text_input("PLease enter the objective equation")
#c.append(collect_numbers(obj))
c = collect_numbers(obj)
#st.write(c)
lhs=[]
rhs=[]
ele=[]
j=1
k=2
for i in range(0,tc):
    numbers = st.text_input("PLease enter the equation lhs",key=i)
    #lhs.append(collect_numbers(numbers))
    sign1=st.selectbox("Choose the inequations?",('<=', '>=','='),j)
    ele.append(sign1)
    r1 = st.number_input('PLease enter the equation rhs',key=k)
    if sign1==">=":
        r1=r1*-1
        collect_num = np.multiply(collect_numbers(numbers),-1)
        #st.write(collect_num)
        #st.write(r1)
        lhs.append(collect_num)
        rhs.append(r1)    
    else:
        lhs.append(collect_numbers(numbers))
        rhs.append(r1)#collect_numbers(r1))
    j+=1
    k+=1    
 
if sign == 'MAX Z':
    c=np.multiply(c,-1)
    #st.write(c)
def function_simplex1(c,A,b,sign):
    # define the upper bound and the lower bound
    R = (0, float("inf"))
    T = (0, float("inf"))
    M = (0,float("inf"))
    # Solve the problem by Simplex method in Optimization   bounds=(R, T)
    res = linprog(c, A_ub=A, b_ub=b, method='simplex')#, options={"disp": True}),  # linear programming problem
    #res = linprog(c, A_ub=A, b_ub=b, method='revised simplex')#, bounds=(R,T), options={"disp": True})
    if sign=='MAX Z':
        st.write("Here, multiply -1 with the value returned from the parameter 'fun' to get MAX Z value.")
        #st.write("Max:",round((res.fun*-1),4))
    st.write(sign,":",round((res.fun*-1),4))
    st.write(res)
    #print(res) # print results
if st.button('display ans'):
    function_simplex1(c,lhs,rhs,sign)
