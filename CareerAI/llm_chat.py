# Import necessary packages
from ibm_watson_machine_learning.foundation_models import Model # type: ignore
import gradio as gr # type: ignore

from dotenv import load_dotenv #type: ignore
import os 

# Load environment variables from .env file
load_dotenv()

# Set up the API key and project ID for IBM Watson 
watsonx_API = os.getenv('WATSONX_API')
project_id= os.getenv('PROJECT_ID')

# Set credentials to use the model
my_credentials = {
    "apikey": watsonx_API,
    "url": "https://us-south.ml.cloud.ibm.com"
}

# Model and project settings
model_id = "meta-llama/llama-2-13b-chat"  # Directly specifying the LLAMA2 model

space_id = None
verify = False
gen_parms = {
        "max_new_tokens": 1000,
        "temperature": 0.1
}

# Initialize the model
model = Model(model_id, my_credentials, gen_parms, project_id, space_id, verify)

# Function to generate a response from the model
def generate_response(prompt_txt):
    generated_response = model.generate(prompt_txt)

    # Extract and return the generated text
    generated_text = generated_response["results"][0]["generated_text"]
    return generated_text

# Create Gradio interface
chat_application = gr.Interface(
    fn=generate_response,
    allow_flagging="never",
    inputs=gr.Textbox(label="Input", lines=2, placeholder="Type your question here..."),
    outputs=gr.Textbox(label="Output"),
    title="Watsonx.ai Chatbot",
    description="Ask any question and the chatbot will try to answer."
)

# Launch the app
chat_application.launch()