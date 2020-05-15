# rm(list = ls())
library(ggplot2)
library(stringr)
setwd("~/_workspace/_wangspring2020project/GSE111672/ST/pancreatic-scripts/plotting")



files = c('GSM3036911_PDAC-A-ST1.tsv',
          'GSM4100721_PDAC-A-st2.tsv',
          'GSM4100722_PDAC-A-st3.tsv',
          'GSM3405534_PDAC-B-ST1.tsv',
          'GSM4100723_PDAC-B-st2.tsv', 
          'GSM4100724_PDAC-B-st3.tsv')

files = c('GSM3036911_PDAC-A-ST1.tsv')
# files = c('GSM3405534_PDAC-B-ST1.tsv')


for (file in files) {
  
  print(file)
  data <- read.table(file = str_c('data/', file), 
                     sep = '\t', 
                     header = TRUE,
                     check.names = FALSE)
  
  # 1st datasets both have flipped axes, for some reason
  if (file == 'GSM3036911_PDAC-A-ST1.tsv') {
    coords <- data[1]
    coords <- unlist(coords, use.names = FALSE)
  } else {
    coords <- colnames(data)
    coords <- coords[2:length(coords)]
  }
  
  
  
  xlist <- vector()
  ylist <- vector()

  for (coord in coords) {
    splitlist <- strsplit(coord, "x")
    xcoord <- splitlist[[1]][1]
    ycoord <- splitlist[[1]][2]
    
    xlist <- c(xlist, xcoord)
    ylist <- c(ylist, ycoord)
  }
  
  plotdata <- data.frame(xlist, ylist)
  plotdata$xlist = as.numeric(plotdata$xlist)
  plotdata$ylist = as.numeric(plotdata$ylist)
  # print(plotdata)
  
  print(ggplot(plotdata, aes(x = xlist, y = ylist)) + 
    # xlim(0, 50) +
    # ylim(0, 50) + 
    geom_point(shape=15) + 
    scale_x_continuous(breaks = round(seq(min(plotdata$x), max(plotdata$x), by = 1),1)) +
    scale_y_continuous(breaks = round(seq(min(plotdata$y), max(plotdata$y), by = 1),1)) +
    theme( axis.title.x=element_blank(),
           axis.title.y=element_blank())
    # + coord_fixed()
  )
  
  ggsave(paste("figures/", 
               str_replace(file, "tsv", "pdf")), 
         plot = last_plot())
  
}
