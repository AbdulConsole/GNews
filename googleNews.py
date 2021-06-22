from GoogleNews import GoogleNews

harvest=GoogleNews()
harvest=GoogleNews(period='7d')

#Change your country...
harvest.search('nigeria')
result=harvest.result()
for x in result:
    print("-"*40)
    print("\033[2;31;43m Title--",x['title'],"\n\033[0;0m")
    
    print("Date & Time --",x['date'],"\n")
    print("Description--",x['desc'],"\n")
    print("Link--",x['link'],"\n")
    print('Code with love by AbdulConsole',"\n")
    

