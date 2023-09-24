# garden.md
(gardening in Markdown) 
Submitted to TechNova 2023 
## Inspiration 💡
I was inspired by [OpenFarm](https://openfarm.cc/) and my neighborhood's community garden. OpenFarm is also a platform to share gardening information, but it is not actively maintained. I wanted to share that information using Markdown files with the hope that it is easier to maintain. I've previously volunteered in the community garden and have seen more youth get involved. So, I wanted to make it easier for older community members (that spend a lot of time in the garden) to share their knowledge with younger community members hoping to contribute. 

## What it does ✏
This project aims to increase access to gardening knowledge in my community. It stores gardening guides in Markdown files and renders them with Hugo. To add guides, it has a script to parse a written guide to Markdown and create a PR to add it to the site. 

## How we built it 👷‍♀️
Hugo to display Markdown guides 
[pytesseract](https://pypi.org/project/pytesseract/) for OCR on written guides 
[PyGithub](https://github.com/PyGithub/PyGithub) to automate PRs to add guides  
Github 
- Pages for deployment 
- Project board for task management 

## Challenges we ran into 😢
Mostly time constraints that led to adapting priorities and requirements. I had issues connecting a custom subdomain to Github pages and with adding a shortcode to render guide steps as `<details>` and `<summary>` blocks. With more time, I would have investigated further and tried to resolve these. 

## Accomplishments that we're proud of and what we learned 😄
It was my first time using a lot of these tools (tesseract, Hugo) and I'm happy with how far I got with them. I can apply this experience to future projects. 

## What's next for garden.md ❓
Lots of UI/UX polishing :] 
I could pitch this to community gardeners and get feedback from the garden facilitator. If it goes well, I could look into deploying this for my neighborhood to access. I could set up guide-making workshops with the seniors and publish those to the site. 
