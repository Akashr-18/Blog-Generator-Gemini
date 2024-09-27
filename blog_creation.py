import os
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def gemini_blog_creation(image, input):
    """
    Input: image and input
    Output: response
    """
    model = genai.GenerativeModel('gemini-pro')
    model_vision = genai.GenerativeModel('gemini-pro-vision')

    if (input != "") and (image == ""):
        print("Only input text is provided")
        system_message = """
               As a blog post content creator, you will be receiving topic name in the text format. 
               Your task is to generate a well-structured and engaging English language blog post centered around that topic. 
               To ensure clarity and organization, please include several subtopics within the main topic, each with their own distinct section or heading. 
               Write in a conversational yet informative tone, aiming to provide value and insights to readers while keeping them engaged throughout the post.
               """
        response = model.generate_content([system_message, input])

    elif (input == "") and (image != ""):
        print("Only input image is provided")
        system_message = """
               You will receive input as image. Describe the image in one sentence.
               As a blog post content creator, your task is to generate a well-structured and engaging blog post centered around that topic. 
               Blog post content should be written in standard American English format.
               To ensure clarity and organization, please include several subtopics within the main topic, each with their own distinct section or heading. 
               Write in a conversational yet informative tone, aiming to provide value and insights to readers while keeping them engaged throughout the post.
               """
        response = model_vision.generate_content([system_message, image])

    elif (input != "") and (image != ""):
        print("Both input and image are present")
        system_message = """
               You are content creator for blog post.
               You will receive input as both image and text.
               Your task is to generate a blog post based on the text and image provided for you.
               """
        response = model_vision.generate_content([system_message, image, input])

    else:
        response = ""

    return response



