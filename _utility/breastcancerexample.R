rm(list = ls())

setwd("~/_workspace/_wangspring2020project/_scripts/SPARK")

library('SPARK')
load("./data/Layer2_BC_Count.rds")

## extract the coordinates from the rawdata
exampleinfo <- cbind.data.frame(x=as.numeric(sapply(strsplit(colnames(rawcount),split="x"),"[",1)),
                         y=as.numeric(sapply(strsplit(colnames(rawcount),split="x"),"[",2)),
                         total_counts=apply(rawcount,2,sum))
rownames(exampleinfo) <- colnames(rawcount)

## filter genes and cells/spots and 
spark <- CreateSPARKObject(counts=rawcount, 
                           location=exampleinfo[,1:2],
                           percentage = 0.1, 
                           min_total_counts = 10)

## total counts for each cell/spot
spark@lib_size <- apply(spark@counts, 2, sum)

## Take the first ten genes as an example
spark@counts   <- spark@counts[1:10,]

## Estimating Parameter Under Null
spark <- spark.vc(spark, 
                  covariates = NULL, 
                  lib_size = spark@lib_size, 
                  num_core = 4,
                  verbose = T,
                  fit.model = "poisson")

## Calculating pval
spark <- spark.test(spark, 
                    check_positive = T, 
                    verbose = F)

head(spark@res_mtest[,c("combined_pvalue","adjusted_pvalue")])
