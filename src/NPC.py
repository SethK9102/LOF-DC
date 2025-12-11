
from main import rprint
import os
import time
from dialogues import MessageManager

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
wait = time.sleep

class NPC:
    def __init__(self, name="Shopkeeper", npcid=0):
        self.name = name
        self.npcid = npcid
        self.dialogues = self.load_dialogues(self.npcid)
        

    def load_dialogues(self, npcid):
        return MessageManager.load_dialogues(npcid)
    


    