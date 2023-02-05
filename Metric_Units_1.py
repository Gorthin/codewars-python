'''
Scientists working internationally use metric units almost exclusively. Unless that is, they wish to crash multimillion dollars worth of equipment on Mars.

Your task is to write a simple function that takes a number of meters, and outputs it using metric prefixes.

In practice, meters are only measured in "mm" (thousandths of a meter), "cm" (hundredths of a meter), "m" (meters) and "km" (kilometers, or clicks for the US military).

For this exercise we just want units bigger than a meter, from meters up to yottameters, excluding decameters and hectometers.

All values passed in will be positive integers. e.g.

meters(5);
// returns "5m"

meters(51500);
// returns "51.5km"

meters(5000000);
// returns "5Mm"
'''


def meters(x):
    #your code here
    unit = ''
    
    if x < 10**3: 
        unit = ''
        
    elif x < 10**6:
        x = x /(10**3)
        unit = 'k'
        
    elif x < 10**9:
        x = x /(10**6)
        unit = 'M'
        
    elif x < 10**12:
        x = x/(10**9)
        unit = 'G'
        
    elif x < 10**15:
        x = x/(10**12)
        unit = 'T'
        
    elif x < 10**18:
        x = x/(10**15)
        unit = 'P'
        
    elif x < 10**21:
        x = x/(10**18)
        unit = 'E'
        
    elif x < 10**24:
        x = x/(10**21)
        unit = 'Z'

    else: 
        x = x/(10**24)
        unit = 'Y'
    
    if x % 1 == 0:
        x = int(x)
    
    return "{}{}{}".format(x, unit, 'm') 

# second solution
# import math
# def meters(x):
#     rank = int(math.log10(x)) / 3
#     symbol = ['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']
#     return "{0:g}{1}m".format(float(x) / 1000 ** rank, symbol[rank])


# third solution
# def meters(x):
#     #your code here
#     arr = ['','k','M','G','T','P','E','Z','Y']
#     count=0
#     while x>=1000 :
#         x /=1000.00 
#         count+=1
#     if int(x)==x:
#         x=int(x) 
#     return str(x)+arr[count]+'m'