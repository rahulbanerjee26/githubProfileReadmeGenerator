import streamlit as st


def displaytext():
    sbar = st.sidebar
    st.subheader("Thank You for using this web app :smile:")
    st.markdown('''
    - Click on 'Generate README' in the sidebar
    - Fill in the text boxes
    - Once you are done, select the 'Generate README' Button
    - If you are happy with the Readme, you can download it
    - For more details, check out this [Tutorial](https://www.realpythonproject.com/a-free-tool-to-take-your-github-profile-to-the-next-level/)
    
    
    <h5 align="center"> Code & Crafted with 💛 Rahul Banerjee </h5>
    ''', unsafe_allow_html=True)
    with sbar:
        st.markdown('''
        ### Tutorial 📖 [here](https://www.realpythonproject.com/a-free-tool-to-take-your-github-profile-to-the-next-level/) 
        ### Twitter 🐦 [here](https://twitter.com/rahulbanerjee99)
        ### LinkedIn 👨‍💻 [here](https://www.linkedin.com/in/rahulbanerjee2699/)
        ''')
