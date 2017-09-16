from django.contrib.gis.utils import LayerMapping

from .models import County

county_mapping = {
    'name': 'county',
    'geom': 'MULTIPOLYGON',
}

county_data = '/home/oty/Desktop/kenya_counties/kenya_counties.shp'


def load_county_data(verbose=True):
    lm = LayerMapping(
        County, county_data, county_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)
