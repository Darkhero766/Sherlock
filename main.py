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

    menu()

    

def body():
        st.subheader("Eveyone beleived that he was just a poor begger but in investigation we have found that the man posses a gold poclet watch engraved with sign 'A.W' .. and. a Key to a safe ....")
        st.subheader("Investigation reveals that Mr. grey was a before Arthur A wealthy businessman who dissappears 20 years ago.")

        if st.button("Return to menu"):
            menu()

def c_scene():
        st.subheader("Blood is spilled everywhere beneath the bridge and there is a knife without any fingerprints... ")

        if st.button("Return to menu "):
            menu()

def suspect():
        if st.button("1. Jack Miller (Former partner)"):
            jack()

        if st.button("2. Sarah (estrangled daughter)"):
            pass
        if st.button("3. Ethan brooks (investigate journalist)"):
            pass

        if st.button("4. Fathee thomas (local priest )"):
            pass

def jack():
        st.subheader("Jack Miller")

        st.markdown("Age : 68 ")
        st.markdown("Former business partner")

        st.markdown("Current CEO of whitmore indutries.")
        st.markdown("Clue : Arthru return would destroy everything jack built ")

        st.markdown("Secret : He forged documents to steal company")

def menu():
        if st.button("Examin the body"):
           
           st.session_state.stage = "body"
    
        if st.button("Investigate Crime scene"):
           st.session_state.stage = "c_scene"

        if st.button("Questions the suspects."):
           st.session_state.stage = "suspect"

    



    




if st.session_state.stage == "Home":
    case()

elif st.session_state.stage == "case1" :
    begger()

elif st.session_state.stage == "case2":
    emily()

elif st.session_state.stage == "case3":
    angelina()

elif st.session_state.stage == "suspect":
     suspect()




