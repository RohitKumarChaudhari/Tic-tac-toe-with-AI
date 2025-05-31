import random


class GameLogic:
    def __init__(self):
        self.row = 0
        self.colm = 0

    def give_row_and_col(self, num):
        # print(num)
        if 1 <= num <=9:
            self.row = (num - 1) // 3
            self.colm = (num - 1) % 3
        else:
            raise ValueError ('Invalid cell section')

def check_winner(grid):
    global  game_on
    ai_move = None
    win_conditions = [
        [grid[0][0], grid[0][1], grid[0][2]],
        [grid[1][0], grid[1][1], grid[1][2]],
        [grid[2][0], grid[2][1], grid[2][2]],
        [grid[0][0], grid[1][0], grid[2][0]],
        [grid[0][1], grid[1][1], grid[2][1]],
        [grid[0][2], grid[1][2], grid[2][2]],
        [grid[0][0], grid[1][1], grid[2][2]],
        [grid[0][2], grid[1][1], grid[2][0]],
    ]

    for winner in win_conditions:
        if winner[0] == winner[1] == winner[2] and  str(winner[0]) in ['X', '0']:
            print(f"\n{winner[0]} Wins the game! 🎉🎉")
            game_on = False
            break

        if winner.count('0') == 2 and any(isinstance(cell, int) for cell in winner):
            ai_move = next(cell for cell in winner if isinstance(cell, int))
            break

        elif winner.count('X') == 2 and any(isinstance(cell, int) for cell in winner):
            ai_move = next(cell for cell in winner if isinstance(cell, int))
            break


        else:
            if grid[1][1] not in ['X', '0']:
                ai_move = grid[1][1]

            else:
                for i in range(1,10):
                    game_logic.give_row_and_col(i)
                    if grid[game_logic.row][game_logic.colm] not in ['X', '0'] and i in [1,3,7,9]:
                        ai_move = i
                        break

                    elif grid[game_logic.row][game_logic.colm] not in ['X', '0'] and i in [2,4,6,8]:
                        ai_move = i
                        break

    return ai_move



def print_grid():
    for i in range(3):
        for j in range(3):
            if j > 1:
                print(board[i][j], end=' ')
            else:
                print(board[i][j], end=' | ')
        if i < 2:
            print("\n___________")

def mode_checker():
    mode = input("Which mode do you want to play Ai or Two player or Impossible? (press a or b or c): ").lower()
    if mode in ['a', 'b', 'c']:
        print_mode(mode)
    else:
        while mode not in ['a', 'b', 'c']:
            print('\nWrong selection. Please choose again.')
            mode = input("\nWhich mode do you want to play Ai or Two player or Impossible? (press a or b or c): ").lower()
            if mode in ['a', 'b', 'c']:
                print_mode(mode)
                break
    return mode

def print_mode(mode):
    if mode == 'a':
        print('Ai mode is selected.')
    elif mode == 'b':
        print('Two player mode is selected.')
    elif mode == 'c':
        print("Impossible Mode is selected.")

    print_grid()



def run_game():
    global  player, moves
    try:
        if current_mode == 'a':
            if player == "X":
                player_num = int(input(f'\nwhere do you want to put {player}?: '))
                game_logic.give_row_and_col(player_num)
            if player == '0':
                while True:
                    ai_num = random.randint(1, 9)
                    game_logic.give_row_and_col(ai_num)
                    if board[game_logic.row][game_logic.colm] not in ['X', '0']:
                        break

        elif current_mode == 'b':
            player_num = int(input(f'\nwhere do you want to put {player}?: '))
            game_logic.give_row_and_col(player_num)

        elif current_mode == 'c':
            if player == "X":
                player_num = int(input(f'\nwhere do you want to put {player}?: '))
                game_logic.give_row_and_col(player_num)

            if player == '0':
                while True:
                    ai_num = check_winner(board)
                    game_logic.give_row_and_col(ai_num)
                    if board[game_logic.row][game_logic.colm] not in ['X', '0']:
                        break
                game_logic.give_row_and_col(ai_num)

        try:
            if board[game_logic.row][game_logic.colm] in ['X', '0']:
                if player == '0' and current_mode == 'a':
                    ai_num = random.randint(1, 9)
                elif player == '0' and current_mode == 'c':
                    ai_num = check_winner(board)

                else:
                    print("\n🤨Invalid selection!")
                    print_grid()
                correct_selection = False
            else:
                correct_selection = True

        except IndexError:
            print('Please choose correct row/col num!')
            print_grid()

        else:
            if game_on and correct_selection:
                moves += 1
                board[game_logic.row][game_logic.colm] = f"{player}"
                if player == 'X':
                    player = "0"
                    print_grid()
                elif player == '0':
                    if current_mode in ['a', 'c']:
                        print(f'\nAi chosen {ai_num}')
                    print_grid()
                    player = 'X'
                check_winner(board)


    except ValueError:
        print('Please enter correct number!')
        print_grid()



def restart_game():
    global current_mode, game_on, moves, player, board
    restart = input("Do you want to play again?(press 'y' or 'n'): ")
    if restart == 'y':
        board = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        moves = 0
        player = 'X'
        game_on = True
        current_mode = mode_checker()
        while game_on and moves in range(9):
            run_game()


board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

restart = ''
player = 'X'
game_on = True
moves = 0

print("Welcome to Tic Tac Toe Game❤️😍.")

game_logic = GameLogic()
current_mode = mode_checker()

while game_on and moves in range(9):
    run_game()
    if not game_on:
        restart_game()


if game_on and moves >= 9:
    print("\nMatch is Draw🤷‍♂️")
    restart_game()

