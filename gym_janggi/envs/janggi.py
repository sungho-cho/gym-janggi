import gym
from gym import spaces

from gym_janggi.constants import (
    NUM_PIECE_TYPE,
    NUM_ROWS,
    NUM_COLS,
    ACTION_SPACE,
)
from gym_janggi.utils import (
    generate_random_game,
    board_to_obs,
    action_to_grids,
    grids_to_action,
)
from gym_janggi.janggi_game import JanggiGame


class JanggiEnv(gym.Env):
    metadata = {"render_modes": ["ansi"]}

    def __init__(self):
        self.observation_space = spaces.Box(
            low=-NUM_PIECE_TYPE,
            high=NUM_PIECE_TYPE,
            shape=(NUM_ROWS, NUM_COLS),
            dtype=int
        )
        self.action_space = spaces.Discrete(ACTION_SPACE)

        self._game = generate_random_game()

    def _get_obs(self):
        return board_to_obs(self._game.board)

    def _get_info(self):
        return {
            "cho_score": self._game.cho_score,
            "han_score": self._game.han_score,
        }

    def reset(self, seed=None, return_info=False, options=None):
        # We need the following line to seed self.np_random
        super().reset(seed=seed)

        self._game = generate_random_game()
        observation = self._get_obs()
        info = self._get_info()
        return (observation, info) if return_info else observation

    def step(self, action):
        (origin, dest) = action_to_grids(action)
        reward, done = self._game.make_move(origin, dest)
        observation = self._get_obs()
        info = self._get_info()

        return observation, reward, done, info

    def legal_actions(self):
        actions = []
        for origin, dest in self._game.get_all_moves:
            actions.append(grids_to_action(origin, dest))
        return actions

    def render(self, mode='ansi'):
        print(f"cho: {self._game.cho_score} / han: {self._game.han_score}")
        print(self._game.board)

    def close(self):
        self._game = None
