import streamlit as st
import numpy as np
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram
def main():
    st.title("Quantum State Representation and Measurement")

    st.header("1. Represent Qubit State Vector")
    st.subheader("Enter the coefficients for ket0:")
    alpha0 = st.number_input("Enter the coefficient for |0> (alpha):", value=0.0, key="alpha0", format="%f")
    beta0 = st.number_input("Enter the coefficient for |1> (beta):", value=1.0, key="beta0", format="%f")
    state_vector = np.array([alpha0, beta0])
    st.write("Qubit state vector notation of ket0:")
    st.latex(r"\begin{pmatrix} " + f"{alpha0} \cr {beta0} \cr " + r" \end{pmatrix}")
    
    st.subheader("Enter the coefficients for ket1:")
    alpha1 = st.number_input("Enter the coefficient for |0> (alpha):", value=1.0, key="alpha1", format="%f")
    beta1 = st.number_input("Enter the coefficient for |1> (beta):", value=0.0, key="beta1", format="%f")
    state_vector = np.array([alpha1, beta1])
    st.write("Qubit state vector notation of ket1:")
    st.latex(r"\begin{pmatrix} " + f"{alpha1} \cr {beta1} \cr " + r" \end{pmatrix}")

    st.header("2. Define and Display State Vectors")
    st.subheader("Define State Vectors")
    
    st.subheader("Enter the coefficients for Custom Vector:")
    x_alpha0 = st.number_input("Enter the coefficient for |0> (alpha):", value=0.8, key="x_alpha0", format="%f")
    x_beta0 = st.number_input("Enter the coefficient for |1> (beta):", value=0.6, key="x_beta0", format="%f")
    x = Statevector([x_alpha0, x_beta0])
    st.write("displaying statevector of Custom Vector:")
    st.latex(r"\begin{pmatrix} " + f"{x_alpha0} \cr {x_beta0} \cr " + r" \end{pmatrix}")
    st.latex(r"| \psi \rangle = " + f"{x_alpha0:.2f}" +r" | 0 \rangle +" +f"{x_beta0:.2f}" +r" | 1 \rangle")
    st.latex(x.draw('text'))
    
    custom_state = x
    st.subheader("Check Vector Validity")
    is_valid = custom_state.is_valid()
    st.write(f"Is the custom state vector valid?:\t {is_valid}")
    if not is_valid:
        st.warning("The custom state vector is not valid. Make sure |alpha|^2 + |beta|^2 = 1")

    st.header("3. Simulate Measurements")
    if is_valid:
        st.write("Measurement :")        
        st.write(x.measure())
        
        num_samples = st.slider("Number of measurements:", min_value=100, max_value=10000, value=1000, step=100)        
        statistics = x.sample_counts(num_samples)
        st.write("Statistics :")        
        st.write(statistics)
        st.pyplot(plot_histogram(statistics))
if __name__ == "__main__":
    main()