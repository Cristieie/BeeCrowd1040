notas = input().split(" ")

for i in range(4):
    notas[i] = float(notas[i])

media = (2*notas[0] + 3*notas[1] + 4*notas[2] + 1*notas[3])/10

if media >= 7.0:
    sit = "Aluno aprovado."
elif media >= 5.0:
    sit = "Aluno em exame."
else:
    sit = "Aluno reprovado."

if sit == "Aluno em exame.":
    n_ex = float(input())
    media_f = (media + n_ex)/2
    if media_f >= 5.0:
        n_sit = "Aluno aprovado."
        print("Media: {:.1f}".format(media))
        print(sit)
        print("Nota do exame: {:.1f}".format(n_ex))
        print(n_sit)
        print("Media final: {:.1f}".format(media_f))
    else:
        n_sit = "Aluno reprovado."
        print("Media: {:.1f}".format(media))
        print(sit)
        print("Nota do exame: {:.1f}".format(n_ex))
        print(n_sit)
        print("Media final: {:.1f}".format(media_f))
else:
    print("Media: {:.1f}".format(media))
    print(sit)
