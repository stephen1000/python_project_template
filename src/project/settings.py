import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).parent
SOME_SETTING = os.getenv("SOME_SETTING")

