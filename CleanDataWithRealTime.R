args = commandArgs(trailingOnly = TRUE)
input_data_path = args[1]
print (input_data_path)

output_data_path =args[2]
print (output_data_path)


cleandata <-read.csv(input_data_path)

numbers <- c(1:nrow(cleandata))
long <-cleandata[["LON"]]
lat <-cleandata[["LAT"]]
magnitude <-cleandata[["MAG"]]
dates <-cleandata[["YYYY.MM.DD"]]
times <-cleandata[["HH.mm.SS.ss"]]
datatime <-as.POSIXct(strptime(paste(dates, times), "%Y/%m/%d %H:%M:%OS"))
newtime <-as.numeric(difftime(datatime,datatime[1],units="days"))

depth <- cleandata[["DEPTH"]]
year <- as.numeric(strftime(datatime, format="%Y"))
month <- as.numeric(strftime(datatime, format="%m"))
day <- as.numeric(strftime(datatime, format="%d"))

df = data.frame(no.= numbers,longitude=long,latitude=lat,magnitude=magnitude,
                time=newtime,depth=depth,year=year,month=month,day=day)
write.csv(df,file=output_data_path)
