def tribonacci(signature, n):
    #pass
    result = signature[:]
    
    if n == 0:
        return[]
    
    while len(result) < n:
        next_num = result[-1] + result[-2] + result[-3]
        result.append(next_num)
        
    return result[:n]   



def binary_array_to_number(arr):
    return int("".join(map(str, arr)),2)
  # your code



def duplicate_count(text):
    # Your code goes here
    #pass
    text = text.lower()
    return sum(1 for char in set(text)if text.count(char) > 1) 
 
def add_binary(a,b):
    #your code here
    return bin(a + b)[2:]

def order(sentence):
    if not sentence:
        return ""
    result = []    #the list that will eventually become our setence
      
    split_up = sentence.split() #the original sentence turned into a list
  
    for i in range(1,10):
        for item in split_up:
            if str(i) in item:
                 result.append(item)    #adds them in numerical order since it cycles through i first
  
    return " ".join(result)