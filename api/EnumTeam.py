from api.EnumAuto import EnumAuto


class EnumTeam(EnumAuto):
    PLAYER_TEAM = ()
    MONSTER_TEAM = ()
    NEUTRAL_TEAM = ()

    def get_ennemi(self):
        if self == EnumTeam.PLAYER_TEAM:
            return EnumTeam.MONSTER_TEAM
        elif self == EnumTeam.MONSTER_TEAM:
            return EnumTeam.PLAYER_TEAM
        else:
            return EnumTeam.NEUTRAL_TEAM
