from gym.envs.registration import register

register(
    id="gym_janggi/Janggi-v0",
    entry_point="gym_janggi.envs:JanggiEnv"
)
