class Solution:    
    def digitdecrypt(self, num):
            #type num: int
            #return type: int
            
            strin = str(num)
            num1 = 0
            while len(strin) > 1:
                num1 = 0
                for i in strin:
                    num1 = num1 + int(strin)
                strin = str(num1)
            return num1
            
            #TODO: Write code below to returnn an int with the solution to the prompt.
            pass
 
def main():
    input1= input()
    input2 = int(input1)

    
    tc1 = Solution()
    ans = tc1.digitdecrypt(input2)
    print(ans)
    
if __name__ == "__main__":
    main()
