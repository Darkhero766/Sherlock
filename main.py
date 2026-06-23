import streamlit as st



stage = "Home"
 
if "stage" not in st.session_state:
    st.session_state.stage = "Home"


def case():
    st.title("Nightmare Diaries\n")
    if st.button("Case 1 : Murder of Street beggger"):
        st.session_state.stage = "case1"
    if st.button("Case 2 : Murder of Emily White"):
        st.session_state.stage ="case2"

    if st.button("Case 3 : Missing of Angelina "):
        st.session_state.stage = "case3"


def emily():
    st.title("Case 2")
    st.header("Murder of Emily White")

    st.subheader("Victim")
    st.caption("A old begger known by Mr. Grey found death beneath the railway bridge.. ")


def angelina():

    pass

def begger():
    st.title("Case 1")
    st.header("Murder of 'Normal' begger")
    st.subheader(" A old bgeer known by Mr. Grey found dead beneath the railway bridge..")

    if st.button("Examin the body"):
        pass
    
    elif st.button("Investigate Crime scene")


    




if st.session_state.stage == "Home":
    case()

elif st.session_state.stage == "case1" :
    begger()

elif st.session_state.stage == "case2":
    emily()

elif st.session_state.stage == "case3":
    angelina()




