"""
This will contain some garbage code golfed, hard to read / maintain / comprehend
"""
_p=print

def e2(s):
    a,b,*c=s
    return "FTarlusee"[a==b::2]+"".join(c)


if __name__ == "__main__":
    _p((lambda a,b,c:eval(a*b+c))("b+",3,"b**7"))
    _p(e2("aa soap"))
    _p(e2("ab corn"))