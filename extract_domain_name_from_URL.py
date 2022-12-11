'''
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
'''

def domain_name(url):
    url = url.replace('www.','')
    url = url.replace('https://','')
    url = url.replace('http://','')
    
    return url[0:url.find('.')]

# second solution
# import re
# def domain_name(url):
#     return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')

# third solution
# def domain_name(url):
#     return url.split("//")[-1].split("www.")[-1].split(".")[0]