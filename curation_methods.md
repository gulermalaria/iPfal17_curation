# Lipid metabolism curation

The curation (the process of improving the model by adding metabolites, reactions, genes or supplemental information such as enzymes EC numbers or citations) was based on the study which outlined over 300 lipids across over 20 classes [1]. The supplementary material delineates all detected lipid species with their corresponding chain lengths. The comprehensiveness of the dataset sheds the light on  the deficiency of the currently available GENREs (genome scale metabolic reconstructions). Even ones that are particularly focused on the metabolic network of lipids lack the detailed information found in the aforsaid study. Often the lipid classes are generalized and the GENREs do not account for the lipid species within the classes, e.g phosphatidylethanolamines are often represented as one metabolite `pe`. In more detailed GENREs the 1,2-diacyl-_sn_-glycero-3-phosphoethanolamines (e.g. `pe180` - 1,2-dioleoylphosphatidylethanolamine) are considered, but none (double check!) accounts for 1-acyl-2-acyl-_sn_-glycero-3-phosphoethanolamines (e.g. `11602180pe` - 1-palmitoyl-2-oleoyl phosphatidylethanolamine). Consequently, the process of curation was performed in the following manner (Fig. 1):

Each iteration of the curation started with addition of all detected lipid species from one class. 
Subesquently, a set of reactions associated with the class was selected from MPMP database. The reactions that were possible to be added concerning the available reactants were added. Lastly, ones that according to the literature are not present in _P.falicparum_ were removed


![Curation workflow](/curation_workflow.png)
*Fig. 1 Lipid metabolism curation workflow*

### References
1. Gulati, S. et al. Profiling the Essential Nature of Lipid Metabolism in Asexual Blood and Gametocyte Stages of Plasmodium falciparum. Cell Host Microbe 18, 371–381 (2015)
