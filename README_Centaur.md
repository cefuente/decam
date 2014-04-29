

run:
--raC 14:30:30 --decC -14:49:30 opposition point on 20140430 16:00:00 UTC (midday between 29, 30)

python call_coord_Centaur_DECam.py --direction south  --raC 14:30:30 --decC -14:49:30 --len_ra 5 --len_dec 1 --exptime 300 --filter VR --npasses 3 --sub_ra 3 --sub_dec 3 --dirout CenCat_20140429 --nameroot Cen > CenCat_20140429/CenCat_20140429.edb; cp CenCat_20140429/CenCat_20140429.edb ~/.xephem/catalogs/.









python point_coord_NEO_DEcam.py --raC 15:30:00 --decC -18:20:00 --exptime 300 --quadrant CentTest --npasses 5 --sub_ra 3 --sub_dec 3 --direction south --dirout CenTest --fname CenTest.json --verbose > CenTest/CenTest.edb ; cp CenTest/CenTest.edb ~/.xephem/catalogs/.



python call_coord_Centaur_DECam.py --direction south  --raC 15:50:00 --decC -10:00:00 --len_ra 3 --len_dec 3 --exptime 300 --filter VR --npasses 3 --dirout CenTest --nameroot CenTest > CenTest/CenTest.edb; cp CenTest/CenTest.edb ~/.xephem/catalogs/.
