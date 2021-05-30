# You may use a Negative Lookahead (?!...) to ensure that content following the
# digit is not a letter you set
#
# Here an example where all digits followed by any of there char GJK are not concerned by the suppression

import re
sentenc = "On 11 December 2008, India entered the 3G arena 1A 3J 5K"
print(re.sub(r"\d(?![GJKA])", "",sentenc ))

print(re.sub(r"\d(?![GJK])", '' ,sentenc ))
# On  December , India entered the 3G arena A 3J 5K

sentence ="{\"data\":{\"correlation_id:\"51g0d88f-3ab8-4mom-betb-b31ed6e1662z\",\"u_originator_uri"
print(re.search(r"correlation_id:(.*\W+)",sentence))
