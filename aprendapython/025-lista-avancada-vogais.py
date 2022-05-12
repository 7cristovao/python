def vogais(s):
	return [i for i in s if i.lower() in ['a','e','i','o','u']]

print(vogais('abcde'))