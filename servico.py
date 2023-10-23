import json

class Servico:
  def __init__(self, id, desc, valor, duracao):
    self.__id = id
    self.__desc = desc
    self.__valor = valor
    self.__duracao = duracao
  def setId(self, id):
    if id != '': self.__id = id
    else: raise ValueError()
  def setDesc(self, desc):
    if desc != '': self.__desc = desc
    else: raise ValueError()
  def setValor(self, valor):
    if valor != '': self.__valor = valor
    else: raise ValueError()
  def setDuracao(self, duracao):
    if duracao != '': self.__duracao = duracao
    else: raise ValueError()
  def getId(self, id):
    return self.__id
  def getDesc(self, desc):
    return self.__desc
  def getValor(self, valor):
    return self.__valor
  def getDuracao(self, duracao):
    return self.__duracao
  def __str__(self):
    return f'{self.__id} - {self.__desc} - {self.__valor} - {self.__duracao}'

class NServico:
  __servicos = []
  @classmethod
  def inserir(cls, s):
    NServico.abrir()
    id = 0
    for servico in cls.__servicos:
      if servico.getId() > id:
        id = servico.getId()
    s.setId(id+1)
    cls.__servicos.append(s)
    NServico.salvar()
  @classmethod
  def listar(cls):
    NServico.abrir()
    return cls.__servicos
  @classmethod
  def listar_id(cls, id):
    NServico.abrir()
    for s in cls.__servicos:
      if id == s.getId():
        return s
    return None
  @classmethod
  def atualizar(cls, snew):
    NServico.abrir()
    servico = cls.listar_id(snew.get_id())
    servico.set_nome(snew.get_nome())
    servico.set_email(snew.get_email())
    servico.set_fone(snew.get_fone())
    NServico.salvar()
  @classmethod
  def excluir(cls, s):
    NServico.abrir()
    for servico in cls.__servicos:
      if servico.getId() == s.getId():
        cls.__servicos.remove(servico)
    NServico.salvar()
  @classmethod
  def abrir(cls):
    try:
      cls.__servicos = []
      with open("./servicos.json", mode="r") as f:
        s = json.load(f)
        for servico in s:
          s = Servico(servico["_Servico__id"], servico["_Servico__nome"],
                     servico["_Servico__email"], servico["_Servico__fone"])
          cls.__servicos.append(s)
    except FileNotFoundError:
      pass
  @classmethod
  def salvar(cls):
    with open("./servicos.json", mode="w") as f:
      json.dump(cls.__servicos, f, default=vars)
