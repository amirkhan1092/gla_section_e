
import urllib.request as url

f = url.urlopen('https://github.com/amirkhan1092/gla_section_e/commit/4707b5ac904c4ff656b4c60977e9fb6157273744#commitcomment-33235980')
data = f.read()

a = open('C:\\Users\\Amirkhan\\Desktop\\index.htm','wb')

a.write(data)
a.close()
print(data)

