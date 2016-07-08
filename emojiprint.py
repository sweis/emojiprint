from codes import EMOJI_UNICODE_VALUES

#print len(EMOJI_UNICODE)
vals = EMOJI_UNICODE_VALUES
hexstring = "A65EB6C09CE4632F2D849F9CF81BF54B83771CDA"

#v = reduce(lambda x, y: (x<<4) + y, map(lambda x: int(x, 16), hexstring))
#print v

v = int(hexstring, 16)
mod = len(EMOJI_UNICODE_VALUES)

out = u""
while v > 0:
  m = v % mod
  v = v / mod
  out += vals[m]

print out
