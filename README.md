# iPfal17_curation
This repository holds the iPfal17 genome-scale metabolic reconstruction with curated lipid metabolism and scripts that perform the curation and facilitate the model exploration.
Additionally, there is a Python 3.5 virtual environment setup.

Usage of ``` curation_script_cmd.py ```: 

```python curation_script_cmd.py -m data/plata_sbml_up_model.xml -d data/reaction_delete_edits_final.csv -e data/edits_additions_or_modifications_final.csv data/biomass_edits_final.csv```

Usage of ``` rxns_browser.py ```:

```python rxns_browser.py -m <metabolite name> -mdl <model name>```

for example:

```python rxns_browser.py -m sphmyln160_c -mdl output/curated_model_2018_01_15_13\:13\:43.xml```
