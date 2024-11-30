from bigfivesurvey import score_dimensions, get_survey_answers
import random

def test_score_1():
    answers = [1, 7, 1, 7, 1, 7, 1, 7, 1, 7] # every answer should be 1
    for score in score_dimensions(answers):
        assert score == 1

def test_score_2():
    answers = [1]*10 # every answer should be 4
    for score in score_dimensions(answers):
        assert score == 4

def test_score_3():
    answers = [1,2,3,4,5,1,2,3,4,5]
    for score in score_dimensions(answers):
        assert score == 4

def test_score_4():
    answers = [1,2,1,7,4,7,7,7,5,1]
    results = [1.0, 6.5, 1.0, 3.0, 5.5]
    for i,score in enumerate(score_dimensions(answers)):
        assert score == results[i]

def test_input_range(monkeypatch):
    ints = list(range(1,8)) + list(range(1,4))
    survey_answers = iter(ints)
    monkeypatch.setattr('builtins.input', lambda _: next(survey_answers))
    raw_answers = get_survey_answers()
    for i,j in enumerate(ints):
        assert raw_answers[i] == j

def test_input_random(monkeypatch):
    ints = random.choices(range(1,8), k=10)
    survey_answers = iter(ints)
    monkeypatch.setattr('builtins.input', lambda _: next(survey_answers))
    raw_answers = get_survey_answers()
    for i in range(10):
        assert raw_answers[i] == ints[i]

def test_input_type(monkeypatch):
    ints = [7,4,2,3,1,5,6,2,3,1]
    survey_answers = iter(ints)
    monkeypatch.setattr('builtins.input', lambda _: next(survey_answers))
    raw_answers = get_survey_answers()
    for i in range(10):
        assert type(raw_answers[i]) == int