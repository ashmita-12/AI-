class SimpleReflexAgent:
    def __init__(self, size):
        self.size = size
        self.agent_location = (0, 0)
        self.agent_orientation = 'right'

    def sense(self, perceptions):
        # Get the perception for the current location
        x, y = self.agent_location
        perception = perceptions.get((x, y), {})

        return perception

    def decide_action(self, perception):
        # Determine the action based on the perception
        if perception.get('glitter', False):
            return 'grab'
        elif perception.get('breeze', False) or perception.get('stench', False):
            return 'move away'
        else:
            return 'move forward'

    def update_location(self, action):
        # Update agent's location based on the action
        x, y = self.agent_location

        if action == 'move forward':
            if self.agent_orientation == 'right' and y < self.size - 1:
                self.agent_location = (x, y + 1)
            elif self.agent_orientation == 'left' and y > 0:
                self.agent_location = (x, y - 1)
            elif self.agent_orientation == 'up' and x > 0:
                self.agent_location = (x - 1, y)
            elif self.agent_orientation == 'down' and x < self.size - 1:
                self.agent_location = (x + 1, y)
        elif action == 'turn left':
            if self.agent_orientation == 'right':
                self.agent_orientation = 'up'
            elif self.agent_orientation == 'up':
                self.agent_orientation = 'left'
            elif self.agent_orientation == 'left':
                self.agent_orientation = 'down'
            elif self.agent_orientation == 'down':
                self.agent_orientation = 'right'
        elif action == 'turn right':
            if self.agent_orientation == 'right':
                self.agent_orientation = 'down'
            elif self.agent_orientation == 'down':
                self.agent_orientation = 'left'
            elif self.agent_orientation == 'left':
                self.agent_orientation = 'up'
            elif self.agent_orientation == 'up':
                self.agent_orientation = 'right'
        elif action == 'grab':
            # Implement grabbing action
            pass

    def act(self, perceptions):
        perception = self.sense(perceptions)
        action = self.decide_action(perception)
        self.update_location(action)
        print(f"Action: {action}, Perceptions: {perception}")
# Example usage
agent = SimpleReflexAgent(size=4)

# Example perceptions for each location
perceptions = {
    (0, 0): {'glitter': True},
    (1, 0): {'breeze': True},
    (2, 1): {'stench': True},
    # Other locations have no perceptions
}
agent.act(perceptions)
