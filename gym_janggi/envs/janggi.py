import gym
from janggi import (
    GameWindow,
    generate_random_game,
)
import numpy as np
import pygame
from typing import List, Optional

from gym_janggi.constants import (
    NUM_PIECE_TYPE,
    NUM_ROWS,
    NUM_COLS,
    ACTION_SPACE,
)
from gym_janggi.utils import (
    board_to_float_array,
    action_to_locations,
    locations_to_action,
)


class JanggiEnv(gym.Env):
    """Open AI environment wrapper for Janggi."""
    metadata = {"render_modes": ["human", "ansi"], "render_fps": 4}

    def __init__(self, render_mode: Optional[str] = None):
        assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.observation_space = gym.spaces.Box(
            low=-NUM_PIECE_TYPE,
            high=NUM_PIECE_TYPE,
            shape=(NUM_ROWS, NUM_COLS),
            dtype=int
        )
        self.action_space = gym.spaces.Discrete(ACTION_SPACE)
        self.render_mode = render_mode
        self._game = generate_random_game()

    def step(self, action):
        """
        Apply action to the game.

        Args:
            action : action of the action_space to take.

        Returns:
            The new observation, the reward and a game-over boolean and info.
        """
        (origin, dest) = action_to_locations(action)
        reward, done = self._game.make_action(origin, dest)
        observation = self._get_obs()
        info = self._get_info()
        if done:
            info["log"] = self._game.log

        return observation, reward, done, info

    def to_play(self) -> int:
        """
        Return the current player.

        Returns:
            The current player, it should be an element of the players list in the config.
        """
        return self._game.turn.value

    def legal_actions(self):
        """
        Should return the legal actions at each turn, if it is not available, it can return
        the whole action space. At each turn, the game have to be able to handle one of returned actions.

        Returns:
            An array of integers, subset of the action space.
        """
        actions = []
        for origin, dest in self._game.get_all_actions():
            actions.append(locations_to_action(origin, dest))
        return actions

    def reset(self, seed=None, return_info=False, options=None):
        """
        Reset the game for a new game.

        Returns:
            Initial observation of the game.
        """
        # We need the following line to seed self.np_random
        super().reset(seed=seed)

        self._game = generate_random_game()
        observation = self._get_obs()
        return observation

    def close(self):
        """
        Properly close the game.
        """
        self._game = None
        return

    def render(self, mode="ansi"):
        """
        Display the game observation.
        """

        if mode == "ansi":
            print(f"cho: {self._game.cho_score} / han: {self._game.han_score}")
            print(self._game.board)
        elif mode == "human":
            if not hasattr(self, "_game_window"):
                self._game_window = GameWindow(self._game.board)
                self.clock = pygame.time.Clock()
            self._game_window.render()
            self.clock.tick(self.metadata["render_fps"])

    def human_input_to_action() -> int:
        """
        For multiplayer games, ask the user for a legal action
        and return the corresponding action number.

        Returns:
            An integer from the action space.
        """
        action = int(input(f"Enter action (0~{ACTION_SPACE}):"))
        if action > 0 and action < ACTION_SPACE:
            return True, action
        else:
            return False, None

    def action_to_human_input(self, action: int) -> str:
        """
        Convert an action number to a string representing the action.

        Args:
            action_number: an integer from the action space.

        Returns:
            String representing the action.
        """
        origin, dest = action_to_locations(action)
        return f"({origin.row}, {origin.col}) to ({dest.row}, {dest.col})"

    def _get_obs(self):
        obs = board_to_float_array(self._game.board)
        if self._game.turn != self._game.player:
            obs = np.flip(obs)
        return obs

    def _get_info(self):
        return {
            "cho_score": self._game.cho_score,
            "han_score": self._game.han_score,
        }
