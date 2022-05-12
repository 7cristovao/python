def obterDominio(s):
	return s.split('@')[-1]

print(obterDominio('email@dominio.com'))