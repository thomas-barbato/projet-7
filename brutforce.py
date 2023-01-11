import operator
from datetime import datetime
import csv

# import matplotlib.pyplot as plt
# import numpy as np
# import psutil
# import os

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
# only used in sorted by profit.
all_actions_list = [
    {
        "actions": value["actions"],
        "price": value["price"],
        "total": value["price"] + (value["price"] * value["profit_for_2_years"]) / 100,
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


def sorted_by_max(data_list: list = []) -> None:
    current_gain: float = 0.0
    current_cost: int = 0
    action_list: list = []
    max_cost: int = 500
    profits_data: list = [data for data in data_list]

    profits_data.sort(key=operator.itemgetter("price"), reverse=True)

    for data in profits_data:
        if current_cost + data["total"] <= max_cost:
            action_list.append(data["actions"])
            current_cost += data["total"]
            current_gain += data["total"] - data["price"]
    print(
        f"Liste des actions à acheter: {', '.join(action_list)}\n"
        f"Couts pour l'entreprise: {round(current_cost, 2)}€\n"
        f"Gain pour l'investisseur: {round(current_gain, 2)}€\n"
    )


# solutions naïves
print("NAIVE SOLUTION:")
sorted_by_profit(all_actions_list)
# sorted_by_max(all_actions_list)
# print("\n\n")


base_action_list: list = [
    ["action-01", 20, 0.05],
    ["action-02", 30, 0.1],
    ["action-03", 50, 0.15],
    ["action-04", 70, 0.2],
    ["action-05", 60, 0.17],
    ["action-06", 80, 0.25],
    ["action-07", 22, 0.07],
    ["action-08", 26, 0.11],
    ["action-09", 48, 0.13],
    ["action-10", 34, 0.27],
    ["action-11", 42, 0.17],
    ["action-12", 110, 0.09],
    ["action-13", 38, 0.23],
    ["action-14", 14, 0.01],
    ["action-15", 18, 0.03],
    ["action-16", 8, 0.08],
    ["action-17", 4, 0.12],
    ["action-18", 10, 0.14],
    ["action-19", 24, 0.21],
    ["action-20", 114, 0.18],
]


def bruteforce(max_cost, actions, selected_actions: list = []):
    # breakpoint
    # cpu_stats.update({(datetime.now() - start_time).total_seconds(): p.cpu_times()[0]})
    if actions:
        # if there is element in action list
        # call recursively "bruteforce" function
        # we have to call it without the first item (index 0)
        # of the list, that's why we begin with
        # action[1:] and not action[0:]
        action_data, list_value1 = bruteforce(max_cost, actions[1:], selected_actions)
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
                print(action_data2)
                return action_data2, list_value2
        return action_data, list_value1
    # when there is no more element,
    # display results.
    else:
        gain = round(sum([action[1] * action[2] for action in selected_actions]), 2)
        cost = sum([action[1] for action in selected_actions])
        actions_list = ", ".join([action[0] for action in selected_actions])
        return (
            f"Gain pour l'investisseur: {gain}€,"
            f" couts pour l'entreprise: {cost}€. ",
            f"Liste des actions à acheter: {actions_list}.",
        )


# used for lesser item length list
print("\nBRUTEFORCE SOLUTION")
start_time = datetime.now()
# used with matplotlib
# p = psutil.Process(os.getpid())
# cpu_stats = {}
print(bruteforce(max_cost=500, actions=base_action_list))
end_time = datetime.now()
print(f"Temp de traitement: {(end_time - start_time).total_seconds()} secondes")

"""
# matplotlib graph
lists = cpu_stats.items()
x, y = zip(*lists)
plt.plot(x, y)
plt.suptitle('bruteforce.py', fontsize=14, fontweight='bold')
plt.ylabel("time in sec")
plt.xlabel("cpu time")
plt.show()
"""

# Test with bigger number of data.
# So long.
"""
def from_csv_to_list(filename):
    data_set: list = []
    with open(filename, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # skip all altered data row
            if float(row["price"]) > 0.0 and float(row["profit"]) > 0.0:
                data_set.append(
                    # delete "," from all values
                    # row["price"] is * 100 to avoid ","
                    # row["profit"] is now in percent and * 100 to avoid ","
                    (
                        row["name"],
                        round(int(float(row["price"])), 2),
                        int((float(row["price"]) * (float(row["profit"])) / 100)),
                    )
                )
    return data_set
print(bruteforce(max_cost=500, actions=from_csv_to_list("data/dataset1_Python+P7.csv")))
"""
