import gym
import gym_janggi
import time
import random

from utils import action_to_grids


def main():
    env = gym.make('gym_janggi/Janggi-v0')
    env.reset()
    env.render()

    done = False
    round = 0
    while not done:
        # Add a slight delay to properly visualize the game.
        time.sleep(1)

        legal_actions = env.legal_actions()
        action = random.choice(legal_actions)
        turn = env._game.turn
        origin, dest = action_to_grids(action)
        piece = env._game.board.get(origin.row, origin.col).piece_type
        _, reward, done, _ = env.step(action)

        print(f"Round: {round}")
        print(f"{turn} made the move {piece} from {origin} to {dest}.")
        print(f"Reward: {reward}")
        print("================")

        round += 1
        env.render()
    env.close()


if __name__ == '__main__':
    main()
