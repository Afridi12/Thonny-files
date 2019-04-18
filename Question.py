class Question:
    def __init__(self, ques1, ans1, ans2, ans3, ans4, num):
        self.__ques1 = ques1
        self.__ans1 = ans1
        self.__ans2 = ans2
        self.__ans3 = ans3
        self.__ans4 = ans4
        self.__num = num
        
    def getAnswer(self):
        return self.__num
    
    def setAnswer(self,ans, ans1, ans2, ans3, ans4):
        if ans == ans1:
            self.__ans = ans1
        elif ans== ans2:
            self.__ans = ans2
        elif ans == ans3:
            self.__ans = ans3
        elif ans == ans4:
            self.__ans = ans4
    
    def __str__(self):
        return self.__ques1 + "\n" + '1 ' + self.__ans1 + "\n" + '2 ' + self.__ans2 + "\n" + '3 ' + self.__ans3 + "\n" + '4 ' + self.__ans4  
        
        
            

            
                     