# a=5
# b=3
# print(a&b) #101&011=001
# print(a|b) #101|011=111
# print(a^b) #101^011=110
# print(~a) #positve(n)=Negative(n+1),negative(n)=positive(n-1)
# # left shift
# x=10
# print(x<<1)
# # right shift
# print(x>>1)
# Even or odd
def number(n):
    if n^1==n+1:
        return True
    else:
        return False
n=int(input("Enter a number:"))
if number(n):
    print("Number is even")
else:
    print("Number is odd")