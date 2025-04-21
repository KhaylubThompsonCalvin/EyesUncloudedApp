# test_openai_env.py
from dotenv import load_dotenv, find_dotenv, dotenv_values
import os

# 1. Find your .env
dotenv_path = find_dotenv()
print("dotenv file found at:", dotenv_path or "None")

# 2. Show exactly what python‑dotenv reads from it:
print("Raw .env contents:", dotenv_values(dotenv_path))

# 3. Load (and override) into os.environ
load_dotenv(dotenv_path, override=True)

# 4. Finally, print the key
print("OPENAI_API_KEY is set to:", os.getenv("OPENAI_API_KEY"))


