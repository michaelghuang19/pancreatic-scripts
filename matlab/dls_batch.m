initCobraToolbox

% load mCADRE-based 
load('models/section_A_ST1_cancerregion_model.mat')
cancer = PM;
load('models/section_A_ST1_ductepithelium_model.mat')
normal = PM;

cancer.genes = regexprep(cancer.genes, '\.[0-9]', '');
normal.genes = regexprep(normal.genes, '\.[0-9]', '');

grRatio_cancer = singleGeneDeletion(cancer);
grRatio_normal = singleGeneDeletion(normal);
diff_lethal_cancer = cancer.genes(grRatio_cancer<0.1 & grRatio_normal>0.9);
diff_lethal_normal = normal.genes(grRatio_cancer>0.9 & grRatio_normal<0.1);

% diff_lethal_cancer, aka those lethal in cancer but not in normal
% diff_lethal_normal, aka those lethal in normal but not in cancer

type = diff_lethal_cancer
type = diff_lethal_normal

for i = 1:length(type)
    candidate_gene = type(i,1)

%     find affected biomass components
    [temp, hasEffect, constrRxnNames, deletedGenes] = deleteModelGenes(cancer, candidate_gene);
    bio_comp = biomassPrecursorCheck(temp);
    
    file_cell = strcat('lethal_biocomp_', candidate_gene, '.txt');
%     fopen(file_cell{1}, 'w');
%     fprintf(file_cell{1}, '%s \n', bio_comp{:, 1});
%     fclose('all');
    writetable(table(bio_comp), file_cell{1})
    
%     find alternative path in ductal epithelium
    [temp, hasEffect, constrRxnNames, deletedGenes] = deleteModelGenes(normal, candidate_gene);
    temp = removeRxns(normal,constrRxnNames);
    
    grRatio_deleted = singleGeneDeletion(temp);
    alt_genes = intersect(normal.genes(grRatio_normal>0.9),temp.genes(grRatio_deleted<0.1));
    
    alt_cell = strcat('lethal_altgene_', candidate_gene, '.txt');
%     fopen(alt_cell{1}, 'w');
%     fprintf(alt_cell{1}, '%s \n', alt_genes{:, 1});
%     fclose('all');
    writetable(table(alt_genes), alt_cell{1})
end