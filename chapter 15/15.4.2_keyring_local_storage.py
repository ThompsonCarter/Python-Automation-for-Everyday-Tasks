# Install: pip install keyring
import keyring, getpass
service = "automation_bot"
keyring.set_password(service, "EMAIL_PASS", getpass.getpass())
pwd = keyring.get_password(service, "EMAIL_PASS")