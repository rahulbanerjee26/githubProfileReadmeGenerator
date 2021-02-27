import base64

def default_html(name = 'Rahul', linkedin_url = '',twitter_url = '',waka_userName = 'rahulbanerjee26',github_username = 'rahulbanerjee26',p1='......',p2='.......',p3='.........',p4='.........'):
    return f'''
# Hello World <img src = "https://raw.githubusercontent.com/MartinHeinz/MartinHeinz/master/wave.gif" width = 50px>
![visitors](https://visitor-badge.glitch.me/badge?page_id={github_username+'.'+github_username})

<div size='20px'> Hi! My name is {name}. Thank You for taking the time to view my GitHub Profile :smile: 
<h2> Connect with me <img src='https://raw.githubusercontent.com/ShahriarShafin/ShahriarShafin/main/Assets/handshake.gif' width="64px"> </h2>
<br>
<a href = '{linkedin_url}> <img width = '36px' align= 'left' src="https://github.com/rahuldkjain/github-profile-readme-generator/blob/master/src/images/icons/Social/linked-in-alt.svg"/></a>
<a href='{twitter_url}'> <img  width='36px' align= 'left' src="https://github.com/rahuldkjain/github-profile-readme-generator/blob/master/src/images/icons/Social/twitter-alt.svg" href = 'https://twitter.com/rahulbanerjee99'> </a>
</div>
<br>
<br>

<h2> About Me</h2>

- 🔭 I’m currently working on {p1}

- 🌱 I’m currently learning {p2}

- 👯 I’m looking to collaborate on {p3}

- 💬 Talk to me about {p4}

## Stuff I worked on last week⌚
<a href="https://github.com/anuraghazra/github-readme-stats">
<img align="center" src="https://github-readme-stats.vercel.app/api/wakatime?username=@{waka_userName}&compact=True"/>
</a>

## My GitHub Stats 📊
<a href="https://github.com/anuraghazra/github-readme-stats">
<img align="left" src="https://github-readme-stats.vercel.app/api?username={github_username}&count_private=true&show_icons=true&theme=radical" />
</a>
<a href="https://github.com/anuraghazra/convoychat">
<img align="center" src="https://github-readme-stats.vercel.app/api/top-langs/?username={github_username}&layout=compact" />
</a>

<!-- BLOG-POST-LIST:START -->
<!-- BLOG-POST-LIST:END -->

'''


def get_yml(feed_url):
    yml_file = f'''
name: Latest blog post workflow
on:
schedule: # Run workflow automatically
- cron: '0 * * * *' # Runs every hour, on the hour
workflow_dispatch: # Run workflow manually (without waiting for the cron to be called), through the Github Actions Workflow page directly
jobs:
update-readme-with-blog:
name: Update this repo's README with latest blog posts
runs-on: ubuntu-latest
steps:
- uses: actions/checkout@v2
- uses: gautamkrishnar/blog-post-workflow@master
    with:
    feed_list: "{feed_url}"
    '''
    b64 = base64.b64encode(yml_file.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="blog-post-workflow.yml">Download yml file</a>'
    return href

def download_readme(code):
    b64 = base64.b64encode(code.encode()).decode()
    href = f'<h4><a href="data:file/csv;base64,{b64}" download="README.md">Dowload README</a></h4>'
    return href

