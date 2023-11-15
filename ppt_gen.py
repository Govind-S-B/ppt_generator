from pptx import Presentation
from pptx.util import Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN


ppt = Presentation()

# Presentation Structure
# Opening Slide - [Title,Subtitle]
# Overview - [1,2,3,4,5,6,7,8]
# Content Slides - [Topic,1,2,3,4,5]
# Thank You Slide

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

# Setting Background
slide_master = ppt.slide_master
slide_master.background.fill.solid()
slide_master.background.fill.fore_color.rgb = RGBColor(0, 0, 0)

# Title Screen
curr_slide = ppt.slides.add_slide(ppt.slide_layouts[0])
curr_slide.shapes.title.text = slide_data[0][0]
curr_slide.shapes.title.text_frame.paragraphs[0].runs[0].font.color.rgb = RGBColor(
    255, 255, 255)
curr_slide.shapes.placeholders[1].text = slide_data[0][1]
curr_slide.shapes.placeholders[1].text_frame.paragraphs[0].runs[0].font.color.rgb = RGBColor(
    255, 255, 255)

# Overview
curr_slide = ppt.slides.add_slide(ppt.slide_layouts[1])
curr_slide.shapes.title.text = slide_data[1][0]
curr_slide.shapes.title.text_frame.paragraphs[0].runs[0].font.color.rgb = RGBColor(
    255, 255, 255)
for content in slide_data[1][1:]:
    tframe = curr_slide.shapes.placeholders[1].text_frame
    para = tframe.add_paragraph()
    para.text = content
    para.level = 1
    para.runs[0].font.color.rgb = RGBColor(
        255, 255, 255)

# Content Slides
for curr_slide_data in slide_data[2:]:
    curr_slide = ppt.slides.add_slide(ppt.slide_layouts[1])
    curr_slide.shapes.title.text = curr_slide_data[0]
    curr_slide.shapes.title.text_frame.paragraphs[0].runs[0].font.color.rgb = RGBColor(
        255, 255, 255)
    for content in curr_slide_data[1:]:
        tframe = curr_slide.shapes.placeholders[1].text_frame
        para = tframe.add_paragraph()
        para.text = content
        para.level = 1
        para.runs[0].font.color.rgb = RGBColor(
            255, 255, 255)


# Thank You Screen
curr_slide = ppt.slides.add_slide(ppt.slide_layouts[2])
curr_slide.shapes.placeholders[1].text = "Thank You"

curr_slide.shapes.placeholders[1].text_frame.paragraphs[0].font.color.rgb = RGBColor(
    255, 255, 255)
curr_slide.shapes.placeholders[1].text_frame.paragraphs[0].font.size = Pt(96)
curr_slide.shapes.placeholders[1].text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER

ppt.save(f"{slide_data[0][0]}.pptx")
print("done")
