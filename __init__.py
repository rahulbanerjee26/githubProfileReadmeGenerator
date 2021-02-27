import streamlit as st
from helpers import *
from main import skills

st.title("Github About Me Template")
st.subheader("Fill in the text boxes and click on Generate README")
st.subheader("You can edit the code in the editor and preview your ReadMe below the editor")

col1 , col2, col3 = st.beta_columns(3)

with col1:
    name = st.text_input("Name")

with col2:
    github = st.text_input("Github UserID")

with col3:
    linkedin = st.text_input("Linkedin userID")

p1 = st.text_area("I am currently working on")
p2 = st.text_area("I am currently learning")
p3 = st.text_area("I am looking to collaborate on")
p4 = st.text_area("talk to me about")

user_skils = st.multiselect("Select Skills",options=skills)

waka_userid = st.text_input("Wakatime User ID")
e1 = st.beta_expander("What is Wakatime and how do I get my user ID?")
with e1:
    st.text('''
            Waktime is an extension for your code editor. 
            It tracks the time you spend coding in a language
            ''')
    st.markdown(''' 
                - On the top right corner click on your profile icon and click on Settings
                - Ensure you have a value in the textbox next to User Name
                - Check the box for the following 'Display photo publicly', 'Display code time publicly ', 'Display languages, editors, os, categories publicly'
                - In the dropdown next to 'Display code time publicly ', select 'Last 7 days' If you have a free version, the other options in the dropdown will not work
                - Click on Save
        ''')
st.markdown('<br> <br>' , unsafe_allow_html = True) 
e2 = st.beta_expander("How to display my latest blog posts?")
with e2:
    feed_url = st.text_input("URL to your feed", value = 'https://realpythonproject.com/feeed')
    st.markdown(f'''
    - After you update the above feed url, give it a minute and Download the below yml file
    {get_yml(feed_url)}
    ''',unsafe_allow_html = True)
    st.markdown(''' 
    - Create a folder .github, inside it create another folder called workflows, inside it paste the downloaded blog-post-workflow.yml. 
    - Essentially create .github/workflows/blog-post-workflow.yml. If you paste this as the file while creating a new file in Github, it creates the folders for you.
    - In your readme, you blog feed will appear in between the lines 
        ``` 
        <!-- BLOG-POST-LIST:START -->
        <!-- BLOG-POST-LIST:END -->
        ```
    - Once you create the folder and store the file, Go to your github repo > Actions. Select the workflow in left sidebar and click on run flow. You will only have to do this once. Github will periodically fetch content from your feed.
    ''')

st.markdown('<br> <br>' , unsafe_allow_html = True)   
save = st.button("Generate README")
if save:
    code = value=default_html(name = name, github_username = github, waka_userName= waka_userid,linkedin_url = linkedin,p1 = p1,p2 = p2,p3 = p3,p4 = p4,skills=user_skills)
    st.markdown(download_readme(code),unsafe_allow_html = True)
    st.markdown(code, unsafe_allow_html = True)
