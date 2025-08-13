from dotenv import load_dotenv
import os
load_dotenv()
class Config:
    base_url = "https://reinstatements-delegations-reinstatement-responsg-iymj66chvq-uc.a.run.app/"
    language = "en_US"  # Options: "Español", "en_US", "it_IT", "pt_BR"
    # Login Credentials
    email = os.getenv("USER_EMAIL") #Add your username here
    password = os.getenv("USER_PASSWORD") #Add your password here
