def platform(region):
    _platform = 'NA1'
    _region = region.upper()

    platforms = {
        'NA': 'NA1',
        'EUW': 'EUW1',
        'EUN': 'EUN1',
        'KR': 'KR',
        'RU': 'RU',
        'BR': 'BR1',
        'JP': 'JP1',
        'LAS': 'LA1',
        'LAN': 'LA2',
        'TUR': 'TR1',
        'OCE': 'OC1',
        'PBE': 'PBE1'
    }

    _platform = platforms[_region]

    return _platform


def game_q_config_id_to_name(q_id, live):

    _live = False

    if live:
        _live = live

    if _live:
        id_to_name = {
            0: 'CUSTOM',
            8: 'NORMAL_3x3',
            2: 'NORMAL_5x5_BLIND',
            14: 'NORMAL_5x5_DRAFT',
            4: 'RANKED_SOLO_5x5',
            6: 'RANKED_PREMADE_5x5',
            9: 'RANKED_FLEX_TT',
            41: 'RANKED_TEAM_3x3',
            42: 'RANKED_TEAM_5x5',
            16: 'ODIN_5x5_BLIND',
            17: 'ODIN_5x5_DRAFT',
            7: 'BOT_5x5',
            25: 'BOT_ODIN_5x5',
            31: 'BOT_5x5_INTRO',
            32: 'BOT_5x5_BEGINNER',
            33: 'BOT_5x5_INTERMEDIATE',
            52: 'BOT_TT_3x3',
            61: 'GROUP_FINDER_5x5',
            65: 'ARAM_5x5',
            70: 'ONEFORALL_5x5',
            72: 'FIRSTBLOOD_1x1',
            73: 'FIRSTBLOOD_2x2',
            75: 'SR_6x6',
            76: 'URF_5x5',
            78: 'ONEFORALL_MIRRORMODE_5x5',
            83: 'BOT_URF_5x5',
            91: 'NIGHTMARE_BOT_5x5_RANK1',
            92: 'NIGHTMARE_BOT_5x5_RANK2',
            93: 'NIGHTMARE_BOT_5x5_RANK5',
            96: 'ASCENSION_5x5',
            98: 'HEXAKILL',
            100: 'BILGEWATER_ARAM_5x5',
            300: 'KING_PORO_5x5',
            310: 'COUNTER_PICK',
            313: 'BILGEWATER_5x5',
            315: 'SEIGE',
            317: 'DEFINITELY_NOT_DOMINION',
            318: 'ARURF_5x5',
            325: 'ARSR_5x5',
            400: 'TEAM_BUILDER_DRAFT_UNRANKED',
            410: 'TEAM_BUILDER_DRAFT_RANKED_5x5',
            420: 'RANKED_SOLO_5x5',  # modified for live
            430: 'TB_BLIND_SUMMONERS_RIFT_5x5',
            440: 'RANKED_FLEX_SR',
            600: 'ASSASSINATE_5x5',
            610: 'DARKSTAR_3x3'
        }
    else:
        id_to_name = {
            0: 'CUSTOM',
            8: 'NORMAL_3x3',
            2: 'NORMAL_5x5_BLIND',
            14: 'NORMAL_5x5_DRAFT',
            4: 'RANKED_SOLO_5x5',
            6: 'RANKED_PREMADE_5x5',
            9: 'RANKED_FLEX_TT',
            41: 'RANKED_TEAM_3x3',
            42: 'RANKED_TEAM_5x5',
            16: 'ODIN_5x5_BLIND',
            17: 'ODIN_5x5_DRAFT',
            7: 'BOT_5x5',
            25: 'BOT_ODIN_5x5',
            31: 'BOT_5x5_INTRO',
            32: 'BOT_5x5_BEGINNER',
            33: 'BOT_5x5_INTERMEDIATE',
            52: 'BOT_TT_3x3',
            61: 'GROUP_FINDER_5x5',
            65: 'ARAM_5x5',
            70: 'ONEFORALL_5x5',
            72: 'FIRSTBLOOD_1x1',
            73: 'FIRSTBLOOD_2x2',
            75: 'SR_6x6',
            76: 'URF_5x5',
            78: 'ONEFORALL_MIRRORMODE_5x5',
            83: 'BOT_URF_5x5',
            91: 'NIGHTMARE_BOT_5x5_RANK1',
            92: 'NIGHTMARE_BOT_5x5_RANK2',
            93: 'NIGHTMARE_BOT_5x5_RANK5',
            96: 'ASCENSION_5x5',
            98: 'HEXAKILL',
            100: 'BILGEWATER_ARAM_5x5',
            300: 'KING_PORO_5x5',
            310: 'COUNTER_PICK',
            313: 'BILGEWATER_5x5',
            315: 'SEIGE',
            317: 'DEFINITELY_NOT_DOMINION',
            318: 'ARURF_5x5',
            325: 'ARSR_5x5',
            400: 'TEAM_BUILDER_DRAFT_UNRANKED',
            410: 'TEAM_BUILDER_DRAFT_RANKED_5x5',
            420: 'TEAM_BUILDER_RANKED_SOLO',
            430: 'TB_BLIND_SUMMONERS_RIFT_5x5',
            440: 'RANKED_FLEX_SR',
            600: 'ASSASSINATE_5x5',
            610: 'DARKSTAR_3x3'
        }

    return id_to_name[q_id]