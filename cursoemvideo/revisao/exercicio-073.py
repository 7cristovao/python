''' Crie uma tupla preenchida com os 20 primeiros colocados 
    da Tabela do Campeonato Brasileiro de Futebol, na ordem
    de colocação. Depois mostre: 
    
    A) Apenas os 5 primeiros colocados.
    B) Os últimos 4 colocados da tabela.
    C) Uma lista com os times em ordem alfabética.
    D) Em que posição na tabela está o time da Chapecoense.
    '''

classificacao = (
    "Palmeiras",
    "Flamengo",
    "Internacional",
    "Grêmio",
    "São Paulo",
    "Atlético Mineiro",
    "Athletico Paranaense",
    "Cruzeiro",
    "Botafogo",
    "Santos",
    "Bahia",
    "Fluminense",
    "Corinthians",
    "Chapecoense",
    "Ceará",
    "Vasco da Gama",
    "América Mineiro",
    "Sport",
    "Vitória",
    "Paraná",
)

print(f'Os cinco primeiro colocados foram: {classificacao[0:5]}')
print(f'Os quatro últimos da tabela foram: {classificacao[0:-4]}')
print(f'Eis a lista dos times em ordem alfabética: {sorted(classificacao)}')
print(f'O time da Chapecoense está na posição {classificacao.index("Chapecoense")}')