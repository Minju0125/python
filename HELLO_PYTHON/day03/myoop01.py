# OopTest
# 자바는 원파일 원클래스
# 책에 나와있음 한 클래스에 들어잇음

class Animal:
    def __init__(self):
        self.flagLife =True
    def die(self):
        self.flagLife = False
        
class Human(Animal):
    def __init__(self):
        super().__init__()
        self.job="백수"        
    def chippo(self, job):
        self.job = job    
        
if __name__ == '__main__':
    hum=Human()
    print("job:", hum.job)
    print("flagLife:",hum.flagLife)
    hum.die()
    hum.chippo("프로그래머")
    print("job:", hum.job)
    print("flagLife:",hum.flagLife)
