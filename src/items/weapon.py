import json, pygame

from src.utils.assets import Assets
from src.utils.soundManager import SoundManager
from src.items.fullauto import Fullauto
from src.items.semiauto import Semiauto
from src.models.weaponModel import WeaponModel
from src.definitions.weaponStats import WeaponStats
from src.definitions.armourStats import ArmourStats
from src.events.eventManager import EventManager
from src.events.eventType import EventType
from src.projectiles.bullet import Bullet
from src.projectiles.rocket import Rocket
from src.projectiles.melee import Melee


class Weapon:

    def __init__(self, wielder, item):

        self.wielder = wielder
        self.model = WeaponModel(item.model_path)

        self.mods = item.mods

        # unpack weapon stats and data
            # maybe ill get rid of the file read at some point who knows
        weapon_type_filepath = item.frame_data["type"]
        weapon_subtype_name = item.frame_data["subtype"]

        with open(weapon_type_filepath) as f:
            weapon_type_data = json.load(f)

        frame_name_reference = {
            "gun-auto" : Fullauto,
            "gun-semiauto" : Semiauto
        }

        projectile_name_reference = {
            "bullet" : Bullet,
            "rocket" : Melee
        }

        Trigger_type = frame_name_reference[weapon_type_data["type"]]
        weapon_subtype_stats = weapon_type_data["subtypes"][weapon_subtype_name]

        self.projectile_type = projectile_name_reference[weapon_type_data["projectile"]]

        # use stats to set up weapons
        self.trigger = Trigger_type()

        self.element = item.element

        self.stats = {
            WeaponStats.DAMAGE : weapon_subtype_stats["damage"],
            WeaponStats.FIRERATE : 3600 // weapon_subtype_stats["firerate"],
            WeaponStats.CRIT_CHANCE : item.stats["crit_chance"]
        }

        self.status_counter = 0

        self.sound = Assets.loadSound("res/sounds/thud.wav")


    def tick(self, handler):
        if self.trigger.tick(handler, self.getStat(WeaponStats.FIRERATE)):

            damage = self.getStat(WeaponStats.DAMAGE) * self.wielder.modded_stats[ArmourStats.DAMAGE]

            EventManager.trigger_event(
                EventType.PROJECTILE,
                self.projectile_type(
                    self.wielder.pos.copy(),
                    handler.getGameMousePos().normalize(),
                    self.element,
                    self.wielder,
                    damage,
                    self.generateEffects
                )
            )

            SoundManager.playSound(self.sound)



    def getStat(self,stat):

        val = self.stats[stat]

        for mod in self.mods:
            if mod and mod.function["type"] == "INCREASE_STAT" and stat == WeaponStats(mod.function["stat"]):
                val *= mod.function["scalar"]

        return val


    def generateEffects(self):

        effects = []

        self.status_counter += self.getStat(WeaponStats.CRIT_CHANCE)
        procs = int(self.status_counter)
        self.status_counter %= 1

        if procs > 0:
            for effect in self.wielder.getElementalEffects(self.element):
                effects.append((effect, procs))

        return effects
