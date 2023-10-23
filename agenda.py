import datetime
import json

class Agenda:
  def __init__(self, id, data, conf, idCliente, idServico):
    self.__id = id
    self.__data = 0
    self.__conf = conf
    self.__idCliente = idCliente
    self.__idServico = idServico
    self.setData(data)
  def setId(self, id):
    if id != '': self.__id = id
    else: raise ValueError()
  def setData(self, data):
    if data != '': self.__data = data
    else: raise ValueError()
  def setConf(self, conf):
    if conf != '': self.__conf = conf
    else: raise ValueError()
  def setIdCliente(self, idCliente):
    if idCliente != '': self.__idCliente = idCliente
    else: raise ValueError()
  def setIdServico(self, idServico):
    if idServico != '': self.__idServico = idServico
    else: raise ValueError()
  def getId(self):
    return self.__id
  def getData(self):
    return self.__data
  def getConf(self):
    return self.__conf
  def getIdCliente(self):
    return self.__idCliente
  def getIdServico(self):
    return self.__idServico
  def to_json(self):
    return { '__id' : self.__id, '__data' : self.__data.strftime('%d/%m/%Y %H:%M'), '__confirmado' : self.__conf, '__idCliente' : self.__idCliente, '__idServico' : self.__idServico}
  def __str__(self):
    return f'{self.__id} - {self.__data} - {self.__conf} - {self.__idCliente} - {self.__idServico}'

class NAgenda:
  __agendas = []
  @classmethod
  def inserir(cls, a):
    NAgenda.abrir()
    id = 0
    for agenda in cls.__agendas:
      if agenda.getId() > id:
        id = agenda.getId()
    a.setId(id+1)
    cls.__agendas.append(a)
    NAgenda.salvar()
  @classmethod
  def listar(cls):
    NAgenda.abrir()
    return cls.__agendas
  @classmethod
  def listar_id(cls, id):
    NAgenda.abrir()
    for a in cls.__agendas:
      if id == a.getId():
        return a
    return None
  @classmethod
  def atualizar(cls, anew):
    NAgenda.abrir()
    agenda = cls.listar_id(anew.get_id())
    agenda.set_nome(anew.get_nome())
    agenda.set_email(anew.get_email())
    agenda.set_fone(anew.get_fone())
    NAgenda.salvar()
  @classmethod
  def excluir(cls, a):
    NAgenda.abrir()
    for agenda in cls.__agendas:
      if agenda.getId() == a.getId():
        cls.__agendas.remove(Agenda)
    NAgenda.salvar()
  @classmethod
  def abrir(cls):
    try:
      cls.__agendas = []
      with open("./agendas.json", mode="r") as f:
        s = json.load(f)
        for agenda in s:
          a = Agenda(agenda["_id"], datetime.datetime.strptime(agenda["_data"], "%d/%m/%Y %H:%M"), agenda["_confirmado"], agenda["_id_cliente"], agenda["_id_servico"])
          cls.__agendas.append(a)
    except FileNotFoundError:
      pass
  @classmethod
  def salvar(cls):
    with open("./agendas.json", mode="w") as f:
      json.dump(cls.__agendas, f, default=vars)
