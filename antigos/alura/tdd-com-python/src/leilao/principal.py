from dominio import Usuario, Lance, Leilao

gui = Usuario('Gui', 150)
yuri = Usuario('Yuri', 50)
paulo = Usuario('Paulo', 500)

lance_do_gui = Lance(gui, 150.0)
lance_do_yuri = Lance(yuri, 100.0)
lance_do_paulo = Lance(paulo, 155.0)
lance_do_paulo = Lance(paulo, 160.0)

leilao = Leilao('Celular')
leilao.lance.append(lance_do_paulo)
leilao.lance.append(lance_do_gui)
leilao.lance.append(lance_do_yuri)

for lance in leilao.lance:
    print(f'O usuário {lance.usuario.nome} deu um lance de {lance.valor}')
