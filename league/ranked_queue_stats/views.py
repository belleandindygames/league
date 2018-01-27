from django.shortcuts import render

# Create your views here.


def ranked_stats(request):

    if request.method == "POST":
        form = submit_summoner_info(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            region = form.cleaned_data['region']

            summoner = validate_summoner_name(name)   # summoner_wrapper(name=name, region=region)
            summoner = summoner.replace(" ", "")
            if summoner:
                # get match data
                print('summoner is valid')
                region = region.lower()
                return redirect('{}/{}/'.format(region, summoner))
    else:
        form = submit_summoner_info()

    return render(request, 'live_match.html', {'form': form})
