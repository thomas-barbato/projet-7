from datetime import datetime
import csv

base_action_list: list = [
    ["action-01", 20, (20 * 5) / 100],
    ["action-02", 30, (30 * 10) / 100],
    ["action-03", 50, (50 * 15) / 100],
    ["action-04", 70, (70 * 20) / 100],
    ["action-05", 60, (60 * 17) / 100],
    ["action-06", 80, (80 * 25) / 100],
    ["action-07", 22, (22 * 7) / 100],
    ["action-08", 26, (26 * 11) / 100],
    ["action-09", 48, (48 * 13) / 100],
    ["action-10", 34, (34 * 27) / 100],
    ["action-11", 42, (42 * 17) / 100],
    ["action-12", 110, (110 * 9) / 100],
    ["action-13", 38, (38 * 23) / 100],
    ["action-14", 14, (14 * 1) / 100],
    ["action-15", 18, (18 * 3) / 100],
    ["action-16", 8, (8 * 8) / 100],
    ["action-17", 4, (4 * 12) / 100],
    ["action-18", 10, (10 * 14) / 100],
    ["action-19", 24, (24 * 21) / 100],
    ["action-20", 114, (114 * 18) / 100],
]


def optimized(max_cost, actions):
    # define matrix and set all index value to 0.
    # use len + 1 to count stage 0.
    matrix: list = [
        [0 for _ in range(max_cost + 1)] for _ in range(len(actions) + 1)
    ]

    # browse actions
    for i in range(1, len(actions) + 1):
        # for each action, browse budget
        for budget in range(1, max_cost + 1):
            # if action cost is lower
            # than budget then
            # get the max between
            # previous action and
            # actual action + optimized choice
            # - cost of the previous action
            if actions[i-1][1] <= budget:

                matrix[i][budget] = max(
                    actions[i-1][2] + matrix[i-1][budget-actions[i-1][1]],
                    matrix[i-1][budget],
                )
            # else keep the previous choice.
            else:
                matrix[i][budget] = matrix[i-1][budget]

    cost: float = max_cost
    action_index: int = len(actions)
    actions_selected: list = []

    while cost >= 0 and action_index >= 0:
        # get last action in actions
        # same as first loop but reversed.
        action = actions[action_index - 1]

        if (
            matrix[action_index][cost] == matrix[action_index - 1][cost - action[1]] + action[2]
        ):
            actions_selected.append(action)
            cost -= action[1]

        action_index -= 1

    return  actions_selected


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
                        round(int(float(row["price"])),2),
                        int(
                            (float(row["price"]) * (float(row["profit"])) / 100)

                        ),
                    )
                )
    return data_set


print("\nOPTIMIZED")
start_time = datetime.now()
actions = optimized(max_cost=500, actions=base_action_list)
end_time = datetime.now()

cost = round(sum([action[1] for action in actions]), 2)
gain = round(sum([action[2] for action in actions]), 2)

print(f"Liste des actions à acheter: {', '.join([action[0] for action in actions])}")
print(f"Cout total : {cost}€")
print(f"Benefice de : {gain}€")
print(f"Temp de traitement: {(end_time - start_time).total_seconds()} secondes")
print("=" * 25)

"""
print("\nOPTIMIZED WITH FILE DATASET 1")
start_time = datetime.now()
dataset1_action = optimized(max_cost=500, actions=from_csv_to_list('dataset1_Python+P7.csv'))
end_time = datetime.now()

dataset1_cost = round(sum([action[1] for action in dataset1_action]), 2)
dataset1_gain = round(sum([action[2] for action in dataset1_action]), 2)


print(f"Liste des actions à acheter: {', '.join([data[0] for data in dataset1_action])}")
print(f"Cout total : {dataset1_cost}€")
print(f"Benefice de : {dataset1_gain}€")
print(f"Temp de traitement: {(end_time - start_time).total_seconds()} secondes")
print("=" * 25)

print("\nOPTIMIZED WITH FILE DATASET 2")
start_time = datetime.now()
dataset2_action = optimized(max_cost=500, actions=from_csv_to_list('dataset2_Python+P7.csv'))
end_time = datetime.now()

dataset2_cost = round(sum([action[1] for action in dataset2_action]), 2)
dataset2_gain = round(sum([action[2] for action in dataset2_action]), 2)

print(f"Liste des actions à acheter: {', '.join([action[0] for action in dataset2_action])}")
print(f"Cout total : {dataset2_cost}€")
print(f"Benefice de : {dataset2_gain}€")
print(f"Temp de traitement: {(end_time - start_time).total_seconds()} secondes")
"""