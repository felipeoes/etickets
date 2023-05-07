from etickets.models import *
from datetime import datetime
import random 

def create_fake_data(n_users: int = 10, n_tickets: int = 10, n_trades: int = 2):
    # Create users
    users = []
    for i in range(n_users):
        user = User(
            name=f'User {i}',
            email= f'email_teste{i}@mail.com',
            phone=f'123456789{i}',
            cpf=f'123456789{i}',
            address=f'Rua {i}',
            cep=f'12345678{i}',
            city=f'Cidade {i}',
            state=f'Estado {i}'
        ).save()
        users.append(user)
        
    # Create tickets
    tickets = []
    for i in range(n_tickets):
        ticket = Ticket(
            name=f'Ingresso {i}',
            event=f'Evento {i}',
            datetime=datetime.now(),
            location=f'Local {i}'
        ).save()
        tickets.append(ticket)
        
    # Create trades
    trades = []
    for i in range(n_trades):
        trade = Trade(
            status=i,
        ).save()
        trades.append(trade)
        
    # Create relationships randomly
    for user in users:
        user.tickets.connect(random.choice(tickets))
        user.interests.connect(random.choice(tickets))
        
    for trade in trades:
        trade.tickets.connect(random.choice(tickets))
        trade.users.connect(random.choice(users))
        
    return users, tickets, trades
         
             
            