from gymnasium.envs.toy_text.frozen_lake import FrozenLakeEnv

class CustomFrozenLakeEnv(FrozenLakeEnv):
    def __init__(self, **kwargs):
        super(CustomFrozenLakeEnv, self).__init__(**kwargs)

    def step(self, action):
        # Get the next state, reward, done, and info using the parent class's step function
        observation, reward, terminated, truncated, info = super(CustomFrozenLakeEnv, self).step(action)
        # Add penalty if an agnet does not reach the goal
        if reward == 0:  # if the agent doesn't reach the goal
            reward = -0.1  # penalize the agent for each step

        if reward == 1:
            reward = 0
        
        return observation, reward, terminated, truncated, info 