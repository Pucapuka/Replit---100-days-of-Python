#Creating dictionary with items with empty value
webSiteData = {'name':None, 'url':None, 'description':None,'rating': None}

#Assigning values
for name in webSiteData.keys():
  webSiteData[name] = input(f"\033[33m{name}: \033[32m")
  
print()  
for name, value in webSiteData.items():
  print (f"\033[33m{name}: {value}")
