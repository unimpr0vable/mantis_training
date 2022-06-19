from model.project import Project
import random
import string

testdata = [
    Project(name="name"+str(random.randint(1, 99999)), description="description"+str(random.randint(1, 99999)))
]

#def random_string(prefix, maxlen):
    #symbols = string.ascii_letters + string.digits +  " "*10
    #return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#testdata = [Group(name="", header="", footer="")] + [
    #Group(name="test_group_name", header="test_group_header", footer="test_group_footer")] + [
    #Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    #for i in range(5)]