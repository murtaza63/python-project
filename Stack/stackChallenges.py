print("1st Challenge Reverse an array")

array = [1,2,3,4,5]
def printInReverse(arr):
   n = len(arr)
   stack = []
   for i in arr:
      stack.append(i)
   for i in range(0, n):
      arr[i] = stack.pop()
   return arr
print("Original Array ", array)  
print("Reversed Array",printInReverse(array))




print("Next Challenge Balance Parentheses")
testing1 = "h((e))llo(world)()"
testing2 = "(hello world"

def checkParentheses(string:str) -> bool:
   stack = []
   for character in string:
      if character == "(":
         stack.append(character)
      elif character == ")":
         if len(stack) == 0:
            return False
         else:
            stack.pop()
   return len(stack) == 0

print(checkParentheses(testing2))
