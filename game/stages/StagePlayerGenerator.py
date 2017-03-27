import os
import random

import pygame

from game.actors.ActorButtonSimple import ActorButtonSimple
from game.actors.ActorSimpleLife import ActorSimpleLife
from game.actors.ActorText import ActorText
from game.utils.Constants import *
from game.stages.StageHandleConsole import StageHandleConsole
from game.utils.SurfaceHelper import load_image

GENERATOR_PATH = "generator/"
SEXE_PATH = ["male/", "female/"]
BODY_PATH = "body/"
EARS_PATH = "ears/"
EYES_PATH = "eyes/"
NOSE_PATH = "nose/"
HAIR_TYPE = "hair/"
LEGS_TYPE = "legs/"
HEAD_TYPE = "head/"
TORSO_TYPE = "torso/"
HANDS_TYPE = "hands/"
FEET_TYPE = "feet/"
BOW_PATH = "bow/"



class StagePlayerGenerator(StageHandleConsole):
    def __init__(self):
        super().__init__()

        # Trucs nécessaire à la génération

        self._sexe = 0  # 0 Pour homme, 1 pour femme

        self.body_list = []
        self._body_index = 0

        self.ears_list = []
        self._ears_index = 0

        self.eyes_list = []
        self._eyes_index = 0

        self.nose_list = []
        self._nose_index = 0

        self.hair_type_list = []
        self._hair_type_index = 0

        self.hair_color_list = {}
        self._hair_color_index = 0

        self.legs_type_list = []
        self._legs_type_index = 0

        self.legs_color_list = {}
        self._legs_color_index = 0

        self.head_type_list = []
        self._head_type_index = 0

        self.head_color_list = {}
        self._head_color_index = 0

        self.torso_type_list = []
        self._torso_type_index = 0

        self.torso_color_list = {}
        self._torso_color_index = 0

        self.hands_type_list = []
        self._hands_type_index = 0

        self.hands_color_list = {}
        self._hands_color_index = 0

        self.feet_type_list = []
        self._feet_type_index = 0

        self.feet_color_list = {}
        self._feet_color_index = 0

        self.bow_list = []
        self._bow_index = 0

        self.generated_sprite = None
        self.sprite_to_draw = None

        self.load_files()
        self.generate()

        buttons = [ActorButtonSimple("previous", self.sexe_previous),
                   ActorText("SEXE"),
                   ActorButtonSimple("next", self.sexe_next),
                   ActorButtonSimple("previous", self.body_previous),
                   ActorText("BODY"),
                   ActorButtonSimple("next", self.body_next),
                   ActorButtonSimple("previous", self.ears_previous),
                   ActorText("EARS"),
                   ActorButtonSimple("next", self.ears_next),
                   ActorButtonSimple("previous", self.eyes_previous),
                   ActorText("EYES"),
                   ActorButtonSimple("next", self.eyes_next),
                   ActorButtonSimple("previous", self.nose_previous),
                   ActorText("NOSE"),
                   ActorButtonSimple("next", self.nose_next),
                   ActorButtonSimple("previous", self.hair_type_previous),
                   ActorText("HAIR TYPE"),
                   ActorButtonSimple("next", self.hair_type_next),
                   ActorButtonSimple("previous", self.hair_color_previous),
                   ActorText("HAIR COLOR"),
                   ActorButtonSimple("next", self.hair_color_next), # à inverser
                   ActorButtonSimple("previous", self.legs_type_previous),
                   ActorText("LEGS TYPE"),
                   ActorButtonSimple("next", self.legs_type_next),
                   ActorButtonSimple("previous", self.legs_color_previous),
                   ActorText("LEGS COLOR"),
                   ActorButtonSimple("next", self.legs_color_next),
                   ActorButtonSimple("previous", self.head_type_previous),
                   ActorText("HEAD TYPE"),
                   ActorButtonSimple("next", self.head_type_next),
                   ActorButtonSimple("previous", self.head_color_previous),
                   ActorText("HEAD COLOR"),
                   ActorButtonSimple("next", self.head_color_next),
                   ActorButtonSimple("previous", self.torso_type_previous),
                   ActorText("TORSO TYPE"),
                   ActorButtonSimple("next", self.torso_type_next),
                   ActorButtonSimple("previous", self.torso_color_previous),
                   ActorText("TORSO COLOR"),
                   ActorButtonSimple("next", self.torso_color_next),
                   ActorButtonSimple("previous", self.hands_type_previous),
                   ActorText("HANDS TYPE"),
                   ActorButtonSimple("next", self.hands_type_next),
                   ActorButtonSimple("previous", self.hands_color_previous),
                   ActorText("HANDS COLOR"),
                   ActorButtonSimple("next", self.hands_color_next),
                   ActorButtonSimple("previous", self.feet_type_previous),
                   ActorText("FEET TYPE"),
                   ActorButtonSimple("next", self.feet_type_next),
                   ActorButtonSimple("previous", self.feet_color_previous),
                   ActorText("FEET COLOR"),
                   ActorButtonSimple("next", self.feet_color_next)
                   ]
        # self.map.add_actor(ActorSimpleLife("character_gen_background.jpg")) Fond d'écran ?

        for index, button in enumerate(buttons):
            self.map.add_actor(button)
            button.rect.center = (100 * (index % 3) + 25, (self.screen.get_height() / (len(buttons) + 2)) * index - (self.screen.get_height() / (len(buttons) + 2)) * (index % 3) + 2 * (self.screen.get_height() / (len(buttons) + 2)))

        # Ajout d'un bouton randomize
        # button_randomize = ActorButtonSimple(files_prefix="randomize", callback_fun=self.randomize)

    def reset(self):
        self._body_index = 0
        self._ears_index = 0
        self._eyes_index = 0
        self._nose_index = 0
        self._hair_type_index = 0
        self._hair_color_index = 0
        self._legs_type_index = 0
        self._legs_color_index = 0
        self._hands_type_index = 0
        self._hands_color_index = 0
        self._feet_type_index = 0
        self._feet_color_index = 0
        self._head_type_index = 0
        self._head_color_index = 0
        self._torso_type_index = 0
        self._torso_color_index = 0

        self.generate()

    def randomize(self):
        self.sexe = random.randint(0, 1)

        self._body_index = random.randint(0, len(self.body_list) - 1)
        self._ears_index = random.randint(0, len(self.ears_list) - 1)
        self._eyes_index = random.randint(0, len(self.eyes_list) - 1)
        self._nose_index = random.randint(0, len(self.nose_list) - 1)
        self._hair_type_index = random.randint(0, len(self.hair_type_list) - 1)
        self._hair_color_index = random.randint(0, len(self.hair_color_list[self.hair_type_list[self.hair_type_index]]) - 1)
        self._legs_type_index = random.randint(0, len(self.legs_type_list) - 1)
        self._legs_color_index = random.randint(0, len(self.legs_color_list[self.legs_type_list[self.legs_type_index]]) - 1)
        self._head_type_index = random.randint(0, len(self.head_type_list) - 1)
        self._head_color_index = random.randint(0, len(self.head_color_list[self.head_type_list[self.head_type_index]]) - 1)
        self._torso_type_index = random.randint(0, len(self.torso_type_list) - 1)
        self._torso_color_index = random.randint(0, len(self.torso_color_list[self.torso_type_list[self.torso_type_index]]) - 1)
        self._hands_type_index = random.randint(0, len(self.hands_type_list) - 1)
        self._hands_color_index = random.randint(0, len(self.hands_color_list[self.hands_type_list[self.hands_type_index]]) - 1)
        self._feet_type_index = random.randint(0, len(self.feet_type_list) - 1)
        self._feet_color_index = random.randint(0, len(self.feet_color_list[self.feet_type_list[self.feet_type_index]]) - 1)

        self.generate()

    def sexe_next(self):
        self.sexe += 1

    def sexe_previous(self):
        self.sexe -= 1

    def body_next(self):
        self.body_index += 1

    def body_previous(self):
        self.body_index -= 1
        
    def ears_next(self):
        self.ears_index += 1

    def ears_previous(self):
        self.ears_index -= 1
    
    def eyes_next(self):
        self.eyes_index += 1

    def eyes_previous(self):
        self.eyes_index -= 1
        
    def nose_next(self):
        self.nose_index += 1

    def nose_previous(self):
        self.nose_index -= 1
        
    def hair_type_next(self):
        self.hair_type_index += 1

    def hair_type_previous(self):
        self.hair_type_index -= 1

    def hair_color_next(self):
        self.hair_color_index += 1

    def hair_color_previous(self):
        self.hair_color_index -= 1
        
    def legs_type_next(self):
        self.legs_type_index += 1

    def legs_type_previous(self):
        self.legs_type_index -= 1

    def legs_color_next(self):
        self.legs_color_index += 1

    def legs_color_previous(self):
        self.legs_color_index -= 1
        
    def head_type_next(self):
        self.head_type_index += 1

    def head_type_previous(self):
        self.head_type_index -= 1

    def head_color_next(self):
        self.head_color_index += 1

    def head_color_previous(self):
        self.head_color_index -= 1

    def torso_type_next(self):
        self.torso_type_index += 1

    def torso_type_previous(self):
        self.torso_type_index -= 1

    def torso_color_next(self):
        self.torso_color_index += 1

    def torso_color_previous(self):
        self.torso_color_index -= 1
        
    def hands_type_next(self):
        self.hands_type_index += 1

    def hands_type_previous(self):
        self.hands_type_index -= 1

    def hands_color_next(self):
        self.hands_color_index += 1

    def hands_color_previous(self):
        self.hands_color_index -= 1
        
    def feet_type_next(self):
        self.feet_type_index += 1

    def feet_type_previous(self):
        self.feet_type_index -= 1

    def feet_color_next(self):
        self.feet_color_index += 1

    def feet_color_previous(self):
        self.feet_color_index -= 1

    def save(self, filename):
        pygame.image.save(self.generated_sprite, "assets/" + filename + ".png")

    def load_files(self):
        path = GENERATOR_PATH + BODY_PATH + SEXE_PATH[self.sexe]
        self.body_list.clear()
        for file in os.listdir(path):
            if os.path.isfile(path + file):
                self.body_list.append(path + file)

        path = GENERATOR_PATH + EARS_PATH + SEXE_PATH[self.sexe]
        self.ears_list.clear()
        for file in os.listdir(path):
            if os.path.isfile(path + file):
                self.ears_list.append(path + file)

        path = GENERATOR_PATH + EYES_PATH + SEXE_PATH[self.sexe]
        self.eyes_list.clear()
        for file in os.listdir(path):
            if os.path.isfile(path + file):
                self.eyes_list.append(path + file)

        path = GENERATOR_PATH + NOSE_PATH + SEXE_PATH[self.sexe]
        self.nose_list.clear()
        for file in os.listdir(path):
            if os.path.isfile(path + file):
                self.nose_list.append(path + file)

        # Chargement des cheveux un petit peu diffèrent !
        path = GENERATOR_PATH + HAIR_TYPE + SEXE_PATH[self.sexe]
        self.hair_type_list.clear()
        for dir in os.listdir(path):
            if os.path.isdir(path + dir):
                self.hair_type_list.append(path + dir + "/")

        items_to_remove = []
        for path in self.hair_type_list:
            self.hair_color_list[path] = []
            for file in os.listdir(path):
                if os.path.isfile(path + file):
                    self.hair_color_list[path].append(path + file)

            if not self.hair_color_list[path]:
                del self.hair_color_list[path]
                items_to_remove.append(path)
        for item in items_to_remove:
            self.hair_type_list.remove(item)

        # Chargement pantalon
        path = GENERATOR_PATH + LEGS_TYPE
        self.legs_type_list.clear()
        for dir in os.listdir(path):
            if os.path.isdir(path + dir):
                self.legs_type_list.append(path + dir + "/" + SEXE_PATH[self.sexe])

        items_to_remove = []
        for path in self.legs_type_list:
            self.legs_color_list[path] = []
            for file in os.listdir(path):
                if os.path.isfile(path + file):
                    self.legs_color_list[path].append(path + file)

            if not self.legs_color_list[path]:
                del self.legs_color_list[path]
                items_to_remove.append(path)
        for item in items_to_remove:
            self.legs_type_list.remove(item)

        # Chargement casque
        path = GENERATOR_PATH + HEAD_TYPE
        self.head_type_list.clear()
        for dir in os.listdir(path):
            if os.path.isdir(path + dir):
                self.head_type_list.append(path + dir + "/" + SEXE_PATH[self.sexe])

        items_to_remove = []
        for path in self.head_type_list:
            self.head_color_list[path] = []
            for file in os.listdir(path):
                if os.path.isfile(path + file):
                    self.head_color_list[path].append(path + file)
            if not self.head_color_list[path]:
                del self.head_color_list[path]
                items_to_remove.append(path)
        for item in items_to_remove:
            self.head_type_list.remove(item)

        # Chargement torsos
        path = GENERATOR_PATH + TORSO_TYPE
        self.torso_type_list.clear()
        for dir in os.listdir(path):
            if os.path.isdir(path + dir):
                self.torso_type_list.append(path + dir + "/" + SEXE_PATH[self.sexe])

        items_to_remove = []
        for path in self.torso_type_list:
            self.torso_color_list[path] = []
            for file in os.listdir(path):
                if os.path.isfile(path + file):
                    self.torso_color_list[path].append(path + file)
            if not self.torso_color_list[path]:
                del self.torso_color_list[path]
                items_to_remove.append(path)
        for item in items_to_remove:
            self.torso_type_list.remove(item)

        # Chargement mains
        path = GENERATOR_PATH + HANDS_TYPE
        self.hands_type_list.clear()
        for dir in os.listdir(path):
            if os.path.isdir(path + dir):
                self.hands_type_list.append(path + dir + "/" + SEXE_PATH[self.sexe])

        items_to_remove = []
        for path in self.hands_type_list:
            self.hands_color_list[path] = []
            for file in os.listdir(path):
                if os.path.isfile(path + file):
                    self.hands_color_list[path].append(path + file)
            if not self.hands_color_list[path]:
                del self.hands_color_list[path]
                items_to_remove.append(path)
        for item in items_to_remove:
            self.hands_type_list.remove(item)

        # Chargement pieds
        path = GENERATOR_PATH + FEET_TYPE
        self.feet_type_list.clear()
        for dir in os.listdir(path):
            if os.path.isdir(path + dir):
                self.feet_type_list.append(path + dir + "/" + SEXE_PATH[self.sexe])

        items_to_remove = []
        for path in self.feet_type_list:
            self.feet_color_list[path] = []
            for file in os.listdir(path):
                if os.path.isfile(path + file):
                    self.feet_color_list[path].append(path + file)
            if not self.feet_color_list[path]:
                del self.feet_color_list[path]
                items_to_remove.append(path)
        for item in items_to_remove:
            self.feet_type_list.remove(item)

        # Chargement de l'arc
        path = GENERATOR_PATH + BOW_PATH
        self.bow_list.clear()
        for file in os.listdir(path):
            if os.path.isfile(path + file):
                self.bow_list.append(path + file)

    def generate(self):
        """Génère l'image produite par les attributs choisis"""

        # On charge d'abord le 'body'
        self.generated_sprite = load_image(self.body_list[self.body_index], False)
        # On copie par dessus nos éléments
        # Ears
        self.generated_sprite.blit(
            load_image(self.ears_list[self.ears_index], False),
            (0, 0))
        # Eyes
        self.generated_sprite.blit(
            load_image(self.eyes_list[self.eyes_index], False),
            (0, 0))
        # Nose
        self.generated_sprite.blit(
            load_image(self.nose_list[self.nose_index], False),
            (0, 0))

        # Hair
        self.generated_sprite.blit(
            load_image(self.hair_color_list[self.hair_type_list[self.hair_type_index]][self.hair_color_index],
                       False),
            (0, 0))

        # Legs
        self.generated_sprite.blit(
            load_image(self.legs_color_list[self.legs_type_list[self.legs_type_index]][self.legs_color_index],
                       False),
            (0, 0))

        # Head
        self.generated_sprite.blit(
            load_image(self.head_color_list[self.head_type_list[self.head_type_index]][self.head_color_index],
                       False),
            (0, 0))

        # Torso
        self.generated_sprite.blit(
            load_image(self.torso_color_list[self.torso_type_list[self.torso_type_index]][self.torso_color_index],
                       False),
            (0, 0))

        # Hands
        self.generated_sprite.blit(
            load_image(self.hands_color_list[self.hands_type_list[self.hands_type_index]][self.hands_color_index],
                       False),
            (0, 0))
        

        # Feet
        self.generated_sprite.blit(
            load_image(self.feet_color_list[self.feet_type_list[self.feet_type_index]][self.feet_color_index],
                       False),
            (0, 0))

        self.sprite_to_draw = self.generated_sprite.subsurface(PLAYER_STANDBY.x * PLAYER_SPRITE_WIDTH,
                                         PLAYER_STANDBY.y * PLAYER_SPRITE_HEIGHT,
                                         PLAYER_SPRITE_WIDTH, PLAYER_SPRITE_HEIGHT)

        # Bow
        self.generated_sprite.blit(
            load_image(self.bow_list[self.bow_index], False),
            (0, 0))

        self.sprite_to_draw = pygame.transform.scale2x(self.sprite_to_draw)

    def draw(self):
        super().draw()
        self.screen.blit(self.sprite_to_draw, ((self.screen.get_width() - self.sprite_to_draw.get_width()) / 2, (self.screen.get_height() - self.sprite_to_draw.get_height()) / 2))

    def execute(self, command):
        super().execute(command)
        commands = command.split(" ")

        if commands[0] == "next":
            if commands[1] == "body":
                self.body_index += 1
            elif commands[1] == "ears":
                self.ears_index += 1
            elif commands[1] == "eyes":
                self.eyes_index += 1
            elif commands[1] == "nose":
                self.nose_index += 1
            elif commands[1] == "hair_type":
                self.hair_type_index += 1
            elif commands[1] == "hair_color":
                self.hair_color_index += 1
            elif commands[1] == "legs_type":
                self.legs_type_index += 1
            elif commands[1] == "legs_color":
                self.legs_color_index += 1
            elif commands[1] == "head_type":
                self.head_type_index += 1
            elif commands[1] == "head_color":
                self.head_color_index += 1
            elif commands[1] == "torso_type":
                self.torso_type_index += 1
            elif commands[1] == "torso_color":
                self.torso_color_index += 1
            elif commands[1] == "hands_type":
                self.hands_type_index += 1
            elif commands[1] == "hands_color":
                self.hands_color_index += 1
            elif commands[1] == "feet_type":
                self.feet_type_index += 1
            elif commands[1] == "feet_color":
                self.feet_color_index += 1
        elif commands[0] == "sexe":
            self.sexe = int(commands[1])
        elif commands[0] == "save":
            self.save(commands[1])
        elif commands[0] == "rand":
            self.randomize()
        elif commands[0] == "reset":
            self.reset()
        else:
            print(command, ": commande non reconnue")

    @property
    def body_index(self):
        return self._body_index

    @body_index.setter
    def body_index(self, index):
        if index != self.body_index:
            self._body_index = index % len(self.body_list)
            self.generate()

    @property
    def bow_index(self):
        return self._bow_index

    @bow_index.setter
    def bow_index(self, index):
        if index != self.bow_index:
            self._bow_index = index % len(self.bow_list)
            self.generate()

    @property
    def ears_index(self):
        return self._ears_index

    @ears_index.setter
    def ears_index(self, index):
        if index != self.ears_index:
            self._ears_index = index % len(self.ears_list)
            self.generate()

    @property
    def eyes_index(self):
        return self._eyes_index

    @eyes_index.setter
    def eyes_index(self, index):
        if index != self.eyes_index:
            self._eyes_index = index % len(self.eyes_list)
            self.generate()

    @property
    def nose_index(self):
        return self._nose_index

    @nose_index.setter
    def nose_index(self, index):
        if index != self.nose_index:
            self._nose_index = index % len(self.nose_list)
            self.generate()

    @property
    def hair_color_index(self):
        return self._hair_color_index

    @hair_color_index.setter
    def hair_color_index(self, index):
        if index != self.hair_color_index:
            self._hair_color_index = index % len(self.hair_color_list[self.hair_type_list[self.hair_type_index]])
            self.generate()

    @property
    def hair_type_index(self):
        return self._hair_type_index

    @hair_type_index.setter
    def hair_type_index(self, index):
        if index != self.hair_type_index:
            self._hair_type_index = index % len(self.hair_type_list)
            try:
                self.hair_color_list[self.hair_type_list[self.hair_type_index]][self.hair_color_index]
            except:
                self.hair_color_index = 0
            self.generate()

    @property
    def legs_color_index(self):
        return self._legs_color_index

    @legs_color_index.setter
    def legs_color_index(self, index):
        if index != self.legs_color_index:
            self._legs_color_index = index % len(self.legs_color_list[self.legs_type_list[self.legs_type_index]])
            self.generate()

    @property
    def legs_type_index(self):
        return self._legs_type_index

    @legs_type_index.setter
    def legs_type_index(self, index):
        if index != self.legs_type_index:
            self._legs_type_index = index % len(self.legs_type_list)
            try:
                self.legs_color_list[self.legs_type_list[self.legs_type_index]][self.legs_color_index]
            except:
                self.legs_color_index = 0
            self.generate()

    @property
    def head_color_index(self):
        return self._head_color_index

    @head_color_index.setter
    def head_color_index(self, index):
        if index != self.head_color_index:
            self._head_color_index = index % len(self.head_color_list[self.head_type_list[self.head_type_index]])
            self.generate()

    @property
    def head_type_index(self):
        return self._head_type_index

    @head_type_index.setter
    def head_type_index(self, index):
        if index != self.head_type_index:
            self._head_type_index = index % len(self.head_type_list)
            try:
                self.head_color_list[self.head_type_list[self.head_type_index]][self.head_color_index]
            except:
                self.head_color_index = 0
            self.generate()

    @property
    def torso_color_index(self):
        return self._torso_color_index

    @torso_color_index.setter
    def torso_color_index(self, index):
        if index != self.torso_color_index:
            self._torso_color_index = index % len(self.torso_color_list[self.torso_type_list[self.torso_type_index]])
            self.generate()

    @property
    def torso_type_index(self):
        return self._torso_type_index

    @torso_type_index.setter
    def torso_type_index(self, index):
        if index != self.torso_type_index:
            self._torso_type_index = index % len(self.torso_type_list)
            try:
                self.torso_color_list[self.torso_type_list[self.torso_type_index]][self.torso_color_index]
            except:
                self.torso_color_index = 0
            self.generate()

    @property
    def hands_color_index(self):
        return self._hands_color_index

    @hands_color_index.setter
    def hands_color_index(self, index):
        if index != self.hands_color_index:
            self._hands_color_index = index % len(self.hands_color_list[self.hands_type_list[self.hands_type_index]])
            self.generate()

    @property
    def hands_type_index(self):
        return self._hands_type_index

    @hands_type_index.setter
    def hands_type_index(self, index):
        if index != self.hands_type_index:
            self._hands_type_index = index % len(self.hands_type_list)
            try:
                self.hands_color_list[self.hands_type_list[self.hands_type_index]][self.hands_color_index]
            except:
                self.hands_color_index = 0
            self.generate()

    @property
    def feet_color_index(self):
        return self._feet_color_index

    @feet_color_index.setter
    def feet_color_index(self, index):
        if index != self.feet_color_index:
            self._feet_color_index = index % len(self.feet_color_list[self.feet_type_list[self.feet_type_index]])
            self.generate()

    @property
    def feet_type_index(self):
        return self._feet_type_index

    @feet_type_index.setter
    def feet_type_index(self, index):
        if index != self.feet_type_index:
            self._feet_type_index = index % len(self.feet_type_list)
            try:
                self.feet_color_list[self.feet_type_list[self.feet_type_index]][self.feet_color_index]
            except:
                self.feet_color_index = 0
            self.generate()

    @property
    def sexe(self):
        return self._sexe

    @sexe.setter
    def sexe(self, new_sexe):
        if new_sexe != self.sexe:
            self._sexe = new_sexe % 2
            self.load_files()
            try:
                self.generate()
            except:
                self.reset()
