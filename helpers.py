import base64

def display_skills(skills,github_username):
    result = []

    for skill in skills:
        link = f'https://github.com/{github_username}?tab=repositories&q=&type=&language={skill}&sort='
        base = f'''<a href= {link} > <img width ='32px' height='32px' src ='{'https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/'+skill+'.svg'}'> </a>'''
        result.append(base)
    return '\n'.join(result)

def display_socials(linkedin,twitter,medium,portfolio,github):
    result = ''
    if linkedin != '':
        linkedin = 'https://www.linkedin.com/in/'+linkedin
        result += f'''<a href = '{linkedin}'> <img width = '32px' align= 'center' src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/linked-in-alt.svg"/></a> \n'''
    
    if twitter != '':
        twitter = 'https://www.twitter.com/'+twitter
        result += f'''<a href = '{twitter}'> <img width = '32px' align= 'center' src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/twitter.svg"/></a> \n'''
    
    if medium != '':
        result += f'''<a href = '{medium}'> <img width = '32px' align= 'center' src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/medium.svg"/></a> \n'''
    
    if portfolio != '':
        result += f'''<a href = '{portfolio}'> <img width = '32px' align= 'center' src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/portfolio.png"/></a> \n'''    
    
    if github != '':
        github = 'https://www.github.com/'+github   
        result += f'''<a href = '{github}'> <img width = '32px' align= 'center' src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/github.svg"/></a> \n'''
    return result

def show_waka(isWaka,waka_userName):
    if isWaka:
        return f'''
<h2> Stuff I worked on last week  <img src = "https://raw.githubusercontent.com/rahulbanerjee26/githubProfileReadmeGenerator/main/gifs/needABreak.gif" width = 50px height= 50px> </h2>
<a href="https://github.com/anuraghazra/github-readme-stats">
<img align="center" src="https://github-readme-stats.vercel.app/api/wakatime?username=@{waka_userName}&compact=True"/>
</a>
<br>
'''
    else:
        return ''

def show_github_stats(github_username,theme,choice = 'type-2'):
    if choice == 'type-1':
        return f'''![Metrics](https://metrics.lecoq.io/{github_username}?template=classic&config.timezone=America%2FToronto)'''

    if choice == 'type-2':
        return f'''![Metrics](https://metrics.lecoq.io/{github_username}?template=terminal&base.header=0&base.activity=0&base.repositories=0&base.metadata=0&languages=1&languages.limit=8&languages.colors=github&languages.threshold=0%25&config.timezone=America%2FToronto)'''
    
    return f'''<a href="https://github.com/anuraghazra/github-readme-stats">
<img align="left" src="https://github-readme-stats.vercel.app/api?username={github_username}&count_private=true&show_icons=true&theme={theme}" />
</a>
<a href="https://github.com/anuraghazra/convoychat">
<img align="center" src="https://github-readme-stats.vercel.app/api/top-langs/?username={github_username}&theme={theme}" />
</a>'''

def show_joke(isJoke,theme):
    if isJoke:
        return f'''<h2> Some Programming Humor for you <img align ='center' src='https://raw.githubusercontent.com/rahulbanerjee26/githubProfileReadmeGenerator/main/gifs/winkFace.gif' width = '32px' height= '32px'></h2>

![Jokes Card](https://readme-jokes.vercel.app/api?theme={theme})
'''
    else:
        return ''

def show_blog(is_blog):
    if is_blog:
        return '''
<h2> My Blog Posts </h2>

<!-- BLOG-POST-LIST:START -->
<!-- BLOG-POST-LIST:END -->
'''
    return ''

def default_html(name = 'Rahul', linkedin_url = '',twitter_url = '',medium_url='',portfolio_url='',waka_userName = 'rahulbanerjee26',github_username = 'rahulbanerjee26',p1='......',p2='.......',p3='.........',p4='.........',skills=[],isWaka = False,github_stats_theme = 'dark',isJoke = False,
joke_theme = 'dark',img_url = '',img_width='',img_height='',github_stats_type = 'type-1',isBlog = False):
    return f'''
<div align="center">
<img width="{img_width}" height = "{img_height}" src="{img_url}" alt="cover" />
</div>

<h1> Hello Fellow < Developers/ >! <img src = "https://raw.githubusercontent.com/rahulbanerjee26/githubProfileReadmeGenerator/main/gifs/wave.gif" width = 50px height='50px'> </h1>
<p align='center'>

![visitors](https://visitor-badge.glitch.me/badge?page_id={github_username+'.'+github_username})

</p>
<div size='20px'> Hi! My name is {name}. Thank You for taking the time to view my GitHub Profile :smile: 
</div>

<h2> About Me <img src = "https://raw.githubusercontent.com/rahulbanerjee26/githubProfileReadmeGenerator/main/gifs/eatSleepCodeRepeat.gif" width = 100px height='100px'></h2>

<img width="55%" align="right" alt="Github" src="https://raw.githubusercontent.com/rahulbanerjee26/githubProfileReadmeGenerator/47a1a7b035154ce002fffc42e803b6ca8acbc4f3/gifs/git-header.svg" />


- 🔭 I’m currently working on {p1}

- 🌱 I’m currently learning {p2} 

- 👯 I’m looking to collaborate on {p3} 

- 💬 Talk to me about {p4} 

<h2> Skills <img src = "https://raw.githubusercontent.com/rahulbanerjee26/githubProfileReadmeGenerator/main/gifs/code.gif" width = 32px height=32px> </h2>
{display_skills(skills,github_username)}


<h2> Connect with me <img src='https://raw.githubusercontent.com/rahulbanerjee26/githubProfileReadmeGenerator/main/gifs/handShake.gif' width="50px" height=50px> </h2>
{display_socials(linkedin_url,twitter_url,medium_url,portfolio_url,github_username)}
{show_waka(isWaka,waka_userName)}

<h2> My GitHub Stats <img src='https://raw.githubusercontent.com/rahulbanerjee26/githubProfileReadmeGenerator/main/gifs/github.gif' width='32px' height=32px> </h2>

{show_github_stats(github_username,github_stats_theme,github_stats_type)}
{show_blog(isBlog)}
{show_joke(isJoke,joke_theme)}

<br>
<footer align='center'>README made with help of <a href='https://github.com/rahulbanerjee26/githubProfileReadmeGenerator'>githubProfileReadmeGenerator</a> </footer>
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
    href = f'<h4><a href="data:file/csv;base64,{b64}" download="README.md">Download README</a></h4>'
    return href
