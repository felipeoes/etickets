from etickets.models import *
from datetime import datetime
from faker import Faker
import random

random.seed(1)

fake = Faker('pt_BR')

fake_shows = [{
    'name': 'Adele Live in Rio',
    'location': 'Estádio do Maracanã, Rio de Janeiro',
    'datetime': datetime(2017, 3, 18, 21, 0, 0),
    'tickets': [
        {
            'name': 'Adele Live in Rio - Pista',
            'sector': 'Pista',
            'type': 'show',
            'quantity': 100
        },
        {
            'name': 'Adele Live in Rio - Cadeira',
            'sector': 'Cadeira',
            'type': 'show',
            'quantity': 50
        },
        {
            'name': 'Adele Live in Rio - Camarote',
            'sector': 'Camarote',
            'type': 'show',
            'quantity': 20
        }
    ]
}, {
    'name': 'Coldplay Paradise Tour',
    'location': 'Allianz Parque, São Paulo',
    'datetime': datetime(2017, 11, 7, 21, 0, 0),
    'tickets': [
        {
            'name': 'Coldplay Paradise Tour - Pista',
            'sector': 'Pista',
            'type': 'show',
            'quantity': 100
        },
        {
            'name': 'Coldplay Paradise Tour - Cadeira',
            'sector': 'Cadeira',
            'type': 'show',
            'quantity': 50
        },
        {
            'name': 'Coldplay Paradise Tour - Camarote',
            'sector': 'Camarote',
            'type': 'show',
            'quantity': 20
        }
    ]
}, {
    'name': 'Beyoncé Formation World Tour',
    'location': 'Arena Fonte Nova, Salvador',
    'datetime': datetime(2017, 9, 10, 21, 0, 0),
    'tickets': [
        {
            'name': 'Beyoncé Formation World Tour - Pista',
            'sector': 'Pista',
            'type': 'show',
            'quantity': 100
        },
        {
            'name': 'Beyoncé Formation World Tour - Cadeira',
            'sector': 'Cadeira',
            'type': 'show',
            'quantity': 50
        },
        {
            'name': 'Beyoncé Formation World Tour - Camarote',
            'sector': 'Camarote',
            'type': 'show',
            'quantity': 20
        }
    ]
}, {
    'name': 'Ed Sheeran Divide World Tour',
    'location': 'Estádio Beira-Rio, Porto Alegre',
    'datetime': datetime(2017, 5, 17, 21, 0, 0),
    'tickets': [
        {
            'name': 'Ed Sheeran Divide World Tour - Pista',
            'sector': 'Pista',
            'type': 'show',
            'quantity': 100
        },
        {
            'name': 'Ed Sheeran Divide World Tour - Cadeira',
            'sector': 'Cadeira',
            'type': 'show',
            'quantity': 50
        },
        {
            'name': 'Ed Sheeran Divide World Tour - Camarote',
            'sector': 'Camarote',
            'type': 'show',
            'quantity': 20
        }
    ]
}, {
    'name': 'Bruno Mars 24K Magic Tour',
    'location': 'Jeunesse Arena, Rio de Janeiro',
    'datetime': datetime(2017, 11, 18, 21, 0, 0),
    'tickets': [
        {
            'name': 'Bruno Mars 24K Magic Tour - Pista',
            'sector': 'Pista',
            'type': 'show',
            'quantity': 100
        },
        {
            'name': 'Bruno Mars 24K Magic Tour - Cadeira',
            'sector': 'Cadeira',
            'type': 'show',
            'quantity': 50
        },
        {
            'name': 'Bruno Mars 24K Magic Tour - Camarote',
            'sector': 'Camarote',
            'type': 'show',
            'quantity': 20
        }
    ]
}, {
    'name': 'Taylor Swift Reputation Stadium Tour',
    'location': 'Arena Corinthians, São Paulo',
    'datetime': datetime(2017, 7, 18, 21, 0, 0),
    'tickets': [
        {
            'name': 'Taylor Swift Reputation Stadium Tour - Pista',
            'sector': 'Pista',
            'type': 'show',
            'quantity': 100
        },
        {
            'name': 'Taylor Swift Reputation Stadium Tour - Cadeira',
            'sector': 'Cadeira',
            'type': 'show',
            'quantity': 50
        },
        {
            'name': 'Taylor Swift Reputation Stadium Tour - Camarote',
            'sector': 'Camarote',
            'type': 'show',
            'quantity': 20
        }
    ]
}, {
    'name': 'Rihanna Diamonds World Tour',
    'location': 'Estádio Mané Garrincha, Brasília',
    'datetime': datetime(2017, 9, 17, 21, 0, 0),
    'tickets': [
        {
            'name': 'Rihanna Diamonds World Tour - Pista',
            'sector': 'Pista',
            'type': 'show',
            'quantity': 100
        },
        {
            'name': 'Rihanna Diamonds World Tour - Cadeira',
            'sector': 'Cadeira',
            'type': 'show',
            'quantity': 50
        },
        {
            'name': 'Rihanna Diamonds World Tour - Camarote',
            'sector': 'Camarote',
            'type': 'show',
            'quantity': 20
        }
    ]
}, {
    'name': 'U2 The Joshua Tree Tour',
    'location': 'Estádio do Morumbi, São Paulo',
    'datetime': datetime(2017, 10, 19, 21, 0, 0),
    'tickets': [
        {
            'name': 'U2 The Joshua Tree Tour - Pista',
            'sector': 'Pista',
            'type': 'show',
            'quantity': 100
        },
        {
            'name': 'U2 The Joshua Tree Tour - Cadeira',
            'sector': 'Cadeira',
            'type': 'show',
            'quantity': 50
        },
        {
            'name': 'U2 The Joshua Tree Tour - Camarote',
            'sector': 'Camarote',
            'type': 'show',
            'quantity': 20
        }
    ]
}, {
    'name': 'Justin Timberlake The 20/20 Experience World Tour',
    'location': 'Estádio Mineirão, Belo Horizonte',
    'datetime': datetime(2017, 11, 20, 21, 0, 0),
    'tickets': [
        {
            'name': 'Justin Timberlake The 20/20 Experience World Tour - Pista',
            'sector': 'Pista',
            'type': 'show',
            'quantity': 100
        },
        {
            'name': 'Justin Timberlake The 20/20 Experience World Tour - Cadeira',
            'sector': 'Cadeira',
            'type': 'show',
            'quantity': 50
        },
        {
            'name': 'Justin Timberlake The 20/20 Experience World Tour - Camarote',
            'sector': 'Camarote',
            'type': 'show',
            'quantity': 20
        }
    ]
}, {
    'name': 'Lady Gaga Joanne World Tour',
    'location': 'Maracanãzinho, Rio de Janeiro',
    'datetime': datetime(2017, 12, 21, 21, 0, 0),
    'tickets': [
        {
            'name': 'Lady Gaga Joanne World Tour - Pista',
            'sector': 'Pista',
            'type': 'show',
            'quantity': 100
        },
        {
            'name': 'Lady Gaga Joanne World Tour - Cadeira',
            'sector': 'Cadeira',
            'type': 'show',
            'quantity': 50
        },
        {
            'name': 'Lady Gaga Joanne World Tour - Camarote',
            'sector': 'Camarote',
            'type': 'show',
            'quantity': 20
        }
    ]
}]

cities = [
    {
        'name': 'Rio de Janeiro',
        'state': 'RJ'
    },
    {
        'name': 'São Paulo',
        'state': 'SP'
    },
    {
        'name': 'Belo Horizonte',
        'state': 'MG'
    },
    {
        'name': 'Brasília',
        'state': 'DF'
    },
]

def create_fake_data(n_users: int = 10):
    # Create users
    users = []
    for i in range(n_users):
        city = random.choice(cities)
        user = User(
            name=fake.name(),
            email=fake.email(),
            phone=f'123456789{i}',
            cpf=f'123456789{i}',
            address=f'Rua {i}',
            cep=f'12345678{i}',
            city=city['name'],
            state=city['state']
        )

        try:
            user.save()
            users.append(user)
        except Exception as e:
            print(f'Error creating user {user}. Error: {e}')


    
    # Create tickets
    tickets = []
    # types = [t[1] for t in TICKET_TYPES]
    for show in fake_shows:
        for ticket in show['tickets']:
            ticket = Ticket(
                    name=ticket['name'],
                    event=show['name'],
                    datetime=show['datetime'],
                    sector=ticket['sector'],
                    type=ticket['type'],
                    location=show['location']
                )
            try:
                ticket.save()
                tickets.append(ticket)
            except Exception as e:
                print(f'Error creating ticket {ticket}. Error: {e}')
    
    # for i in range(
    #     ticket = Ticket(
    #         name=f'Ingresso {i}',
    #         event=f'Evento {i}',
    #         datetime=datetime.now(),
    #         sector=f'Setor {i}',
    #         type=random.choice(TICKET_TYPES),
    #         location=f'Local {i}'
    #     )
    #     try:
    #         ticket.save()
    #         tickets.append(ticket)
    #     except Exception as e:
    #         print(f'Error creating ticket {ticket}. Error: {e}')

    # # Create trades
    # trades = []
    # for i in range(n_trades):
    #     trade = Trade(
    #         status=i,
    #     )
    #     try:
    #         trade.save()
    #         trades.append(trade)
    #     except:
    #         print(f'Error creating trade {trade}')

    # if len(users) == 0 or len(tickets) == 0 or len(trades) == 0:
    #     print('Error creating fake data. No data was created.')
    #     return

    # # Create relationships randomly
    # for user in users:
    #     owned_ticket = random.choice(tickets)
    #     interest_ticket = random.choice(tickets)        

    #     user.tickets.connect(owned_ticket)

    #     # increase quantity of owned ticket
    #     owned_ticket.quantity += 1
    #     owned_ticket.save()

    #     # check if user already owns the interest ticket
    #     if interest_ticket in user.tickets.all():
    #         continue

    #     user.interests.connect(interest_ticket)

    #     for user_ticket in user.tickets.all():
    #         user_ticket.interests.connect(interest_ticket)

    # for trade in trades:
    #     trade.tickets.connect(random.choice(tickets))
    #     trade.users.connect(random.choice(users))

    # return users, tickets, trades