# todo - Aanchal
def get_question_from_statement(statement):
    """
    Returns a question in natural language, based on a Statement

    :param statement: a Statement, comprising a predicate (isLegendary)
             and 0 or 1 terms (Red, for the predicate isColor)
    :return: a string, the natural language question
    """
    feature, value = get_feature_and_value_from_statement(statement)
    if feature == 'isColor':
        return f'Is the Pokemon {value} in color?'
    if feature == 'isLegendary':
        return f'Is it a legendary Pokemon?'
    if feature == 'canEvolve':
        return f'Can the Pokemon evolve into another Pokemon?'
    if feature == 'isPrimaryColor':
        return f'Is the main color of the Pokemon a primary color?'
    if feature == 'isType':
        return f'Is it a/an {value} type Pokemon?'


def get_feature_and_value_from_statement(statement):
    feature = statement.predicate
    if len(statement.terms) == 0:
        value = None
    else:
        value = statement.terms[0]
    return feature, value
