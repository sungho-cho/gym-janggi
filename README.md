# Gym Janggi

<img src="https://user-images.githubusercontent.com/46757971/173596086-ade59dd1-8064-4946-89e8-a4ca2e18555d.gif" width=30% height=30%>

**Gym Janggi** provides an reinforcement learning environment for Korean chess called [Janggi](https://en.wikipedia.org/wiki/Janggi). As an [OpenAI Gym](https://gym.openai.com/) environment, this package can be used for reinforcement learning algorithms, such as AlphaZero.

## Documentation
Check out the [GitHub Page](https://sungho-cho.github.io/gym-janggi/) for Gym environment documentation.

## Getting Started

### Using the Gym Enviornment in Your Package

1. Install package via pip:

    `pip install gym-janggi`

2. Import in your Python module:

    `import gym`

    `import gym_janggi`

3. Make a Gym environment instance:

    `gym.make("gym_janggi/Janggi-v0")`

    Check out the [Documentation](#documentation) section for more details.


### Testing Functionality
**Gym Janggi** is originally designed to be imported by other packages and provide a Gym environemnt for Janggi, but if you want to check if the package itself is working, you can follow these steps:

1. Clone the repository:

    `git clone https://github.com/sungho-cho/gym-janggi.git`

2. Install the module:

    `pip install -e .`

3. Run `play.py`, which generates a game with a series of random moves:

    `python gym_janggi/play.py`

    If you see the UI window and moves being played, the package is working!


## Releases
Check out the [PyPi Package](https://pypi.org/project/gym-janggi) for releases.

## License
This package is licensed under the [GNU General Public License v3.0](LICENSE).
