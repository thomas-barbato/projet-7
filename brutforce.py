import operator

actions: list = [
    {"actions": "Action-1", "price": 20, "profit_for_2_years": 5},
    {"actions": "Action-2", "price": 30, "profit_for_2_years": 10},
    {"actions": "Action-3", "price": 50, "profit_for_2_years": 15},
    {"actions": "Action-4", "price": 70, "profit_for_2_years": 20},
    {"actions": "Action-5", "price": 60, "profit_for_2_years": 17},
    {"actions": "Action-6", "price": 80, "profit_for_2_years": 25},
    {"actions": "Action-7", "price": 22, "profit_for_2_years": 7},
    {"actions": "Action-8", "price": 26, "profit_for_2_years": 11},
    {"actions": "Action-9", "price": 48, "profit_for_2_years": 13},
    {"actions": "Action-10", "price": 34, "profit_for_2_years": 27},
    {"actions": "Action-11", "price": 42, "profit_for_2_years": 17},
    {"actions": "Action-12", "price": 110, "profit_for_2_years": 9},
    {"actions": "Action-13", "price": 38, "profit_for_2_years": 23},
    {"actions": "Action-14", "price": 14, "profit_for_2_years": 1},
    {"actions": "Action-15", "price": 18, "profit_for_2_years": 3},
    {"actions": "Action-16", "price": 8, "profit_for_2_years": 8},
    {"actions": "Action-17", "price": 4, "profit_for_2_years": 12},
    {"actions": "Action-18", "price": 10, "profit_for_2_years": 14},
    {"actions": "Action-19", "price": 24, "profit_for_2_years": 21},
    {"actions": "Action-20", "price": 114, "profit_for_2_years": 18},
]

# get results values.
all_actions_list = [
    {
        "actions": value["actions"],
        "price": value["price"],
        "total": value["price"]
        + ((value["price"] * value["profit_for_2_years"]) / 100),
    }
    for value in actions
]


def get_list(data_list: list, sort_by: str = "") -> list:
    # if sort_by is defined, set sort for data_list
    # else return unchanged list
    temp_list = [data for data in data_list]
    match sort_by:
        case "min":
            temp_list.sort(key=operator.itemgetter("total"), reverse=False)
        case "max":
            temp_list.sort(key=operator.itemgetter("total"), reverse=True)
    return temp_list


def get_sorted_results(data_list: list, sort_by: str = "") -> None:
    current_gain = 0
    current_cost = 0
    action_list = []
    max_cost = 500

    current_action_list = get_list(data_list, sort_by)

    for action in current_action_list:
        if (action["total"] + current_cost) <= max_cost:
            action_list.append(action["actions"])
            current_cost += action["total"]
            current_gain += action["total"] - action["price"]
    print(
        f"Liste des actions à acheter: {action_list}\n"
        f"Couts pour l'entreprise: {round(current_cost, 2)}€\n"
        f"Gain pour l'investisseur: {round(current_gain, 2)}€\n"
    )


def sorted_by_profit(data_list: list = []) -> None:
    current_gain = 0
    current_cost = 0
    action_list = []
    max_cost = 500
    profits_data = [data for data in data_list]

    for data in profits_data:
        data.update({"profit": round((data["total"] - data["price"]), 2)})

    profits_data.sort(key=operator.itemgetter("profit"), reverse=True)

    for data in profits_data:
        if current_cost + data["total"] <= max_cost:
            action_list.append(data)
            current_cost += data["total"]
            current_gain += data["profit"]
    print(
        f"Liste des actions à acheter: {[data['actions'] for data in profits_data]}\n"
        f"Couts pour l'entreprise: {round(current_cost, 2)}€\n"
        f"Gain pour l'investisseur: {round(current_gain, 2)}€\n"
    )

# same result has get_sorted_results(no_sort_parameter)
"""

def bruteforced_results(data_list: list, data_used: list = [], current_gain: float = 0.0):
    current_cost = sum([element["total"] for element in data_used]) if len(data_used) > 0 else 0
    current_gain = current_gain if current_gain > 0.0 else 0.0
    max_cost = 500.0
    for i, action in enumerate(data_list):
        cost_sum = current_cost + action["total"]
        if cost_sum < max_cost:
            data_used.append(action)
            current_gain += action["total"] - action["price"]
            del data_list[i]
            return bruteforced_results(data_list, data_used, current_gain)
    else:
        print(
            f"Liste des actions à acheter: {[data['actions'] for data in data_used]}\n"
            f"Couts pour l'entreprise: {round(current_cost, 2)}€\n"
            f"Gain pour l'investisseur: {round(current_gain, 2)}€\n"
        )
"""

get_sorted_results(all_actions_list, "max")
get_sorted_results(all_actions_list, "min")
get_sorted_results(all_actions_list)
sorted_by_profit(all_actions_list)
#bruteforced_results(all_actions_list)
