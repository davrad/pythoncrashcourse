def make_shirt(size='L',message='I love Python'):
    print("A shirt size", size)
    print("Message:",message)
make_shirt('M')
make_shirt('L')
s = "Strange women lying in ponds distributing swords\n"
s += "is no basis for a system of government!"
make_shirt(message=s,size='L')