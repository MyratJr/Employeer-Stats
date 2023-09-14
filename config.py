from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST=os.environ.get("DB_HOST")
DB_PORT=os.environ.get("DB_PORT")
DB_NAME=os.environ.get("DB_NAME")
DB_USER=os.environ.get("DB_USER")
DB_PASS=os.environ.get("DB_PASS")

SMTP_USER_TO=os.environ.get("SMTP_USER_TO")
SMTP_USER=os.environ.get("SMTP_USER")
SMTP_PASSWORD=os.environ.get("SMTP_PASSWORD")

SECRET_AUTH=os.environ.get("SECRET_AUTH")

DB_HOST_TEST=os.environ.get("DB_HOST_TEST")
DB_PORT_TEST=os.environ.get("DB_PORT_TEST")
DB_NAME_TEST=os.environ.get("DB_NAME_TEST")
DB_USER_TEST=os.environ.get("DB_USER_TEST")
DB_PASS_TEST=os.environ.get("DB_PASS_TEST")