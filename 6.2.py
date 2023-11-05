#Se o fatiamento do string s[-2:-1], onde s ="ABCDEFGHI"
#dá como resultado o string H, quais valores de x e y devemos
#colocar em [x:y:-1] para obter o mesmo resultado de
#s[-2:-1]?

#Quando usamos o comando "print(s)", a primeira variável define onde os caracteres começarão a ser contados
#sendo que os positivos se iniciam com o valor "print(s[0::])" na esquerda e "print(s[-9::]) na direita
#A parte intermediária do comando define onde é o ponto de parada da exibição da string
#A parte final define quantos saltos e em qual direção serão dados, sendo possível "saltar" caracteres da string

#Portanto, onde s = "ABCDEFGHI" ...

s = "ABCDEFGHI"

if s[-2:-1:] == s[7:6:-1]:
    print("s[-2:-1] é igual a s[7:8:-1], ambos representam a letra %c" % s[7:6:-1])
