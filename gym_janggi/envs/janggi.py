from typing import List
import gym

from gym_janggi.constants import (
    NUM_PIECE_TYPE,
    NUM_ROWS,
    NUM_COLS,
    ACTION_SPACE,
)
from gym_janggi.utils import (
    generate_random_game,
    board_to_obs,
    action_to_locations,
    locations_to_action,
)


class JanggiEnv(gym.Env):
    """Open AI environment wrapper for Janggi."""
    metadata = {"render_modes": ["ansi"]}

    def __init__(self):
        self.observation_space = gym.spaces.Box(
            low=-NUM_PIECE_TYPE,
            high=NUM_PIECE_TYPE,
            shape=(NUM_ROWS, NUM_COLS),
            dtype=int
        )
        self.action_space = gym.spaces.Discrete(ACTION_SPACE)

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

        move_logs = self._game.move_logs
        self._game = generate_random_game()
        observation = self._get_obs()
        return observation, move_logs

    def close(self):
        """
        Properly close the game.
        """
        self._game = None
        return

    def render(self, mode='ansi'):
        """
        Display the game observation.
        """
        print(f"cho: {self._game.cho_score} / han: {self._game.han_score}")
        print(self._game.board)

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
        return board_to_obs(self._game.board)

    def _get_info(self):
        return {
            "cho_score": self._game.cho_score,
            "han_score": self._game.han_score,
        }

    def simulate_logs(self, move_logs) -> List[str]:
        board = self._game.initial_board
        board_logs = [str(board)]
        for from_location, to_location in move_logs:
            piece = board.get(from_location.row, from_location.col)
            board.put(to_location.row, to_location.col, piece)
            board.remove(from_location.row, from_location.col)
            board_logs.append(str(board))
        return board_logs

