from NPC import NPC
from main import rprint
import os
import time


clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
wait = time.sleep

class Home_NPC(NPC):
    def __init__(self, name="Archivist", npcid=1):
        super().__init__(name, npcid)
        self.dialogues = self.load_dialogues(self.npcid)

    def talk(self, event):
        match event:
            case "start":
                for i in self.dialogues['start']:
                    rprint(i)
                    input("Press Enter to continue...")
                    
                    clear()
