# Aula referente ao Video Aula 09 do Curso em Vídeo

frase = 'Curso em Video Python'
print(frase[1:15:2]) # fatiando a frase

frase = 'Curso em Vídeo Python'
print(frase.capitalize()) # iniciar a frase com a primeira palavra com letra maiúscula

frase = 'Curso em Vídeo Python'
print(frase.count('o')) # contar quantas vezes o mesmo caractere aparece numa frase

frase = 'Curso em Vídeo Python'
print(frase.find('Marlon')) # find irá procurar um valor/string dentro da frase retornando o mesmo ou -1 indicando que não encontrou o valor/string

frase = 'Curso em Vídeo Python'
print(frase.title()) # a cada frase digitada após o espaço irá iniciar com a primeira letra em maiúsculo

frase = 'Curso em Vídeo Python'
print(frase.lower()) # todos os caracteres dentro da frase será passado para a letra minúscula

frase = 'Curso em Vídeo Python'
print(frase.upper()) # todos os caracteres dentro da frase será passando para a letra maiúscula

frase = 'Curso em Vídeo Python'
print(frase.split()) # dividir a frase; no caso em uma lista

frase = 'Curso em Vídeo Python'
#frase = frase.replace('Python','PHP') # pro caso de não fazer o método direto no print
print(frase.replace('Python','PHP')) # o replace irá "trocar" o valor/string selecionada por outro valor/string

frase = 'Curso em Vídeo Python'
print('Curso' in frase) # usa-se para verificar se o conteúdo está na frase

frase = 'Curso em Vídeo Python'
print(frase.find('Curso')) # find irá procurar na frase se contém a palavra "Curso" na posição em que ele foi "salvo" na memória, por exemplo "Curso" está na posição 0 na frase 

frase = 'Curso em Vídeo Python'
print(frase.strip()) # strip elimina espaços inúteis, seja no início ou no final da frase; porém; não o espaço do meio entre as frases
 
