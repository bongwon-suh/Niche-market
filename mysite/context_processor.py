from market.models import Location, Market


def nav_menu(request):
        queryset = Location.objects.all()
        queryset1 = Market.objects.filter(location_id=3)
        return {
            'location': queryset,
            'market_list': queryset1,
        }