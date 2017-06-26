from django import template
from ..API import get_summoner_spell_info

register = template.Library()


def sum_spell_name(spell_id):
    spell = spell_id
    try:
        spell = get_summoner_spell_info('NA1', spell, 'en_US')
    except ValueError:
        return None
    return spell['name']

register.filter(sum_spell_name)