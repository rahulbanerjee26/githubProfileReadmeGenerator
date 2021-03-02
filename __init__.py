import streamlit as st
from helpers import *
from main import skills

st.title("Github About Me Template")
st.subheader("Fill in the text boxes and click on Generate README")
st.subheader("You can edit the code in the editor and preview your ReadMe below the editor")

sbar = st.sidebar

col1 , col2, col3 = st.beta_columns(3)

with col1:
    name = st.text_input("Name")
    twitter = st.text_input("Twitter")

with col2:
    github = st.text_input("Github UserID")
    portfolio = st.text_input("Portfolio")

with col3:
    linkedin = st.text_input("Linkedin userID")
    medium = st.text_input("Medium URL")

theme_list = ["default","solarized-light","dark", "radical", "merko", "gruvbox", "tokyonight", "onedark", "cobalt", "synthwave", "highcontrast", "dracula"]
github_stats_theme = sbar.selectbox(label="Select theme for GitHub Stats",options=theme_list)

p1 = st.text_area("I am currently working on")
p2 = st.text_area("I am currently learning")
p3 = st.text_area("I am looking to collaborate on")
p4 = st.text_area("talk to me about")

user_skills = st.multiselect("Select Skills",options=skills)

isWaka = sbar.checkbox(label= "Include WakaTime Stats",value = False)
isJoke = sbar.checkbox(label= "Include Joke Card",value = False)
joke_theme = sbar.selectbox(label="Select theme for Joke Card",options=theme_list)
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
st.markdown('<br>' , unsafe_allow_html = True) 
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
img_url = st.text_input(label='Enter Banner Image to be added at the top of the README',value = 'https://cdn.pixabay.com/photo/2018/01/14/23/12/nature-3082832_1280.jpg')
c1,c2 = st.beta_columns(2)
e3 = st.beta_expander("Getting Image URL")
with e3:
    st.markdown(''' 
- Enter the URL to the image, ensure URL ends with an extension like '.png','.svg','.gif'
- If you would like to use a downloaded image, uploade the image to your GitHub repo
- Click on the image file in your repo and click on either Download/Raw
- Copy the URL of image
    ''')
with c1:
    img_width = st.text_input(label='Enter Image witdh(include units % or px)',value = '100%')
with c2:
    img_height = st.text_input(label='Enter Image height(include units % or px)',value = '250px')

save = st.button("Generate README")
if save:
    code = default_html(name = name, github_username = github, waka_userName= waka_userid,linkedin_url = linkedin,p1 = p1,p2 = p2,p3 = p3,p4 = p4,skills=user_skills,twitter_url=twitter,medium_url = medium, portfolio_url = portfolio,isWaka = isWaka,github_stats_theme = github_stats_theme,isJoke = isJoke, joke_theme = joke_theme,img_url = img_url, img_width= img_width, img_height = img_height)
    st.markdown(download_readme(code),unsafe_allow_html = True)
    st.markdown(code, unsafe_allow_html = True)
