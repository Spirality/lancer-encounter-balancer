from LCP_Reader import LCP_Reader
from pathlib import Path
import os

class Encounter:
    def __init__(self, name='New Encounter'):
        self.name = name
        self.npcs = []
        