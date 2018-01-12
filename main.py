from datetime import datetime

Y = int(datetime.now().year)
M = int(datetime.now().month)
D = int(datetime.now().day)
H = int(datetime.now().hour)


def jdate(y, m, d, h):
    if m == 1 or m == 2:
        m += 12
        y -= 1

    a = int(y/100)
    b = int(a/4)
    c = 2 - a + b
    e = 365.25 * (y + 4716)
    f = 30.6001 * (M+1)
    jd = c+d+e+f-1524.5
    jdo = jd - 1
    d = jd - 2451545.0
    do = jdo - 2451545.0
    gmst = 18.697374558 + (24.06570982441908 * d)
    print(gmst)


jdate(Y, M, D, H)

