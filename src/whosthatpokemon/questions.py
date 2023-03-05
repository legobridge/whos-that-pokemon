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
    elif feature == 'isLegendary':
        return f'Is it a legendary Pokemon?'
    elif feature == 'canEvolve':
        return f'Can the Pokemon evolve into another Pokemon?'
    elif feature == 'isPrimaryColor':
        return f'Is the main color of the Pokemon a primary color?'
    elif feature == 'wasIntroducedIn':
        return f'Was the Pokemon introduced in {value}?'
    elif feature == 'howEffective':
        effectiveness = statement.predicate
        attack_type = statement.terms[0]
        get_attack_question(attack_type, effectiveness)
    elif feature == 'isAshOwned':
        return f'Is the Pokemon owned by Ash?'
    elif feature == 'isGenus':
        return f'Does the Pokemon belong to the {value} genus?'
    elif feature == 'isType':
        return f'Is it a/an {value} type Pokemon?'
    elif feature == 'itWeighs':
        if value == 'veryLight':
            return 'Is it a very lightweight Pokemon?'
        elif value == 'veryHeavy':
            return 'Is it a very heavyweight Pokemon?'
    elif feature == 'itHasHeight':
        if value == 'veryShort':
            return 'Is it a very short Pokemon?'
        elif value == 'veryTall':
            return 'Is it a very big Pokemon?'
    elif feature == 'evolvesFromSomething':
        return f'Does the Pokemon evolve from another Pokemon?'
    elif feature == 'hasShape':
        if value == 'Quadruped':
            return f'Does the Pokemon have four legs?'
        elif value == 'Upright':
            return f'Does the Pokemon have two legs and a tail?'
        elif value == 'Armor':
            return f'Does the Pokemon have an insectoid body and hard shell?'
        elif value == 'Squiggle':
            return f'Is the Pokemon serpentine (snake-like)?'
        elif value == 'Bug-Wings':
            return f'Does the Pokemon have wings and an insectoid body?'
        elif value == 'Wings':
            return f'Does the Pokemon have wings?'
        elif value == 'Humanoid':
            return f'Is the Pokemon humanoid shaped with two legs and no tail?'
        elif value == 'Legs':
            return f'Does the Pokemon have two legs and no arms?'
        elif value == 'Blob':
            return f'Is the Pokemon Blob shaped?'
        elif value == 'Heads':
            return f'Does the Pokemon have multiple bodies?'
        elif value == 'Tentacles':
            return f'Does the Pokemon have tentacles?'
        elif value == 'Arms':
            return f'Does the Pokemon only has one head and arms?'
        elif value == 'Fish':
            return f'Does the Pokemon have fins?'
        elif value == 'Ball':
            return f'Is the Pokemon ball-shaped with no arms?'

    return statement


def get_feature_and_value_from_statement(statement):
    feature = statement.predicate
    if len(statement.terms) == 0:
        value = None
    else:
        value = str(statement.terms[0])
    return feature, value


def get_attack_question(attack_type, effectiveness):
    if effectiveness == "super_effective":
        return f"Is {attack_type} attack super effective against the Pokemon?"
    elif effectiveness == "not_very_effective":
        return f"Is {attack_type} attack not very effective against the Pokemon?"
    elif effectiveness == "has_no_effect":
        return f"Does a/an {attack_type} attack has no effect against the Pokemon?"
    else:
        return None
