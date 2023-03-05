from src.knowledgebase import read
from src.knowledgebase.kb import KnowledgeBase
from src.knowledgebase.logical_classes import *

import random


class PokemonGuesser:

    def __init__(self,
                 kb_file='../../data/pokemon_kb.txt',
                 perm_rules_file='../../data/pokemon_perm_rules_kb.txt'):
        self.KB = KnowledgeBase([], [], [])

        self.predicate_difficulty_categories = {
            'easy': ['wasIntroducedIn', 'isLegendary', 'canEvolve', 'isAshOwned',
                     'isPrimaryColor', 'isType', 'evolvesFrom'],
            'ok': ['isColor', 'itHasHeight', 'itHasWeight', 'hasShape'],
            'hard': ['howEffective', 'isGenus'],
        }

        # Assert starter rules
        data = read.read_tokenize(kb_file)
        for item in data:
            if isinstance(item, Fact) or isinstance(item, Rule):
                self.KB.kb_assert(item)

        # Assert permanent rules
        perm_rule_data = read.read_tokenize(perm_rules_file)
        for perm_rule in perm_rule_data:
            if isinstance(perm_rule, Rule):
                self.KB.kb_assert(perm_rule)
                self.KB.permanent_rules.append(perm_rule)

    def get_best_statement_for_next_question(self):
        """
        Based on the current pool of Pokemon in the KB,
        return the best statement to ask a question about.

        :return: a Statement, comprising a predicate (isLegendary)
                 and 0 or 1 terms (Red, for the predicate isColor)
        """
        # todo - choose statements better

        all_statements = {}
        for rule in self.KB.rules:
            if rule in self.KB.permanent_rules:
                continue
            for statement in rule.lhs:
                if statement not in all_statements:
                    all_statements[statement] = 0
                all_statements[statement] += 1

        best_statement = self.get_best_splitting_statement(all_statements, self.predicate_difficulty_categories['easy'])
        if best_statement is not None:
            return best_statement

        best_statement = self.get_best_splitting_statement(all_statements, self.predicate_difficulty_categories['ok'])
        if best_statement is not None:
            return best_statement

        best_statement = self.get_best_splitting_statement(all_statements, self.predicate_difficulty_categories['hard'])

        return best_statement

    def get_best_splitting_statement(self, all_statements, predicates_to_choose_from):
        pokemon_rules_left = len(self.KB.rules) - len(self.KB.permanent_rules)
        best_statement = None
        lowest_split_error = 10000000
        for statement, frequency in all_statements.items():
            if statement.predicate in predicates_to_choose_from:
                split_error = abs(0.5 - (frequency / pokemon_rules_left))
                if best_statement is None or split_error < lowest_split_error:
                    best_statement = statement
                    lowest_split_error = split_error
        return best_statement

    def return_pokemon_if_found(self):
        """
        Returns the guessed Pokemon, if we have narrowed it down to 1.

        :return: False if it is still not narrowed down to 1 Pokemon.
                 Name of the guessed Pokemon otherwise.
        """
        pokemon_rules_left = len(self.KB.rules) - len(self.KB.permanent_rules)
        if pokemon_rules_left > 1:
            return False
        if pokemon_rules_left == 0:
            final_question = Fact(Statement(['isPokemon', '?x']))
            bindings = self.KB.kb_ask(final_question)
            if len(bindings) == 0:
                return None
            else:
                return bindings[0]['?x']
        for rule in self.KB.rules:
            if rule not in self.KB.permanent_rules:
                return rule.rhs.terms[0].term.element

    def add_user_answer_to_kb(self, question_statement: Statement, answer: bool):
        """
        Adds the users answer to the question asked to the KB.

        :param question_statement: the Statement that was used to ask the question.
        :param answer: True if the user said yes, False otherwise
        """
        if not answer:
            question_statement = Statement(['~' + question_statement.predicate] + question_statement.terms)
        self.KB.kb_add(Fact(question_statement))

    def remove_ambiguous_predicate(self, question_statement: Statement):
        """
        Remove predicate from difficulty list if user does not know the answer.

        """
        predicate = question_statement.predicate
        for k, v in self.predicate_difficulty_categories.items():
            if predicate in v:
                v = v.remove(predicate)