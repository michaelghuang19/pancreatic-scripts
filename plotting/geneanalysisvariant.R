rm(list = ls())

setwd("~/_workspace/_wangspring2020project/GSE111672/ST/tsv")

library('SPARK')

# Form data loop

# files = c('GSM4100722_PDAC-A-st3.tsv', "GSM4100723_PDAC-B-st2.tsv", "GSM4100724_PDAC-B-st3.tsv", "GSM4100725_PDAC-D-st1.tsv", "GSM4100726_PDAC-E-st1.tsv", "GSM4100727_PDAC-F-st1.tsv", "GSM4100728_PDAC-G-st1.tsv")

files = c("GSM4100727_PDAC-F-st1.tsv")

for (filename in files) {
  
  filename = "GSM4100727_PDAC-F-st1.tsv"
  data <- read.table(file = filename, sep = '\t', header = TRUE, check.names = FALSE)
  
  rownames(data) <- data[, 1]
  
  data <- data[, 2:ncol(data)]
  
  ## extract the coordinates from the rawdata
  
  info <- cbind.data.frame(x=as.numeric(sapply(strsplit(colnames(data),split="x"),"[",1)),
                           y=as.numeric(sapply(strsplit(colnames(data),split="x"),"[",2))
                           # comment the next line out if don't want to add total counts
                           ,total_counts=apply(data,2,sum)
  )
  
  rownames(info) <- colnames(data)
  
  ## filter genes and cells/spots and 
  spark <- CreateSPARKObject(counts=data, 
                                   location=info[,1:2],
                                   percentage = 0.1, 
                                   min_total_counts = 10)
  
  ## total counts for each cell/spot
  spark@lib_size <- apply(spark@counts, 2, sum)
  
  ## Take the first ten genes as an example
  # spark@counts   <- spark@counts[1:10,]
  
  ## Estimating Parameter Under Null
  spark <- spark.vc(spark, 
                          covariates = NULL, 
                          lib_size = spark@lib_size, 
                          num_core = 4,
                          verbose = T
                          # , fit.maxiter = 500
                          # , fit.tol = 1e-05
                          # , fit.model = "poisson"
  )
  
  final_spark <- spark.test(spark,
                            check_positive =  T,
                            verbose = T)
  
  result = final_spark@res_mtest[,c("combined_pvalue","adjusted_pvalue")]
  
  write.table(result, file = paste(filename, ".csv"), sep = ",", row.names = TRUE, col.names = TRUE)
  
}
