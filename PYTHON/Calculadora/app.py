# 1) https://pypi.org/project/streamlit/      pip install streamlit

# 2) Terminal: cd PYTHON/Calculadora > streamlit run app.py


# 3) Welcome to Streamlit! / You can now view your Streamlit app in your browser.
        # Local URL: http://localhost:8501
        # Network URL: http://100.126.10.200:8501

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
import streamlit as st
import streamlit.components.v1 as components

# Custom CSS Styling
st.markdown(
    """
<style>
    
</style>
    """,
    unsafe_allow_html=True,
)

# Calculator Logic (Moved to Python)
def append_to_result(value):
    st.session_state.result += value

def calculate_result():
    try:
        st.session_state.result = str(eval(st.session_state.result))
    except Exception:
        st.session_state.result = "Error"

def clear_result():
    st.session_state.result = ""

# Streamlit App Layout
if 'result' not in st.session_state:  # Initialize the result
    st.session_state.result = ""

# Display the calculator result in a text input
st.text_input(
    label="",  # No label needed for the display
    value=st.session_state.result,
    key="result",  # Key for session state
    disabled=True,  # Make the input readonly
)

# Create the calculator buttons with Streamlit
col1, col2, col3, col4 = st.columns(4)  # Create four columns for buttons
with col1:
    st.button("AC", key="AC", on_click=clear_result, use_container_width=True)
    st.button("7", key="7", on_click=append_to_result, args=('7',), use_container_width=True)
    st.button("4", key="4", on_click=append_to_result, args=('4',), use_container_width=True)
    st.button("1", key="1", on_click=append_to_result, args=('1',), use_container_width=True)
    st.button("0", key="0", on_click=append_to_result, args=('0',), use_container_width=True)
with col2:
    st.button("8", key="8", on_click=append_to_result, args=('8',), use_container_width=True)
    st.button("5", key="5", on_click=append_to_result, args=('5',), use_container_width=True)
    st.button("2", key="2", on_click=append_to_result, args=('2',), use_container_width=True)
    st.button(".", key="dot", on_click=append_to_result, args=('.',), use_container_width=True)
with col3:
    st.button("9", key="9", on_click=append_to_result, args=('9',), use_container_width=True)
    st.button("6", key="6", on_click=append_to_result, args=('6',), use_container_width=True)
    st.button("3", key="3", on_click=append_to_result, args=('3',), use_container_width=True)
    st.button("=", key="equals", on_click=calculate_result, use_container_width=True)
with col4:
    st.button("Div", key="div", on_click=append_to_result, args=('/',), use_container_width=True)
    st.button("Mul", key="mul", on_click=append_to_result, args=('*',), use_container_width=True)
    st.button("Sub", key="sub", on_click=append_to_result, args=('-',), use_container_width=True)
    st.button("Add", key="add", on_click=append_to_result, args=('+',), use_container_width=True)