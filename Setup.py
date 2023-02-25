import os, sys
try:
    __import__("Setup").Main()
except Exception as e:
    exit(str(e))
