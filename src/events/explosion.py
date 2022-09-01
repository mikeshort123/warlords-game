

class Explosion:

    def __init__(self, pos, radius, colour, damage, element, source, effects):

        self.pos = pos
        self.radius = radius
        self.colour = colour
        self.damage = damage
        self.element = element
        self.source = source
        self.effects = effects

    def genEffect(self, particleManager):

        particleManager.burst(self.pos, self.colour, 40, self.radius)

    def applyDamage(self, guys):

        for guy in guys:
            d = (self.pos - guy.pos).length()

            if d > self.radius: continue

            damage = self.damage * (1 - d / (2 * self.radius))

            guy.applyDamage(damage, self.element)

            for (EffectType, procs) in self.effects():

                if EffectType.TARGET:
                    guy.applyEffect(EffectType, procs, self.source) # debuff, apply to target
                else:
                    self.source.applyEffect(EffectType, procs, self.source) # buff, apply to source
