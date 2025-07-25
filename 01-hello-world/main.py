#print("Hello, GitHub Actions!")
import getpass
import platform
from datetime import datetime

def greet_user():
    username = getpass.getuser()
    os_info = platform.system()
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"👋 Hello, {username}!")
    print(f"🖥️ You're running this on: {os_info}")
    print(f"⏰ Current time: {time_now}")
    print("🚀 GitHub Actions is awesome!")

if __name__ == "__main__":
    greet_user()
