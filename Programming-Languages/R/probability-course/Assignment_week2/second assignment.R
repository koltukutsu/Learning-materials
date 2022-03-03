
# 1.14 A tire manufacturer wants to determine the inner
#diameter of a certain grade of tire. Ideally, the diameter would
#be 570mm. The data are as folows:
#572, 572, 573,568,569,575,565,570
#a- find the sample mean and median
#b- Find the sample variance, standard deviation and range
#c- Using the calculated statistics in parts a and b, can
# you comment of the quality of the tires?


the_samples_of_tire = c(572, 572, 573,568,569,575,565,570)
###A PART
## sample mean
s_mean <- mean(the_samples_of_tire)
## sample median
s_median <- median(the_samples_of_tire)

###B PART

##sample variance
s_variance <- var(the_samples_of_tire)
##sample standard deviation
s_sd <- sd(the_samples_of_tire)
##sample range
s_range <- range(the_samples_of_tire)
  
### C PART
cat('By looking the values which are based on the diaeter of the tires shown below the line, could you comment about the tire quality\nNote: Theorically the diameter must be 570','The mean \n',s_mean,'The median\n',s_median,'The variance \n',s_variance,'The standard daviation\n',s_sd,'The range\n',s_range)
comment_mine <- 'my comment' ##buraya bir comment ekle
cat('You commented that: \n',comment_mine)  

#1.17 A study of the effects of the smoking on sleep patterns
#is conducted. The measure observed is the time, in minutes,
# that it takes to fall asleep. These data are obtained:
# smokers : 69.3 ,56.0 ,22.1 ,47.6 ,53.2 ,48.1 ,52.7 ,34.4 ,60.2 ,43.8 ,23.2 ,13.8 ,
# nonsmokers :28.6 ,25.1 ,26.4 ,34.9 ,29.8 ,28.4 ,38.5 ,30.2 ,30.6 ,31.8 ,41.6 ,21.1 ,36.0 ,37.9 ,13.9
# a- find the sample mean for each group
# b - find the sample standard deviation for each group 
# c- make a dot plot of the data sets A and B on the same line
# d- comment on what kind of impact smoking appears to have on the time
#required to fall asleep
smokers <- c(69.3 ,56.0 ,22.1 ,47.6 ,53.2 ,48.1 ,52.7 ,34.4 ,60.2 ,43.8 ,23.2 ,13.8)
nonsmokers <- c(28.6 ,25.1 ,26.4 ,34.9 ,29.8 ,28.4 ,38.5 ,30.2 ,30.6 ,31.8 ,41.6 ,21.1,36.0 ,37.9 ,13.9)
##A PART
s_mean_smokers <- mean(smokers)
length(smokers)
length(nonsmokers)
s_mean_nonsmokers <- mean(nonsmokers)
##B PART
s_sd_smokers <- sd(smokers)
s_sd_nonsmokers <- sd(nonsmokers)
##C PART
smokers <- c(smokers,c(0,0,0))
plotted_1 <- data.frame(smokers,nonsmokers)
plot(smokers)
plot(nonsmokers)
#long <- seq(1,length(smokers))
#viz <- ggplot(plotted_1, aes(x = long, y = smokers, color = nonsmokers)) + geom_point()
#viz
##D PART
cat('mean smokers\n',s_mean_smokers,'\nmean nonsmokers \n',s_mean_nonsmokers,'\nsd smokers\n',s_sd_smokers,'\nsd nonsomkers\n',s_sd_nonsmokers)
comment_on_sleep <- 'by comparing the smokers with nonsmokers, in fact we can conclude that these smokers are ,eviently, more inclined to sleep later'

#1.20
#The following data represent the length of life, in seconds,
#of 50 fruit flies subject to a new spray in a controlled laboratory experiment:
#17 ,20 ,10 ,9 ,23 ,13 ,12 ,19 ,18 ,24 ,12 ,14 ,6 ,9 ,13 ,6 ,7 ,10 ,13 ,7 ,16 ,18 ,8 ,13 ,3 ,32 ,9 ,7 ,11 ,13 ,7 ,18 ,7 ,10 ,4 ,27 ,19 ,16 ,8 ,7 ,10 ,5 ,14 ,15 ,10 ,9 ,6 ,7 ,15
# a- construct a double-stem-and-leaf plot for the life span of the fruit flies
#using the stems 0*,0.,1*,1.,2*,2., ad 3* such that stems coded by the symbols
#* and . are associated, respectively, with leaves 0 through
#4 and 4 through 9.
#b- set up a relative frequency distribution
#c- construct a relative frequency distribution
#d-find the median

f_flies = c(17 ,20 ,10 ,9 ,23 ,13 ,12 ,19 ,18 ,24 ,12 ,14 ,6 ,9 ,13 ,6 ,7 ,10 ,13 ,7 ,16 ,18 ,8 ,13 ,3 ,32 ,9 ,7 ,11 ,13 ,7 ,18 ,7 ,10 ,4 ,27 ,19 ,16 ,8 ,7 ,10 ,5 ,14 ,15 ,10 ,9 ,6 ,7 ,15) 
##a
stem(f_flies, scale = 1)
##b
set_up <- prop.table(table(f_flies))

##c
constructed_frequency <- plot(table(f_flies))
constructed_frequency 
##d median
flies_median <- median(f_flies)

#1.30
#Below are the lifetimes, in hours, of fifty 40-watt,
#110-volt internally frosted incandescent lamps, taken form forced life tets:
#919 ,1196 ,785 ,1126 ,936 ,918 ,1156 ,920 ,948 ,1067 ,1092 ,1162 ,1170 ,929 ,950 ,905 ,972 ,1035 ,1045 ,855 ,1195 ,1195 ,1340 ,1122 ,938 ,970 ,1237 ,956 ,1102 ,1157 ,978 ,832 ,1009 ,1157 ,1151 ,1009 ,765 ,958 ,902 ,1022 ,1333 ,811 ,1217 ,1085 ,896 ,958 ,1311 ,1037 ,702 ,923
#Construct a box plot for these data
lamp_lives <- c(919 ,1196 ,785 ,1126 ,936 ,918 ,1156 ,920 ,948 ,1067 ,1092 ,1162 ,1170 ,929 ,950 ,905 ,972 ,1035 ,1045 ,855 ,1195 ,1195 ,1340 ,1122 ,938 ,970 ,1237 ,956 ,1102 ,1157 ,978 ,832 ,1009 ,1157 ,1151 ,1009 ,765 ,958 ,902 ,1022 ,1333 ,811 ,1217 ,1085 ,896 ,958 ,1311 ,1037 ,702 ,923)
##box plot
b_plot <- boxplot(lamp_lives)
