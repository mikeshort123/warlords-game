import pygame, random, math

from src.utils.vector import Vector

class ParticleManager:

    class Particle:

        def __init__(self, c, pos, vel, l):

            self.c = c
            self.pos = pos
            self.vel = vel
            self.l = l

        def tick(self):

            self.pos += self.vel
            self.l -= 1

        def render(self, renderer, cam):

            w_pos = renderer.getWorldPos(self.pos, cam)
            w_size = renderer.getWorldSize(0.016 * self.l, cam)
            pygame.draw.circle(renderer.display, self.c, w_pos.list(), w_size)

    def __init__(self):

        self.particles = []

    def tick(self):

        for particle in self.particles:
            particle.tick()
            if particle.l < 0:
                self.particles.remove(particle)

    def render(self, renderer, cam):

        for particle in self.particles:
            particle.render(renderer, cam)

    def burst(self, pos, colour, amount, radius):

        r = 2 * math.pi / amount

        for i in range(amount):

            d = r * i
            v = Vector(math.sin(d), math.cos(d)) * radius * random.randint(1,10) / 100

            self.particles.append(ParticleManager.Particle(colour, pos.copy(), v, 10))
