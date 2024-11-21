from qualifiers import Qualifier1, Qualifier2, Qualifier3, Qualifier4, Qualifier5, Qualifier6, Qualifier7, Qualifier8, Qualifier9
from graphs import plot_graphs_pm, plot_graphs_nlp, plot_graphs_sql

def execute_analysis(perspective: str, dataset):
    if perspective == 'process_mining':
        stats = get_statistics_pm(dataset)
        print_statistics('Qualifier 1 - Case and Event Level', stats['qualifier1'], [0, 2, 4])
        print_statistics('Qualifier 2 - Purpose Level', stats['qualifier2'], [0, 2, 4])
        print_statistics('Qualifier 9 - Domain value generic Level', stats['qualifier9'], [0, 2, 4])
        print_statistics('Qualifier 3 - Projection Level', stats['qualifier3'], [0, 2, 4])
        print_statistics('Qualifier 4 - Condition Level', stats['qualifier4'], [0, 2, 4])
        plot_graphs_pm(stats, '../images/process_mining_qualifiers.png')

    elif perspective == 'sql':
        stats = get_statistics_sql(dataset)
        print_statistics('Qualifier 6 - Projection aggregation', stats['qualifier6'], [0, 2, 4])
        print_statistics('Qualifier 7 - Condition group', stats['qualifier7'], [0, 2, 4])
        print_statistics('Qualifier 8 - SQL Complexity', stats['qualifier8'], [0, 2, 4])
        plot_graphs_sql(stats, '../images/sql_qualifiers.png')

    elif perspective == 'nlp':
        stats = get_statistics_nlp(dataset)
        print_statistics('Qualifier 5 - Wh Questions', stats['qualifier5'], [0, 2, 4])
        plot_graphs_nlp(stats, '../images/question_type_qualifier.png', '../images/question_type_qualifier.png')
    else:
        print("Perspectiva não reconhecida")

def get_statistics_pm(dataset):
    qualifier1 = Qualifier1(dataset)
    qualifier2 = Qualifier2(dataset)
    qualifier3 = Qualifier3(dataset)
    qualifier4 = Qualifier4(dataset)
    qualifier9 = Qualifier9(dataset)

    stats = {
        'qualifier1': qualifier1.get_counts_percentages('Events_cases_classification'),
        'qualifier2': qualifier2.get_counts_percentages('Purpose_classification_class'),
        'qualifier3': qualifier3.get_counts_percentages('Projection_classification'),
        'qualifier4': qualifier4.get_counts_percentages('Condition_classification'),
        'qualifier9': qualifier9.get_counts_percentages('Domain_value_generic'),
    }
    return stats

def get_statistics_nlp(dataset):
    qualifier5 = Qualifier5(dataset)
    stats = {
        'qualifier5': qualifier5.get_counts_percentages('Wh_classification')
    }
    return stats

def get_statistics_sql(dataset):
    qualifier6 = Qualifier6(dataset)
    qualifier7 = Qualifier7(dataset)
    qualifier8 = Qualifier8(dataset)
    stats = {
        'qualifier6': qualifier6.get_counts_percentages('Projection_aggregation'),
        'qualifier7': qualifier7.get_counts_percentages('Condition_group_classification'),
        'qualifier8': qualifier8.get_counts_percentages('Spider_classification')
    }
    return stats
    

def print_statistics(description, qualifier, indices):
    print(description)
    for index in indices:
        for key, value in qualifier[index].items():
            print(f'{key}: {value}')
        print(f'----------------')
