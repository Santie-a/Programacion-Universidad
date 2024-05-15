class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [['-' for _ in range(size)] for _ in range(size)]  # 'O' representa agua
        self.ships = []  # Lista para almacenar los barcos colocados en el tablero
    
    def add_ship(self, ship):
        for x, y in ship.positions:
            if not self.is_valid_position(x, y):
                raise ValueError("El barco no cabe en el tablero o se superpone con otro barco")
            self.grid[y][x] = 'S'  # 'S' representa parte del barco
        self.ships.append(ship)
    
    def is_valid_position(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size and self.grid[y][x] == '-'
    
    def check_shot(self, x, y):
        if self.grid[y][x] == 'S':
            self.grid[y][x] = 'X'  # 'X' representa un disparo acertado
            return 'hit'
        else:
            self.grid[y][x] = 'M'  # 'M' representa un disparo fallido
            return 'miss'
    
    def display(self):
        for row in self.grid:
            print(' '.join(row))

    def all_ships_sunk(self):
        for x in self.grid:
            for y in x:
                if y == "S":
                    return False
        return True


class Ship:
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.positions = []  # Lista de tuplas (x, y) que representan las posiciones ocupadas por el barco
    
    def place(self, x, y, direction, board):
        self.positions.clear()  # Limpiar las posiciones existentes
        
        if direction == 'horizontal':
            for i in range(self.length):
                if x + i >= board.size:
                    raise ValueError("El barco no cabe en el tablero")
                if not board.is_valid_position(x + i, y):
                    raise ValueError("El barco se superpone con otro barco")
                self.positions.append((x + i, y))
                board.grid[y][x + i] = 'S'
        elif direction == 'vertical':
            for i in range(self.length):
                if y + i >= board.size:
                    raise ValueError("El barco no cabe en el tablero")
                if not board.is_valid_position(x, y + i):
                    raise ValueError("El barco se superpone con otro barco")
                self.positions.append((x, y + i))
                board.grid[y + i][x] = 'S'
        else:
            raise ValueError("Dirección inválida")
        
    def get_positions(self):
        return self.positions


class Game:
    def __init__(self, board_size):
        self.board_size = board_size
        self.players = []
        self.current_player = None
        self.opponent = None
    
    def add_player(self, player):
        self.players.append(player)
        if len(self.players) == 2:
            self.current_player = self.players[0]
            self.opponent = self.players[1]
    
    def switch_turn(self):
        self.current_player, self.opponent = self.opponent, self.current_player
    
    def shoot(self, x, y):
        if self.current_player == None:
            raise ValueError("No hay suficientes jugadores para iniciar el juego")
        if not self.is_valid_shot(x, y):
            raise ValueError("Disparo fuera del tablero o repetido")
        
        result = self.opponent.board.check_shot(x, y)
        if result == 'hit':
            print("¡Acierto!")
        elif result == 'miss':
            print("¡Fallo!")
            self.switch_turn()
    
    def is_valid_shot(self, x, y):
        return 0 <= x < self.board_size and 0 <= y < self.board_size and \
               self.opponent.board.grid[y][x] not in ['X', 'M']
    
    def play(self):
        while True:
            self.display_boards()
            print(f"Turno de {self.current_player.name}")
            try:
                x, y = self.get_input()
                self.shoot(x, y)
                if self.opponent.board.all_ships_sunk():
                    print(f"{self.current_player.name} gana!")
                    break
            except ValueError as e:
                print(e)
    
    def display_boards(self):
        print("\nTablero de", self.current_player.name)
        self.current_player.board.display()
        print("\nTablero de", self.opponent.name)
        self.opponent.board.display()
    
    def get_input(self):
        try:
            x = int(input("Ingrese la coordenada x (0-9): "))
            y = int(input("Ingrese la coordenada y (0-9): "))
            return x, y
        except ValueError:
            print("Por favor, ingrese números enteros.")
            return self.get_input()
    

class Player:
    def __init__(self, name, board):
        self.name = name
        self.board = board


if __name__ == "__main__":
    board_size = 10
    player1_board = Board(board_size)
    player2_board = Board(board_size)

    ship1_player1 = Ship("Portaaviones", 5)
    ship1_player1.place(0, 0, 'horizontal', player1_board)

    ship2_player1 = Ship("Acorazado", 4)
    ship2_player1.place(1, 1, 'vertical', player1_board)

    ship3_player1 = Ship("Submarino", 3)
    ship3_player1.place(5, 5, 'horizontal', player1_board)

    ship4_player1 = Ship("Destructor", 3)
    ship4_player1.place(2, 7, 'vertical', player1_board)

    ship5_player1 = Ship("Patrullera", 2)
    ship5_player1.place(9, 0, 'vertical', player1_board)

    ship1_player2 = Ship("Portaaviones", 5)
    ship1_player2.place(0, 0, 'vertical', player2_board)

    ship2_player2 = Ship("Acorazado", 4)
    ship2_player2.place(4, 3, 'horizontal', player2_board)

    ship3_player2 = Ship("Submarino", 3)
    ship3_player2.place(8, 5, 'vertical', player2_board)

    ship4_player2 = Ship("Destructor", 3)
    ship4_player2.place(2, 7, 'horizontal', player2_board)

    ship5_player2 = Ship("Patrullera", 2)
    ship5_player2.place(6, 9, 'horizontal', player2_board)

    player1 = Player("Jugador 1", player1_board)
    player2 = Player("Jugador 2", player2_board)

    game = Game(board_size)
    game.add_player(player1)
    game.add_player(player2)

    game.play()