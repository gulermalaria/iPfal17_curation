# iPfal17_curation
This repository holds the iPfal17 genome-scale metabolic reconstruction with curated lipid metabolism and scripts that perform the curation and facilitate the model exploration.
Additionally, there is a Python 3.5 virtual environment setup.

### Main curation script

Usage of ``` curation_script_cmd.py ```: 

```python curation_script_cmd.py -m data/model_changed_names.xml -d data/delete_reactions.csv -e data/add_reactions.csv data/edit_biomass.csv```

### Auxiliary scripts

Usage of ``` rxns_browser.py ```:

```python rxns_browser.py -m <metabolite name> -mdl <model name>```

for example:

```python rxns_browser.py -m sphmyln160_c -mdl output/curated_model_2018_01_15_13\:13\:43.xml```

Due to metabolite names adjustments which emerged during the lipid metabolism curation the correction of metabolites names in that already exist in the model is necessary, i.e running the line below:

```python change_met_names_model.py -mdl data/plata_sbml_up_model.xml```

In order to ascertain the correctness of the reactions' reversibility in the file with reactions to be added to the model run the line below:

``` python fix_reversibility.py -f data/edits_additions_or_modifications_final_corrected.csv ```

In order to check reaction's stoichiometric balance run:

``` python balance_checker.py -r <reaction> -mdl <model>```

for example:

``` python balance_checker.py -r DGAT116121603181 -mdl output/curated_model_2018_01_15_13\:13\:43.xml ```

### Model performance assessment 

Matlab script inspired by work published in https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-017-3905-1, for more details see: https://github.com/gulermalaria/iPfal17

``` metabolic_tasks.m ```
