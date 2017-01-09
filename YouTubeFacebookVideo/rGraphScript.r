library(readr)
dataset <- read_csv("YouTube_FB_2800.csv")
library(ggplot2)
g <- ggplot(data = dataset, aes(x = Video_Title))+geom_histogram(mapping = NULL, data = NULL, stat = "count", position = "stack", binwidth = 10, bins = NULL, na.rm = FALSE, show.legend = NA, inherit.aes = TRUE)
print(g)
