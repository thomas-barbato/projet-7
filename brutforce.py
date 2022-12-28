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


def sorted_by_profit(data_list: list = []) -> None:
    current_gain: float = 0.0
    current_cost: int = 0
    action_list: list = []
    max_cost: int = 500
    profits_data: list = [data for data in data_list]

    for data in profits_data:
        data.update({"profit": round((data["total"] - data["price"]), 2)})

    profits_data.sort(key=operator.itemgetter("profit"), reverse=True)

    for data in profits_data:
        if current_cost + data["total"] <= max_cost:
            action_list.append(data["actions"])
            current_cost += data["total"]
            current_gain += data["profit"]
    print(
        f"Liste des actions à acheter: {', '.join(action_list)}\n"
        f"Couts pour l'entreprise: {round(current_cost, 2)}€\n"
        f"Gain pour l'investisseur: {round(current_gain, 2)}€\n"
    )


# solutions naïves
sorted_by_profit(all_actions_list)


actions_tuple_list: list = [
    ("action-1", 20, 0.05),
    ("Action-2", 30, 0.1),
    ("Action-3", 50, 0.15),
    ("Action-4", 70, 0.2),
    ("Action-5", 60, 0.17),
    ("Action-6", 80, 0.25),
    ("Action-7", 22, 0.07),
    ("Action-8", 26, 0.11),
    ("Action-9", 48, 0.13),
    ("Action-10", 34, 0.27),
    ("Action-11", 42, 0.17),
    ("Action-12", 110, 0.09),
    ("Action-13", 38, 0.23),
    ("Action-14", 14, 0.01),
    ("Action-15", 18, 0.03),
    ("Action-16", 8, 0.08),
    ("Action-17", 4, 0.12),
    ("Action-18", 10, 0.14),
    ("Action-19", 24, 0.21),
    ("Action-20", 114, 0.18),
]


def bruteforce(max_cost, actions, selected_actions: list = []):
    # breakpoint
    if actions:
        # if there is element in action list
        # call recursively "bruteforce" function
        # we have to call it without the first item
        # of the list, that's why we begin with
        # action[1:] and not action[0:]
        action_data, list_value1 = bruteforce(
            max_cost, actions[1:], selected_actions
        )
        # take the first element of action list
        selected_action = actions[0]
        # if original action price is
        # lower than max_cost (500 per default)
        if selected_action[1] <= max_cost:
            # then call bruteforce function and
            # decrement selected_action[1] value from
            # max_cost (eg : 500 - 20)
            # and we add selected_action (as a list element)
            # in selected_actions
            action_data2, list_value2 = bruteforce(
                max_cost - selected_action[1],
                actions[1:],
                selected_actions + [selected_action],
            )
            # check best solution
            if action_data < action_data2:
                return action_data2, list_value2
        return action_data, list_value1
    # when there is no more element,
    # display results.
    else:
        return (
            f"Gain pour l'investisseur: {round(sum([(i[1] * i[2]) for i in selected_actions]), 2)}€, "
            f"couts pour l'entreprise: {round(sum([i[1] for i in selected_actions]),2)}€. ",
            f"Liste des actions à acheter: {', '.join([i[0]for i in selected_actions])}.",
        )


# used for lesser item length list
print(bruteforce(max_cost=500, actions=actions_tuple_list))


# optimised solution
def dynamic(max_cost, actions):
    # define matrix and set all index to 0.
    # use len + 1 to count stage 0.
    matrix: list = [
        [0 for _ in range(max_cost + 1)] for _ in range(len(actions) + 1)
    ]

    for i in range(1, len(actions) + 1):
        for w in range(1, max_cost + 1):
            if actions[i-1][1] <= w:
                matrix[i][w] = max(actions[i-1][2] + matrix[i-1][w-actions[i-1][1]], matrix[i-1][w])
            else:
                matrix[i][w] = matrix[i-1][w]

    cost: int = max_cost
    action_index: int = len(actions)
    actions_selected: list = []

    while cost >= 0 and action_index >= 0:
        action = actions[action_index-1]
        if matrix[action_index][cost] == matrix[action_index-1][cost-action[1]] + action[2]:
            actions_selected.append(action)
            cost -= action[1]
        action_index -= 1

    return (
        f"Actions à acheter: {', '.join([action[0] for action in actions_selected])},",
        f"Gain pour l'investisseur: {sum([ action[1]*action[2] for action in actions_selected])}€",
        f"Couts pour l'entreprise: {sum([ action[1] for action in actions_selected])}€"
    )

print("\n")
print(dynamic(max_cost=500, actions=actions_tuple_list))
