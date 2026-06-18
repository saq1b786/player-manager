from models import Player 
from database import * 

def main() -> None:
    create_tables()

    while True:
        print('1. Add Player')
        print('2. Get all players list ')
        print('3. Add to a players tally ')
        print('4. Delete a player (Via name)')
        print('5. Get all flagged players')
        print('6. Quit')

        try:
            user_choice = int(input('Please enter a number between 1-6: '))
            if user_choice <1 or user_choice >6:
                print('You must pick a number between 1-6')
                continue
        except ValueError:
            print('You can only choose numbers between 1-6 only.')
            continue

        # where the user starts choosing⬇️

        if user_choice == 1:
            name = input('enter a name: ')
            position = input('enter players position: ')
            phone = input('enter players phone number: ')

            user_added_player = Player(name, position, phone)

            add_player(user_added_player)

        elif user_choice == 2: 
            players = get_all_players()
            for player in players:
                print(player)

        elif user_choice == 3: 
            player = input('Please enter the players name you want to add a tally to: ')
            add_tally(player)
            
        elif user_choice == 4: 
            player_to_delete = input('Please enter the name of the player you wannt to delete: ')
            delete_player(player_to_delete)

        elif user_choice == 5:
            flagged = get_flagged_players()
            for players in flagged:
                print(players)

        elif user_choice == 6: 
            print('You have presed quit. goodbye.')
            break


if __name__ == '__main__':
    main()