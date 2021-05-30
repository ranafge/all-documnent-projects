# Explanation
#
# (?<!\S) Whitespace boundary at the left
# (?=\w{5}) Assert 5 word chars
# [^\W\d]* Match optional word chars without a digit
# \d Match 1 digit
# \w* Match optional word chars
# (?!\S) Assert a whitespace boundary at the right
