
# CS 109 Lab 1: Measuring Personality Traits

## Overview
Personality tests are popular ways to quantify a person's tendencies and traits. Some companies use them to inform how they build and work in teams; individuals may use them for introspection or personal interest. They can also be used by marketing companies to target specific demographics. In one famous example, Cambridge Analytica was alleged to have used individuals' Facebook data to target advertisements to their personalities in the 2016 US Presidential election. The strategy, popularly termed "psychographic targeting" sought to quantify a person's personality across five dimensions based on their Facebook likes. Read more about this controversy here: [The scant science behind Cambridge Analytica’s controversial marketing techniques](https://www.nature.com/articles/d41586-018-03880-4).

At the center of the Cambridge Analytica controversy were five traits used to model people's personalities. These traits, popularly known as the Big Five traits, have been theorized by some psychologists to represent the five basic dimensions that describe personality. These five traits have historically included: Extraversion, Agreeableness, Conscientiousness, Neuroticism, and Openness to Experience. The personality test that we will use in this project slightly modifies these, replacing Neuroticism with Emotional Stability. You can read more about the five factor model of personality and its history here: [An Introduction to the Five-Factor Model and its Applications](Mcrae1992.pdf).

In this project, you will implement a ten-question Big Five personality test using Python. Your program will use Python’s input() function to prompt a user to rate themselves on a scale of 1-7 with respect to 10 sets of adjectives. It will process their answers and use them to calculate how strong their personality is in each of five different factors, using the instructions defined below. You will then display a friendly report of the results to the user.

## Relevant Skills
To complete this project, you should be familiar with the following:
* Defining and decomposing problems
* Writing an algorithm to solve a problem
* Taking user input from the terminal using input()
* Defining and calling functions
* Assigning values to variables
* Casting variables to different types (e.g. casting a string to an integer)
* Performing basic math operations using Python
* Accessing (indexing) specific items in a Python list (see below)
* Displaying output using print()

**Important: You do NOT need any Python concepts beyond what has been covered in the reading, class, homework, and this writeup to complete the project. Use of Python constructs that have not been covered will be penalized.**

## Preliminary Note: Accessing (Indexing) Specific Items in a List
So far, we've seen how to access items in a Python list using a for loop. It is also possible to access individual elements using something called indexing. To access an item from a list, we use its position (or index) in the list. Synctactically, we do this using the list name and square brackets. For example, suppose I had a list of `numbers = [1, 3, 2, 6, 5]`. To access the third item in the list, I would use the syntax `numbers[2]`. The statement `third = numbers[2]` would assign the value 2 to the variable third. Why is the index of the third item 2 and not 3? It's because we _zero-index_; that is, the first position is index 0, the second position is index 1, etc. Thus, the nth item in a list is accessed using index n-1. 

## The Ten Item Personality Measure (TIPI)

The following survey was developed at the University of Texas to assess a person in each of the Big Five personality dimensions using ten simple questions. The following wording has been taken verbatim from that survey. Your project should print the same messages to prompt the user. Since the researchers at UT who developed the survey have designed and tested it, we want to keep as much of their wording and presentation as possible.
[The Ten Item Peresonality Measure](https://gosling.psy.utexas.edu/scales-weve-developed/ten-item-personality-measure-tipi/).

### The Five Factors Measured by TIPI
* Extraversion
* Agreeableness
* Conscientiousness
* Emotional Stability
* Openness to Experience

### Survey:
Here are a number of personality traits that may or may not apply to you. Please write a number next to each statement to indicate the extent to which you agree or disagree with that statement. You should rate the extent to which the pair of traits applies to you, even if one characteristic applies more strongly than the other.

1 = Disagree strongly
2 = Disagree moderately
3 = Disagree a little
4 = Neither agree nor disagree
5 = Agree a little
6 = Agree moderately
7 = Agree strongly

I see myself as:

1. _____ Extraverted, enthusiastic.

2. _____ Critical, quarrelsome.

3. _____ Dependable, self-disciplined.

4. _____ Anxious, easily upset.

5. _____ Open to new experiences, complex.

6. _____ Reserved, quiet.

7. _____ Sympathetic, warm.

8. _____ Disorganized, careless.

9. _____ Calm, emotionally stable.

10. _____ Conventional, uncreative.


## Scoring the TIPI Survey

1. The survey intentionally reverses the scale for every other question. In other words, questions 1, 3, 5, 7, and 9 are scored as if 7 is the highest score for the corresponding personality dimension, while questions 2, 4, 6, 8, and 10 are scored as if 1 is the highest. Thus, you need to reverse the scores for the even-numbered answers. For example, if a user entered 7 for question number 2, you should change that number to 1, 6 becomes 2, 5 becomes 3, etc.

2. The questions map to each of the personality dimensions as follows:

| Personality Dimension | Corresponding Questions |
| -----------  | --------- |
| Extraversion | 1, 6 (reversed) |
| Agreeableness | 2 (reversed), 7 |
| Conscientiousness | 3, 8 (reversed) |
| Emotional Stability | 4 (reversed), 9 |
| Openness to Experience | 5, 10 (reversed) |

 
For each dimension, the result is the average of the corresponding question results, once you’ve reversed the score for the even-numbered questions. For example: if a user enters 5 for question 1 and 2 for question 6, to get their Extraversion score:
1. Reverse their answer for question 6: 2 becomes 6.
2. Take the average of 5 and 6, which is 5.5.

Your program should calculate these numbers for each of the five personality dimensions, based on the number the user responds to each of the ten prompts with.

## Program Structure
I've given you a file, bigfivesurvey.py to start with. Inside this file I have defined the following functions:

* take_survey(): A function to handle running the survey from start to finish.
* print_instructions(): A function to print survey instructions to the user
* print_report(): A function to print the final report to the user with their results
* get_survey_answers(): A function that prompts the user with each of the ten survey item and returns a list of their answers as ints
* score_dimensions(raw_scores): a function that calculates the user's Big Five personality scores from their survey responses and returns them as floats
* reverse_even_scores(raw_scores): a function that reverses the raw scores for the reverse-coded survey questions. Note that you could choose to do this on a trait by trait or question by question basis instead of implementing this function on the whole list of inputs.

While this skeleton is intended to give you some structure in approaching this problem, you are strongly encouraged to apply the problem-solving framework we've been practicing in class: start by defining the problem(s) you are trying to solve, then developing the algorithms to do so, before implementing and testing them. The writeup has been structured to encourage this.

IMPORTANT: You can choose to decompose the problem differently into different functions as you wish. However, DO NOT REMOVE OR CHANGE THE NAME, ARGUMENTS, OR RETURN VALUE of score_dimensions or get_survey_answers! This will cause your program to fail the tests that I have defined based on those function headers.

## Sample Output
Your survey and report may look something like this, but they do not have to. Feel free to design more user-friendly inputs and outputs, so long as you use the TIPI text to prompt for each question and clearly specify the scores and identify each dimension when you print the report.

```
Hello! Welcome to the Big Five Personality Factors Survey!

Here are a number of personality traits that may or may not apply to you. Please write a number next to each statement to indicate the extent to which you agree or disagree with that statement. You should rate the extent to which the pair of traits applies to you, even if one characteristic applies more strongly than the other.

1 = Disagree strongly
2 = Disagree moderately
3 = Disagree a little
4 = Neither agree nor disagree
5 = Agree a little
6 = Agree moderately
7 = Agree strongly

I see myself as:
1. Extraverted, enthusiastic (1-7): 1
2. Critical, quarrelsome (1-7): 2
3. Dependable, self-disciplined (1-7): 1
4. Anxious, easily upset (1-7): 7
5. Open to new experiences, complex (1-7): 4
6. Reserved, quiet (1-7): 7
7. Sympathetic, warm (1-7): 7
8. Disorganized, careless (1-7): 7
9. Calm, emotionally stable (1-7): 5
10. Conventional, uncreative (1-7): 1

**************************************************
Your Big Five Personality Report
**************************************************
Based on your responses, your personality profile is as follows:
Extraversion: 1.0 out of 7
Agreeableness: 6.5 out of 7
Conscientiousness: 1.0 out of 7
Emotional Stability: 3.0 out of 7
Openness to Experience: 5.5 out of 7

```

## Deliverables
The two primary deliverables for this project are a completed program in bigfivesurvey.py, as well as a final writeup.
I have provided a template for the writeup in writeup.md. While you are free to add additional content to your writeup, and/or submit a file in a different format (e.g. .doc or .pdf), you must at least complete the sections in writeup.md to receive credit.
You and your partner should sync (i.e. commit) a final version of your code and writeup by the deadline.
A rubric for grading can be found below, and the late policy for projects is outlined in the syllabus.

Additionally, you should sync (commit) a copy of your group contract, which is worth part of your teamwork score. You can do this by editing the groupcontract.md file or adding a scan or image of a paper contract that you filled out in class to your project1 directory and sync'ing it. If you are unsure how to do this at this point in the class, please see the professor or TA for assistance.

## Teamwork
As much as possible, all groupmates should contribute equally to the completion of this project. Note that these contributions may not look the same, as you and your partner probably have different strengths and experiences. Ideally, you will meet to plan, devise the algorithms, write the code, and write the report together, rather than simply dividing the work and working separately. To facilitate this, I've included a group contract (groupcontract.md) as a quick way to plan how you will meet and collaborate. Please fill this out and sync it early on--this will count towards the teamwork score. Additionally, you will include a contributions statement describing how each of you contributed to the effort in the report writeup.

Please note: It is absolutely not acceptable to have one person solely responsible for the algorithms and code and another person solely responsible for the writeup. You will receive zero points for teamwork if this is the case.



## Rubric
The project will be graded as follows:

|              | Description                       |
| -----------  | --------------------------------- |
| Correctness  | Does the program correctly calculate the Big Five dimensions from survey responses? Does the project correctly prompt for inputs? Is a readable report printed with the correct values? |
| Style and Structure |  Is the code readable? Is there reasonable decomposition into functions? Are there excessive or unnecessary global variables? Does the program effectively use main as a single entry point? Do variables and functions have meaningful names? Are there meaningful comments to document the code? |
| Writeup | Completeness: Are all the sections in the template completed? | 
| | Clarity: Does the writeup clearly  explain the project, how to use it, and correctly describe how it was implemented? Are there significant grammatical errors or typos that make the report difficult to understand? |
|  | Ethical and Personal Reflections: Is there a thorough discussion of both benefits and risks of this kind of technology? Are personal reflections on the project discussed? | 
| | Teamwork   Does the contribution statement make it clear how both teammates contributed to the project and is the distribution of work even? This score and the overall lab score may be adjusted individually but group work issues should be brought to the professor BEFORE submission. Part of this score is completing and submitting the group contract.


## Optional Extensions
If you complete the project and want to explore further for your own edification (no extra credit), here are some optional extensions you might try. Note that these extensions will not make up for incorrect output or poor style, so make sure you are happy with your project first. Also, be careful to abide by the policy about using advanced Python constructs--check with me if you ahve questions about this.

* Add some automatically generated written analysis of a user's scores to the report. For example, state if they have a high or low Extraversion score or identify their most dominant traits.
* Use text to visualize the person's results (for example, you might make a bar graph with asterisks)
