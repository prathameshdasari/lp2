import streamlit as st
from typing import List

knowledge_base = {
    "software_developer": [
        "1: Web Developer",
        "2: Mobile App Developer",
        "3: Data Scientist",
        "4: Please learn programming languages such as Python, Java, or JavaScript."
    ],

    "digital_marketing_specialist": [
        "1: Social Media Manager",
        "2: SEO Specialist",
        "3: Content Marketer",
        "4: Please familiarize yourself with digital marketing tools and platforms like Google Analytics, Facebook Ads, etc."
    ],

    "financial_analyst": [
        "1: Investment Analyst",
        "2: Risk Manager",
        "3: Financial Planner",
        "4: Please develop strong analytical and quantitative skills, and consider pursuing certifications such as CFA or CPA."
    ],

    "business_owner": [
        "1: Entrepreneur",
        "2: Small Business Owner",
        "3: Startup Founder",
        "4: Please focus on building leadership, management, and business development skills."
    ],

    "healthcare_professional": [
        "1: Physician",
        "2: Nurse Practitioner",
        "3: Physical Therapist",
        "4: Please pursue relevant medical education and training, and gain clinical experience."
    ]
}

st.header("Career Counseling Expert System")

def respond(input: List[str]):
    skills, interests, traits, career_goals = input

    if (skills == "programming" and "problem solving" in interests and "analytical" in traits and "tech industry" in career_goals):
        st.write("Based on your inputs, we recommend pursuing a career as a software developer!")
        st.write("Here are some career paths and recommendations:")
        for i in knowledge_base["software_developer"]:
            st.write(i)
    elif (skills == "marketing" and "creative" in interests and "social" in traits and "digital industry" in career_goals):
        st.write("Based on your inputs, we recommend pursuing a career as a digital marketing specialist!")
        st.write("Here are some career paths and recommendations:")
        for i in knowledge_base["digital_marketing_specialist"]:
            st.write(i)
    elif (skills == "financial analysis" and "analytical" in interests and "detail-oriented" in traits and "finance industry" in career_goals):
        st.write("Based on your inputs, we recommend pursuing a career as a financial analyst!")
        st.write("Here are some career paths and recommendations:")
        for i in knowledge_base["financial_analyst"]:
            st.write(i)
    elif (skills == "leadership" and "innovative" in interests and "management" in traits and "entrepreneurship" in career_goals):
        st.write("Based on your inputs, we recommend pursuing a career as a business owner!")
        st.write("Here are some career paths and recommendations:")
        for i in knowledge_base["business_owner"]:
            st.write(i)
    elif (skills == "medical" and "caring" in interests and "empathetic" in traits and "healthcare industry" in career_goals):
        st.write("Based on your inputs, we recommend pursuing a career in healthcare!")
        st.write("Here are some career paths and recommendations:")
        for i in knowledge_base["healthcare_professional"]:
            st.write(i)
    else:
        st.write("We couldn't find a suitable career recommendation based on your inputs. Please seek further career counseling.")

if __name__ == "__main__":
    skills = st.selectbox("Select your skills:", ["programming", "marketing", "financial analysis", "leadership", "medical"])
    interests = st.multiselect("Select your interests:", ["problem solving", "creative", "analytical", "innovative", "caring"])
    traits = st.multiselect("Select your personality traits:", ["social", "analytical", "detail-oriented", "management", "empathetic"])
    career_goals = st.multiselect("Select your career goals:", ["tech industry", "digital industry", "finance industry", "entrepreneurship", "healthcare industry"])
    
    if st.button("Get Career Recommendations"):
        respond([skills, interests, traits, career_goals])

