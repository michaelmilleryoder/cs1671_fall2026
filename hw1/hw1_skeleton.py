'''Homework 1 Text and string processing in Python

This is an individual homework.
Implement the following functions.

'''

import re


def text_to_csv(filepath):
    ''' 
    Refer to the instructions for Part 1.
    '''

    pass


def check_for_foo_or_bar(text):
   '''Checks whether the input string meets the conditions described in Part 2.

   Return:
     True if the condition is met, False otherwise.
   '''

   pass


def replace_rgb(text):
   '''Replaces all RGB or hex colors with the word 'COLOR',
   according to the instructions for Part 2.

   Returns:
     The text with all RGB or hex colors replaced with the word 'COLOR'
   '''

   pass


def wine_text_processing(wine_file_path, stopwords_file_path):
  '''Process the two files to answer the questions according to the Part 3 instructions
  and output results to stdout.

  No return value.
  '''

  pass



''' Code below is used for grading. Students can disregard this. '''
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--part2', nargs='+', dest='part2', default=None, help='<function> <argument>')
    parser.add_argument('--part3', nargs='+', dest='part3', default=None, help='<wine_file_path> <stopwords_file_path>')
    args = parser.parse_args()
    
    if args.part2 is not None:
        function_name = args.part2[0]
        argument = args.part2[1]

        fn = globals()[function_name]
        fn(argument)

    if args.part3 is not None:
        wine_text_processing(args.part3[0], args.part3[1])

if __name__ == '__main__':
    main()
