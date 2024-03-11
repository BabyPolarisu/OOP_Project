import streamlit as st

st.set_page_config(
    page_title = "Formula 1 2024",
    page_icon = "🏎"
)
st.sidebar.title("Home Page")
st.sidebar.success("Select page")

bg = """
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://preview.redd.it/dux4xq5v0zs41.jpg?width=1080&crop=smart&auto=webp&s=e1fddcfebc5b99225cf1bf1a3297e450cc840b6a");
background-size: cover;
}

}
</style>
"""
st.markdown(bg, unsafe_allow_html=True)                                 

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""
    
my_input = st.text_input("Input a your name here!", st.session_state["my_input"])
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered:", my_input)
    st.write("Welcome to our website! Enjoy!")
    st.image("https://files.gqthailand.com/uploads/fi-001.jpg")