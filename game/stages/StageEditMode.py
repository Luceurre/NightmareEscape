import copy

from api.EnumAuto import EnumAuto
from api.Map import Map
from api.StageManager import StageManager
from api.StageState import StageState
from game.actors.ActorSimpleLife import ActorSimpleLife
from game.stages.StageHandleConsole import StageHandleConsole
from game.stages.StageTileSelector import StageTileSelector
from game.utils.Constants import EVENT_TP
from game.utils.Grid2 import Grid2
from game.utils.Register import Register
from game.utils.Vector import Vector



class EDIT_MODE(EnumAuto):
    PICK = ()
    MOVE = ()
    REMOVE = ()
    LAYER = ()
    NONE = ()
    COPY = ()


class StageEditMode(StageHandleConsole):
    """
    Stage de l'Ã©diteur de maps
    """
    def __init__(self):
        super().__init__()

        self.mouse_pos = Vector(0, 0)
        self.object_pick = None

        self.is_paused = True
        self.mode = EDIT_MODE.PICK
        self.grid = Grid2()             #grille pour mieux positionner acteurs

        self.draw_hit_box = False

    def pause(self):
        super().pause()

        stage = StageManager().stack[-1]
        if isinstance(stage, StageTileSelector):
            self.object_pick = stage.tile_picked
            if self.object_pick is not None:
                self.state = StageState.RESUME

    def draw(self): #"Affiche l'acteur dans la main de l'utilisateur"
        super().draw()

        if self.mode == EDIT_MODE.PICK:
            #if self.grid.should_draw == True:
            #    self.fake_mouse_pos = self.grid.new_position(self.mouse_pos)              # Cette partie du code permet d'afficher les actuers, non pas à côté de la souris, mais dans les cases
            #else:                                                                          # correspondantes ( selon la grid)
            #    self.fake_mouse_pos = self.mouse_pos


            if self.object_pick is not None:
                self.screen.blit(self.object_pick.sprite, (self.mouse_pos.x, self.mouse_pos.y))
                #self.screen.blit(self.object_pick.sprite, (self.fake_mouse_pos.x, self.fake_mouse_pos.y))

        self.grid.draw(self.screen)

    def update(self):
        if self.is_paused == False:
            super().update()

    def execute(self, command): # rÃ©cupÃ¨re la commande fournie par StageCommand, agit selon celle-ci
        super().execute(command)

        commands = command.lower().split(sep=" ")
        bug = False

        if commands[0] == "map":
            if commands[1] == "load":
                self.map = Map.load_editor(commands[2])         #pour charger une map
            elif commands[1] == "save":
                self.map.save()
            elif commands[1] == "print":                        #pour sauvegarder la map
                self.map.info("Je suis : " + self.map.name)
            elif commands[1] == "type":
                if commands[2] == "print":
                    self.info(self.map.type)
                elif commands[2] == "set":
                    self.map.type = commands[3]
                else:
                    bug = True
            else:
                bug = True
        elif commands[0] == "pick":                         # pour prendre et poser des acteurs
            try:
                id = int(commands[1])
            except:
                id = commands[1]

            if isinstance(id, type("")):                    # pour obtenir l'acteur, d'abord selon son nom ( test str ) , ensuite selon son id ( int )
                class_name = Register().get_actor_by_name(id)
            else:
                class_name = Register().get_actor(id)
            if class_name is not None:
                self.object_pick = class_name(*commands[2:])
                #self.object_pick.should_update = False            #Ne sais pas l'utilité : mais est cause bug : empêche player de bouger dans editeur
            else:
                self.object_pick = None
        elif commands[0] == "pause":                        #pour mettre en pause
            self.is_paused = True
        elif commands[0] == "resume":                       #voilÃ ...
            self.is_paused = False
        elif commands[0] == "mode":                         #changer le mode actuel
            if commands[1] == "get":
                self.info(self.mode)
            elif commands[1] == "set":
                if commands[2] == "pick":                   #permet de poser acteurs
                    self.mode = EDIT_MODE.PICK
                elif commands[2] == "move":                 #permet de dÃ©placer un acteur
                    self.mode = EDIT_MODE.MOVE
                elif commands[2] == "remove":               #__________enlever___________
                    self.mode = EDIT_MODE.REMOVE
                elif commands[2] == "layer":                #changer la hauteur d'un acteur ( + ou - selon le cÃ´tÃ© oÃ¹ l'on clic )
                    self.mode = EDIT_MODE.LAYER
                elif commands[2] == "copy":                 # de copier l'acteur en question ( avec la hauteur et tt)
                    self.mode = EDIT_MODE.COPY
                else:
                    bug = True
            else:
                bug = True
        elif commands[0] == "grid":                         # pour crÃ©er une grille -> Posage d'acteur plus prÃ©cis
            if commands[1] == "turn":
                if commands[2] == "on":                     # voili voulou, allumer, Ã©teindre, rien de nouveau sous le soleil
                    self.grid.should_draw = True
                elif commands[2] == "off":
                    self.grid.should_draw = False
                else:
                    bug = True
            elif commands[1] == "set":
                try:
                    if commands[3] == "":
                        self.grid.set_size(int(commands[2]),int(commands[2]))
                    else:                                                                #Afin de donner largeur et hauteur des rectangles de la grille
                        self.grid.set_size( int(commands[2]), int(commands[3]))
                except:
                    bug = True

            elif commands[1] == "origin":
                if commands[2] == "" or commands [3] == "":
                    self.grid.set_origin(0,0)                                       #On dÃ©termine l'origine de la grille
                else:
                    self.grid.set_origin(int(commands[2]),int(commands[3]))
            else:
                bug = False

        elif commands[0] == "actor":
            if commands[1] != "":
                self.object_pick = ActorSimpleLife(commands[1])                     #permet de prendre un acteur particulier parmis les images de assets (au-dessus de tout)
            else:
                bug = True
        elif commands[0] == "tilesets":                                 #lance le stage tilesets, pour avoir une image/acteur
            self.state = StageState.PAUSE
            StageManager().push(StageTileSelector())

        else:
            bug = True

        if bug:
            print("\"", command, "\"", " est une commande inconnue", sep="")

    def handle_mouse(self, pos, rel, buttons):
        self.mouse_pos.x = pos[0]
        self.mouse_pos.y = pos[1]

        return True

    def handle_mouse_button_down(self, pos, button): # gÃ¨re ce qu'il se passe quand on clic selon le stage en cours
        if self.mode == EDIT_MODE.REMOVE:           # enlÃ¨ve l'acteur en collision avec la souris
            actor = self.map.get_actor_at(pos[0], pos[1])
            if actor is not None:
                self.map.remove_actor(actor)
        elif self.mode == EDIT_MODE.PICK:           #enregistre l'acteur Ã  la position
            if self.object_pick is not None:

                actor = copy.deepcopy(self.object_pick)
                actor.reload()

                if self.grid.should_draw:
                    actor.rect.x = self.grid.get_pos_x(pos[0])
                    actor.rect.y = self.grid.get_pos_y(pos[1])
                else:
                    actor.rect.topleft = pos

                self.map.add_actor(actor)

        elif self.mode == EDIT_MODE.MOVE:                   # prend l'acteur (l'enlÃ¨ve de la map), et le prend dans la main/souris
            actor = self.map.get_actor_at(pos[0], pos[1])
            if actor != None:
                self.map.remove_actor(actor)
                self.mode = EDIT_MODE.PICK
                self.object_pick = copy.deepcopy(actor)
                self.object_pick.reload()

        elif self.mode == EDIT_MODE.LAYER:                  # incrÃ©mente + ou - l'acteur selon que ce soit clic droit ou gauche
            actor = self.map.get_actor_at(pos[0], pos[1])
            if actor is not None:
                if button == 1:
                    actor.z += 1
                elif button == 3:
                    actor.z -= 1

        elif self.mode == EDIT_MODE.COPY:                   # meme chose que move sans supprimer l'acteur de la map
            actor = self.map.get_actor_at(pos[0], pos[1])
            if actor != None:
                self.object_pick = copy.deepcopy(actor)
                self.object_pick.reload()
                self.mode = EDIT_MODE.PICK

    def handle_userevent(self, event):                      # gÃ¨re les tÃ©lÃ©portations dans l'Ã©diteur ( un peu comme le StageLevel en plus ascÃ©tique)
        if event.name == EVENT_TP:
            actor = event.actor
            actor.rect.x = int(event.spawn_pos.x)
            actor.rect.y = int(event.spawn_pos.y)
            self.map = Map.load_editor(event.map_name)
            self.map.add_actor(event.actor)
