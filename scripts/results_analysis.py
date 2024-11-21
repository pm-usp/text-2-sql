
import pandas as pd
from qualifiers import Qualifier1, Qualifier2, Qualifier3, Qualifier4, Qualifier5, Qualifier6, Qualifier7, Qualifier8, Qualifier9
from loader_results import LoaderResults

DATASET_PATH = '../dataset/text2sql4pm.tsv'

def process_results_analyis(perspective: str, lang):
    dataset = pd.read_csv(DATASET_PATH, sep='\t')
    dataset = dataset.dropna(how='all')

    # Load results
    results_ex = LoaderResults()
    results_ex.load_results({'opr_gpt35': {'lang': lang, 'representation': 'openai_shot0', 'metric': 'EX'}})
    shot0_ex = results_ex.concat_all_results()
    shot0_ex.columns = ['id_opr_gpt35_ex', 'predicted_opr_gpt35_ex', 'gold_opr_gpt35_ex', 'score_opr_gpt35_ex', 'hardness_opr_gpt35_ex']

    results_em = LoaderResults()
    results_em.load_results({'opr_gpt35': {'lang': lang, 'representation': 'openai_shot0', 'metric': 'EM'}})
    shot0_em = results_em.concat_all_results()

    if perspective == 'process_mining':
        results = get_results_pm(dataset, shot0_em, shot0_ex)

    elif perspective == 'sql':
        results = get_results_sql(dataset, shot0_em, shot0_ex)
    
    elif perspective == 'nlp':
        results = get_results_nlp(dataset, shot0_em, shot0_ex)
    else:
        print("Perspectiva não reconhecida")
    print(results)
#
def get_results_pm(dataset, shot0_em, shot0_ex):
    tmp_dataset = dataset[['Group_id', 'Utterance_id', 'Base_paraphrase', 'Domain_value_generic', 'Events_cases_classification', 'Purpose_classification']]
    tmp_dataset = tmp_dataset.reset_index(drop=True)

    ds = pd.concat([tmp_dataset, shot0_em, shot0_ex[['score_opr_gpt35_ex']]], axis=1)
    qualifier1 = Qualifier1(ds)
    qualifier2 = Qualifier2(ds)
    qualifier9 = Qualifier9(ds)

    results = {
        'qualifier1': { 'EM': qualifier1.get_results_em('Events_cases_classification'), 'EX': qualifier1.get_results_ex('Events_cases_classification')},
        'qualifier2': { 'EM': qualifier2.get_results_em('Purpose_classification_class'), 'EX': qualifier2.get_results_ex('Purpose_classification_class')},
        'qualifier9': { 'EM': qualifier9.get_results_em('Domain_value_generic'), 'EX': qualifier9.get_results_ex('Domain_value_generic')}
    }
    return results

def get_results_nlp(dataset, shot0_em, shot0_ex):
    tmp_dataset = dataset[['Group_id', 'Utterance_id', 'Base_paraphrase', 'Wh_classification']]
    tmp_dataset = tmp_dataset.reset_index(drop=True)

    ds = pd.concat([tmp_dataset, shot0_em, shot0_ex[['score_opr_gpt35_ex']]], axis=1)
    qualifier5 = Qualifier5(ds)

    results = {
        'qualifier5': { 'EM': qualifier5.get_results_em('Wh_classification'), 'EX': qualifier5.get_results_ex('Wh_classification')}
    }
    return results

def get_results_sql(dataset, shot0_em, shot0_ex):
    tmp_dataset = dataset[['Group_id', 'Utterance_id', 'Base_paraphrase', 'Spider_classification']]
    tmp_dataset = tmp_dataset.reset_index(drop=True)

    ds = pd.concat([tmp_dataset, shot0_em, shot0_ex[['score_opr_gpt35_ex']]], axis=1)
    qualifier8 = Qualifier8(ds)
    
    results = {
        'qualifier8': { 'EM': qualifier8.get_results_em('hardness_opr_gpt35'), 'EX': qualifier8.get_results_ex('hardness_opr_gpt35')}
    }
    return results


