import re


def censor(s1):
    pattern = re.compile(r'\bw*(frack)\w*\b', re.I)
    return pattern.sub("CENSORED", s1)


print(censor("Frack you"))                #"CENSORED you"
print(censor("I hope you fracking die"))  #"I hope you CENSORED die"
print(censor("you fracking Frack"))

