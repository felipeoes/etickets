from etickets.models import *
from datetime import datetime, timedelta
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

    def create_random_date(min_datetime=datetime(2022, 6, 1), max_datetime=datetime(2023, 6, 1)):
    delta = max_datetime - min_datetime
    delta_seconds = delta.total_seconds()

    random_seconds = random.uniform(0, delta_seconds)
    random_datetime = min_datetime + timedelta(seconds=random_seconds)
    return random_datetime




def create_fake_data(n_users: int = 100, n_tickets: int = 500, n_trades: int = 2, n_tickets_per_user_min=1,n_tickets_per_user_max=10):

    # def create_fake_data(n_users: int = 10):
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

    # Create tickets for each user
    n_tickets_per_user_total = 0
    for user in users:
        n_tickets_per_user = random.randint(n_tickets_per_user_min,n_tickets_per_user_max)        
        for i in range(n_tickets_per_user):
            ticket = Ticket(
                name=f'Ingresso {i+n_tickets_per_user_total}',
                event=f'Evento {i+n_tickets_per_user_total}',
                datetime=datetime.now(),
                sector=f'Setor {i+n_tickets_per_user_total}',
                location=f'Local {i+n_tickets_per_user_total}'
            )
            try:

                # increase quantity of owned ticket
                ticket.quantity += 1
                ticket.save()
                user.tickets.connect(ticket)
            except Exception as e:
                print(f'Error creating ticket {ticket}. Error: {e}')        
        n_tickets_per_user_total+=n_tickets_per_user

    for user1 in users:
        qtd_users2_sample = random.randint(0,int(len(users)*.2))
        users2_sample = random.sample(users,qtd_users2_sample)
        for user2 in users2_sample:
            if users.index(user1) != users.index(user2):
                qtd_samples1 = random.randint(0,int(len(user1.tickets.all())*.2))
                qtd_samples2 = random.randint(0,int(len(user1.tickets.all())*.2))
                # random subset sample of all the user1 tickets
                choosen_ticket_user1 = random.sample(user1.tickets.all(),qtd_samples1)
                choosen_ticket_user2 = random.sample(user2.tickets.all(),qtd_samples2)
                lowest_qtd = min([len(choosen_ticket_user1),len(choosen_ticket_user2)])
                # for each user1 chosen ticket, create a EXCHANGE_OFFER relashionship with a randomly chosen user2 ticket
                for idx in range(lowest_qtd):
                    choosen_ticket_user1[idx].interests.connect(choosen_ticket_user2[idx], {'start_relationship_date':create_random_date()})
    # for user1 in users:
    #     for user2 in users:
    #         if users.index(user1) != users.index(user2):
    #             qtd_samples1 = random.randint(0,int(len(user1.tickets.all())/2))
    #             qtd_samples2 = random.randint(0,int(len(user1.tickets.all())/2))
    #             # random subset sample of all the user1 tickets
    #             choosen_ticket_user1 = random.sample(user1.tickets.all(),qtd_samples1)
    #             choosen_ticket_user2 = random.sample(user2.tickets.all(),qtd_samples2)
    #             lowest_qtd = min([choosen_ticket_user1,choosen_ticket_user2])
    #             # for each user1 chosen ticket, create a EXCHANGE_OFFER relashionship with a randomly chosen user2 ticket
    #             for idx in range(lowest_qtd):
    #                 choosen_ticket_user1[idx].interests.connect(choosen_ticket_user2[idx], {'start_relationship_date':create_random_date()})

    # # Create tickets
    # tickets = []
    # for i in range(n_tickets):

    
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