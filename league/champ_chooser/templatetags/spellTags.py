from django import template
from ..API import get_summoner_spell_info
from ..models import SummonerSpell
from django.shortcuts import get_object_or_404

register = template.Library()


def sum_spell_name(spell_id):
    try:
        spell = get_object_or_404(SummonerSpell, id=spell_id)
    except ValueError:
        return None
    return spell.key

register.filter(sum_spell_name)