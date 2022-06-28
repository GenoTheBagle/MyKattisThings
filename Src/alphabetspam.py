chs = input().strip()
chs = [ord(c) for c in chs]
chs_t = len(chs)

up_ch = [c for c in chs if 64 < c < 91]
up_ch = len(up_ch)
lo_ch = [c for c in chs if 96 < c < 123]
lo_ch = len(lo_ch)

dash_t = chs.count(95) # _ unicode
f = chs_t - up_ch - lo_ch - dash_t

print(dash_t/chs_t)
print(lo_ch/chs_t)
print(up_ch/chs_t)
print(f/chs_t)