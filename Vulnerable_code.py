import subprocess

# Beispiel für unsicheren Code
def unsichere_subprocess_nutzung(user_input):
    subprocess.call("echo " + user_input, shell=True)

# Beispielhafter Aufruf
unsichere_subprocess_nutzung("Hello World")
