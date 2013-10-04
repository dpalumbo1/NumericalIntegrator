class Body:
    def _init_ (self, mass, charge, position, velocity):
        self.mass = mass
        self.charge = charge
        self.position = position
        self.velocity = velocity
    def accelerate (self, force, dt):
        self.velocity += acceleration / self.mass * dt
        self.position += velocity * dt
        
