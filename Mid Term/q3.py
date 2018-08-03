'''
Implement a function called closest_power that meets the specifications below.

def closest_power(base, num):

#     base: base of the exponential, integer > 1
#     num: number you want to be closest to, integer > 0
#     Find the integer exponent such that base**exponent is closest to num.
#     Note that the base**exponent may be either greater or smaller than num.
#     In case of a tie, return the smaller value.
#     Returns the exponent.


 closest_power(3,12) returns 2
 closest_power(4,12) returns 2
 closest_power(4,1) returns 0
'''

def closest_power(base, num):
    test1=0
    while base**test1 <= num:
        test1 +=1  # when 3^3 in closest_power(3,12) ,27>12, test1=3
    test2 = test1-1
    
    if abs(base**test1-num) >= abs(base**test2-num): # 27-12  >  9-12
        return test2
    else:
        return test1
# correct     
