


class Filter:
    
    block_row = []
    with open("./PromptFilter/block-key.txt", "r", encoding="utf-8") as b:
        for row in b.readlines():
            block_row.append(row.replace("\n", ""))
        
    
    @classmethod
    def is_valid_prompt(self, text):
        for block in self.block_row:
            if block in text:
                return False
        return True
        
if __name__ == "__main__":
    print(
        Filter.is_valid_prompt("")
        )