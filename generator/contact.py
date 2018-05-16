from model.contact import Contact
import string
import random
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", address="", homephone="",
                    mobilephone="", workphone="", email="", email2="", email3="")] + [
               Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 20),
                       address=random_string("address", 20), homephone=random_string("12", 5),
                       mobilephone=random_string("34", 5), workphone=random_string("56", 5),
                       email=random_string("email1", 5),
                       email2=random_string("email2", 5), email3=random_string("email3", 5))
               for i in range(n)
           ]
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json",indent=2)
    out.write(jsonpickle.encode(testdata))
