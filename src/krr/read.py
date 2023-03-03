from logical_classes import *


# read_tokenize takes the name of a file, reads it in and tokenizes the
# statements and rules in that file.
def read_tokenize(file):
    """Reads in a file and processes contents into lists of facts and rules.

    Args:
        file (file): A txt file with facts of the form (predicate subject
        object) such as "fact: (isa cube block)". As well, there are rules with
        a right and left hand side that are essentially (fact1 and fact2) ->
        (fact3) such as "rule: ((inst ?x ?y) (isa ?y ?z)) -> (inst ?x ?z)".
        These facts and rules each go on a new line in the file and are looped
        over to build the two seperate lists of facts and rules.

    Returns:
        A list of Facts and Rules.
    """
    file = open(file, "r")
    elements = []
    current = ""
    for line in file:
        if line[0:5] in ("fact:", "rule:"):
            elements.append(current)
            current = line.rstrip()
        else:
            current = current + " " + line.rstrip().strip()
    elements.append(current)
    output = []
    for e in elements:
        parsed = parse_input(e)
        if isinstance(parsed, Fact) or isinstance(parsed, Rule):
            output.append(parsed)
    file.close()
    return output


def parse_input(e):
    """Parses input, assigning labels and splitting rules into LHS & RHS

    Args:
        e (string): Input string to parse

    Returns:
        (number, string | listof string): label, then parsed input
    """
    if len(e) == 0:
        # return (BLANK, None)
        return None
    elif e[0] == '#':
        # return (COMMENT, e)
        return e[1:]
    elif e[0:5] == "fact:":
        e = e[5:].replace(")", "").replace("(", "").rstrip().strip().split()
        # return (FACT, e)
        return Fact(e)
    elif e[0:5] == "rule:":
        e = e[5:].split("->")
        rhs = e[1].replace(")", "").replace("(", "").rstrip().strip().split()
        lhs = e[0].rstrip(") ").strip("( ").replace("(", "").split(")")
        lhs = map(lambda x: x.rstrip().strip().split(), lhs)
        # return (RULE, [lhs, rhs])
        return Rule([lhs, rhs])
    else:
        print("PARSE ERROR: input header", e[0:5], "not recognized.")
