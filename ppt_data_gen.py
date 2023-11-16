"""
Target Schema :

slide_data = [
    ["Ethics in Design",
     "Integrating Ethics into Design Processes"],

    ["Introduction",
     "User-Centered Design",
     "Transparency and Honesty",
     "Data Privacy and Security",
     "Accessibility and Inclusion",
     "Social Impact and Sustainability",
     "Ethical AI and Automation",
     "Collaboration and Professional Ethics"],

    ["Introduction",
     "Ensuring responsible decision-making in design.",
     "Moral obligation to prioritize user well-being.",
     "Promoting trust, inclusivity, and positive social impact."],

    ["User-Centered Design",
     "Prioritize needs and experiences of users.",
     "Design with empathy and user feedback.",
     "Respect user privacy and ensure informed consent.",
     "Avoid manipulative practices and prioritize inclusivity."],

    ["Transparency and Honesty",
     "Be transparent about design intentions and limitations.",
     "Disclose risks and biases in the design.",
     "Avoid deceptive practices and false advertising.",
     "Establish trust through clear and accurate communication."],

    ["Data Privacy and Security",
     "Safeguard user data with strong privacy measures.",
     "Collect only necessary data with explicit consent.",
     "Regularly assess and update security measures.",
     "Establish data retention policies and allow user data deletion."],

    ["Accessibility and Inclusion",
     "Design interfaces accessible to users with disabilities.",
     "Provide alternative formats for content.",
     "Consider diverse cultural and cognitive backgrounds.",
     "Test designs with a diverse group of users."],

    ["Social Impact and Sustainability",
     "Consider broader social and environmental implications.",
     "Promote sustainability by reducing waste and energy consumption.",
     "Avoid designs contributing to inequality or harm.",
     "Engage in socially responsible collaborations."],

    ["Ethical AI and Automation",
     "Ensure fairness and accountability in AI algorithms.",
     "Audit and monitor AI systems for bias and discrimination.",
     "Be transparent about AI-driven decision-making processes.",
     "Anticipate and mitigate potential negative impacts."],

    ["Collaboration and Professional Ethics",
     "Foster a collaborative and inclusive work environment.",
     "Respect intellectual property rights and avoid plagiarism.",
     "Uphold professional standards and codes of ethics.",
     "Be open to feedback and continuous learning."],
]
"""

# ADDITIONAL STEP At each step , search for the appropriate content , fetch top 3 results , use RAG on that

# Generate Title and Subtitle given Topic

# Given topic title and subtitle generate table of content for 7 slides

# Iterate over TOC , for each sub topic given the topic title and subtitle , generate 5 points or sentences , each of 100 characters in length

# Format at each step to proper list

import re
from langchain.llms import Ollama
from langchain.prompts import PromptTemplate

llm = Ollama(model="dolphin2.1-mistral",
             temperature="0.4")

# llm_low_temp = Ollama(model="dolphin2.1-mistral",
#                       temperature="0")


def extract_title_items(text):
    pattern = r'<<\s*"([^"]+)"\s*\|\s*"([^"]+)"\s*>>'
    matches = re.findall(pattern, text)
    return [item for match in matches for item in match]


def extract_items(input_string):
    # Find the text inside the << >>
    content = re.search(r'<<(.+?)>>', input_string)

    if content:
        content = content.group(1)
    else:
        return []

    # Split the content by the | separator and remove whitespace
    items = [item.strip() for item in content.split('|')]

    # Remove the quotes from each item
    items = [re.sub(r'^"|"$', '', item) for item in items]

    return items


topic = "Pentesting in software development"

slide_data = []

slide_data.append(extract_title_items(llm(f"""
You are a text summarization and formatting specialized model that fetches relevant information

For the topic "{topic}" suggest a presentation title and a presentation subtitle it should be returned in the format :
<< "title" | "subtitle >>

example :
<< "Ethics in Design" | "Integrating Ethics into Design Processes" >>
""")))

slide_data.append(extract_items(llm(f"""
You are a text summarization and formatting specialized model that fetches relevant information
          
For the presentation titled "{slide_data[0][0]}" and with subtitle "{slide_data[0][1]}" for the topic "{topic}"
Write a table of contents containing the title of each slide for a 7 slide presentation
It should be of the format :
<< "slide1" | "slide2" | "slide3" | ... | >>
          
example :
<< "Introduction" | "User-Centered Design" | "Transparency and Honesty" | "Data Privacy and Security" | "Accessibility and Inclusion" | "Social Impact and Sustainability" | "Ethical AI and Automation" | "Collaboration and Professional Ethics" >>          
          """)))

for subtopic in slide_data[1]:

    data_to_clean = llm(f"""
You are a content generation specialized model that fetches relevant information and presents it in clear concise manner
          
For the presentation titled "{slide_data[0][0]}" and with subtitle "{slide_data[0][1]}" for the topic "{topic}"
Write the contents for a slide with the subtopic {subtopic}
Write 5 points. Each point 10 words maximum.
Make the points short, concise and to the point.
""")

    cleaned_data = llm(f"""
You are a text summarization and formatting specialized model that fetches relevant information and formats it into user specified formats
Given below is a text draft for a presentation slide containing 5 points , extract the 5 sentences and format it as :
              
<< "point1" | "point2" | "point3" | ... | >>
              
example :
<< "Foster a collaborative and inclusive work environment." | "Respect intellectual property rights and avoid plagiarism." | "Uphold professional standards and codes of ethics." | "Be open to feedback and continuous learning." >>

-- Beginning of the text --
{data_to_clean}
-- End of the text --         
    """)

    print(subtopic)
    print(extract_items(cleaned_data))
