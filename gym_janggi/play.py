import gym
import gym_janggi
import time
import random

from janggi import Camp

from utils import action_to_locations


def main():
    env = gym.make('gym_janggi/Janggi-v0')
    env.reset()
    env.render()

    done = False
    round = 0
    while not done:
        legal_actions = env.legal_actions()
        action = random.choice(legal_actions)
        origin, dest = action_to_locations(action)
        _, reward, done, _ = env.step(action)
        
        print(f"Round: {round}")
        print(f"{Camp(env.to_play()).name} made the move from {origin} to {dest}.")
        print(f"Reward: {reward}")
        print("================")
        env.render()

        round += 1
    env.close()


if __name__ == '__main__':
    main()
