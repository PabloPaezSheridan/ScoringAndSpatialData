import geopandas as gpd

gdfm =gpd.read_file("cartografias/Munic04_ESP.shp") 
gdfm_Madrid =gdfm[gdfm['COD_PROV']=='28']


gdfm_Madrid.explore(column='PrecioIn16', 
                   scheme='NaturalBreaks',
                   k=9, cmap='YlOrRd',
                   legend=False,
                   style_kwds=dict(fillOpacity=0.8)) 