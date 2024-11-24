
import pandas as pd
from qualifiers import Qualifier1, Qualifier2, Qualifier3, Qualifier4, Qualifier5, Qualifier6, Qualifier7, Qualifier8, Qualifier9
from loader_results import load_results

def process_results_analyis(perspective: str, metric):
    # Load results
    dataset, shot0_en, shot0_pt = load_results(metric)
   
    if perspective == 'process_mining':
        results = get_results_pm(dataset, shot0_en, shot0_pt, metric)
        print('------------PROCESS_MINING QUALIFIERS-----------------------------------------------------------------\n')
        print_results(results['qualifier1'])
        print('------------------------------------------------------------------------------------------------------\n')
        print_results(results['qualifier2'])
        print('------------------------------------------------------------------------------------------------------\n')
        print_results(results['qualifier9'])
        print('------------------------------------------------------------------------------------------------------\n')

    elif perspective == 'sql':
        results = get_results_sql(dataset, shot0_en, shot0_pt, metric)
        print('------------SQL QUALIFIERS----------------------------------------------------------------------------\n')
        print_results(results['qualifier8'])
        print('------------------------------------------------------------------------------------------------------\n')
    
    elif perspective == 'nlp':
        results = get_results_nlp(dataset, shot0_en, shot0_pt, metric)
        print('------------NLP QUALIFIERS----------------------------------------------------------------------------\n')
        print_results(results['qualifier5'])
        print('------------------------------------------------------------------------------------------------------\n')

    else:
        print("Perspectiva não reconhecida")



def print_results(qualifier_result):
    rows = []
    keys = qualifier_result['EN'][2].index.tolist()
    en_data = qualifier_result['EN']
    pt_data = qualifier_result['PT']
    for key in keys:
        row = {
            '': key,
            'Portuguese_base': format_output(pt_data[1].get(key, 0), pt_data[0].get(key, 0)),
            'Portuguese_paraphrase': format_output(pt_data[3].get(key, 0), pt_data[2].get(key, 0)),
            'English_base': format_output(en_data[1].get(key, 0), en_data[0].get(key, 0)),
            'English_paraphrase': format_output(en_data[3].get(key, 0), en_data[2].get(key, 0))
        }
        rows.append(row)
        
    # Convert rows into a DataFrame for better formatting
    df = pd.DataFrame(rows)

    # Print the DataFrame
    print(df.to_string(index=False))

def format_output(value, total):
    percentage = 0 if total == 0 else (value / total) * 100
    return f"{percentage:.1f}% ({value}/{total})"


def get_results_pm(dataset, shot0_en, shot0_pt, metric):
    tmp_dataset = dataset[['Group_id', 'Utterance_id', 'Base_paraphrase', 'Domain_value_generic', 'Events_cases_classification', 'Purpose_classification']]
    tmp_dataset = tmp_dataset.reset_index(drop=True)

    ds_en = pd.concat([tmp_dataset, shot0_en], axis=1)
    qualifier1_en = Qualifier1(ds_en)
    qualifier2_en = Qualifier2(ds_en)
    qualifier9_en = Qualifier9(ds_en)

    ds_pt = pd.concat([tmp_dataset, shot0_pt], axis=1)
    qualifier1_pt = Qualifier1(ds_pt)
    qualifier2_pt = Qualifier2(ds_pt)
    qualifier9_pt = Qualifier9(ds_pt)

    method_name = f"get_results_{'em' if metric == 'EM' else 'ex'}"

    results = {
        'qualifier1': { 'EN': getattr(qualifier1_en, method_name)('Events_cases_classification'), 'PT': getattr(qualifier1_pt, method_name)('Events_cases_classification')},
        'qualifier2': { 'EN': getattr(qualifier2_en, method_name)('Purpose_classification_class'), 'PT': getattr(qualifier2_pt, method_name)('Purpose_classification_class')},
        'qualifier9': { 'EN': getattr(qualifier9_en, method_name)('Domain_value_generic'), 'PT': getattr(qualifier9_pt, method_name)('Domain_value_generic')}
    }
    return results

def get_results_nlp(dataset, shot0_en, shot0_pt, metric):
    tmp_dataset = dataset[['Group_id', 'Utterance_id', 'Base_paraphrase', 'Wh_classification']]
    tmp_dataset = tmp_dataset.reset_index(drop=True)

    ds_en = pd.concat([tmp_dataset, shot0_en], axis=1)
    qualifier5_en = Qualifier5(ds_en)

    ds_pt = pd.concat([tmp_dataset, shot0_pt], axis=1)
    qualifier5_pt = Qualifier5(ds_pt)

    method_name = f"get_results_{'em' if metric == 'EM' else 'ex'}"
    results = {
        'qualifier5': { 'EN': getattr(qualifier5_en, method_name)('Wh_classification'), 'PT': getattr(qualifier5_pt, method_name)('Wh_classification')}
    }
    return results

def get_results_sql(dataset, shot0_en, shot0_pt, metric):
    tmp_dataset = dataset[['Group_id', 'Utterance_id', 'Base_paraphrase', 'Spider_classification']]
    tmp_dataset = tmp_dataset.reset_index(drop=True)

    ds_en = pd.concat([tmp_dataset, shot0_en], axis=1)
    qualifier8_en = Qualifier8(ds_en)

    ds_pt = pd.concat([tmp_dataset, shot0_pt], axis=1)
    qualifier8_pt = Qualifier8(ds_pt)

    method_name = f"get_results_{'em' if metric == 'EM' else 'ex'}"    
    results = {
        'qualifier8': { 'EN': getattr(qualifier8_en, method_name)('hardness_opr_gpt35'), 'PT': getattr(qualifier8_pt, method_name)('hardness_opr_gpt35')}
    }
    return results


