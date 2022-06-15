class VoterException(Exception):
    pass


try:
    x = 17
    if int(x) < 18:
        raise VoterException("person not eligible for vote")
except VoterException as s:
    print(s)

print("hello")
