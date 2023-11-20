tarefas = []
while True:
  print('»»————-　Sistemas De Tarefas　————-««')
  print('1 - Cadastrar nova tarefa')
  print('2 - Marcar tarefa como concluída')
  print('3 - Relatório Das Tarefas')
  print('4 - Deletar Tarefa')
  print('5 - Sair do programa')
  print('»»————-　★　————-««')

  opcao = int(input('Qual opção você deseja escolher: '))
  if opcao == 1:
    print('»»————- Cadastrar nova tarefa ————-««')
    nome = input('Digite o nome da tarefa: ')
    descricao = input('Digite a descrição da tarefa: ')
    tarefas.append({
      'nome': nome,
      'descricao': descricao,
      'concluido': False
    })
    print('Tarefa cadastrada com sucesso!')
    print('»»————- ★ ————-««')
  elif opcao == 2:
    print('»»————- Marcar tarefa como concluída ————-««')
    nome = input('Digite o nome da tarefa: ')
    for tarefa in tarefas:
      if tarefa['nome'] == nome:
        tarefa['concluido'] = True
        print('Tarefa marcada como concluída com sucesso!')
        print('»»————- ★ ————-««')
        break
  elif opcao == 3:
    print('»»————- Relatório Das Tarefas ————-««')
    for tarefa in tarefas:
      print(f'Nome: {tarefa["nome"]}')
      print(f'Descrição: {tarefa["descricao"]}')
      print(f'Concluída: {tarefa["concluido"]}')
      print('»»————- ★ ————-««')
  elif opcao == 5:
    print('»»————- Sistemas De Tarefas ————-««')
    print('»»————- ★ ————-««')
    print('»»————- Obrigado por usar o sistema ★ ————-««')
    print('»»————- ★ ————-««')
    break
  elif opcao == 4:
    print('»»————- Deletar Tarefa ————-««')
    nome = input('Digite o nome da tarefa que deseja deletar: ')
    for i, tarefa in enumerate(tarefas):
      if tarefa['nome'] == nome:
        del tarefas[i]
  else:
    print('Opção inválida!')
    print('»»————- ★ ————-««')
