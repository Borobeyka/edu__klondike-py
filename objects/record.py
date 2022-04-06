class Record:
    
    def __init__(self, path):
        self.path = path

    def load(self):
        try:
            file = open(self.path, "r")
            score = int(file.readline())
        except:
            file = open(self.path, "a+")
            file.writelines("0")
            score = 0
        file.close()
        return score

    def write(self, score):
        with open(self.path, "w") as file:
            return file.writelines(str(score))