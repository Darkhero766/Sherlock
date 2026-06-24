import streamlit as st

clues = []

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

        clues.append("Pocket watch")
        if st.button("Return to menu"):
            menu()

def c_scene():
        st.subheader("Blood is spilled everywhere beneath the bridge and there is a knife without any fingerprints... ")

        if st.button("Return to menu "):
            menu()

def suspect():
        st.subheader(" Select the suspect to investigate")
        if st.button("1. Jack Miller (Former partner)"):
            st.session_state.stage = "jack"

        if st.button("2. Sarah (estrangled daughter)"):
            st.session_state.stage = "sarah"
        if st.button("3. Ethan brooks (investigate journalist)"):
            st.session_state.stage =" ethan"

        if st.button("4. Fathee thomas (local priest )"):
            st.session_state.stage = "father"

def jack():
        st.subheader("Jack Miller")

        st.markdown("Age : 68 ")
        st.markdown("Former business partner")

        st.markdown("Current CEO of whitmore indutries.")
        st.markdown("Clue : Arthru return would destroy everything jack built ")

        st.markdown("Secret : He forged documents to steal company")

        if st.button(" return to suspects"):
             st.session_state.stage = "suspect"

def father ():
     st.subheader("Father Thomas ")
     st.markdown("Age : 61")
     st.markdown("Local priest")

     st.markdown("THE only person who knows arthur real personality")
     st.markdown("Secret : Hidden")
     st.markdown("Motive : He has been hiding from detectives")

def sarah():
     st.subheader("Sarah Whitmore ")
     st.markdown("Age : 40")

     st.markdown("believes that arthur abandoned the family")
     st.markdown("Motivee : Years of resentment")
     st.markdown("SECRET : She recently found out that her father is still alive")

     if st.button("Return to suspects"):
          st.session_state.stage = "suspect"

def ethan():
     st.subheader("Ethan Brooks")
     st.markdown("Age: 35")

     st.markdown("Investigative journalist")
     st.markdown("Has spent years of investigating in Arthur's disappearance")
     st.markdown("Secret : A sensational story could make his career")

     st.markdown("Motive : He secretly met arthur one week before his murder ")
     if st.button("return to suspects"):
          st.session_state.stage = "suspect"

def menu():
        if st.button("Examine the body"):
           
           st.session_state.stage = "body"
        if st.button("Visit Locations"):
             st.session_state.stage = "location"
    
        if st.button("Investigate Crime scene"):
           st.session_state.stage = "c_scene"

        if st.button("Questions the suspects."):
           st.session_state.stage = "suspect"
def location():
     st.subheader("Select the location to investigate")

     if st.button("Bank"):
          st.session_state.stage = "bank"
     if st.button("Shelter"):
          st.session_state.stage = "shelter"

def bank():
     st.subheader("Bank")

     st.markdown("Inside Safety deposit box you found")

     st.markdown("- Ownership paper")

     st.info("'Nothing important found")

     if st.button("Return to locations"):
          st.session_state.stage= "location"

def shelter():
     st.subheader("Shelter")
     st.markdown("You searched arthur's shelter")
     st.markdown("You found")

     st.markdown("- OLD Photographs")
     st.markdown("- His DIARY")

     st.markdown(" The Diary Says : ' After 20 years I will finally expose them ' ")

     if st.button("Return to menu"):
          st.session_state.stage = "menu"

def clues():
     pass



    




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

elif st.session_state.stage == "c_scene":
     c_scene()
elif st.session_state.stage == "body":
    body()

elif st.session_state.stage == "jack":
     jack()

elif st.session_state.stage == "emily":
     emily()

elif st.session_state.stage == "location":
     location()

elif st.session_state.stage == "bank":
     bank()

elif st.session_state.stage == "shelter":
     shelter()





