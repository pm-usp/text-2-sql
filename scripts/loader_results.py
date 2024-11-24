import pandas as pd

DATASET_PATH = '../data/dataset/text2sql4pm.tsv'

class LoaderResults(object):
    def __init__(self, *args, **kwargs):
        self.results = {}
        self.representation_path_EN = {
            'openai_shot0': '../results/english/openAI-representation_0-shot/evaluations/'
        }
        self.representation_path_PT = {
            'openai_shot0': '../results/portuguese/openAI-representation_0-shot/evaluations/'
        }

    def get_data_frame_results(self, path, model):
        tmp_df = pd.read_csv(path, sep='\t', header = None)
        tmp_df.columns = ['id_' + model, 'predicted_' + model, 'gold_' + model, 'hardness_' + model, 'score_' + model]
        return tmp_df

    def load_results(self, models_r: dict):
        for key, value in models_r.items():
            file_path = self.__dict__[f"representation_path_{value['lang']}"][value['representation']] + 'scores_' + key + '_'  + value['metric'] + ".tsv"
            tmp_df = self.get_data_frame_results(file_path, key)
            self.results[key] = tmp_df

    def concat_all_results(self):
        tmp_df = pd.DataFrame()
        for value in self.results.values():
            tmp_df = pd.concat([tmp_df, value], axis=1)
        return tmp_df

def load_dataset():
  dataset = pd.read_csv(DATASET_PATH, sep='\t')
  dataset = dataset.dropna(how='all')
  return dataset

def load_results(metric):
  dataset = load_dataset()
  
  # Load results
  results_en = LoaderResults()
  results_en.load_results({'opr_gpt35': {'lang': 'EN', 'representation': 'openai_shot0', 'metric': metric}})
  shot0_en = results_en.concat_all_results()
    
  results_pt = LoaderResults()
  results_pt.load_results({'opr_gpt35': {'lang': 'PT', 'representation': 'openai_shot0', 'metric': metric}})
  shot0_pt = results_pt.concat_all_results()
  return dataset, shot0_en, shot0_pt