# Lista para armazenar as informações 
tarefas = []
# Iniciamos com um Loop While
while True:
  # Menu do software 
  print('»»————-　Sistemas De Tarefas　————-««')
  print('1 - Cadastrar nova tarefa')
  print('2 - Marcar tarefa como concluída')
  print('3 - Relatório Das Tarefas')
  print('4 - Deletar Tarefa')
  print('5 - Sair do programa')
  print('»»————-　★　————-««')
  # Opção para escolher alguma função do menur do software
  opcao = int(input('Qual opção você deseja escolher: '))
  # Nesse if, ele irá representar o que a função 1 do software irá fazer (Cadastrar nova tarefa)
  if opcao == 1:
    print('»»————- Cadastrar nova tarefa ————-««')
    # Digitar o nome da tarefa que o usuário deseja cadastrar
    nome = input('Digite o nome da tarefa: ')
    # Digitar a descrição da tarefa que o usuário cadastrou
    descricao = input('Digite a descrição da tarefa: ')
    # Irá adiconar o nome (que seria a tarefa) e a descrição (descrição da tarefa)
    tarefas.append({
      'nome': nome,
      'descricao': descricao,
      # O concluído está "false", pois o marcar tarefa como concluído é outra função do software
      'concluido': False
    })
    print('Tarefa cadastrada com sucesso!')
    print('»»————- ★ ————-««')
  # Nesse elif, ele irá representar o que a função 2 do software irá fazer (Marcar tarefa como concluída)
  elif opcao == 2:
    print('»»————- Marcar tarefa como concluída ————-««')
    # O usuário irá escolher a tarefa cadastrada pelo nome
    nome = input('Digite o nome da tarefa: ')
    # Nesse laço for, seria se a tarefa adicionada está dentro da lista "tarefas"
    for tarefa in tarefas:
      # O if, é se estiver o nome da tarefa dentro da lista
      if tarefa['nome'] == nome:
        # Ele irá transformar seu valor booleano que lá no início era false (concluido) para true
        tarefa['concluido'] = True
        print('Tarefa marcada como concluída com sucesso!')
        print('»»————- ★ ————-««')
        break
  # Nesse elif, ele irá representar o que a função 3 do software irá fazer (Relatório Das Tarefas)
  elif opcao == 3:
    print('»»————- Relatório Das Tarefas ————-««')
    # Nesse laço for, seria se a tarefa adicionada, a descrição e se a tarefa já está concluída estão dentro da lista "tarefas"
    for tarefa in tarefas:
      print(f'Nome: {tarefa["nome"]}')
      print(f'Descrição: {tarefa["descricao"]}')
      print(f'Concluída: {tarefa["concluido"]}')
      print('»»————- ★ ————-««')
  # Nesse elif, ele irá representar o que a função 3 do software irá fazer (Relatório Das Tarefas)
  elif opcao == 5:
    # Final do software
    print('»»————- Sistemas De Tarefas ————-««')
    print('»»————- ★ ————-««')
    print('»»————- Obrigado por usar o sistema ★ ————-««')
    print('»»————- ★ ————-««')
    break
  # Nesse elif, ele irá representar o que a função 3 do software irá fazer (Deletar Tarefa)
  elif opcao == 4:
    print('»»————- Deletar Tarefa ————-««')
    # O usuário irá inserir p nome da tarefa que ele cadastrou, para deletar a mesma 
    nome = input('Digite o nome da tarefa que deseja deletar: ')
    # Nesse laço for, seria se a tarefa adicionada dentro da lista "tarefas" e assim ele rá encontrar a tarefa pelo o seu nome
    for i, tarefa in enumerate(tarefas):
      if tarefa['nome'] == nome:
        # Irá ser deletada
        del tarefas[i]
  # Esse else, é se inserir alguma opção que não esteja no menu, irá apresentar "Opção inválida!"
  else:
    print('Opção inválida!')
    print('»»————- ★ ————-««')
