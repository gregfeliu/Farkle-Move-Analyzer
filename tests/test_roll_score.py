from functions import *



## ROLLS TO TEST
### Special Rolls for 6 Dice
def six_of_a_kind(roll):
    score = get_score_of_roll(roll)
    return score 

def test_six_of_a_kind():
    correct_number_of_points = 3000
    assert six_of_a_kind(('1', '1', '1', '1', '1', '1')) == correct_number_of_points, f"A six of a kind should give you {correct_number_of_points} points"

def two_triplets(roll):
    score = get_score_of_roll(roll)
    return score 

def test_two_triplets():
    correct_number_of_points = 2500
    assert two_triplets(('1', '1', '1', '3', '3', '3')) == correct_number_of_points, f"Two triplets should give you {correct_number_of_points} points"
    
    
def straight(roll):
    score = get_score_of_roll(roll)
    return score 

def test_straight():
    correct_number_of_points = 1500
    assert straight(('1', '2', '3', '4', '5', '6')) == correct_number_of_points, f"A straight should give you {correct_number_of_points} points"
    
def three_pairs(roll):
    score = get_score_of_roll(roll)
    return score 

def test_three_pairs():
    correct_number_of_points = 1500
    assert straight(('2', '2', '4', '4', '5', '5')) == correct_number_of_points, f"Three pairs should give you {correct_number_of_points} points"
    
def four_of_a_kind_plus_two_pair(roll):
    score = get_score_of_roll(roll)
    return score 

def test_four_of_a_kind_plus_two_pair():
    correct_number_of_points = 1500
    assert straight(('4', '4', '4', '4', '5', '5')) == correct_number_of_points, f"A four of a kind plus a pair should give you {correct_number_of_points} points"

### Special Rolls for 5 Dice
def five_of_a_kind_w_six_dice(roll):
    score = get_score_of_roll(roll)
    return score 

def test_five_of_a_kind_w_six_dice():
    correct_number_of_points = 2000
    assert five_of_a_kind_w_six_dice(('4', '4', '4', '4', '4', '6')) == correct_number_of_points, f"A five of a kind should give you {correct_number_of_points} points"

def five_of_a_kind_w_five_dice(roll):
    score = get_score_of_roll(roll)
    return score 

def test_five_of_a_kind_w_five_dice():
    correct_number_of_points = 2000
    assert five_of_a_kind_w_five_dice(('4', '4', '4', '4', '4')) == correct_number_of_points, f"A five of a kind should give you {correct_number_of_points} points"

def four_of_a_kind_w_six_dice(roll):
    score = get_score_of_roll(roll)
    return score 

def test_four_of_a_kind_w_six_dice():
    correct_number_of_points = 1000
    assert four_of_a_kind_w_six_dice(('2', '4', '4', '4', '4', '6')) == correct_number_of_points, f"A four of a kind should give you {correct_number_of_points} points"

def four_of_a_kind_w_five_dice(roll):
    score = get_score_of_roll(roll)
    return score 

def test_four_of_a_kind_w_five_dice():
    correct_number_of_points = 1000
    assert four_of_a_kind_w_five_dice(('4', '4', '4', '4', '6')) == correct_number_of_points, f"A five of a kind should give you {correct_number_of_points} points"

### Special Rolls for 3 Dice in a Roll with 6 Dice
def three_ones_w_6_dice(roll):
    score = get_score_of_roll(roll)
    return score 

def test_three_ones_w_6_dice():
    correct_number_of_points = 300
    assert three_ones_w_6_dice(('1', '1', '1', '3', '4', '6')) == correct_number_of_points, f"Three ones should give you {correct_number_of_points} points"

def three_twos_w_6_dice(roll):
    score = get_score_of_roll(roll)
    return score 

def test_three_twos_w_6_dice():
    correct_number_of_points = 200
    assert three_twos_w_6_dice(('2', '2', '2', '3', '4', '6')) == correct_number_of_points, f"Three twos should give you {correct_number_of_points} points"

def three_threes_w_6_dice(roll):
    score = get_score_of_roll(roll)
    return score 

def test_three_threes_w_6_dice():
    correct_number_of_points = 300
    assert three_threes_w_6_dice(('2', '3', '3', '3', '4', '6')) == correct_number_of_points, f"Three threes should give you {correct_number_of_points} points"

def three_fours_w_6_dice(roll):
    score = get_score_of_roll(roll)
    return score 

def test_three_fours_w_6_dice():
    correct_number_of_points = 400
    assert three_fours_w_6_dice(('2', '2', '4', '4', '4', '6')) == correct_number_of_points, f"Three fours should give you {correct_number_of_points} points"

def three_fives_w_6_dice(roll):
    score = get_score_of_roll(roll)
    return score 

def test_three_fives_w_6_dice():
    correct_number_of_points = 500
    assert three_fives_w_6_dice(('2', '4', '5', '5', '5', '6')) == correct_number_of_points, f"Three fives should give you {correct_number_of_points} points"

def three_sixes_w_6_dice(roll):
    score = get_score_of_roll(roll)
    return score 

def test_three_sixes_w_6_dice():
    correct_number_of_points = 600
    assert three_sixes_w_6_dice(('2', '4', '4', '6', '6', '6')) == correct_number_of_points, f"Three sixes should give you {correct_number_of_points} points"

### Special Rolls for 3 Dice in a Roll with 3 Dice
def three_ones_w_3_dice(roll):
    score = get_score_of_roll(roll)
    return score 

def test_three_ones_w_3_dice():
    correct_number_of_points = 300
    assert three_ones_w_3_dice(('1', '1', '1')) == correct_number_of_points, f"Three ones should give you {correct_number_of_points} points"

def three_twos_w_3_dice(roll):
    score = get_score_of_roll(roll)
    return score 

def test_three_twos_w_3_dice():
    correct_number_of_points = 200
    assert three_twos_w_3_dice(('2', '2', '2')) == correct_number_of_points, f"Three twos should give you {correct_number_of_points} points"

def three_threes_w_3_dice(roll):
    score = get_score_of_roll(roll)
    return score 

def test_three_threes_w_3_dice():
    correct_number_of_points = 300
    assert three_threes_w_3_dice(('3', '3', '3')) == correct_number_of_points, f"Three threes should give you {correct_number_of_points} points"

def three_fours_w_3_dice(roll):
    score = get_score_of_roll(roll)
    return score 

def test_three_fours_w_3_dice():
    correct_number_of_points = 400
    assert three_fours_w_3_dice(('4', '4', '4' )) == correct_number_of_points, f"Three fours should give you {correct_number_of_points} points"

def three_fives_w_3_dice(roll):
    score = get_score_of_roll(roll)
    return score 

def test_three_fives_w_3_dice():
    correct_number_of_points = 500
    assert three_fives_w_3_dice(('5', '5', '5')) == correct_number_of_points, f"Three fives should give you {correct_number_of_points} points"

def three_sixes_w_3_dice(roll):
    score = get_score_of_roll(roll)
    return score 

def test_three_sixes_w_3_dice():
    correct_number_of_points = 600
    assert three_sixes_w_3_dice(('6', '6', '6')) == correct_number_of_points, f"Three sixes should give you {correct_number_of_points} points"

### Cases that Combine Special Rolls with ones and fives
def three_sixes_w_one_4_dice(roll):
    score = get_score_of_roll(roll)
    return score 

def test_three_sixes_w_one_4_dice():
    correct_number_of_points = 700
    assert three_sixes_w_one_4_dice(('1', '6', '6', '6')) == correct_number_of_points, f"Three sixes should give you {correct_number_of_points} points"
    
def four_twos_one_five(roll):
    score = get_score_of_roll(roll)
    return score 

def test_four_twos_one_five():
    correct_number_of_points = 1150
    assert four_twos_one_five(('1', '2', '2', '2', '2', '5')) == correct_number_of_points, f"Three sixes should give you {correct_number_of_points} points"   
    
    
    
    
    

