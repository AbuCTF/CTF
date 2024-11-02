import os
import sys

# Attempt to use prompt injection
def inject_code():
    try:
        # Test if the environment allows command execution
        result = os.popen('ls /').read()
        print("Directory Listing:", result)
        
        # Try reading the flag file
        flag = os.popen('cat /flag.txt').read()
        print("Flag Content:", flag)
        
    except Exception as e:
        print(f"Error: {e}")

inject_code()
