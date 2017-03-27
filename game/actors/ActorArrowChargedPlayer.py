import pygame

from api.ActorAnimation import ActorAnimation
from api.Animation import Animation
from api.EnumTeam import EnumTeam
from api.Rect import Rect
from game.actors.ActorArrowPlayer import ActorArrowPlayer
from game.utils.Constants import EVENT_EXPLOSION
from game.utils.Direction import DIRECTION
from game.utils.SurfaceHelper import load_image
from game.utils.Vector import Vector, VECTOR_NULL
from api.EnumAuto import EnumAuto


class ActorArrowChargedPlayer(ActorArrowPlayer, ActorAnimation):
    class State(EnumAuto):
        TRAVEL = ()
        EXPLODE = ()

    def __init__(self, dir=DIRECTION.NONE, velocity=VECTOR_NULL):
        super().__init__(dir, velocity)

        self.radius = 128
        self.damage = 20

    def load_sprite(self):
        self.animations = {}
        self.animations[ActorArrowChargedPlayer.State.TRAVEL] = Animation(load_image("assets/bullet_charged.png", False), Rect(0, 0, 48, 48), 1, -1, True)
        self.animations[ActorArrowChargedPlayer.State.EXPLODE] = Animation(load_image("assets/bullet_charged_explosion.png", False), Rect(0, 0, 192, 192), 5, 100, callback_fun=self.bye)

        self._state = ActorArrowChargedPlayer.State.TRAVEL

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_state):
        rect = self.rect
        self._state = new_state
        self.rect.center = rect.center
    @property
    def animation(self):
        return self.animations[self.state]

    def destroy(self):
        self.speed = 0
        self.state = ActorArrowChargedPlayer.State.EXPLODE
        event = pygame.event.Event(pygame.USEREVENT, name=EVENT_EXPLOSION,
                                   pos=Vector(self.rect.centerx, self.rect.centery), radius=self.radius, team=self.team,
                                   damage=self.damage)
        pygame.event.post(event)
        self.team = EnumTeam.NEUTRAL_TEAM

    def bye(self):
        self.map.remove_actor(self)
        del self