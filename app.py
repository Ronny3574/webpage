from PIL import Image
import streamlit as st

st.set_page_config(page_title="DARKWEB FIXED MATCHES", layout="wide")

# Use local_css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

#--- LOAD ASSETS ---
# Adjust the filenames as needed
img_ticket_vip_active = Image.open("images/pic 1.png")
img_recent_winning_ticket = Image.open("images/pic 2.png")

# Header section
with st.container():
    st.subheader("OWARD LOTUS FIXED INFO")
    st.header("Who We Are")
    st.write("WE ARE PASSIONATE ABOUT MAKING OUR CLIENTS WIN ON A DAILY BASIS AND TURNING GAMBLING INTO A PROFITABLE INVESTMENT")
    st.write("[Learn More>](https://wa.me/+12172714974)")

# What we Do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What We Do")
        st.markdown("""
            On our website, social media accounts, and telegram channels, we:
            - Offer free fixed matches to all our followers and subscribers on day one.
            - Build trust and confidence through our games which are 95-100% fixed.
            - Pay back our clients in case of a loss after they subscribe. 
            - Get our information from low-value leagues that are easily paid off to provide the scores we desire.
        
            If this sounds interesting to you, please subscribe to our telegram channels and follow us on all social media platforms.
        """)
        st.markdown("[Telegram channel >](https://t.me/jakegreenb)")

#--- PROJECTS ---
with st.container():
    st.write("---")
    st.header("Our Projects")
    # First Project
    st.write("##")
    col1, col2 = st.columns(2)
    with col1:
        st.image(img_ticket_vip_active, caption="VIP Ticket at Active State", use_column_width=True)
    with col2:
        st.write("The image shows a screenshot of our closed VIP ticket at its active state hours before kickoff.")
    
    # Second Project
    st.write("##")
    col3, col4 = st.columns(2)
    with col3:
        st.image(img_recent_winning_ticket, caption="Recent Winning Ticket", use_column_width=True)
    with col4:
        st.write("The image shows a screenshot of one of our most recent tickets showing the games, the correct scores, the stake, and the accrued winnings.")

# --- CONTACT ---
with st.container():
     st.write("---")
     st.header("Get in touch with us!")
     st.write("##")
     contact_form = """
     <form action="https://formsubmit.co/owardlotus1@gmail.com" method="POST">
     <input type="hidden" name="_capcha" value="false">
     <input type="text" name="name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
     </form>
     """
     left_column, right_column = st.columns(2)
     with left_column:
         st.markdown(contact_form, unsafe_allow_html=True)
     with right_column:
         st.empty()
