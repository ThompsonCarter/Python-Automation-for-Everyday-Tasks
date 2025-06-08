from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv("API_KEY")
# Never commit .env.
# Use GitHub Secrets or Docker secrets in CI.
