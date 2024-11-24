# Text-to-SQL Oriented to the Process Mining Domain: A PT-EN Dataset for Query Translation

This repository contains resources and instructions necessary for reproduciability. Descriptions of each resorce used are detailed and steps used for experiments are presented.

## Resource
- dataset:
  - text2sql4pm.tsv: the dataset created in tsv format. Each line contains a unique identifier, a group identifier, the English utterance, Portuguese utterance, gold SQL statement with English values, gold SQL statement with Portuguese values and each qualifier presented on paper.
- scripts: the scripts used to collect dataset statistics and graphs. Also contains scripts used to analyse the results on process mining perspective, nlp perspective and sql perspective.
  - main.py: start point for each type of exection (dataset_statistics, result_analysis and results_grouped_by_utterance).
  - loader_results.py: class and functions to load the dataset and the results file.
  - qualifiers.py: classes with specifities for each qualifier, utilities to segregate the utterances (base and paraphrase), utilities to calculate counts and percentages and utilities to process results for structure indicator (EM) and run indicator (EX).
  - graphs.py: functions used to generate the graphs presented on paper.
  - dataset_analysis.py: functions used to collect the dataset statistics and generate the graphs for each perspective (process_mining, nlp, sql).
  - results_analysis.py: functions to process the evaluations results obtained from GPT-3.5 Turbo model execution. The results were obtained adapting the scripts provided on [https://github.com/taoyds/test-suite-sql-eval] which the adapted version are provided on [https://github.com/brunoyui/test-suite-sql-eval].
  - results_grouped_by_utterance.py: functions used to generate the graphs grouped by utterance putting together both metrics, the structure and run indicators.
  - run_statistics.sh: shell script to execute all dataset statistics.
  - run_results.sh: shell script to process all results obtained (Portuguese and English).
  - run_grouped_by_utterance.sh: shell script to generate the graphs grouped by utterance.
- images: contains graphs images of dataset statistics and graphs of result analysis.
- results: contains the SQL statements generated by the GPT-3.5 Turbo model for both languages, English and Portuguese. Also contains the results of evaluations for strutcture indicator metric (EM) and run indicator metric (EX).
  - english/openAI-representation_0-shot:
    - RESULTS_MODEL-gpt3.5-turbo.txt: SQL statements (English) generated by the GPT-3.5 Turbo model using openAI representation with 0-shot strategy.
    - evaluations:
      - scores_opr_gpt35_EM: results of evaluation using structure indicator of SQL statements generated by GPT-3.5 Turbo model
      - scores_opr_gpt35_EX: results of evaluation using run indicator of SQL statements generated by GPT-3.5 Turbo model
  - portuguese/openAI-representation_0-shot:
    - RESULTS_MODEL-gpt3.5-turbo.txt: SQL statements (Portuguese) generated by the GPT-3.5 Turbo model using openAI representation with 0-shot strategy.
    - evaluations:
      - scores_opr_gpt35_EM: results of evaluation using structure indicator of SQL statements generated by GPT-3.5 Turbo model
      - scores_opr_gpt35_EX: results of evaluation using run indicator of SQL statements generated by GPT-3.5 Turbo model
