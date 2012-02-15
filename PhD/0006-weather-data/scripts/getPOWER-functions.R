#Julian Ramirez-Villegas
#January 2012
#CIAT / CCAFS / UoL

require(XML)
require(raster)

#read the data for a given row of a day (to be used in a sapply way)
#do it using an apply function to speed it up and get the data sorted out quickly
getDataDay <- function(i,sk=0,dDir) {
  wthData <- read.csv(paste(dDir,"/cell-",i,"/data.csv",sep=""),nrows=1,skip=sk)
  names(wthData) <- c("WEYR","WEDAY","SRAD","TMAX","TMIN","RAIN","WIND","DEW","T2M","RH2M")
  rainData <- wthData$RAIN
  return(rainData)
}


###################################################
#Function to get the NASA POWER data
getPOWER <- function(lat,lon,outDir) {
  setwd(outDir)
  if (!file.exists("temp.wth")) {
    baseURL <- "http://power.larc.nasa.gov/cgi-bin/cgiwrap/solar/agro.cgi?email=agroclim%40larc.nasa.gov&step=1&lat="
    theurl <- paste(baseURL,lat,"&lon=",lon,"&ms=1&ds=1&ys=1997&me=9&de=1&ye=2009&submit=Yes&p=RAIN",sep="")
    doc <- htmlTreeParse(theurl,useInternalNodes=T)
    x <- xpathApply(doc, "//body", xmlValue)
    x <- x[[1]]; x <- substring(x,1)
    fx <- file("temp.wth","w")
    writeLines(x,fx)
    close(fx)
  }
  
  #find the proper line
  tarChar <- "x"
  ff <- file("temp.wth","r")
  thisLine <- 0
  while (tarChar!="@ WEYR") {
    xx <- readLines(ff,n=1)
    tarChar <- substr(xx,1,6)
    thisLine <- thisLine+1
  }
  close(ff)
  
  y <- read.fortran("temp.wth",skip=thisLine,format=c("I6","I5","8F7"))
  names(y) <- c("WEYR","WEDAY","SRAD","TMAX","TMIN","RAIN","WIND","DEW","T2M","RH2M")
  write.csv(y[1:(nrow(y)-1),],"data.csv",quote=F,row.names=F)
}
