# Descrição do Projeto: Uma plataforma de troca e (vendas de ingressos) .

# Tema: Banco de Dados em Grafos (Neo4J)

# Atualmente concertos e eventos representam uma parcela importante do mercado brasileiro, neste contexto, é muito comum encontrar pessoas que não conseguiram comprar um ingresso, ou, que compraram, mas que por alguma razão, precisam se desfazer do mesmo.
# Diante disso, as redes sociais se tornam o ambiente mais comum para fazer transações, como por exemplo: troca e compra de ingressos.
# Entretanto, estes ambientes se tornaram propicios para cometerem fraudes como ingressos falsos e falta de pagamento.
# Neste cenário, nossa plataforma busca utilizar o potencial do banco de dados grafos para automatizar essas transações e fazer trocas dinâmicas entre os usuários.

from neomodel import StructuredNode, StringProperty, IntegerProperty, DateTimeProperty, UniqueIdProperty, RelationshipTo

TRANSACTION_STATUSES = (
    (0, 'Pendente'),
    (1, 'Aceita'),
    (2, 'Recusada'),
)


class User(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(required=True)
    email = StringProperty(unique_index=True)
    phone = StringProperty(required=False)
    cpf = StringProperty(required=True)
    address = StringProperty(required=False)
    cep = StringProperty(required=False)
    city = StringProperty(required=False)
    state = StringProperty(required=False)
    tickets = RelationshipTo('Ticket', 'HAS_TICKET')
    interests = RelationshipTo('Ticket', 'INTERESTED_IN')

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<User: {}>'.format(self.name)

    def to_dict(self):
        return {
            'uid': self.uid,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'cpf': self.cpf,
            'address': self.address,
            'cep': self.cep,
            'city': self.city,
            'state': self.state,
        }


class Ticket(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(required=True)
    event = StringProperty(required=True)
    datetime = DateTimeProperty(required=True)
    location = StringProperty(required=True)
    quantity = IntegerProperty(default=0)

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Ticket: {}>'.format(self.name)

    def to_dict(self):
        return {
            'uid': self.uid,
            'name': self.name,
            'event': self.event,
            'datetime': self.datetime,
            'location': self.location,
            'quantity': self.quantity,
        }

class Trade(StructuredNode):
    uid = UniqueIdProperty()
    status = IntegerProperty(required=True, choices=TRANSACTION_STATUSES)
    tickets = RelationshipTo('Ticket', 'EXCHANGE_TICKETS')
    users = RelationshipTo('User', 'EXCHANGE_USERS')

    def __str__(self):
        return self.uid

    def __repr__(self):
        return f'<Trade: {self.uid} | Status : {self.status}>'
    
    def to_dict(self):
        return {
            'uid': self.uid,
            'status': self.status,
        }
