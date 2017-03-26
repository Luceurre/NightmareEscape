from game.utils.Vector import Vector

PLAYER_SPRITE_WIDTH = 64
PLAYER_SPRITE_HEIGHT = 64
PLAYER_MOVE_TOP = Vector(1, 8)
PLAYER_MOVE_LEFT = Vector(1, 9)
PLAYER_MOVE_BOTTOM = Vector(1, 10)
PLAYER_MOVE_RIGHT = Vector(1, 11)
PLAYER_DYING = Vector(1, 20)
PLAYER_MOVE_TILES_NUMBER = 8
PLAYER_DIE_TILES_NUMBER = 6
PLAYER_MOVE_TIME = 70
PLAYER_DYING_TIME = 300
PLAYER_STANDBY = Vector(1, 10)
PLAYER_WIDTH = 48
PLAYER_HEIGHT = 50
PLAYER_DEPTH = 20

WINDOW_WIDTH = 1408
WINDOW_HEIGHT = 832



EVENT_TP = "EVENT_TELEPORT"
# Evenement défini par :
# map_name: le nom de la Map à charger
# actor: l'Actor à téléporter
# spawn_pos: Un Vector représentant la position de l'Actor à téléporter.

EVENT_PLAYER_INTERACT = "EVENT_PLAYER_INTERACT"
# Evenement défini par :
# actor: L'Actor qui demande l'intéraction

EVENT_GAME_OVER = "EVENT_GAME_OVER"
#Evenement défini par:
# rien 

EVENT_WIN = "EVENT_GAME_WIN"