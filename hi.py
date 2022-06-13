import os
import argparse as ap

parser = ap.ArgumentParser(description='install or setup')
parser.add_argument('-i', '--install', type=bool, default=False, help='default is Ture')
parser.add_argument('-s', '--setup', type=bool, default=False, help='default is False')

args = parser.parse_args()

if args.install:
    envs = os.listdir('.')
    envs.remove("hi.py")
    envs.remove('README.md')
    for path in envs:
        os.system(f"cd {path} && . bin/activate && pip install -r requirements.txt")

if args.setup:
    envs = os.listdir('.')
    envs.remove("hi.py")
    envs.remove('README.md')
    for path in envs:
        os.system(f"cd {path} && . bin/activate && pip freeze > requirements.txt && deactivate")