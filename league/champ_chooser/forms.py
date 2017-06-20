from django import forms

REGIONS = [
    ('NA1','NA'),
    ('EUW1','EUW'),
    ('EUN1','EUN'),
    ('KR','KR'),
    ('RU','RUS'),
    ('BR1','BR'),
    ('JP1','JP'),
    ('LA1','LAN'),
    ('LA2','LAS'),
    ('TR1','TUR'),
    ('OC1','OCE'),
    ('PBE1','PBE')
]

class submit_summoner_info(forms.Form):
    name = forms.CharField()
    region = forms.CharField(label='Region:',widget=forms.Select(choices=REGIONS))