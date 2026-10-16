import os

from dotenv import load_dotenv

load_dotenv()
environment = os.getenv("ENVIRONMENT")
model_name = os.getenv("MODEL_NAME")

print("Environment:", environment)
print("Model Name:", model_name)
