'''
Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).

All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.

Examples
* With input "10.0.0.0", "10.0.0.50"  => return   50 
* With input "10.0.0.0", "10.0.1.0"   => return  256 
* With input "20.0.0.10", "20.0.1.0"  => return  246
'''

def ips_between(start, end):
    diffs = [int(b)-int(a) for a,b in zip(start.split('.'), end.split('.'))]
    sum_of_ip_address = 0
    for d in diffs:
        sum_of_ip_address *= 256
        sum_of_ip_address += d
    return sum_of_ip_address

# second solution
# from ipaddress import ip_address

# def ips_between(start, end):
#     return int(ip_address(end)) - int(ip_address(start))

# third solution
# def ips_between(start, end):
#     a = sum([int(e)*256**(3-i) for i, e in enumerate(start.split('.'))])
#     b = sum([int(e)*256**(3-i) for i, e in enumerate(end.split('.'))])
#     return abs(a-b)