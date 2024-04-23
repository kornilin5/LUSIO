import os
from dotenv import load_dotenv


class Settings:
    load_dotenv()
    user = os.getenv("user")
    password = os.getenv("password")
    user_last_name = os.getenv("last_name")
    user_email = os.getenv("email")
    selenoid_url = os.getenv("selenoid_url_video")
    selenoid_url_authorization = os.getenv('selenoid_url_authorization')
    domain_url = os.getenv('domain_url')
    default_version_browser = "122.0"
    default_verion_name_browser = "chrome"


settings = Settings()
