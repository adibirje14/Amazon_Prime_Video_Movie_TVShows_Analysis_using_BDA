# dark_mode.py

import streamlit as st

def toggle_dark_mode():
    """Toggle dark mode functionality."""
    if 'dark_mode' not in st.session_state:
        st.session_state.dark_mode = False

    dark_mode = st.sidebar.checkbox("Enable Dark Mode", value=st.session_state.dark_mode)

    # Update session state when the checkbox is toggled
    if dark_mode != st.session_state.dark_mode:
        st.session_state.dark_mode = dark_mode

    # Set styles based on the dark mode toggle
    if st.session_state.dark_mode:
        st.markdown("""
        <style>
            .reportview-container {
                background: #1e1e1e;
                color: white;
            }
            .sidebar .sidebar-content {
                background: #2e2e2e;
                color: white;
            }
        </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <style>
            .reportview-container {
                background: #f5f5f5;
                color: black;
            }
            .sidebar .sidebar-content {
                background: #ffffff;
                color: black;
            }
        </style>
        """, unsafe_allow_html=True)


