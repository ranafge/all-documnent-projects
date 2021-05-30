# (?!) - negative lookahead
# (?=) - positive lookahead
# (?<=) - positive lookbehind
# (?<!) - negative lookbehind
#
# (?>) - atomic group
#
# bar(?=bar)     finds the 1st bar ("bar" which has "bar" after it)
# bar(?!bar)     finds the 2nd bar ("bar" which does not have "bar" after it)
# (?<=foo)bar    finds the 1st bar ("bar" which has "foo" before it)
# (?<!foo)bar    finds the 2nd bar ("bar" which does not have "foo" before it)
#
# https://stackoverflow.com/questions/2973436/regex-lookahead-lookbehind-and-atomic-groups
# https://stackoverflow.com/questions/6109882/regex-match-all-characters-between-two-strings
#
# The [^;] is a character class, it matches everything but a semicolon
