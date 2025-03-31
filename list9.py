def find_missing_number(nums):
    n = len(nums) + 1  
    expected_sum=n*(n+1)//2  
    actual_sum = sum(nums)  
    return expected_sum - actual_sum  


nums = [1, 2, 4, 5, 6] 
print(find_missing_number(nums))
def anagram(str1,str2):
    str1=str1.lower()
    str2=str2.lower()
    return sorted(str1)==sorted(str2)
str1="bad"
str2="dab"
if anagram(str1,str2):
    print("anagram")
else:
    print("not anagram")
print("--------------")
def sieve_of_eratosthenes(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
print(sieve_of_eratosthenes(10))

