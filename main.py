from parser.RegexParser import parse_regex
import pprint

regex_primer = r"(a|b)*abb"
parsirani_regex = parse_regex(regex_primer)
pprint.pprint(parsirani_regex)
