#rodarflask.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


import enum
from datetime import datetime


app = Flask(__name__)
db = SQLAlchemy(app)

if __name__ == "__main__": app.run()

#CLIENTE
"""
    Módulo cliente -
    Classe Cliente -
    Atributos:
        _id       - chave primária    - informado
        _nome     - nome do cliente   - informado
        _codigo   - codigo do cliente - informado
        _cnpjcpf  - cnpj ou cpf       - informado
        _tipo     - tipo de cliente   - informado
                    (Pessoa Fisica ou Juridica)
"""

class Cliente(db.Model):
    __tablename__ = "CLIENTE"
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String)
    codigo = db.Column(db.String, unique = True)
    cnpjcpf = db.Column (db.String, unique = True)
    
    def __init__(self, id, nome, codigo, cnpjcpf):
        self._id = id
        self._nome = nome
        self._codigo = codigo
        self._cnpjcpf = cnpjcpf

    def str(self):
        string = "\nId={3} Codigo={2} Nome={1} CNPJ/CPF={0} ".format(self._cnpjcpf, self._codigo,
                                                                             self._nome, self._id)
        return string

if __name__ == '__main__':
    cliente = Cliente(1, "Jose Maria", 100, '200.100.345-34' )
    print(cliente.str())

#PRODUTO

"""
    Módulo produto
    Classe Produto
    Atributos :
        id            - informado
        codigo        - informado
        descricao     - informado
        valorUnitario - informado.
"""

class Produto(db.Model):
    __tablename__ = "PRODUTO"
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String, unique=True)
    descricao = db.Column(db.String)
    valorUnitario = db.Column(db.Float)

    def __init__(self, id, codigo, descricao, valorUnitario):
        self._id = id
        self._codigo = codigo
        self._descricao = descricao
        self._valorUnitario = valorUnitario

    def getDescricao(self):
        return self._descricao

    def getValorUnitario(self):
        return self._valorUnitario

    def str(self):
        string = "\nId={3} Codigo={2} Descricao={1} Valor Unitario={0}".format(self._valorUnitario, self._descricao,
                                                                               self._codigo, self._id)
        return string

if __name__ == '__main__':
    produto = Produto(1, 100, 'Arroz', 5.5)
    print(produto.str())


#ITEM

"""
    Módulo itemnotafiscal
    Classe ItemNotaFiscal
    Atributos :
        id         - informado
        sequencial - informado
        quantidade - informado
        produto    - informado
        valor      - calculado.
"""

class ItemNotaFiscal(db.Model):
    __tablename__ = "PRODUTO"
    id = db.Column(db.Integer, primary_key=True)
    id_notafiscal = db.Column(db.Integer, db.ForeignKey("PRODUTO"))
    sequencial = db.Column(db.String)
    quantidade = db.Column(db.Integer)
    produto = db.Column(db.String, db.ForeignKey("PRODUTO.codigo"))
    descricao = db.Column(db.String, db.ForeignKey("PRODUTO.descricao"))
    valorUnitario = db.Column(db.Float, db.ForeignKey("PRODUTO.valorUnitario"))
    valorItem = db.Column(db.Float)
	
    nota_fiscal = db.relationship("NotaFiscal", foreign_keys=id_notafiscal)
    produto = db.relationship("Produto", foreign_keys=produto)
    descricao = db.relationship("Produto", foreign_keys=descricao)
    valor_unitario = db.relationship("Produto", foreign_keys=valorUnitario)

    def __init__(self, id, sequencial, quantidade, produto):
        self._id = id
        self._sequencial = sequencial
        self._quantidade = quantidade
        self._produto = produto
        self._descricao = self._produto.getDescricao()
        self._valorUnitario = self._produto.getValorUnitario()
        self._valorItem = float(self._quantidade * self._valorUnitario)

    def str(self):
        string = "\nId={5} Sequencial={4} Quantidade={3} Produto={2} Valor Unitario={1} Valor Item={0}".format(
            self._valorItem,
            self._valorUnitario,
            self._descricao,
            self._quantidade,
            self._sequencial,
            self._id)
        return string

    def getId(self):
        return self._id

    def getvalorItem(self):
        return self._valorItem

    def getValorUnitario(self):
        return self._valorUnitario

    def getDescricao(self):
        return self._descricao

    def getQuantidade(self):
        return self._quantidade

    def getSequencial(self):
        return self._sequencial

if __name__ == '__main__':
    produto = Produto(1, 100, 'Arroz', 5.5)
    item = ItemNotaFiscal(1, 1, 12, produto)
    print(item.str())

#NOTA FISCAL

"""
  Módulo main - objetos de classes definidas em
                módulos do pacote projeto01.
"""

def main():
    cli = Cliente(1, "Jose Maria", 100, "200.100.345-34")

    p1 = Produto(1, 100, "Arroz Agulha", 5.5)
    it1 = ItemNotaFiscal(1, 1, 10, p1)

    p2 = Produto(2, 200, "Feijao Mulatinho", 8.5)
    it2 = ItemNotaFiscal(2, 2, 10, p2)

    p3 = Produto(3, 300, "Macarrão Fortaleza", 4.5)
    it3 = ItemNotaFiscal(3, 3, 10, p3)

    nf = NotaFiscal(1, 100, cli)

    nf.adicionarItem(it1)

    nf.adicionarItem(it2)

    nf.adicionarItem(it3)

    nf.calcularNotaFiscal()

    print("Valor Nota Fiscal= " + str(nf.valorNota))

    nf.imprimirNotaFiscal()

if __name__ == '__main__':
    main()

#NOTA FISCAL DO PRODUTO

"""
"""

class NotaFiscal_Produto():

    def __init__(self):
        self._notasFiscais = []
        self._produtos = []

    def adicionarNotaProduto(self, nota, produto):
        if isinstance(nota, NotaFiscal) and isinstance(produto, Produto):
            self._notasFiscais.append(nota)
            self._produtos.append(produto)


#NOTA FISCAL

"""
    Módulo notafiscal -
    Classe NotaFiscal -
        Atributos :
            id        - informado.
            codigo    - informado.
            data      - informado.
            cliente   - informado.
            items     - informado
            valornota - calculado.
"""

class NotaFiscal(db.Model):
    __table__ = "NOTA FISCAL"
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String)
    cliente = db.Column(db.String, db.ForeignKey("CLIENTE.codigo"))
    data = db.Column(db.Datatime)
    valorNota = db.Column(db.Float)
    
    cliente = db.relationship('Cliente', foreign_keys=codigo)
    
    def __init__(self, Id, codigo, cliente):
        self._Id = Id
        self._codigo = codigo
        self._cliente = cliente
        self._data = datetime.today()
        self._itens = []
        self._valorNota = 0.0

    def setCliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente = cliente
            return self._cliente

    def adicionarItem(self, item):
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)

    def calcularNotaFiscal(self):
        valor = 0.0
        for item in self._itens:
            valor +=  item._valorItem
        self.valorNota = valor

    def imprimirNotaFiscal(self):
        print(f'''---------------------------------------------------------------------------------------------------
NOTA FISCAL \t\t\t\t {self._data}
Cliente: {self._cliente._codigo}\t\t\t\t Nome: {self._cliente._nome}
CPF/CNPJ: {self._cliente._cnpjcpf}
---------------------------------------------------------------------------------------------------
ITENS
---------------------------------------------------------------------------------------------------
Seq                        Descrição                           QTD   Valor Unit         Preço
---- -------------------------------------------------------- ----- ------------ ------------------''')
        for c in range(0, 3):
            print('{0:<17}{1:^34}{2:^28}{3:<8}{4}'.format(self._itens[c].getSequencial(),  self._itens[c].getDescricao(), self._itens[c].getQuantidade(), self._itens[c].getValorUnitario(), self._itens[c].getvalorItem()))

        print('Valor Total:', self.valorNota)

#TIPO CLIENTE

"""
    Modulo tipocliente -
    Classe TipoCliente - Enumeration de Tipos de Cliente
"""

class TipoClient(enum.Enum):
    PESSOA_FISICA = 1
    PESSOA_JURIDICA = 2

if __name__ == '__main__':
    print("Os numeros enum sao: ")
    for tipo in (TipoClient):
        print(type(tipo))
        print(tipo)

