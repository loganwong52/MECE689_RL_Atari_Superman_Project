from gymnasium import ActionWrapper

class SupermanActionReducer(ActionWrapper):
    def __init__(self, env, allowed_actions=None):
        super().__init__(env)
        
        if allowed_actions is None:
            # Basic movement only: Cardinal directions & diagonal directions
            allowed_actions = [2,3,4,5, 6,7,8,9]
            
            # Cardinal directions, diagonal directions, AND x-ray vision
            # allowed_actions = [2,3,4,5, 6,7,8,9, 10,11,12,13]
        
        self.allowed_actions = allowed_actions
        self.action_space = gym.spaces.Discrete(len(allowed_actions))
        
    def action(self, action):
        # Map the reduced action index back to the original action
        return self.allowed_actions[action]