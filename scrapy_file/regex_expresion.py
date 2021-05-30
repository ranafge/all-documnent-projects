# Pattern Details:
# \bv[\d+]+[\w.]*(?:[-\s]+(?:alpha|beta|build)[\w.]*)?
# \bv: Match v after a word boundary
# [\d+]+: Match 1+ digit or dot characters
# [\w.]*: Match 0 or more word or dot characters
# (?:[-\s]+(?:alpha|beta|build)[\w.]*)?:
# starting with whitespace or hyphen, optionally match alpha|beta|build part
# followed by 0 or more word or dot characters


'foo;;[[1;;2;;3]];;bar;;[[0;;2;;3]]'
# L = re.split(r';;(?![^[]*])', m)
# Here it will split on ;; with a negative lookahead (?![^[]*]) which means on right hand side there should not be a ] after 0 or more non-[ characters, thus ignore matching ;; inside [...].
#

# (?<=ed)         : positive lookbehind asserts that current position
#                   is immediately preceded by 'ed'
# \d+             : match 1+ digits
# (?=.*\bouter\b) : positive lookahead asserts that current match is
#                   followed by 0+ characters other than line terminators,
#                   followed by 'outer' with word boundaries


# ^               : assert beginning of string
# (?=.*\bouter\b) : positive lookahead asserts that the string
#                   contains 'outer' with word boundaries
# .*ed            : match 0+ characters other than line terminators,
#                   followed by 'ed'
# (\d+)           : match 1+ digits in capture group 1






