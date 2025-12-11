import json
import os

class MessageManager:
    dialogues = {}
    @staticmethod
    def start_up():
        if not os.path.exists('dialogues.json'):
            with open('dialogues.json', 'w') as f:
                json.dump({}, f)
        with open('dialogues.json', 'r') as f:
            MessageManager.dialogues = json.load(f)
    start_up()
    @staticmethod
    def load_dialogues(npcid):
        return MessageManager.dialogues.get(npcid)