# gym-janggi package

## Subpackages
* [gym_janggi.envs.janggi module](#gymjanggienvsjanggi-module)
  * [action_to_human_input](#actiontohumaninput)
  * [janggi.base.camp module](#janggibasecamp-module)
  * [janggi.base.formation module](#janggibaseformation-module)
  * [janggi.base.location module](#janggibaselocation-module)
  * [janggi.base.move module](#janggibasemove-module)
  * [janggi.base.piece module](#janggibasepiece-module)


# gym_janggi.envs.janggi module

## _class_ gym_janggi.envs.janggi.JanggiEnv(render_mode: Optional[str] = None)
Bases: `Env`

Open AI environment wrapper for Janggi.

### action_to_human_input(action: int)
Convert an action number to a string representing the action.

Args:

    action_number: an integer from the action space.

Returns:

    String representing the action.


### close()
Properly close the game.


### human_input_to_action()
For multiplayer games, ask the user for a legal action
and return the corresponding action number.

Returns:

    An integer from the action space.


### legal_actions()
Should return the legal actions at each turn, if it is not available, it can return
the whole action space. At each turn, the game have to be able to handle one of returned actions.

Returns:

    An array of integers, subset of the action space.


### metadata(_ = {'render_fps': 4, 'render_modes': ['human', 'ansi']_ )

### observation_space(_: spaces.Space[ObsType_ )

### render(mode='ansi')
Display the game observation.


### reset(seed=None, return_info=False, options=None)
Reset the game for a new game.

Returns:

    Initial observation of the game.


### step(action)
Apply action to the game.

Args:

    action : action of the action_space to take.

Returns:

    The new observation, the reward and a game-over boolean and info.


### to_play()
Return the current player.

Returns:

    The current player, it should be an element of the players list in the config.
