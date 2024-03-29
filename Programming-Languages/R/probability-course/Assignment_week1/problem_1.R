#A distributor has just received a shipment of 90 drain pipes from
#a major manufacturer of such pipes. The distribütör wishes to
#select a sample of size 5 to carefully inspect for defects. Describe
#a method for obtaining a simple random sample of 5 pipes from
#the shipment of 90 pipes. Use R to implement the method. Give
#the R commands and the sample you obtained.

#There are 90 drain pipes
drain_pipes <- seq(1,90)

#5 drain pipes are choosen for inspecting
selected_pipes <- sample(drain_pipes, size = 5)

cat("There are -", length(selected_pipes), "- drain pipes selected to inspect, and their numbers are:\n", selected_pipes)
