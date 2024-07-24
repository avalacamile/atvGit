class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome            
        self.idade = idade          
        self._cpf = cpf             
        self.__endereco = None      

    def consultar_cpf(self):
        return self._cpf           

    def alterar_cpf(self, novo_cpf):
        self._cpf = novo_cpf       

    def consultar_endereco(self):
        return self.__endereco    

    def alterar_endereco(self, novo_endereco):
        self.__endereco = novo_endereco   


class Cliente(Pessoa):
    def __init__(self, nome, idade, cpf, endereco):
        super().__init__(nome, idade, cpf)
        self.endereco = endereco   

    def exibir_informacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'CPF: {self.consultar_cpf()}')
        print(f'Endereço: {self.consultar_endereco()}')
        print(f'Endereço de entrega: {self.endereco}')


class Teste:
    def __init__(self):
        pass

    def executar(self):
        
        cliente1 = Cliente('Maria', 30, '123.456.789-00', 'Rua Principal, 123')

        
        print('Informações antes da alteração:')
        cliente1.exibir_informacoes()

        cliente1.alterar_cpf('987.654.321-00')
        cliente1.alterar_endereco('Av. Nova, 456')

        print('\nInformações após a alteração:')
        cliente1.exibir_informacoes()


if __name__ == "__main__":
    teste = Teste()
    teste.executar()

