
import os
from dotenv import load_dotenv
load_dotenv()

USE_OPENAI = True
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = "gpt-3.5-turbo"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
CHUNK_SIZE = 500
SENSITIVE_KEYWORDS = ["客戶名", "價格", "內部流程"]
