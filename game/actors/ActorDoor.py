from api.ActorSprite import ActorSprite
from game.actors.ActorPlayer import ActorPlayer
from game.utils.SurfaceHelper import load_image
from game.utils.Vector import Vector
from api.Map import Map


class ActorDoor(ActorSprite):
    def __init__(self, next_map="", spawn_pos = Vector(0,0)):
        super().__init__(True)

        self.is_open = True
        self.next_map = next_map
        self.spawn_pos = spawn_pos

    def load_sprite(self):
        super().load_sprite()

        self.sprites = {}
        self.sprites[True] = load_image("assets/button_edit_hovered.png", False)
        self.sprites[False] = load_image("assets/button_edit_hovered.png", False)
        self.rect.w = 200
        self.rect.h = 50

    def unload_sprite(self):
        super().unload_sprite()
        del self.sprites

    @property
    def sprite(self):
        return self.sprites[self.is_open]

    def interact(self, actor):
        
        if isinstance(actor, ActorPlayer) and self.next_map != "" and self.is_open:
            import GameNightmareEscape

            del self.map
            GameNightmareEscape.GameNightmareEscape.CURRENT_STAGE.map = Map.load_editor(self.next_map)
            actor.rect.x = self.spawn_pos.x
            actor.rect.y = self.spawn_pos.y
            GameNightmareEscape.GameNightmareEscape.CURRENT_STAGE.map.add_actor(actor)
            print(self.map.actors[0].sprite)

            return True
        else:
            return False
