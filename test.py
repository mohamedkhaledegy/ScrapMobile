from django.contrib.gis.geos import GEOSGeometry
pnt = GEOSGeometry('SRID=4326;POINT(40.396764 -3.68042)')
pnt2 = GEOSGeometry('SRID=4326;POINT( 48.835797 2.329102  )')
pnt.distance(pnt2) * 100