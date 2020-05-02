# Python program to compute 
# factorial of big numbers 
  
# Maximum number of digits in  
# output 
MAX=100000
  
# This function multiplies x 
# with the number represented by res[]. 
# res_size is size of res[] or 
# number of digits in the number 
# represented by res[]. This function 
# uses simple school mathematics 
# for multiplication. 
# This function may value of res_size 
# and returns the new value of res_size 
def multiply(x, res, res_size): 
  
    # Initialize carry 
    carry = 0
  
    # One by one multiply n with 
    # individual digits of res[] 
    for i in range(res_size): 
        prod = res[i] * x + carry 
  
        # Store last digit of 
        # 'prod' in res[] 
        res[i] = prod % 10
  
        # Put rest in carry 
        carry = prod // 10
  
    # Put carry in res and 
    # increase result size 
    while (carry): 
        res[res_size] = carry % 10
        carry = carry // 10
        res_size+=1
  
    return res_size 
  
  
# This function finds 
# power of a number x 
def power(x,n): 
      
    # printing value "1" for power = 0 
    if (n == 0) :  
        print("1") 
    return
      
    res=[0 for i in range(MAX)] 
    res_size = 0
    temp = x 
  
    # Initialize result 
    while (temp != 0): 
        res[res_size] = temp % 10; 
        res_size+=1
        temp = temp // 10
  
  
    # Multiply x n times 
    # (x^n = x*x*x....n times) 
    for i in range(2, n + 1): 
        res_size = multiply(x, res, res_size) 
  
    print(x , "^" , n , " = ",end="") 
    for i in range(res_size - 1, -1, -1): 
        print(res[i], end="") 
  
  
# Driver program 
  
""" exponent = 100
base = 2
power(base, exponent)  """
  
# This code is contributed 
# by Anant Agarwal. 

k = 110147360880977326145454323208221071089784097565692230883406944964885283866809403126305248705095738645969886839883972829698185023465616223853188508575646895119112813982949306635369092626464429143567242208129503631864031757968830572178817452781169212310750061873270404450233561253396099991206848635615097818383
print(2 ** k)