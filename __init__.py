import streamlit as st

st.set_page_config(layout='wide',page_title="GitHub Profile Readme Generator",initial_sidebar_state="expanded")
from Webpages import Homepage,Aboutpage
from streamlit_option_menu import option_menu

page = option_menu(None,["Home", 'About Us'],
        icons=[' ', ' '], orientation='horizontal')

st.markdown('''
<h1> Github Profile README Generator </h1>

[![GitHub stars](https://img.shields.io/github/stars/rahulbanerjee26/githubProfileReadmeGenerator.svg?style=for-the-badge&label=Star&maxAge=25920000&logo=github)](https://github.com/rahulbanerjee26/githubProfileReadmeGenerator/stargazers/)
''', unsafe_allow_html=True)

if page == 'Home':
    Homepage.md_generator()
if page == 'About Us':
    Aboutpage.displaytext()
