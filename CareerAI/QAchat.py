from ibm_watson_machine_learning.foundation_models import Model # type: ignore
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams # type: ignore
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes, DecodingMethods # type: ignore

from dotenv import load_dotenv #type: ignore
import os 

# Load environment variables from .env file
load_dotenv()

# Set up the API key and project ID for IBM Watson 
watsonx_API = os.getenv('WATSONX_API')
project_id= os.getenv('PROJECT_ID')

generate_params = {
    GenParams.MAX_NEW_TOKENS: 250
}

model = Model(
    model_id = 'meta-llama/llama-2-13b-chat', # you can also specify like: ModelTypes.LLAMA_2_70B_CHAT
    params = generate_params,
    credentials={
        "apikey": watsonx_API,
        "url": "https://us-south.ml.cloud.ibm.com"
    },
    project_id= project_id
    )

q = "How to be happy?"
generated_response = model.generate(prompt=q)
print(generated_response['results'][0]['generated_text'])