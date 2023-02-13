def titleize(s1):
    # return " ".join([x.capitalize() for x in s1.split(" ")])
    return " ".join([x[0].upper() + x[1::] for x in s1.split(" ")])


print(titleize('this is awesome')) # "This Is Awesome"
print(titleize('oNLy cAPITALIZe fIRSt')) # "ONLy CAPITALIZe FIRSt"
print(titleize('oNLy cAPITALIZe a new fIRSt')) # "ONLy CAPITALIZe FIRSt"

