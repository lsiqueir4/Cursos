from datetime import datetime, timedelta

class Projeto:
    def __init__(self, nome):
        self.nome =nome
        self.tarefas = [] 

    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self, descricao, vencimento=None):
        self.tarefas.append(Tarefa(descricao, vencimento))
        
    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]
    
    def procurar(self, descricao):
        #Possivel IndexError
        return [tarefa for tarefa in self.tarefas
                if tarefa.descricao == descricao] [0]
    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefas pendente(s))'

class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.vencimento = vencimento
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append('(Concluída)')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('(Vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(vence em{dias} dias)')

        return f'{self.descricao} ' + ''.join(status)


def main():
   casa = Projeto('Tarefas da casa')
   casa.add('Passar roupa', datetime.now())
   casa.add('Lavar Prato', datetime.now() + timedelta(days=3))
   for tarefa in casa:
       (print(f'- {tarefa}'))
   print(casa)

if __name__ == '__main__':
    main()
