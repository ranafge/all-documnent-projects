import re

s4 = '5 days 19 hours'

pattern = r"(?P<days>(\d+)(\sdays))? ?(?P<hours>(\d+)(\shours))? ?(?P<minutes>(\d+)(\sminutes))?"

match = re.match(pattern, s4)
print(match.groupdict())
