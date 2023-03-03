from logical_classes import *
from util import *

verbose = 0


class KnowledgeBase(object):
    def __init__(self, facts, rules, permanent_rules):
        self.facts = facts
        self.rules = rules
        self.permanent_rules = permanent_rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def _get_fact(self, fact):
        """INTERNAL USE ONLY
        Get the fact in the KB that is the same as the fact argument

        Args:
            fact (Fact): Fact we're searching for

        Returns:
            Fact: matching fact
        """
        for kbfact in self.facts:
            if fact == kbfact:
                return kbfact

    def _get_rule(self, rule):
        """INTERNAL USE ONLY
        Get the rule in the KB that is the same as the rule argument

        Args:
            rule (Rule): Rule we're searching for

        Returns:
            Rule: matching rule
        """
        for kbrule in self.rules:
            if rule == kbrule:
                return kbrule

    def _get_fact_rule_from_kb(self, fact_rule):
        if isinstance(fact_rule, Fact):
            kb_supported_fact_rule = self._get_fact(fact_rule)
        elif isinstance(fact_rule, Rule):
            kb_supported_fact_rule = self._get_rule(fact_rule)
        else:
            raise TypeError('fact_rule is neither a Fact nor a Rule')
        return kb_supported_fact_rule

    def kb_add(self, fact_rule):
        """Add a fact or rule to the KB
        Args:
            fact_rule (Fact or Rule) - Fact or Rule to be added
        Returns:
            None
        """
        printv("Adding {!r}", 1, verbose, [fact_rule])
        if isinstance(fact_rule, Fact):
            if fact_rule not in self.facts:
                new_facts_all = []
                new_rules_all = []
                self.facts.append(fact_rule)

                # match the new fact with all existing rules
                for rule in self.rules:
                    new_facts, new_rules = fc_infer(fact_rule, rule)
                    new_facts_all += new_facts
                    new_rules_all += new_rules

                # replace the old rules with new ones that are consistent with the new fact
                self.rules = new_rules_all
                # re-add permanent rules
                for permanent_rule in self.permanent_rules:
                    self.kb_add(permanent_rule)
                # add all newly derived facts to the KB
                for new_fact in new_facts_all:
                    self.kb_add(new_fact)
        elif isinstance(fact_rule, Rule):
            if fact_rule not in self.rules:
                self.rules.append(fact_rule)

    def kb_assert(self, fact_rule):
        """Assert a fact or rule into the KB

        Args:
            fact_rule (Fact or Rule): Fact or Rule we're asserting
        """
        printv("Asserting {!r}", 0, verbose, [fact_rule])
        self.kb_add(fact_rule)

    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Statement to be asked (will be converted into a Fact)

        Returns:
            listof Bindings|False - list of Bindings if result found, False otherwise
        """
        print("Asking {!r}".format(fact))
        if factq(fact):
            f = Fact(fact.statement)
            bindings_lst = ListOfBindings()
            # ask matched facts
            for fact in self.facts:
                binding = match(f.statement, fact.statement)
                if binding:
                    bindings_lst.add_bindings(binding, [fact])

            return bindings_lst if bindings_lst.list_of_bindings else []

        else:
            print("Invalid ask:", fact.statement)
            return []


def fc_infer(fact, rule):
    """Forward-chaining to infer new facts and rules

    Args:
        fact (Fact) - A fact from the KnowledgeBase
        rule (Rule) - A rule from the KnowledgeBase

    Returns:
        Newly inferred facts and rules
    """

    new_facts = []
    new_rules = []

    if fact.statement.predicate[0] != '~':
        bindings = False
        matched_statement = None
        for lhs_matching_statement in rule.lhs:
            bindings = match(fact.statement, lhs_matching_statement)
            if bindings:
                matched_statement = lhs_matching_statement
                break
        if bindings:
            if len(rule.lhs) == 1:
                # New fact can be inferred
                new_fact = Fact(instantiate(rule.rhs, bindings))
                new_facts.append(new_fact)
            else:
                # New rule can be inferred
                new_rule_lhs = []
                for lhs_statement in rule.lhs:
                    if lhs_statement != matched_statement:
                        new_rule_lhs.append(instantiate(lhs_statement, bindings))
                new_rule_rhs = instantiate(rule.rhs, bindings)
                new_rule = Rule([new_rule_lhs, new_rule_rhs])
                new_rules.append(new_rule)
    else:
        bindings = False
        statement_inverted = invert(fact.statement)
        for lhs_matching_statement in rule.lhs:
            bindings = match(statement_inverted, lhs_matching_statement)
            if bindings:
                break
        if not bindings:
            # if the inverted fact did not match with this rule, then we want to retain this rule
            new_rules.append(rule)

    return new_facts, new_rules
