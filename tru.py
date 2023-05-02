import streamlit as st;
st.header("TRUTH TABLE FOR LOGICAL GATES")
# Operation = st.text_input('Enter Operation to be performed AND, OR, NAND, XOR, NOT, NOR and XNOR')
# st.write("Resultant Table : ", Operation)



def truthTable(expression,inputs=2):
  st.write("Boolean Expression:")
  st.write("  X = " + expression.upper())
  expression = expression.lower()
  
  #replace Boolean Operators with bitwise operators
  expression = expression.replace("and","&")
  expression = expression.replace("xor","^")
  expression = expression.replace("or","|")
  expression = expression.replace("not","~")
  
  st.write("\nTruth Table:")
  if inputs==2:
    
    # st.write("  -------------")
    st.write("  | A | B | X |")
    # st.write("  -------------")
    
    for a in range(0,2):
      for b in range(0,2):
        x = eval(expression)
        st.write("  | " + str(a) + " | " + str(b) + " | " + str(x) + " |" )
        # st.write("  -------------")
    st.write("------------------------")    
  elif inputs==3:
    
    # st.write("  -----------------")
    st.write("  | A | B | C | X |")
    # st.write("  -----------------")
    
    for a in range(0,2):
      for b in range(0,2):
        for c in range(0,2):
          x = eval(expression)
          st.write("  | " + str(a) + " | " + str(b) + " | " + str(c) + " | " + str(x) + " |" )
          # st.write("  -----------------")
    st.write("------------------------")       
    
  elif inputs==4:
    # st.write("  ---------------------")
    st.write("  | A | B | C | D | X |")
    # st.write("  ---------------------")
    
    for a in range(0,2):
      for b in range(0,2):
        for c in range(0,2):
          for d in range(0,2):
            x = eval(expression)
            st.write("  | " + str(a) + " | " + str(b) + " | " + str(c) + " | " + str(d) + " | " + str(x) + " |" )
            # print("  ---------------------")
    st.write("------------------------") 
##############################################
expression = "A AND B "
truthTable(expression,2)

expression = "A AND B AND C"
truthTable(expression,3)

expression = "A AND B AND C AND D"
truthTable(expression,4)
