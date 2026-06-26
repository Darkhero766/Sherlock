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
    st.caption("A teacher found dead in sweltering july day")
    st.write(" ")
    st.write(" ")

    if st.button("Menu"):
         st.session_state.stage = "menu1"



def angelina():

    st.title("Case 3")
    st.caption(" On a DarkScary night ⛈️⛈️⛈️ ")
    st.write(" ")
    st.caption("When a strong thunderbolt Hit the Eath We can hear someone screaming....")
    st.write(" ")
    st.caption("Ahhhhhhhh........")
    st.write(" ")
    st.caption("Anglina was found dead in her own private library.....")
    st.write(" ")
    st.write(" ")
    st.write(" ")

    if st.button("Menu"):
         st.session_state.stage = "menu2"

def begger():
    st.title("Case 1")
    st.header("Murder of 'Normal' begger")

    st.subheader(" A old bgeer known by Mr. Grey found dead beneath the railway bridge..")

    if st.button("Menu"):
         st.session_state.stage = "menu"

    

def body():
        st.subheader("Eveyone beleived that he was just a poor begger but in investigation we have found that the man posses a gold poclet watch engraved with sign 'A.W' .. and. a Key to a safe ....")
        st.subheader("Investigation reveals that Mr. grey was a before Arthur A wealthy businessman who dissappears 20 years ago.")

        st.info("Mr. Grey was a Former millioonaire")
        if st.button("Return to menu"):
            st.session_state.stage = "menu"
def body1():
     st.subheader("Body of Emily ")
     st.write(" ")
     st.write(" ")

     st.subheader(" A Ftesh murdered body , No sign of force entry, No Fingerprints on body. ")
     st.write(" ")
     st.warning(" A sign of vey deep cut in the body ")
     st.write(" ")
     if st.button("Return to menu "):
          st.session_state.stage = "menu1"
def body2():
     st.title("Body of Victim")
     st.write(" ")
     st.caption("Frail bluish body ")
     st.write(" ")
     st.caption("Its look like something 'Heavy fall on her body' ")
     st.write(" ")
     st.info ("Cause of death : Due to heavy load on her body .....")

     st.write(" ")
     st.write(" ")
     if st.button("Return to menu"):
          st.session_state.stage = "menu2"

def c_scene():
        st.subheader("Blood is spilled everywhere beneath the bridge and there is a knife without any fingerprints... ")
        st.markdown("A sign was drawn in sand")
        st.info("ylimaf ")

        if st.button("Return to menu "):
            st.session_state.stage = "menu"
def c_scene1():
     st.subheader("Crime scene of Emily ")
     st.write(" ")

     st.subheader("No sign of forced Entry ! No murder weapon  found. ")
     st.info("Just 'Dusty all over around' ")

     st.write(" ")
     if st.button("Return to menu"):
          st.session_state.stage = "menu1"

def c_scene2():
     st.title("Crime Scene")
     st.write(" ")
     st.caption(" A Room of books filled with mystery.....🎶🎶🎶")
     st.write(" ")
     st.caption(" A body marks on floor , No forced Entry sign , But window is open ")
     st.write(" ")
     st.caption("Found a piece. of paper Says")
     st.write(" ")

     st.info("     'Mine'    ")

     if st.button("Return to menu "):
          st.session_state.stage = "menu2"


def suspect():
        st.subheader(" Select the suspect to investigate")
        if st.button("1. Jack Miller (Former partner)"):
            st.session_state.stage = "jack"

        if st.button("2. Sarah (estrangled daughter)"):
            st.session_state.stage = "sarah"
        if st.button("3. Ethan brooks (investigate journalist)"):
            st.session_state.stage ="ethan"

        if st.button("4. Fathee thomas (local priest )"):
            st.session_state.stage = "father"

        st.write("")
        if st.button("Return to menu"):
             st.session_state.stage = "menu"

def suspect1():
     st.subheader("Select the culprit to investigate")
     st.write(" ")

     if st.button("1. Gardner "):
          st.session_state.stage = "gardner"
     st.write(" ")

     if st.button("2. The librarian"):
          st.session_state.stage = "librarian"

     st.write(" ")

     if st.button("3. Principal"):
          st.session_state.stage = "principal"
     st.write(" ")

     if st.button("Return to menu"):
          st.session_state.stage = "menu1"

def suspect2():
     st.title(" Suspects ")
     st.write(" ")
     st.subheader("Select from following to question")
     st.write(" ")
     if st.button("1. Arthur (Peon) "):
          st.session_state.stags = "arthur"
     st.write(" ")
     st.write(" ")
     if st.button("2. Sweeper"):
          st.session_state.stage = "sweeper"
     st.write(" ")

     st.write(" ")

     if st.button(" Holmes (Fiance)"):
          st.session_state.stage = "holmes"

     st.write(" ")
     st.write(" ")
     if st.button("Return to menu"):
          st.session_state.stage = "menu2"
#case 3

def arthur():
     st.title(" Suspect : Arthur (Peon) ")
     st.write(" ")
     st.write(" ")

     st.caption("Testimony : 'I was on duty outside the building When i hear the scream.....")
     st.write(" ")
     if st.button("Return to suspects"):

          st.session_state.stage = "suspect2"

def sweeper():
     st.title("Suspect 2 : Sweeper ")
     st.write(" ")
     st.write(" ")
     st.caption("Testimony : I was on duty just cleaning the floor....")
     st.write(" ")
     if st.button("Return to suspects"):
          st.session_state.stage = "suspect2"

def holmes():
     st.title("Suspect 3 : Holmes (Fiance)")
     st.write(" ")

     st.write(" ")
     st.caption("Testimony : 'I was at my home but she texted me that that someone is following her two days before it.....")
     st.write(" ")

     if st.button("Return to suspects"):
          st.session_state.stage = "suspect2"
#case 2

def gardner():
     st.subheader("Suspect 1 : Gardner")

     st.write(" ")
     st.write(" ")

     st.subheader("Testimony : He says he was trimming the bushes")

     st.write(" ")
     if st.button("Retun to suspects"):
          st.session_state.stage = "suspect1"

def librarian():
     st.subheader("Suspect 2 : Librarian")
     st.write(" ")
     st.write("")
     st.subheader("Testimony : She says she was organizing the books in AC controlled library")

     st.write(" ")
     if st.button("Return to suspects"):
          st.session_state.stage = "suspect1"

def principal():
     st.subheader("Suspect 3 : Principal")

     st.write(" ")
     st.write(" ")

     st.subheader("Testimony : He says he was in meeting all day")
     st.write(" ")

     if st.button("return to suspects"):
          st.session_state.stage = "suspect1"

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
        st.subheader("Menu\n\n")
        if st.button("Examine the body"):
           
           st.session_state.stage = "body"
        if st.button("Visit Locations"):
             st.session_state.stage = "location"
    
        if st.button("Investigate Crime scene"):
           st.session_state.stage = "c_scene"

        if st.button("Questions the suspects."):
           st.session_state.stage = "suspect"

        if st.button("Found the Accused"):
             st.session_state.stage = "accusation"

def menu1():
     st.subheader("Menu")
     st.write(" ")
     st.write(" ")

     if st.button("Examine the body"):
          st.session_state.stage = "body1"
     st.write(" ")
     if st.button("Invetigate Crime Scene"):
          st.session_state.stage = "scene1"
     st.write(" ")

     if st.button("Invetigate suspects"):
          st.session_state.stage = "suspect1"
     st.write(" ")
     if st.button("Find the Accused"):
          st.session_state.stage = "accusation1"

def menu2():
     st.title("Menu")
     st.write(" ")
     st.write(" ")
     st.subheader("Select the option to continue")

     st.write(" ")
     st.write(" ")
     if st.button("Examine the Body"):
          st.session_state.stage = "body2"
     st.write(" ")
     if st.button("Investigate Crime Scene"):
          st.session_state.stage = "scene2"
     st.write(" ")
     if st.button("Question the suspects"):
          st.session_state.stage = "suspect2"
     st.write(" ")
     if st.button("Announce the Culprit"):
          st.session_state.stage = "accustaion2"


     
def location():
     st.subheader("Select the location to investigate")

     if st.button("Bank"):
          st.session_state.stage = "bank"
     if st.button("Shelter"):
          st.session_state.stage = "shelter"

     st.write("")
     st.write("")

     if st.button("Return to menu"):
          st.session_state.stage = "menu"

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

def accusation():
     st.subheader("Choose the murderer")
     if st.button("Father Thomas"):
          st.session_state.stage ="f"
     if st.button("Sarah Whitmore"):
          st.session_state.stage = "s"
     if st.button("Ethan brooks"):
          st.session_state.stage = "e"
     if st.button("Jack Miller"):
          st.session_state.stage = "j"
def accusation1():
     st.title(" Find the Culprit !!")
     st.write(" ")
     if st.button("1. Gardner"):
          st.session_state.stage = "g"
     st.write(" ")
     if st.button("2. Librarian"):
          st.session_state.stage = "l"
     st.write(" ")

     if st.button("3. Principal"):
          st.session_state.stage = "p"
def accusation2():
     st.title("Find the culprit !!")
     st.write(" ")
     if st.button("1. Arthur (peon)"):
          st.session_state.stage = "ar"
     st.write(" ")
     if st.button("2. Sweeper"):
          st.session_state.stage = "sw"
     st.write(" ")
     if st.button("3. Holmes (Fiance)"):
          st.session_state.stage = "ho"

def ar():
     st.title("Arthur (peon)")
     st.write(" ")
     st.warning("Wrong Person....... ")

def sw():
     st.title("Sweeper...")
     st.write(" ")

     st.warning("Wrong person....... You lose")

def ho():
     st.title("Holmes (Fiance)")
     st.write(" ")
     st.success("You found the real culprit ")
     st.write(" ")
     st.caption(" This man killed herr cuz he found about her past relationship")
     
#case 3 upar
def f ():
     st.subheader("Father Thomas")
     st.warning("Wrong Accused.......")
def s():
    st.subheader("Sarah Whitemore")
    st.success("Found the murderer")
    st.write("She killed her father out of resentment.... We found 'ylimaf' in crime scene it reverse says 'family' ")
def j():
     st.subheader("Jack Miller")
     st.warning("Wrong accused....")

def e():
     st.subheader("Ethan Brooks")
     st.warning("WRONG ACCUSED....")

#case2

def g ():
     st.subheader("Gardner")

     st.write (" ")
     st.write(" ")
     st.success(" Found it .The real culprit")
     st.write("")
     st.info("He killed it Cause she set foot on his best flower. (Psychoo)")

def l ():
     st.subheader(" Librarian")
     st.write(" ")
     st.write(" ")

     st.warning("Wrong Person......... You lose")



def p():
     st.subheader("Principal")
     st.write(" ")
     st.write(" ")
     st.warning("Wrong Person..... YOU LOSE.")






if st.session_state.stage == "Home":
    case()
elif st.session_state.stage == "menu":
     menu()
elif st.session_state.stage == "menu1":
     menu1()
elif st.session_state.stage == "menu2":
     menu2()

elif st.session_state.stage == "case1" :
    begger()

elif st.session_state.stage == "case2":
    emily()

elif st.session_state.stage == "case3":
    angelina()

elif st.session_state.stage == "suspect":
     suspect()
elif st.session_state.stage == "suspect1":
     suspect1()
elif st.session_state.stage == "suspect2":
     suspect2()

elif st.session_state.stage == "c_scene":
     c_scene()
elif st.session_state.stage == "scene1":
     c_scene1()
elif st.session_state.stage == "scene2":
     c_scene2()

elif st.session_state.stage == "body":
    body()
elif st.session_state.stage == "body1":
     body1()
elif st.session_state.stage =="body2":
     body2()

elif st.session_state.stage == "jack":
     
     jack()

elif st.session_state.stage == "sarah":
     sarah()

elif st.session_state.stage == "father":
     father()
elif st.session_state.stage == "ethan":
     ethan()
elif st.session_state.stage == "emily":
     emily()
elif st.session_state.stage == "gardner":
     gardner()
elif st.session_state.stage == "librarian":
     librarian()
elif st.session_state.stage == "principal":
     principal()
elif st.session_state.stage == "location":
     location()

elif st.session_state.stage == "bank":
     bank()

elif st.session_state.stage == "shelter":
     shelter()
elif st.session_state.stage == "f":
     f()
elif st.session_state.stage == "e":
     e()
elif st.session_state.stage == "s":
     s()
elif st.session_state.stage == "j":
     j()

#case 2
elif st.session_state.stage == "g":
     g()
elif st.session_state.stage == "l":
     l()
elif st.session_state.stage == "p":
     p()
elif st.session_state.stage == "arthur":
     arthur()

elif st.session_state.stage == "sweeper":
     sweeper()
elif st.session_state.stage == "holmes":
     holmes()

elif st.session_state.stage == "ho":
     ho()
elif st.session_state.stage == "sw":
     sw()
elif st.session_state.stage == "ar":
     ar()
elif st.session_state.stage == "accusation":
     accusation()
elif st.session_state.stage == "accusation1":
     accusation1()
elif st.session_state.stage == "accusation2":
     accusation2()







