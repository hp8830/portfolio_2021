class Target:
    def __init__(self, target):
        self.target = target 
    
    def target_achieved(self, actualscore):
        if actualscore.score.target >= self.target:
            return True
        else:
            return False


class Actual: 

    def __init__(self, score):
        self.score = score
