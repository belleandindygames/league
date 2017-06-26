from django import forms

REGIONS = [
    ('NA','NA'),
    ('EUW','EUW'),
    ('EUN','EUN'),
    ('KR','KR'),
    ('RU','RUS'),
    ('BR','BR'),
    ('JP','JP'),
    ('LAN','LAN'),
    ('LAS','LAS'),
    ('TUR','TUR'),
    ('OCE','OCE'),
    ('PBE','PBE')
]

class submit_summoner_info(forms.Form):
    name = forms.CharField()
    region = forms.CharField(label='Region:',widget=forms.Select(choices=REGIONS))