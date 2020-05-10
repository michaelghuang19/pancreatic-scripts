rm(list = ls())

setwd("~/_workspace/_wangspring2020project/GSE111672/ST/tsv")

library('SPARK')

# Load data
# load("GSM4100721_PDAC-A-st2.tsv")

# gives us the dataframe rawcount
# data = load("./Layer2_BC_Count.rds")

A_ST2_data <- read.table(file = 'GSM4100721_PDAC-A-st2.tsv', sep = '\t', header = TRUE, check.names = FALSE)

rownames(A_ST2_data) <- A_ST2_data[, 1]

A_ST2_data <- A_ST2_data[, 2:ncol(A_ST2_data)]

# typeof(A_ST1_data)
## extract the coordinates from the rawdata

info <- cbind.data.frame(x=as.numeric(sapply(strsplit(colnames(A_ST2_data),split="x"),"[",1)),
                         y=as.numeric(sapply(strsplit(colnames(A_ST2_data),split="x"),"[",2))
# comment the next line out if don't want to add total counts
                                                  ,total_counts=apply(A_ST2_data,2,sum)
                         )

rownames(info) <- colnames(A_ST2_data)

## filter genes and cells/spots and 
A_ST2_spark <- CreateSPARKObject(counts=A_ST2_data, 
                           location=info[,1:2],
                           percentage = 0.1, 
                           min_total_counts = 10)

## total counts for each cell/spot
A_ST2_spark@lib_size <- apply(A_ST2_spark@counts, 2, sum)

## Take the first ten genes as an example
# A_ST2_spark@counts   <- A_ST2_spark@counts[1:10,]

## Estimating Parameter Under Null
A_ST2_spark <- spark.vc(A_ST2_spark, 
                  covariates = NULL, 
                  lib_size = A_ST2_spark@lib_size, 
                  num_core = 4,
                  verbose = T
                  # , fit.maxiter = 500
                  # , fit.tol = 1e-05
                  # , fit.model = "poisson"
                  )

final_spark <- spark.test(A_ST2_spark,
                    check_positive =  T,
                    verbose = T)

result = final_spark@res_mtest[,c("combined_pvalue","adjusted_pvalue")]

write.table(result, file = "A_ST2.csv", sep = ",", row.names = TRUE, col.names = TRUE)
