# Text-to-SQL Oriented to the Process Mining Domain: A PT-EN Dataset for Query Translation

This repository contains instructions used on experiments and resources necessary for reproduciability. Descriptions of each resorce used are detailed and steps used for experiments are presented.

## Resource
- dataset:
  - text2sql4pm.tsv: contains the dataset created in tsv format. Each line contains a unique identifier, a group identifier, the English utterance, Portuguese utterance, gold SQL statement with English values, gold SQL statement with Portuguese values and each qualifier presented on paper.
- scripts: contains the scripts used to collect dataset statistics and graphs. Also contains scripts used to analyse the results on process mining perspective, nlp perspective and sql perspective.
  - main.py: start point for each type of exection (dataset_statistics, result_analysis and results_grouped_by_utterance).
  - loader_results.py: contains class and functions to load the dataset and the results file.
  - qualifiers.py: contains class with specifities for each qualifier, utilities to segregate the utterances (base and paraphrase), utilities to calculate counts and percentages and utilities to process results for structure indicator (EM) and run indicator (EX).
  - graphs.py: contains functions used to generate the graphs presented on paper.
  - dataset_analysis.py: contains the functions used to collect the dataset statistics and generate the graphs for each perspective (process_mining, nlp, sql).
  - results_analysis.py: contains the functions to process the evaluations results obtained from GPT-3.5 Turbo model. The results were obtained adapting the scripts provided on [https://github.com/taoyds/test-suite-sql-eval] which the adapted version are provided on [https://github.com/brunoyui/test-suite-sql-eval].
  - results_grouped_by_utterance.py: contains the functions used to generate the graphs grouped by utterance putting together both metrics, the structure and run indicators.
  - run_statistics.sh: shell script to execute all dataset statistics.
  - run_results.sh: shell script to process all results obtained (Portuguese and English).
  - run_grouped_by_utterance.sh: shell script to generate the graphs grouped by utterance.
