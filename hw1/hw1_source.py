#!/usr/bin/env python3

# Parse arguments
import sys

# Quit if not three arguments provided
if len(sys.argv) < 4:
    print("Needs three arguments:")
    print("hw1_parse.sh <grammar_file> <test_sentence_file> <output_file>")
    sys.exit(0)

# Store arguments
grammar_file = sys.argv[1]
test_sentence_file = sys.argv[2]
output_file = sys.argv[3]

# Empty text file
open(output_file, 'w').close()

# Setup nltk, grammar, and parser
import nltk
grammar = nltk.data.load(grammar_file, 'cfg')
parser = nltk.parse.EarleyChartParser(grammar)
total_trees = 0


# Iterate over sentences
from nltk.tokenize import word_tokenize
num_sentences = 0
sentence_file = open(test_sentence_file)
for line in sentence_file:
    # Print sentence
    print(line, file=open(output_file, "a"))

    # Tokenize sentence
    line_tokens = word_tokenize(line)

    # Print parses
    parse_trees = parser.parse(line_tokens)
    num_trees = 0
    for parse_tree in parse_trees:
        print(parse_tree, file=open(output_file, "a"))
        num_trees += 1

    # Print number of parses
    print("Number of parses: " + str(num_trees), file=open(output_file, "a"))

    # Keep running total of trees encountered
    total_trees += num_trees

    # Print empty line
    print("", file=open(output_file, "a"))
    num_sentences += 1

# Calculate average number of parses per sentence obtained by the grammar
average_parses_per_sentence = round(total_trees / float(num_sentences), 3)
print("Average parses per sentence: " + str(average_parses_per_sentence), file=open(output_file, "a"))
