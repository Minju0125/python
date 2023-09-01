class gugu:
    def __init__(self, Dan):
        self.Dan = Dan
    
    def getGugu(self, minDan, maxDan):
        res=""
        for i in range (2, 9+1) :
            for j in range (1, 9+1) :
                res+= "{}*{}={}\r".format(i,j, i*j)
                res+="\r"
        print(res)

if __name__ == "__main__" :
    def getGugu(self, minDan, maxDan):