class Ball(object):
    # your code goes here
    def __init__(self, ball_type=None):
        self.ball_type = ball_type
        
        if self.ball_type is None:
            self.ball_type = 'regular'
        print(self.ball_type)  
