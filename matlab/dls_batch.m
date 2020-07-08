initCobraToolbox
load('models/section_A_ST1_cancerregion_model.mat')
cancer=PM;
load('models/section_A_ST1_ductepithelium_model.mat')
normal=PM;

cancer.genes=regexprep(cancer.genes, '\.[0-9]', '');
normal.genes=regexprep(normal.genes, '\.[0-9]', '');

grRatio_cancer = singleGeneDeletion(cancer);
grRatio_normal = singleGeneDeletion(normal);
diff_lethal_cancer=cancer.genes(grRatio_cancer<0.1 & grRatio_normal>0.9);
diff_lethal_normal=normal.genes(grRatio_cancer>0.9 & grRatio_normal<0.1);

% diff_lethal_cancer, aka those lethal in cancer but not in normal

class(diff_lethal_cancer)
diff_lethal_cancer{1,1}

% diff_lethal_normal, aka those lethal in normal but not in cancer

class(diff_lethal_normal)
diff_lethal_normal{1,1}
