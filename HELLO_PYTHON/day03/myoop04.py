class Biden:
    def __init__(self):
        self.dollar =10
    def reelected(self):
        self.dollar+=10
        
class Xi:
    def __init__(self):
        self.cnt_nuclear = 200
    def war(self,cnt):
        self.cnt_nuclear -= cnt
    
class Musk:
    def __init__(self):
        self.cnt_spacex=100
    def twitter(self,cnt):
        self.cnt_spacex +=cnt

class Kyeongseok(Biden, Xi, Musk):
    def __init__(self):
        Biden.__init__(self)
        Xi.__init__(self)
        Musk.__init__(self)
        super().__init__()
        self.weight=3.2
    def now(self):
        self.weight = 80

if __name__ =='__main__':
    ks = Kyeongseok()
    print("dollar",ks.dollar)
    print("cnt_nuclear",ks.cnt_nuclear)
    print("cnt_spaceX",ks.cnt_spacex)
    print("weight",ks.weight)
    ks.now()
    ks.reelected()
    ks.war(10)
    ks.twitter(10)
    print("dollar",ks.dollar)
    print("cnt_nuclear",ks.cnt_nuclear)
    print("cnt_spaceX",ks.cnt_spacex)
    print("weight",ks.weight)
    