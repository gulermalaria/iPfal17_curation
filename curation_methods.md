# Lipid metabolism curation

The curation (the process of improving the model by adding metabolites, reactions, genes or supplemental information such as enzymes EC numbers or citations) was based on the study which outlined over 300 lipids across over 20 classes [1]. The supplementary material delineates all detected lipid species with their corresponding chain lengths. The comprehensiveness of the dataset sheds the light on  the deficiency of the currently available GENREs (genome scale metabolic reconstructions). Even ones that are particularly focused on the metabolic network of lipids lack the detailed information found in the aforsaid study. Often the lipid classes are generalized and the GENREs do not account for the lipid species within the classes, e.g phosphatidylethanolamines are often represented as one metabolite `pe`. In more detailed GENREs the 1,2-diacyl-_sn_-glycero-3-phosphoethanolamines (e.g. `pe180` - 1,2-dioleoylphosphatidylethanolamine) are considered, but none (double check!) accounts for 1-acyl-2-acyl-_sn_-glycero-3-phosphoethanolamines (e.g. `11602180pe` - 1-palmitoyl-2-oleoyl phosphatidylethanolamine). Consequently, the process of curation was performed in the following manner (Fig. 1):

Each iteration of the curation started with addition of all detected lipid species within a class, e.g. 28 metabolites from phosphatidylethanolamines class including both 1,2-diacyl-_sn_-glycero-3-phosphoethanolamines and 1-acyl-2-acyl-_sn_-glycero-3-phosphoethanolamines. 
Subesquently, a set of reactions associated with the class was selected from MPMP database [2] through the metabolism maps and KEGG database exploration [3]. The reactions that could be added considering their reactants and products availability in the GENRE were introduced. Otherwise metabolites from another lipid class were included.  Lastly, a literature review was performed and the reaction that were proven not to be present in _P.falicparum_ were removed. 


![Curation workflow](/curation_workflow.png)
*Fig. 1 Lipid metabolism curation workflow*

### References
1. Gulati, S. et al. Profiling the Essential Nature of Lipid Metabolism in Asexual Blood and Gametocyte Stages of Plasmodium falciparum. Cell Host Microbe 18, 371–381 (2015)
2. Ginsburg, H. Progress in in silico functional genomics: the malaria Metabolic Pathways database. Trends in Parasitology 22, 238–240 (2006).
3. Kanehisa, M., Sato, Y., Kawashima, M., Furumichi, M. & Tanabe, M. KEGG as a reference resource for gene and protein annotation. Nucleic Acids Res 44, D457–D462 (2016).


