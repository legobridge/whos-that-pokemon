def get_question_from_statement(statement):
    """
    Returns a question in natural language, based on a Statement

    :param statement: a Statement, comprising a predicate (isLegendary)
             and 0 or more terms (Red, for the predicate isColor)
    :return: a string, the natural language question
    """

    feature, values = get_feature_and_values_from_statement(statement)
    if feature == 'isColor':
        return f'Is the Pokemon {values[0]} in color?'

    if feature == 'isLegendary':
        return f'Is it a legendary Pokemon?'

    if feature == 'canEvolve':
        return f'Can the Pokemon evolve into another Pokemon?'

    if feature == 'isPrimaryColor':
        return f'Is the main color of the Pokemon a primary color?'

    if feature == 'wasIntroducedIn':
        return f'Was the Pokemon introduced in {values[0]}?'

    if feature == 'howEffective':
        return get_attack_question(values[0], values[1])

    if feature == 'isAshOwned':
        return f'Is the Pokemon owned by Ash?'

    if feature == 'isGenus':
        return f'Does the Pokemon belong to the {values[0]} genus?'

    if feature == 'isType':
        return f'Is it a/an {values[0]} type Pokemon?'

    if feature == 'itWeighs':
        if values[0] == 'veryLight':
            return 'Is it a very lightweight Pokemon?'
        if values[0] == 'veryHeavy':
            return 'Is it a very heavyweight Pokemon?'

    if feature == 'itHasHeight':
        if values[0] == 'veryShort':
            return 'Is it a very short Pokemon?'
        if values[0] == 'veryTall':
            return 'Is it a very big Pokemon?'

    if feature == 'evolvesFromSomething':
        return f'Does the Pokemon evolve from another Pokemon?'

    if feature == 'hasShape':
        return get_shape_question(values[0])

    if feature == 'isFirstLetter':
        return f'Does the name of the Pokemon start with {values[0]}?'

    # if there's no question, return the raw statement itself
    return statement


def get_feature_and_values_from_statement(statement):
    feature = statement.predicate
    values = [str(term) for term in statement.terms]
    return feature, values


def get_attack_question(attack_type, effectiveness):
    if effectiveness == "super_effective":
        return f"Are {attack_type}-type attacks super effective against the Pokemon?"
    if effectiveness == "not_very_effective":
        return f"Are {attack_type}-type attacks not very effective against the Pokemon?"
    if effectiveness == "has_no_effect":
        return f"Do {attack_type}-type attacks have no effect against the Pokemon?"
    else:
        return None


def get_shape_question(shape):
    if shape == 'Quadruped':
        return f'Does the Pokemon walk/run on four legs?'
    if shape == 'Upright':
        return f'Is it a tailed Pokemon that walks upright on two legs?'
    if shape == 'Armor':
        return f'Does the Pokemon have an insectoid body and hard shell?'
    if shape == 'Squiggle':
        return f'Is the Pokemon serpentine (snake-like)?'
    if shape == 'Bug-Wings':
        return f'Does the Pokemon have wings and an insectoid body?'
    if shape == 'Wings':
        return f'Does the Pokemon have wings?'
    if shape == 'Humanoid':
        return f'Is the Pokemon humanoid shaped with two legs and no tail?'
    if shape == 'Legs':
        return f'Does the Pokemon have two legs and no arms?'
    if shape == 'Blob':
        return f'Is the Pokemon Blob shaped?'
    if shape == 'Heads':
        return f'Does the Pokemon have multiple bodies?'
    if shape == 'Tentacles':
        return f'Does the Pokemon have tentacles?'
    if shape == 'Arms':
        return f'Does the Pokemon only has one head and arms?'
    if shape == 'Fish':
        return f'Does the Pokemon have fins?'
    if shape == 'Ball':
        return f'Is the Pokemon ball-shaped with no arms?'
    return None
