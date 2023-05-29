from etickets.models import *
from datetime import datetime
import random


def create_fake_data(n_users: int = 10, n_tickets: int = 10, n_trades: int = 2):

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

    # Create tickets
    tickets = []
    for i in range(n_tickets):
        ticket = Ticket(
            name=f'Ingresso {i}',
            event=f'Evento {i}',
            datetime=datetime.now(),
            sector=f'Setor {i}',
            location=f'Local {i}'
        )
        try:
            ticket.save()
            tickets.append(ticket)
        except Exception as e:
            print(f'Error creating ticket {ticket}. Error: {e}')

    # Create trades
    trades = []
    for i in range(n_trades):
        trade = Trade(
            status=i,
        )
        try:
            trade.save()
            trades.append(trade)
        except:
            print(f'Error creating trade {trade}')

    if len(users) == 0 or len(tickets) == 0 or len(trades) == 0:
        print('Error creating fake data. No data was created.')
        return

    # Create relationships randomly
    for user in users:
        owned_ticket = random.choice(tickets)
        interest_ticket = random.choice(tickets)

        user.tickets.connect(owned_ticket)

        # increase quantity of owned ticket
        owned_ticket.quantity += 1
        owned_ticket.save()

        # check if user already owns the interest ticket
        if interest_ticket in user.tickets.all():
            continue

        user.interests.connect(interest_ticket)

    for trade in trades:
        trade.tickets.connect(random.choice(tickets))
        trade.users.connect(random.choice(users))

    return users, tickets, trades