import json


def get_odds(titan_level, tier_of_champion, nbr_of_champs_out_of_pool=0):

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
    find_champ_per_shop = shop_odds * find_champion_odds

    return find_champ_per_shop

    # 5 champions per shop reroll
    #reroll = 5

    #while odds_of_finding_champion < 0.5:
    #    no_hit = (1 - find_champ_per_shop)**reroll
    #    odds_of_finding_champion = 1 - no_hit
    #    reroll += 5

def three_star_reroll_cost(titan_level, champ_tier):

    # Initialize variable
    odd_res = []

    # input
    for i in range(3):
        total_odds, shop_odds = get_odds(titan_level, champ_tier, i)
        odd_res.append((total_odds, shop_odds))
        print("titan lvl : " + titan_level + "\nFinding champ of : "+ champ_tier)
        print("Gold cost for < 50%: " + str(shop_odds*2))
    print(odd_res)


def calc_odds():

    # Set of inputs:
    input_set = [
        ("Level_6", "Tier4", 2),
        ("Level_7", "Tier4", 2),
        ("Level_8", "Tier4", 2),
        ]

    # input set
    for input in input_set:
        total_odds, shop_odds = get_odds(input[0], input[1], input[2])
        print("titan lvl : " + input[0] + "\nFinding champ of : "+ input[1])
        print("Gold cost for < 50%: " + str(shop_odds*2))


if __name__ == "__main__":
    for i in range(10):
        print(get_odds("Level_6", "Tier3",i))