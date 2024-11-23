import pandas as pd
from loader_results import load_results
from graphs import plot_metric_groupped


def process_results_grouped_by_utterance():
  # Load results
  dataset_em, shot0_en_em, shot0_pt_em = load_results('EM')
  dataset_ex, shot0_en_ex, shot0_pt_ex = load_results('EX')
  shot0_en_ex.columns =  ['id_opr_gpt35_ex', 'predicted_opr_gpt35_ex', 'gold_opr_gpt35_ex', 'hardness_opr_gpt35_ex', 'score_opr_gpt35_ex']
  shot0_pt_ex.columns =  ['id_opr_gpt35_ex', 'predicted_opr_gpt35_ex', 'gold_opr_gpt35_ex', 'hardness_opr_gpt35_ex', 'score_opr_gpt35_ex']

  utterance_group = dataset_ex[['Group_id', 'Utterance_id']]
  utterance_group = utterance_group.reset_index(drop=True)
  
  shot0_en = pd.concat([utterance_group, shot0_en_em, shot0_en_ex[['score_opr_gpt35_ex']]], axis=1)
  shot0_pt = pd.concat([utterance_group, shot0_pt_em, shot0_pt_ex[['score_opr_gpt35_ex']]], axis=1)

  shot0_en = shot0_en.sort_values(by=['hardness_opr_gpt35', 'Group_id'],
                    key=lambda x: pd.Categorical(x, categories=['easy', 'medium', 'hard', 'extra', 'no_hardness']))
  shot0_pt = shot0_pt.sort_values(by=['hardness_opr_gpt35', 'Group_id'],
                    key=lambda x: pd.Categorical(x, categories=['easy', 'medium', 'hard', 'extra', 'no_hardness']))

  total_by_group = shot0_en.groupby(["Group_id", "hardness_opr_gpt35"], as_index=False, sort=False)["Utterance_id"].count()
  total_em_by_group = count_true_values(shot0_en, 'score_opr_gpt35 == "True"')
  total_ex_by_group = count_true_values(shot0_en, 'score_opr_gpt35_ex == 1')

  total_by_group_pt = shot0_pt.groupby(["Group_id", "hardness_opr_gpt35"], as_index=False, sort=False)["Utterance_id"].count()
  total_em_by_group_pt = count_true_values(shot0_pt, 'score_opr_gpt35 == "True"') 
  total_ex_by_group_pt = count_true_values(shot0_pt, 'score_opr_gpt35_ex == 1')

  total_group = pd.concat([total_by_group, total_em_by_group['count'], total_ex_by_group['count']], axis=1)
  total_group.columns = ['Group_id', 'hardness', 'total', 'EM', 'EX']

  total_group_pt = pd.concat([total_by_group_pt, total_em_by_group_pt['count'], total_ex_by_group_pt['count']], axis=1)
  total_group_pt.columns = ['Group_id', 'hardness', 'total', 'EM', 'EX']

  plot_metric_groupped(total_group_pt, total_group, '../images/hardness_success_by_utterance.png')



def count_true_values(df, filter):
  true_count_by_group = df.query(filter).groupby("Group_id")["Utterance_id"].count()

  # Get a list of unique 'Group_id' values
  group_ids = df["Group_id"].unique()

  # Create a dictionary to store the counts
  counts = {}

  # Iterate over the unique 'Group_id' values
  for group_id in group_ids:
    # If the 'Group_id' is in the 'true_count_by_group' index, get the count
    if group_id in true_count_by_group.index:
      counts[group_id] = true_count_by_group[group_id]
    # Otherwise, set the count to 0
    else:
      counts[group_id] = 0
  counts_df = pd.DataFrame.from_dict(counts, orient='index', columns=['count'])

  # Reset the index to make 'Group_id' a regular column
  counts_df = counts_df.reset_index()
  return counts_df