from fuzzywuzzy import process
from utils.speedtest import speedtest

class Filter:
    
    block_row = []
    with open("./PromptFilter/block-key.txt", "r", encoding="utf-8") as b:
        for row in b.readlines():
            block_row.append(row.replace("\n", ""))
        

    @classmethod
    @speedtest
    def is_valid_prompt(self, text: str):
        text = text.split(" ")
        for word in text:
            if (process.extractOne(word, self.block_row)[1]) >= 80:
                return False
            return True

        
