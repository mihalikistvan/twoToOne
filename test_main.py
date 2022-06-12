from main import * 

def test():
    assert longest("aretheyhere", "yestheyarehere")== "aehrsty"
    assert longest("loopingisfunbutdangerous", "lessdangerousthancoding")== "abcdefghilnoprstu"
    assert longest("inmanylanguages", "theresapairoffunctions")== "acefghilmnoprstuy"
    assert longest("lordsofthefallen", "gamekult")== "adefghklmnorstu"
    assert longest("codewars", "codewars")== "acdeorsw"
    assert longest("agenerationmustconfrontthelooming", "codewarrs")== "acdefghilmnorstuw"