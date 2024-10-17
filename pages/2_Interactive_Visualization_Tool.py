import streamlit as st
from pygwalker.api.streamlit import StreamlitRenderer

def main():
    # Config streamlit interface
    st.set_page_config(
        page_title="Interactive Visualization Tool",
        page_icon="📈",
        layout="wide")
   
    st.header("📈 Interactive visualization tool")
    st.write(
        "### Welcome to our plot analysis tool. This tools can assist your daily plot visualization tasks. Please enjoy !"
    )

    if st.session_state.get("df") is not None:
        pyg_app = StreamlitRenderer(st.session_state.df)
        pyg_app.explorer()
    else:
        st.info("Please upload the dataset in order to proceed this tool")
    # render pygwalker


if __name__ == "__main__":  
    main()