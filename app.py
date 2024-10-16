import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Input fields for two numbers
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

# Dropdown menu to select the operation
operation = st.selectbox("Choose an operation", ("Add", "Subtract", "Multiply", "Divide"))

# Perform calculation based on the selected operation
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
        st.success(f"The result is: {result}")
    elif operation == "Subtract":
        result = num1 - num2
        st.success(f"The result is: {result}")
    elif operation == "Multiply":
        result = num1 * num2
        st.success(f"The result is: {result}")
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
            st.success(f"The result is: {result}")
        else:
            st.error("Division by zero is not allowed")

# Instructions for deploying the app on Streamlit Cloud:
st.write("To deploy this app, save this code in a file (e.g., `calculator.py`) and run the following command:")
st.code("streamlit run calculator.py")
