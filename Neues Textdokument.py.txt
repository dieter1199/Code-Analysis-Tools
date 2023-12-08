import os

# Unsicheres Code-Snippet, das ein Command-Injection-Sicherheitsrisiko enthält
user_input = input("Bitte geben Sie einen Dateinamen ein: ")
os.system(f"cat {user_input}")
