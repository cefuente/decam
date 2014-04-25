Cesar I. Fuentes, CFG
20140213

Code to spit out the pointing centroids for DECam observations centered around a given RA, Dec

right now it runs as:

# Upgraded the field centers to coincide with the opposition point on 4/29 midnight (middle of obsrun)

python call_coord_NEO_DECam_201404.py --direction south --night 20140422 --raC 14:24:54 --decC -14:22:11 --len_ra 8 --len_dec 8 --exptime 40 --filter VR --npasses 5 > 20140226_neodecam.edb

L4_0425:
python call_coord_NEO_DECam_201404.py --direction south  --raC 22:21:06.6 --decC -10:16:42 --len_ra 3 --len_dec 3 --exptime 40 --filter VR --npasses 5 --dirout L4_0425 --nameroot L4_0425 > L4_0425/L4_0425.edb; cp L4_0425/L4_0425.edb ~/.xephem/catalogs/.





For getting the obs_times:
python NEO_DECam_obs_times.py --utcinit '2014-04-22 23:34:26' obsplan_json_8x8/Q05_obsplan.txt obsplan_json_8x8/Q04_obsplan.txt obsplan_json_8x8/Q03_obsplan.txt obsplan_json_8x8/Q02_obsplan.txt obsplan_json_8x8/Q10_obsplan.txt obsplan_json_8x8/Q11_obsplan.txt obsplan_json_8x8/Q12_obsplan.txt obsplan_json_8x8/Q13_obsplan.txt obsplan_json_8x8/Q21_obsplan.txt obsplan_json_8x8/Q20_obsplan.txt obsplan_json_8x8/Q19_obsplan.txt obsplan_json_8x8/Q18_obsplan.txt obsplan_json_8x8/Q26_obsplan.txt obsplan_json_8x8/Q27_obsplan.txt obsplan_json_8x8/Q28_obsplan.txt obsplan_json_8x8/Q29_obsplan.txt obsplan_json_8x8/Q37_obsplan.txt obsplan_json_8x8/Q36_obsplan.txt obsplan_json_8x8/Q35_obsplan.txt obsplan_json_8x8/Q34_obsplan.txt obsplan_json_8x8/Q42_obsplan.txt obsplan_json_8x8/Q43_obsplan.txt obsplan_json_8x8/Q44_obsplan.txt obsplan_json_8x8/Q45_obsplan.txt


