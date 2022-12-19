import operator

actions: list = [
    {"Actions": "Action-1", "price": 20, "profit_for_2_years": 5},
    {"Actions": "Action-2", "price": 30, "profit_for_2_years": 10},
    {"Actions": "Action-3", "price": 50, "profit_for_2_years": 15},
    {"Actions": "Action-4", "price": 70, "profit_for_2_years": 20},
    {"Actions": "Action-5", "price": 60, "profit_for_2_years": 17},
    {"Actions": "Action-6", "price": 80, "profit_for_2_years": 25},
    {"Actions": "Action-7", "price": 22, "profit_for_2_years": 7},
    {"Actions": "Action-8", "price": 26, "profit_for_2_years": 11},
    {"Actions": "Action-9", "price": 48, "profit_for_2_years": 13},
    {"Actions": "Action-10", "price": 34, "profit_for_2_years": 27},
    {"Actions": "Action-11", "price": 42, "profit_for_2_years": 17},
    {"Actions": "Action-12", "price": 110, "profit_for_2_years": 9},
    {"Actions": "Action-13", "price": 38, "profit_for_2_years": 23},
    {"Actions": "Action-14", "price": 14, "profit_for_2_years": 1},
    {"Actions": "Action-15", "price": 18, "profit_for_2_years": 3},
    {"Actions": "Action-16", "price": 8, "profit_for_2_years": 8},
    {"Actions": "Action-17", "price": 4, "profit_for_2_years": 12},
    {"Actions": "Action-18", "price": 10, "profit_for_2_years": 14},
    {"Actions": "Action-19", "price": 24, "profit_for_2_years": 21},
    {"Actions": "Action-20", "price": 114, "profit_for_2_years": 18},
]

# get results values.
actions_total = [
    {
        "Actions": value["Actions"],
        "total": value["price"] + ((value["price"] * value["profit_for_2_years"]) / 100),
    }
    for value in actions
]

# sort by total , from hightest to lowest.
actions_total.sort(key=operator.itemgetter("total"), reverse=True)

print(actions_total)
