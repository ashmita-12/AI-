class ModelBasedAgent:
    def __init__(self, size):
        self.size = size
        self.agent_location = (0, 0)
        self.agent_orientation = 'right'
        self.internal_model = [[{'stench': False, 'breeze': False, 'glitter': False} for _ in range(size)] for _ in range(size)]

    def sense(self, perceptions):
        x, y = self.agent_location
        return perceptions.get((x, y), {'stench': False, 'breeze': False, 'glitter': False})

    def update_model(self, perceptions):
        x, y = self.agent_location
        self.internal_model[x][y] = perceptions

    def decide_action(self):
        x, y = self.agent_location
        current_perceptions = self.internal_model[x][y]

        if current_perceptions['glitter']:
            return 'grab'
        elif current_perceptions['breeze'] or current_perceptions['stench']:
            return 'move away'
        else:
            return 'move forward'

    def move(self, action):
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

    def act(self, perceptions):
        current_perceptions = self.sense(perceptions)
        self.update_model(current_perceptions)
        action = self.decide_action()
        self.move(action)
        print(f"Action: {action}, Perceptions: {current_perceptions}")

# Example usage
agent = ModelBasedAgent(size=4)

# Example perceptions for each location
perceptions = {
    (0, 0): {'glitter': True},
    (1, 0): {'breeze': True},
    (2, 1): {'stench': True},
    # Other locations have no perceptions
}
agent.act(perceptions)
