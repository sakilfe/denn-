from cliente import Cliente, NCliente

class View:
    @classmethod
    def ClienteInserir(cls, nome, email, fone):
        cliente = Cliente(0, nome, email, fone)
        NCliente.inserir(cliente)

    @classmethod
    def ClienteListar(cls): 
        return NCliente.listar()

    @classmethod
    def ClienteAtualizar(id, nomenv, emailnv, fonenv):
        cliente = Cliente(id, nomenv, emailnv, fonenv)
        NCliente.atualizar(cliente)

    @classmethod
    def ClienteExcluir(cls, id):
        NCliente.excluir(id)
