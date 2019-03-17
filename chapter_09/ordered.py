from collections import OrderedDict
#Only five words

glossary = [('dict' , 'map'),('python' , 'interpreted programming language'),
            ('print' , 'function that prints to stdout'),("':'" , 'no {,} necessary!')
            ,('list' , 'data structure')]
order = OrderedDict(glossary)
for word, meaning in order.items():
    print("Word:",word,"Meaning:",meaning)
