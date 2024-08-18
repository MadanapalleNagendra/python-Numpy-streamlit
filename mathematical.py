import numpy as np
import streamlit as st

st.title('Mathematical Calculator for Complex Functions')

# Sidebar for selecting operations
operation = st.sidebar.selectbox(
    'Select Operation',
    ['Matrix Multiplication', 'Matrix Inversion', 'Eigenvalues', 'Numerical Integration', 'Optimization']
)
if operation == 'Matrix Multiplication':
    st.subheader('Matrix Multiplication')

    # Input for matrix A
    st.text('Enter matrix A (comma-separated values for each row):')
    matrix_a = st.text_area('Matrix A', '1,0\n0,1')
    matrix_a = np.array([list(map(float, row.split(','))) for row in matrix_a.split('\n')])

    # Input for matrix B
    st.text('Enter matrix B (comma-separated values for each row):')
    matrix_b = st.text_area('Matrix B', '1,0\n0,1')
    matrix_b = np.array([list(map(float, row.split(','))) for row in matrix_b.split('\n')])

    # Compute multiplication
    if st.button('Compute'):
        try:
            result = np.dot(matrix_a, matrix_b)
            st.write('Result:')
            st.write(result)
        except ValueError as e:
            st.error(f'Error: {e}')
elif operation == 'Matrix Inversion':
    st.subheader('Matrix Inversion')

    # Input for matrix
    st.text('Enter matrix (comma-separated values for each row):')
    matrix = st.text_area('Matrix', '1,0\n0,1')
    matrix = np.array([list(map(float, row.split(','))) for row in matrix.split('\n')])

    # Compute inversion
    if st.button('Compute'):
        try:
            result = np.linalg.inv(matrix)
            st.write('Result:')
            st.write(result)
        except np.linalg.LinAlgError as e:
            st.error(f'Error: {e}')
elif operation == 'Eigenvalues':
    st.subheader('Eigenvalue Calculation')

    # Input for matrix
    st.text('Enter matrix (comma-separated values for each row):')
    matrix = st.text_area('Matrix', '1,0\n0,1')
    matrix = np.array([list(map(float, row.split(','))) for row in matrix.split('\n')])

    # Compute eigenvalues
    if st.button('Compute'):
        try:
            eigenvalues, _ = np.linalg.eig(matrix)
            st.write('Eigenvalues:')
            st.write(eigenvalues)
        except np.linalg.LinAlgError as e:
            st.error(f'Error: {e}')
elif operation == 'Numerical Integration':
    st.subheader('Numerical Integration')

    # Input for function
    function_str = st.text_area('Function', 'np.sin(x)')
    function = lambda x: eval(function_str, {'np': np, 'x': x})

    # Input for integration limits
    a = st.number_input('Lower limit', value=0.0)
    b = st.number_input('Upper limit', value=1.0)

    # Compute integration
    if st.button('Compute'):
        from scipy.integrate import quad
        result, error = quad(function, a, b)
        st.write('Result:')
        st.write(result)
        st.write('Error estimate:')
        st.write(error)
elif operation == 'Optimization':
    st.subheader('Optimization')

    # Input for function
    function_str = st.text_area('Objective Function', 'x**2 - 4*x + 4')
    function = lambda x: eval(function_str, {'x': x})

    # Input for initial guess
    x0 = st.number_input('Initial Guess', value=0.0)

    # Compute optimization
    if st.button('Compute'):
        from scipy.optimize import minimize
        result = minimize(function, x0)
        st.write('Optimal Value:')
        st.write(result.fun)
        st.write('Optimal Parameters:')
        st.write(result.x)
        st.write('Success:')
        st.write(result.success)
        st.write('Message:')
        st.write(result.message)
