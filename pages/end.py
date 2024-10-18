import streamlit as st

st.set_page_config(initial_sidebar_state="collapsed" )


st.markdown(
    """


	&nbsp;&nbsp;
    The END !
	&nbsp;&nbsp;
    &nbsp;&nbsp;


    """
)


st.markdown("""---""")



if st.button("Back"):
    st.switch_page("Subjective_Experiment.py")
