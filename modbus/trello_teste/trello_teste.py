from trello import TrelloClient

client = TrelloClient(
    api_key='303c72d244421df83111b5f095d243d3',
    api_secret='d63f414134470cf18e574c6297b567872fe34050a382fec319a6fe331d61243a',
    token='ATTA07208206c87baa6fc9eebb7e6d3711ccedbcf3be4d1b46581d479cfb7102c1b69569E072',
)

all_boards = client.list_boards() # Recupera todos os quadros

my_board = all_boards[2]  # Pega o quadro da Unicoba

all_lists = my_board.list_lists()  # Mostra todas as colunas

todo_list = all_lists[3]  #

colunas = todo_list.list_cards()

print("\n")

print(f'Nome da coluna : {todo_list.name}')

for card in colunas:
    print("\n")
    print(card.name, ',', card.card_created_date, ',' , card.labels)