import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import time

class ConwaysGameOfLife:
    def __init__(self, size, density):
        # Big Bang/Singularity
        self.universe = np.zeros(shape=size)
        self.universe = self.populate_life(self.universe, density)
        self.next_state = np.copy(self.universe)
        self.start_state = np.copy(self.universe)

    def populate_life(self, universe, density):
        universe_size = universe.shape
        population_size = int(universe_size[0] * universe_size[1] * density)
        x_axis = np.random.randint(1, universe_size[1], size=population_size)
        y_axis = np.random.randint(1, universe_size[1], size=population_size)

        universe[x_axis, y_axis] = 1

        return universe

    def population_control(self, position):
        if position[1] == 0:
            return self.reproduce(position)

        position = position[0]
        neighbourhood = self.universe[position[0] - 1:position[0] + 2, position[1] - 1:position[1] + 2]

        if neighbourhood.sum() - 1 in [2, 3]:
            # Alive, but till when?
            self.next_state[position[0], position[1]] = 1
        else:
            # Purge
            self.next_state[position[0], position[1]] = 0

        return

    def reproduce(self, position):
        position = position[0]
        neighbourhood = self.universe[position[0] - 1:position[0] + 2, position[1] - 1:position[1] + 2]

        if neighbourhood.sum() == 3:
            # Life
            self.next_state[position[0], position[1]] = 1

        return

    def live(self, steps=100):
        figure, ax = plt.subplots(figsize=(10, 10))
        plt.ion()
        plt.axis('off')
        for i in range(steps):
            np.fromiter(map(self.population_control, np.ndenumerate(self.universe)), dtype=float)
            self.universe = np.copy(self.next_state)

            cmap_ = sns.diverging_palette(250, 30, s=80, l=55, n=9)
            sns.heatmap(game.universe, cmap = cmap_, xticklabels=False, yticklabels=False, linewidths=1, cbar=False, ax=ax)
            # ax.imshow(game.universe, cmap='Greys')
            ax.set_title(f'Gen: {i}')
            plt.draw()

            plt.pause(0.01)

        plt.ioff()
        plt.show()

        return


if __name__ == '__main__':
    game = ConwaysGameOfLife((25, 25), 0.75)
    game.live(1000)




