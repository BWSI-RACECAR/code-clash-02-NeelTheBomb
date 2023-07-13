class Solution:    
    def digitdecrypt(self, num):
            #type num: int
            #return type: int
            strin = str(num)
            for i in range(len(strin-1)):
                 num = num + int(strin[i])
            return num
            
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
