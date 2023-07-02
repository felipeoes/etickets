from etickets.models import *
from datetime import datetime, timedelta
import random
random.seed(1)

def create_random_date(min_datetime=datetime(2022, 6, 1), max_datetime=datetime(2023, 6, 1)):
    delta = max_datetime - min_datetime
    delta_seconds = delta.total_seconds()

    random_seconds = random.uniform(0, delta_seconds)
    random_datetime = min_datetime + timedelta(seconds=random_seconds)
    return random_datetime




def create_fake_data(n_users: int = 100, n_tickets: int = 500, n_trades: int = 2, n_tickets_per_user_min=1,n_tickets_per_user_max=10):

    # Create users
    users = []
    for i in range(n_users):
        user = User(
            name=f'User {i}',
            email=f'email_teste{i}@mail.com',
            phone=f'123456789{i}',
            cpf=f'123456789{i}',
            address=f'Rua {i}',
            cep=f'12345678{i}',
            city=f'Cidade {i}',
            state=f'Estado {i}'
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
    #     ticket = Ticket(
    #         name=f'Ingresso {i}',
    #         event=f'Evento {i}',
    #         datetime=datetime.now(),
    #         sector=f'Setor {i}',
    #         location=f'Local {i}'
    #     )
    #     try:
    #         ticket.save()
    #         tickets.append(ticket)
    #     except Exception as e:
    #         print(f'Error creating ticket {ticket}. Error: {e}')

    # Create trades
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
    #         # Create the EXCHANGE_OFFER relashionship among tickets with a datetime property 
    #         user_ticket.interests.connect(interest_ticket, {'start_relationship_date':create_random_date()})

    # for trade in trades:
    #     trade.tickets.connect(random.choice(tickets))
    #     trade.users.connect(random.choice(users))

    # return users, tickets, trades