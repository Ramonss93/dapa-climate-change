##### python D:\dapa-climate-change\IPCC-CMIP5\inventory_cmip5_daily.py T:\gcm\cmip5\raw\daily T:\gcm\cmip5\raw\daily
import os, sys, glob, string, shutil, errno
import os.path
import string
import os
import glob
import re
import itertools
import operator
import urllib2

dirbase = sys.argv[1]
outdir = sys.argv[2]
# outdir = 'X:\rcm\cordex'


### dirbase = 'F:\jtarapues\CORDEX\\'

	


sresDc = {"historical":"1"}#{"historical":"1","rcp2_6": "2", "rcp4_5": "3", "rcp6_0": "4", "rcp8_5": "5"}
varDc = {"pr":"1", "tas":"3", "tasmax":"2", "tasmin":"4", "hur":"7", "rsds":"5","sfcWind":"8"}
modelDc = {"cccma_canesm2":"1","gfdl_cm3":"2","gfdl_esm2g":"3","gfdl_esm2m":"4","giss_e2_h":"5","giss_e2_h_cc":"6","giss_e2_r":"7","giss_e2_r_cc":"8","inm_cm4":"9","ipsl_cm5a_lr":"10","ipsl_cm5a_mr":"11","ipsl_cm5b_lr":"12","miroc_miroc5":"13","mri_cgcm3":"14","ncar_ccsm4":"15","bcc_csm1_1":"16","bcc_csm1_1_m":"17","bnu_esm":"18","cesm1_bgc":"19","cesm1_cam5":"20","cnrm_cm5":"21","csiro_access1_0":"22","csiro_access1_3":"23","csiro_mk3_6_0":"24","ec_earth":"25","fio_esm":"26","lasg_fgoals_g2":"27","miroc_esm":"28","miroc_esm_chem":"29","mohc_hadgem2_cc":"30","mohc_hadgem2_es":"31","mpi_esm_lr":"32","mpi_esm_mr":"33","ncc_noresm1_m":"34","nimr_hadgem2_ao":"35","cccma_cancm4":"36","cmcc_cms":"37","lasg_fgoals_s2":"38","miroc_miroc4h":"39","mohc_hadcm3":"40","mohc_hadcm3":"40"}


		
for sres in sorted(sresDc):	
	dirouttxt=outdir+"\\"+sres+"_inventory_cmip5_daily.txt"
	if not os.path.exists(dirouttxt):
		dirouttxt = open(dirouttxt,'w')
		# dirouttxt.write("id"+ "\t"+ "name"+ "\t"+ "method_id"+ "\t"+ "scenario_id"+ "\t"+ "period_id"+ "\t"+ "model_id"+ "\t"+ "variable_id"+ "\t"+ "resolution_id"+ "\t"+ "format_id"+ "\t"+ "file_set_id"+ "\t"+ "region_id"+ "\t"+ "tiles"+ "\t"+ "local_url"+ "\t"+ "availability_status_id"+ "\n")
		dirouttxt.close()		
	modellist = sorted(os.listdir(dirbase + "\\" + sres))
	for model in modellist:
		# for var in varlist:
		indir = dirbase + "\\" + sres  + "\\" + model +"\\r1i1p1"
		localurl = "/" + sres + "/" + model+"/r1i1p1"
		
		os.chdir(indir)
		nclis = glob.glob("*.nc")
		for nc in nclis:
			var=nc.split("_")[0]
			yi=nc.split("_")[5].split("-")[0]
			yf=nc.split("_")[5].split("-")[1].split(".")[0]
			print nc
			sizeFile=os.path.getsize(indir+"\\"+nc)
			txt = open(dirouttxt,'a')
			txt.write(nc+ "\t1\t"+ sresDc[sres]+ "\t"+ modelDc[model]+ "\t"+ varDc[var]+ "\t"+ yi+ "\t"+ yf+ "\t"+ str(sizeFile)+ "\t"+ localurl+ "\n")
	dirouttxt.close()
				