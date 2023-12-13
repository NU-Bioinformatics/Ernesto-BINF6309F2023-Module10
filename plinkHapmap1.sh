#!/usr/bin/env bash
#plinkHapmap1.sh 

echo "Making a binary PED file at default filter settings"
plink --file hapmap1 --make-bed --out hapmap1
echo "Summary statistics: missing rates"
plink --bfile hapmap1 --missing --out miss_stat
echo "Summary statistics: allele frequencies (without stratification)"
plink --bfile hapmap1 --freq --out freq_stat
echo "Summary statistics: allele frequencies (stratified by pop.phe data)"
plink --bfile hapmap1 --freq --within pop.phe --out freq_stat
echo "Basic association analysis"
plink --bfile hapmap1 --assoc --adjust --out as2
echo "Genotypic and other association models"
plink --bfile hapmap1 --model --cell 0 --out mod2
echo "Stratification analysis"
plink --bfile hapmap1 --cluster --mc 2 --ppc 0.05 --out str1
echo "Association analysis, accounting for clusters"
plink --bfile hapmap1 --cluster --cc --ppc 0.01 --out version2
plink --bfile hapmap1 --mh --within version2.cluster2 --adjust --out aac2
echo "Quantitative trait association analysis"
plink --bfile hapmap1 --assoc --pheno qt.phe --perm --within str1.cluster2 --out quant2
echo "Extracting a SNP of interest"
plink --bfile hapmap1 --snp rs2222162 --recodeAD --out rec_snp1
