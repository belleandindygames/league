def platform(region):
    _platform = 'NA1'

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

    _platform = platforms[region]

    return _platform
