import streamlit as st
from controller.calculator_controller import CalculatorController
from view.calculator_view import CalculatorView

def main():
    view = CalculatorView()
    controller = CalculatorController()

    if "current_input" not in st.session_state:
        st.session_state.current_input = ""

    # Display the UI
    view.display_ui()

    if "button_clicked" in st.session_state:
        st.session_state.current_input = controller.handle_input(
            st.session_state.button_clicked, st.session_state.current_input
        )
        del st.session_state.button_clicked

if __name__ == "__main__":
    main()