import numpy as np
import itertools
import math
import random
from fractions import Fraction





def all_combos(num_of_dice: int):
    assert num_of_dice < 7
    all_combos = list(itertools.product("123456", repeat=num_of_dice))
    return all_combos

def roll_the_dice(all_combos: list):
    rand_roll_index = random.randint(0, len(all_combos))
    roll = all_combos[rand_roll_index]
    return roll, rand_roll_index

def roll_to_dict(roll):
    special_combos_dict = {"1": 0, "2":0, "3":0, "4":0, "5": 0, "6":0}
    for die in roll:
        special_combos_dict[die] += 1
    return special_combos_dict

def check_single_die(roll: tuple):
    """
    returns the num of points the roll earned
    """
    points = 0
    single_die_score_dict = {"1": 100, "2":0, "3":0, "4":0, "5": 50, "6":0}
    value = roll[0]
    points = single_die_score_dict[value]
    return points

def check_multiple_single_dies(roll_remainder: set, points=0):
    for die in roll_remainder:
        points += check_single_die(die)
    return points

def check_6_dice_combos(roll: set):
    values_count_dict = roll_to_dict(roll)
    unique_values_of_roll = set(values_count_dict.values())
    # account for all of the special pairs that use 6 dice (in order of points descending)
    # 6 of a kind
    if unique_values_of_roll == {0, 6}: 
#         print("You got a six of a kind! You get 3,000 points")
        return 3000
    # 2 triplets can't be solved with the set only b/c it will overlap with one triplet...
    elif unique_values_of_roll == {0, 3}: 
#         print("You got two triplets! You get 2,500 points")
        return 2500
    # straight
    elif unique_values_of_roll == {1}:
#         print("You got a straight! You get 1,500 points")
        return 1500
    # 3 pairs
    elif unique_values_of_roll == {0, 2}: 
#         print("You got a three pairs! You get 1,500 points")
        return 1500
    # four of a kind + a pair
    elif unique_values_of_roll == {0, 2, 4}: 
#         print("You got a four of a kind + a pair! You get 1,500 points")
        return 1500
    
# dealing with mid-number-of-dice combos plus extras...
def check_5_4_dice_combos(roll: set):
    points = 0
    values_count_dict = roll_to_dict(roll)
#     print(f"{values_count_dict}")
    unique_values_of_roll = set(values_count_dict.values())
#     print(f"{unique_values_of_roll}")
    # 5 of a kind
    if 5 in unique_values_of_roll:
        points = 2000
#         # find value of non-quintuple roll value
        if len(roll) > 5:
            non_5_pair_die = tuple(key for key, value in values_count_dict.items() if value == 1)
            points += check_single_die(non_5_pair_die)
#         print(f"You got a five of a kind! You get {points} points")
        return points
    # four of a kind
    elif 4 in unique_values_of_roll:
        points = 1000
        if len(roll) > 4:
            non_4_pair_die = tuple(key for key, value in values_count_dict.items() if 1 <= value <= 2)
            points = check_multiple_single_dies(non_4_pair_die, points)
#         print(f"You got a four of a kind! You get {points} points")
        return points
    else:
        return None
    
def check_3_dice_combos(roll: set):
    triples_dict = {"1":300, "2":200, "3":300, "4":400, "5": 500, "6":600}
    points = 0
    values_count_dict = roll_to_dict(roll)
    unique_values_of_roll = set(values_count_dict.values())
    # check if there's a triple 
    if list(values_count_dict.values()).count(3) == 1:
        tripled_number = [key for key, value in values_count_dict.items() if value == 3]
        points = triples_dict[tripled_number[0]]
        if len(roll) > 3:
            other_dice = tuple(key for key, value in values_count_dict.items() if 1 <= value <= 2)
            points = check_multiple_single_dies(other_dice, points)
#         print(f"You got a triple! You get {points} points")
    else:
        points = check_multiple_single_dies(roll, points)
        if points > 0:
            pass
#             print(f"You got a one or a five! You get {points} points")
        elif points == 0: 
            points = 0
#             print("Sorry, you didn't score any points.")
    return points

# the important function
def get_score_of_roll(roll: set):
    points = None
    if len(roll) == 6:
        points = check_6_dice_combos(roll)
    if points == None and len(roll) <= 6:
        points = check_5_4_dice_combos(roll)
        if points == None:
            points = check_3_dice_combos(roll)
    return points


def find_unique_combos(x_dice_combos: list):
    combos_sum_dict = {}
    for roll in x_dice_combos:
        new_key = ""
        for die in roll:        
            new_key += die
        sorted_key = "".join(sorted(new_key))
        if combos_sum_dict.get(sorted_key) == None:
            combos_sum_dict[sorted_key] = None
    return combos_sum_dict

def find_values_of_unique_combos(x_dice_combos_dict: dict):    
    for key, value in x_dice_combos_dict.items():
        key_set = tuple(x for x in key)
        new_value = get_score_of_roll(key_set)
        if x_dice_combos_dict[key] == None:
            x_dice_combos_dict[key] = new_value
        elif new_value > x_dice_combos_dict[key]:
            x_dice_combos_dict[key] = new_value
    return x_dice_combos_dict

def find_scores_for_each_possible_roll(all_possible_combos: list, score_dict: dict):
    all_combos_scores = []
    for roll in all_possible_combos:
        string_roll =  ""
        for die in roll:        
            string_roll += die
        sorted_roll = "".join(sorted(string_roll))
        score = score_dict[sorted_roll]
        all_combos_scores.append(score)
    all_combos_scores_w_scores = list(zip(all_possible_combos, all_combos_scores))
    return all_combos_scores, all_combos_scores_w_scores

def get_average(all_combos_scores:list):
    return round(sum(all_combos_scores) / len(all_combos_scores),1)

def find_mean_score_of_x_dice(num_of_dice: int):
    x_dice_combos = all_combos(num_of_dice)
#     x_dice_special_combos_dict = roll_to_dict(roll)
    x_dice_combos_dict = find_unique_combos(x_dice_combos)
    x_dice_combos_dict_w_scores = find_values_of_unique_combos(x_dice_combos_dict)
    all_combos_for_x_dice,all_combos_for_x_dice_w_scores = find_scores_for_each_possible_roll(x_dice_combos,
                                                                                             x_dice_combos_dict_w_scores)
    x_dice_average_score = get_average(all_combos_for_x_dice)
    return all_combos_for_x_dice_w_scores, x_dice_average_score

def find_max_score(all_combos_for_x_dice_w_scores: list):
    return max(list(zip(*all_combos_for_x_dice_w_scores))[1])

def find_median_score(all_combos_for_x_dice_w_scores: dict):
    scores_for_x_dice = np.array([x[1] for x in all_combos_for_x_dice_w_scores])
    return np.median(scores_for_x_dice)

def find_count_of_scores(all_combos_for_x_dice_w_scores: dict):
    # count how many values have a certain score
    ## make a dict of scores
    ### count how many times it appears
    #### gives odds 
    scores_for_x_dice = np.array(sorted([x[1] for x in all_combos_for_x_dice_w_scores]))
    scores_w_count = np.unique(scores_for_x_dice, return_counts=True)
    number_of_possibilities = len(scores_for_x_dice)
    scores_w_count_dict = {}
    for idx, item in enumerate(scores_w_count[0]):
        pct_probability = round((scores_w_count[1][idx] / number_of_possibilities) * 100, 1) 
        fraction_probability = Fraction(scores_w_count[1][idx], number_of_possibilities)
        scores_w_count_dict[item] = [pct_probability, fraction_probability]
#     scores_w_count_dict = dict(zip(scores_w_count[0], scores_w_count[1]))
    return scores_w_count_dict

def find_odds_of_scoring_at_or_above_x(score_to_beat: int, count_of_scores_x:dict):
    assert score_to_beat > 0
    assert score_to_beat <= 3001, f"It's impossible to roll above 3000, so you won't be able to roll score_to_beat"
    dict_keys = [int(x) for x in count_of_scores_x]
    dict_keys_above_score_to_beat = [x for x in dict_keys if x >= score_to_beat]
    count_of_scores_above_scores_to_beat = {key: value for key,value in count_of_scores_x.items()
                                           if key in dict_keys_above_score_to_beat}
    running_prob = sum([value[0] for value in count_of_scores_above_scores_to_beat.values()])
    return running_prob

def find_odds_for_multiple_scores(scores_to_beat: list, count_of_scores_x:dict):
    scores = [find_odds_of_scoring_at_or_above_x(item, count_of_scores_x) for item in scores_to_beat]
    return scores
