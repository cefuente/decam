Cesar I. Fuentes, CFG


20140213

Code to spit out the pointing centroids for DECam observations centered around a given RA, Dec

right now it runs as:

# Upgraded the field centers to coincide with the opposition point on 4/29 midnight (middle of obsrun)

python call_coord_NEO_DECam_201404.py --direction south --night 20140422 --raC 14:24:54 --decC -14:22:11 --len_ra 8 --len_dec 8 --exptime 40 --filter VR --npasses 5 > 20140226_neodecam.edb



20140420
python call_coord_NEO_DECam_201404.py --direction south --raC 14:24:54 --decC -14:22:11 --len_ra 10 --len_dec 10 --exptime 40 --filter VR --npasses 5 --dirout obsplan_json > ~/.xephem/catalogs/neodecam_201404_10x10.edb 




20140503:
In order to run a smaller 6x6 field I run in the following way:

python call_coord_NEO_DECam_201404.py --direction south --night 20140503 --raC 14:40:00 --decC -40:00:00 --len_ra 8 --len_dec 8 --exptime 40 --filter VR --npasses 5 --quadstr S --dirout S_0503 --nameroot S_0503 > S_0503/S_0503.edb; cp S_0503/S_0503.edb ~/.xephem/catalogs/.



L4_0MDD:

python call_coord_NEO_DECam_201404.py --direction south  --raC 22:10:00 --decC -11:19:24 --len_ra 3 --len_dec 3 --exptime 40 --filter VR --npasses 5 --dirout L4_0422 --nameroot L4_0422 > L4_0422/L4_0422.edb; cp L4_0422/L4_0422.edb ~/.xephem/catalogs/.
python call_coord_NEO_DECam_201404.py --direction south  --raC 22:13:42 --decC -10:58:42 --len_ra 3 --len_dec 3 --exptime 40 --filter VR --npasses 5 --dirout L4_0423 --nameroot L4_0423 > L4_0423/L4_0423.edb; cp L4_0423/L4_0423.edb ~/.xephem/catalogs/.
python call_coord_NEO_DECam_201404.py --direction south  --raC 22:17:24 --decC -10:37:48 --len_ra 3 --len_dec 3 --exptime 40 --filter VR --npasses 5 --dirout L4_0424 --nameroot L4_0424 > L4_0424/L4_0424.edb; cp L4_0424/L4_0424.edb ~/.xephem/catalogs/.
python call_coord_NEO_DECam_201404.py --direction south  --raC 22:21:06.6 --decC -10:16:42 --len_ra 3 --len_dec 3 --exptime 40 --filter VR --npasses 5 --dirout L4_0425 --nameroot L4_0425 > L4_0425/L4_0425.edb; cp L4_0425/L4_0425.edb ~/.xephem/catalogs/.
python call_coord_NEO_DECam_201404.py --direction south  --raC 22:24:48 --decC -9:55:30 --len_ra 3 --len_dec 3 --exptime 40 --filter VR --npasses 5 --dirout L4_0426 --nameroot L4_0426 > L4_0426/L4_0426.edb; cp L4_0426/L4_0426.edb ~/.xephem/catalogs/.
python call_coord_NEO_DECam_201404.py --direction south  --raC 22:28:29 --decC -9:34:06 --len_ra 3 --len_dec 3 --exptime 40 --filter VR --npasses 5 --dirout L4_0427 --nameroot L4_0427 > L4_0427/L4_0427.edb; cp L4_0427/L4_0427.edb ~/.xephem/catalogs/.
python call_coord_NEO_DECam_201404.py --direction south  --raC 22:32:10 --decC -9:12:36 --len_ra 3 --len_dec 3 --exptime 40 --filter VR --npasses 5 --dirout L4_0428 --nameroot L4_0428 > L4_0428/L4_0428.edb; cp L4_0428/L4_0428.edb ~/.xephem/catalogs/.
python call_coord_NEO_DECam_201404.py --direction south  --raC 22:35:50 --decC -8:51:00 --len_ra 3 --len_dec 3 --exptime 40 --filter VR --npasses 5 --dirout L4_0429 --nameroot L4_0429 > L4_0429/L4_0429.edb; cp L4_0429/L4_0429.edb ~/.xephem/catalogs/.
python call_coord_NEO_DECam_201404.py --direction south  --raC 22:39:29 --decC -8:29:12 --len_ra 3 --len_dec 3 --exptime 40 --filter VR --npasses 5 --dirout L4_0430 --nameroot L4_0430 > L4_0430/L4_0430.edb; cp L4_0430/L4_0430.edb ~/.xephem/catalogs/.
python call_coord_NEO_DECam_201404.py --direction south  --raC 22:43:08 --decC -8:07:18 --len_ra 3 --len_dec 3 --exptime 40 --filter VR --npasses 5 --dirout L4_0501 --nameroot L4_0501 > L4_0501/L4_0501.edb; cp L4_0501/L4_0501.edb ~/.xephem/catalogs/.
python call_coord_NEO_DECam_201404.py --direction south  --raC 22:46:47 --decC -7:45:18 --len_ra 3 --len_dec 3 --exptime 40 --filter VR --npasses 5 --dirout L4_0502 --nameroot L4_0502 > L4_0502/L4_0502.edb; cp L4_0502/L4_0502.edb ~/.xephem/catalogs/.
python call_coord_NEO_DECam_201404.py --direction south  --raC 22:50:25 --decC -7:23:12 --len_ra 3 --len_dec 3 --exptime 40 --filter VR --npasses 5 --dirout L4_0503 --nameroot L4_0503 > L4_0503/L4_0503.edb; cp L4_0503/L4_0503.edb ~/.xephem/catalogs/.
python call_coord_NEO_DECam_201404.py --direction south  --raC 22:54:03 --decC -7:01:00 --len_ra 3 --len_dec 3 --exptime 40 --filter VR --npasses 5 --dirout L4_0504 --nameroot L4_0504 > L4_0504/L4_0504.edb; cp L4_0504/L4_0504.edb ~/.xephem/catalogs/.
python call_coord_NEO_DECam_201404.py --direction south  --raC 22:57:40 --decC -6:38:42 --len_ra 3 --len_dec 3 --exptime 40 --filter VR --npasses 5 --dirout L4_0505 --nameroot L4_0505 > L4_0505/L4_0505.edb; cp L4_0505/L4_0505.edb ~/.xephem/catalogs/.





For getting the obs_times:
python NEO_DECam_obs_times.py --utcinit '2014-04-22 23:34:26' obsplan_json_8x8/Q05_obsplan.txt obsplan_json_8x8/Q04_obsplan.txt obsplan_json_8x8/Q03_obsplan.txt obsplan_json_8x8/Q02_obsplan.txt obsplan_json_8x8/Q10_obsplan.txt obsplan_json_8x8/Q11_obsplan.txt obsplan_json_8x8/Q12_obsplan.txt obsplan_json_8x8/Q13_obsplan.txt obsplan_json_8x8/Q21_obsplan.txt obsplan_json_8x8/Q20_obsplan.txt obsplan_json_8x8/Q19_obsplan.txt obsplan_json_8x8/Q18_obsplan.txt obsplan_json_8x8/Q26_obsplan.txt obsplan_json_8x8/Q27_obsplan.txt obsplan_json_8x8/Q28_obsplan.txt obsplan_json_8x8/Q29_obsplan.txt obsplan_json_8x8/Q37_obsplan.txt obsplan_json_8x8/Q36_obsplan.txt obsplan_json_8x8/Q35_obsplan.txt obsplan_json_8x8/Q34_obsplan.txt obsplan_json_8x8/Q42_obsplan.txt obsplan_json_8x8/Q43_obsplan.txt obsplan_json_8x8/Q44_obsplan.txt obsplan_json_8x8/Q45_obsplan.txt




