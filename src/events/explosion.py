

class Explosion:

    def __init__(self, pos, radius, colour, damage, element):

        self.pos = pos
        self.radius = radius
        self.colour = colour
        self.damage = damage
        self.element = element

    def genEffect(self, particleManager):

        particleManager.burst(self.pos, self.colour, 40, self.radius)

    def applyDamage(self, guys):

        for guy in guys:
            d = (self.pos - guy.pos).length()

            if d > self.radius: continue

            damage = self.damage * (1 - d / (2 * self.radius))

            guy.applyDamage(damage, self.element)
