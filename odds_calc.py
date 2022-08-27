import json

def get_odds(titan_level, tier_of_champion, nbr_of_champs_out_of_pool):
    # get the json files with "reroll chances" & "champion pool"
    with open("reroll_chances.json") as json_file:
        odds_dict = json.load(json_file)
    
    with open("champion_pool.json") as json_file:
        pool_dict = json.load(json_file)

    # output
    odds_of_finding_champion = 0

    # odds of a tierX champion to appear in shop
    shop_odds = odds_dict[titan_level][tier_of_champion]
    
    # get the constants for the current state of the game
    number_of_available_copies = pool_dict[tier_of_champion]["champion_qty"] - nbr_of_champs_out_of_pool
    pool_size = pool_dict[tier_of_champion]["pool_size"]
    
    # Odds of finding a specific tier champion
    find_champion_odds = number_of_available_copies/pool_size
    
    # Multiplying the odds 
    total_odds = shop_odds * find_champion_odds

    # 5 champions per shop reroll
    reroll = 5
    while odds_of_finding_champion < 0.5:
        no_hit = (1 - total_odds)**reroll
        odds_of_finding_champion = 1 - no_hit
        reroll += 5
    return total_odds, reroll/5

def three_star_reroll_cost():
    # Initialize variable
    total_reroll_cost = 0

    # Set of inputs:
    input_set = ("Level_6", "Tier3")
    
    # input
    for i in range(3):
        total_odds, shop_odds = get_odds(input_set[0], input_set[1], i)
        print("titan lvl : " + input_set[0] + "\nFinding champ of : "+ input_set[1])
        print("Gold cost for < 50%: " + str(shop_odds*2))
        total_reroll_cost += shop_odds*2
    print(total_reroll_cost)

def calc_odds():
    # Set of inputs:
    input_set = [
        ("Level_6", "Tier4", 2),
        ("Level_7", "Tier4", 2),
        ("Level_8", "Tier4", 2),
        ]
    # input
    for input in input_set:
        total_odds, shop_odds = get_odds(input[0], input[1], input[2])
        print("titan lvl : " + input[0] + "\nFinding champ of : "+ input[1])
        print("Gold cost for < 50%: " + str(shop_odds*2))

if __name__ == "__main__":
    three_star_reroll_cost()