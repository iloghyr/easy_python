import urllib

str1 = "1'%3E%5C';%3C/script%3E%3E%5C%22%3E%3Cscript%3Ealert(9527)%3C/script%3E'"
print urllib.unquote(str1)
print urllib.quote(str1)