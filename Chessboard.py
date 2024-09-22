import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

board = np.tile([1, 0], (8, 4))  # Create the board
for i in range(board.shape[0]):
    board[i] = np.roll(board[i], i % 2)  # Shift rows for the checker pattern

color_map = ListedColormap(['#779556', '#ebecd0'])  # Define color map
plt.matshow(board, cmap=color_map)  # Display the board
plt.xticks([])  # Hide x ticks
plt.yticks([])  # Hide y ticks
plt.show()  # Show the plot
