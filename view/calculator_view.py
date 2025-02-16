import streamlit as st

class CalculatorView:
    def __init__(self):
        self.display = st.empty()

    def display_ui(self):
        st.title("Scientific Calculator")
        st.write("A realistic Casio-style scientific calculator")

        self.display.text_input("", st.session_state.get("current_input", ""), disabled=True, key="display")

        buttons = [
            '7', '8', '9', '/', '√',
            '4', '5', '6', '*', 'sin',
            '1', '2', '3', '-', 'cos',
            '0', '.', '=', '+', 'tan',
            'C', 'log', 'ln', '^'
        ]

        cols = st.columns(5)
        for i, button in enumerate(buttons):
            with cols[i % 5]:
                if st.button(button, key=f"btn_{button}", use_container_width=True):
                    st.session_state.button_clicked = button