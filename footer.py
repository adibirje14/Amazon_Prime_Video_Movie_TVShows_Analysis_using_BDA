import streamlit as st

def display_footer():
    st.markdown(
        """
        <style>
            .footer {
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                background-color: #f5f5f5;
                text-align: center;
                padding: 10px;
                font-size: 14px;
                color: #333;
            }
        </style>
        <div class="footer">
            Made by Gaurang ,Soham, Aditya, Sumit
        </div>
        """,
        unsafe_allow_html=True
    )
