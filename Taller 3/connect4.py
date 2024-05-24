class Board:
    def __init__(self, rows=6, columns=7):
        self.rows = rows
        self.columns = columns
        self.board = [[' ' for _ in range(columns)] for _ in range(rows)]

    def add_piece(self, column, piece):
        """
        Adds a piece to the board.
        
        :param column: The column (0-indexed) where the piece will be dropped.
        :param piece: The piece to be added ('X' or 'O').
        :return: Boolean indicating if the piece was successfully added.
        """
        if column < 0 or column >= self.columns:
            print("Invalid column. Please choose a column between 0 and", self.columns - 1)
            return False
        
        for row in reversed(range(self.rows)):
            if self.board[row][column] == ' ':
                self.board[row][column] = piece
                return True
        print("Column is full. Please choose a different column.")
        return False

    def display(self):
        """Displays the current state of the board."""
        for row in self.board:
            print('|'.join(row))
            print('-' * (self.columns * 2 - 1))

    def check_winner(self):
        """Checks if there is a winner on the board."""
        # Check horizontal, vertical, and diagonal wins
        for row in range(self.rows):
            for col in range(self.columns):
                if self.board[row][col] != ' ':
                    piece = self.board[row][col]
                    if self.check_line_winner(row, col, piece):
                        return piece
        return None

    def check_line_winner(self, row, col, piece):
        """Helper method to check for line winners from a given position."""
        directions = [
            (0, 1),  # Horizontal
            (1, 0),  # Vertical
            (1, 1),  # Diagonal down-right
            (1, -1)  # Diagonal down-left
        ]

        for dr, dc in directions:
            if self.check_direction(row, col, dr, dc, piece):
                return True
        
        # Check for L-shaped and 2x2 wins
        if self.check_L_shape(row, col, piece) or self.check_2x2(row, col, piece):
            return True
        
        return False

    def check_direction(self, row, col, dr, dc, piece):
        """Checks a direction for a winning line of four."""
        count = 0
        for i in range(4):
            r, c = row + dr * i, col + dc * i
            if 0 <= r < self.rows and 0 <= c < self.columns and self.board[r][c] == piece:
                count += 1
            else:
                break
        return count == 4

    def check_L_shape(self, row, col, piece):
        """Checks for L-shaped wins (3x1 or 1x3)."""
        L_shapes = [
            [(0, 1), (0, 2), (1, 0)],  # L shape right-down
            [(0, 1), (0, 2), (-1, 0)], # L shape right-up
            [(0, -1), (0, -2), (1, 0)],# L shape left-down
            [(0, -1), (0, -2), (-1, 0)],# L shape left-up
            [(1, 0), (2, 0), (0, 1)],  # L shape down-right
            [(1, 0), (2, 0), (0, -1)], # L shape down-left
            [(-1, 0), (-2, 0), (0, 1)],# L shape up-right
            [(-1, 0), (-2, 0), (0, -1)]# L shape up-left
        ]

        for shape in L_shapes:
            if all(0 <= row + dr < self.rows and 0 <= col + dc < self.columns and self.board[row + dr][col + dc] == piece for dr, dc in shape):
                return True
        return False

    def check_2x2(self, row, col, piece):
        """Checks for 2x2 wins."""
        if row + 1 < self.rows and col + 1 < self.columns:
            return (self.board[row][col] == piece and 
                    self.board[row + 1][col] == piece and 
                    self.board[row][col + 1] == piece and 
                    self.board[row + 1][col + 1] == piece)
        return False

def play_connect_four():
    while True:
        board = Board()  # Creamos un nuevo tablero para cada juego
        
        # Variables para controlar los turnos de los jugadores
        players = ['X', 'O']
        current_player = 0
        
        print("¡Bienvenido a Cuatro en Línea!")
        print("Para colocar una ficha, introduce el número de columna (0-6).")
        print("Para salir, escribe 'exit'.")
        
        while True:
            # Mostrar el estado actual del tablero
            print()
            board.display()
            
            # Obtener el movimiento del jugador
            column_input = input(f"Turno de '{players[current_player]}': ")
            
            # Salir del juego si se escribe 'exit'
            if column_input.lower() == 'exit':
                print("¡Gracias por jugar!")
                return
            
            # Verificar si el input es un número válido
            if not column_input.isdigit():
                print("Entrada inválida. Introduce un número de columna válido (0-6) o 'exit'.")
                continue
            
            column = int(column_input)
            
            # Intentar agregar la ficha al tablero
            if board.add_piece(column, players[current_player]):
                # Verificar si hay un ganador
                winner = board.check_winner()
                if winner:
                    print(f"¡Felicidades! ¡{winner} ha ganado!")
                    break  # Salir del bucle de juego si hay un ganador
                else:
                    # Cambiar al siguiente jugador
                    current_player = (current_player + 1) % 2
            else:
                continue  # Volver a solicitar un movimiento si la columna está llena
        
        # Preguntar al jugador si desea reiniciar el juego
        
		# Mostrar por última vez el tablero
        print()
        board.display()
        
        play_again = input("¿Quieres jugar de nuevo? (s/n): ")
        if play_again.lower() != 's':
            print("¡Hasta luego!")
            break  # Salir del bucle principal si no se desea jugar de nuevo


# Ejecutar el juego
if __name__ == "__main__":
    play_connect_four()