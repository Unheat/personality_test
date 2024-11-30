'''
CS 109 Fall 2024 Lab 1
Measuring the Big Five Personality Dimensions
Authors: <Your Names>
'''

def print_instructions():
    '''
    This function prints the instructions for the Big Five Personality Survey
    Inputs: None
    Outputs: None
    '''
    return

def get_survey_answers():
    '''
    This function prompts the user to answer each of the ten survey questions, converts their answers
    to integers, and returns those ten integers in order.
    Inputs: None

    Outputs: 
            raw_scores: A list of 10 raw user responses to questions in question order:
            [Response for Q1, Response for Q2, ... Response for Q10]
            Important: These scores must be integers!!!
    '''
    raw_scores = None # this variable is the output of your function!
    return raw_scores

def reverse_even_scores(raw_scores):
    '''
    This function takes a list of ten integers, each between 1 and 7. It returns a list of ten integers,
    where each of the even-indexed numbers in the list has been "reversed" as follows:
        7 --> 1; 6 --> 2; 5 --> 3; 4 --> 4; 3 --> 5; 2 --> 6; 1 --> 7;  
    Inputs: 
        raw_scores: A list of ten integers, each between 1 and 7
    Outputs: 
        reversed_scores: A list of ten integers, where the even-indexed scores have been reversed

    '''
    reversed_scores = None # this variable is the output of your function!
    return reversed_scores

def score_dimensions(raw_scores):
    '''
    This function calculates the scores for each of the Big Five dimensions
    Inputs: 
            raw_scores: A list of 10 raw user responses to questions in question order:
            [Response for Q1, Response for Q2, ... Response for Q10]
            Important: These scores must be integers!!!
    Outputs: 
            big_five_scores: A list of five scores for each of the five dimensions in this order:
            [Extraversion, Agreeableness, Conscientiousness, Emotional Stability, Openness to Experience]
            Important: These scores must be floating point numbers (decimals)!!!
    '''
    big_five_scores = None # this variable is the output of your function!
    return big_five_scores

def take_survey():
    '''
    This function handles running the survey from start to finish. It should call
    functions to print the instructions, prompt for and store user input, calculate the results,
    and print them to the screen. It takes no inputs and returns a list of the five dimension scores
    in this order: [Extraversion, Agreeableness, Conscientiousness, Emotional Stability, Openness to Experience]
    Inputs: None

    Outputs: 
            big_five_scores: A list of five scores for each of the five dimensions in this order:
            [Extraversion, Agreeableness, Conscientiousness, Emotional Stability, Openness to Experience]
            Important: These scores must be floating point numbers (decimals)!!!
    '''
    big_five_scores = None # this variable is the output of your function!
    return big_five_scores
def main():
    '''
    Add your own docstring here
    '''
    return

if __name__=='__main__':
    main()
