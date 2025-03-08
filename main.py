import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import base64
import os
GEMINI_API_KEY=st.sidebar.text_input(label="Enter your Gemini-pro API key")
load_dotenv()
import warnings
warnings.filterwarnings("ignore")

# def get_response(text):
#     model=ChatGoogleGenerativeAI(
#         api_key=api_key,
#         model="gemini-2.0-flash",
#         temperature=1
#     )

#     response=model.invoke(text)
#     return response.content

def get_response(input_text):
    model=ChatGoogleGenerativeAI(
        api_key=GEMINI_API_KEY,
        model="gemini-2.0-flash",
        temperature=0.6 
    )
    response=model.invoke(input_text)
    return response.content

def get_file(file):
        content=file.read()
        encode=base64.b64encode(content).decode()
        return encode

     
st.image("image2.jpg")
st.title("SnapCode")
st.write("SnapCode is an AI-powered chatbot that converts hand-drawn wireframes, sketches, or diagrams into clean and structured HTML & CSS code.")
file_upload=st.sidebar.file_uploader("upload image",type=["jpg","png","jpeg"])
if file_upload:
    st.sidebar.image(file_upload)
    st.sidebar.success("submit the image ✅")
st.sidebar.info("""
   
Concepts Behind the Chatbot
Computer Vision & OCR: The chatbot extracts and processes Snapcodes to generate raw images.
AI & Machine Learning: Enhances accuracy in decoding Snapcodes and improving output quality.
Web Development Automation: Automatically converts processed images into structured HTML & CSS code.
Real-Time Processing: Ensures quick response time for seamless user experience.

""")
st.sidebar.info("""About the Developer 
Vicky, A passionate Artificial Intelligence and Data Science student, is the mastermind behind this innovative chatbot. Known for his technical expertise and problem-solving skills, he developed this chatbot to simplify the process of converting Snapcodes into raw images and further transforming them into HTML & CSS.""")

camera_disabled= file_upload is not None
if st. button("close the camera"):
    camera_disabled=True
if st.button("open the camera"):
    if file_upload:
        camera_disabled=True
        st.markdown(body="Please clear the image",unsafe_allow_html=False)
    else:
        camera_disabled=False
photo=st.camera_input("take a photo",disabled=camera_disabled)
if photo:
    encode=get_file(photo)
elif file_upload:
    encode=get_file(file_upload)
else:
    encode=None
submit=st.button("submit the image")
text_area=st.text_area("Make the needed adjustments.",height=100)  


prompt="""


"You are an AI-powered chatbot that converts hand-drawn wireframes, sketches, or diagrams into clean and structured HTML & CSS code. Your task is to analyze an uploaded image, extract the layout structure, and generate semantically correct, responsive HTML and CSS code. Ensure that the output follows best practices, including accessibility, modern styling techniques, and responsive design. If the image is unclear, ask users for clarification. Always provide concise and well-documented code snippets. Offer suggestions for improvements when needed. Maintain a professional, helpful, and friendly tone in interactions. in single file "

"""

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": f"follow the instruction {prompt}"                #f-string is important 
            },
            {                                                             #error  Object of type set is not JSON serializab
                "type": "image_url",
                "image_url": f"data:image/jpeg;base64,{encode}" 
            },
            {
                "type":"text",
                "text":f" coustomize the by {text_area}"
            }
        ] 
    }  
]

if submit:    
        with st.spinner("coding"):
            response=get_response(messages)
            code=st.write(response)
            st.code(code)
