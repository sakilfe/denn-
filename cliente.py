import json

class Cliente:
  def __init__(self, id, nome, email, fone):
    self.__id = id
    self.__nome = nome
    self.__email = email
    self.__fone = fone
  def setId(self, id):
    if id != '': self.__id = id
    else: raise ValueError()
  def setNome(self, nome):
    if nome != '': self.__nome = nome
    else: raise ValueError()
  def setEmail(self, email):
    if email != '': self.__email = email
    else: raise ValueError()
  def setFone(self, fone):
    if fone != '': self.__fone = fone
    else: raise ValueError()
  def getId(self):
    return self.__id
  def getNome(self):
    return self.__nome
  def getEmail(self):
    return self.__email
  def getFone(self):
    return self.__fone
  def __str__(self):
    return f'{self.__id} - {self.__nome} - {self.__email} - {self.__fone}'

class NCliente:
  __clientes = []
  @classmethod
  def inserir(cls, c):
    NCliente.abrir()
    id = 0
    for cliente in cls.__clientes:
      if cliente.getId() > id:
        id = cliente.getId()
    c.setId(id+1)
    cls.__clientes.append(c)
    NCliente.salvar()
  @classmethod
  def listar(cls):
    NCliente.abrir()
    return cls.__clientes
  @classmethod
  def listar_id(cls, id):
    NCliente.abrir()
    for c in cls.__clientes:
      if id == c.getId():
        return c
    return None
  @classmethod
  def atualizar(cls, cnew):
    NCliente.abrir()
    cliente = cls.listar_id(cnew.getId())
    cliente.setNome(cnew.getNome())
    cliente.setEmail(cnew.getEmail())
    cliente.setFone(cnew.getFone())
    NCliente.salvar()
  @classmethod
  def excluir(cls, id):
    NCliente.abrir()
    for cliente in cls.__clientes:
      if cliente.getId() == id:
        cls.__clientes.remove(cliente)
    NCliente.salvar()
  @classmethod
  def abrir(cls):
    try:
      cls.__clientes = []
      with open("./clientes.json", mode="r") as f:
        s = json.load(f)
        for cliente in s:
          c = Cliente(cliente["_Cliente__id"], cliente["_Cliente__nome"],
                     cliente["_Cliente__email"], cliente["_Cliente__fone"])
          cls.__clientes.append(c)
    except FileNotFoundError:
      pass
  @classmethod
  def salvar(cls):
    with open("./clientes.json", mode="w") as f:
      json.dump(cls.__clientes, f, default=vars)
