from dotenv import load_dotenv
import os
load_dotenv()
class Config:
    # Application settings
    BASE_URL: str = os.getenv("BASE_URL", "https://reinstatements-delegations-reinstatement-responsg-iymj66chvq-uc.a.run.app")
    LANGUAGE: str = os.getenv("LANGUAGE", "Español")  # Options: "Español", "en_US", "it_IT", "pt_BR"

    # Login Credentials
    EMAIL: str = os.getenv("USER_EMAIL") #Add your username here
    PASSWORD: str = os.getenv("USER_PASSWORD") #Add your password here
