from dataset_analysis import execute_analysis
import pandas as pd
from results_analysis import process_results_analyis
from results_grouped_by_utterance import process_results_grouped_by_utterance

#import argparse

if __name__ == "__main__":
    #parser = argparse.ArgumentParser()
    #parser.add_argument("--sql_complexity", type=str)
    #parser.add_argument("--metric", type=str)
    #parser.add_argument("--lang", type=str)
    #parser.add_argument("--file", type=str)
#
    #args = parser.parse_args()
#
    #if args.metric == "EX":
    #    metric_label = 'Execution Acc. (%)'
    #else:
    #    metric_label = 'Exact Match Acc. (%)'
    #dataset = pd.read_csv('../dataset/text2sql4pm.tsv', sep='\t')
    #dataset = dataset.dropna(how='all')
    #execute_analysis('sql', dataset)
    #process_results_analyis('process_mining', 'EX')
    process_results_grouped_by_utterance()