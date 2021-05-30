import re
soup = 1
soup.select("a[href*=location]")
soup.find_all("a", href=re.compile("location"))
