import os
envs = os.listdir('.')
envs.remove("hi.py")
for path in envs:
    os.system(f"cd {path} && . bin/activate && pip freeze > requirements.txt")