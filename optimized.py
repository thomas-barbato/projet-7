from datetime import datetime
import csv


base_action_list: list = [
    ["action-01", 20, 5],
    ["action-02", 30, 10],
    ["action-03", 50, 15],
    ["action-04", 70, 20],
    ["action-05", 60, 17],
    ["action-06", 80, 25],
    ["action-07", 22, 7],
    ["action-08", 26, 11],
    ["action-09", 48, 13],
    ["action-10", 34, 27],
    ["action-11", 42, 17],
    ["action-12", 110, 9],
    ["action-13", 38, 23],
    ["action-14", 14, 1],
    ["action-15", 18, 3],
    ["action-16", 8, 8],
    ["action-17", 4, 12],
    ["action-18", 10, 14],
    ["action-19", 24, 21],
    ["action-20", 114, 18],
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
                    actions[i-1][2]
                    + matrix[i-1][budget-actions[i-1][1]],
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
            matrix[action_index][cost]
            == matrix[action_index - 1][cost - action[1]] + action[2]
        ):
            actions_selected.append(action)
            cost -= action[1]

        action_index -= 1
    gain = round(sum([action[1] * (action[2]/100) for action in actions_selected]), 2)
    cost = sum([action[1] for action in actions_selected])
    actions_list = ", ".join([action[0] for action in actions_selected])
    return (
        f"Gain pour l'investisseur: {gain}€",
        f"Couts pour l'entreprise: {cost}€",
        f"Actions à acheter: {actions_list},",
    )


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


def optimized_with_file(max_cost, actions):
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
                    actions[i-1][2]
                    + matrix[i-1][budget - actions[i-1][1]],
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
            matrix[action_index][cost]
            == matrix[action_index - 1][cost - action[1]] + action[2]
        ):
            actions_selected.append(action)
            cost -= action[1]

        action_index -= 1

    # get last matrix record
    # divided by 100 and round by 2.
    gain = matrix[-1][-1]
    cost = sum([(float(action[1])) for action in actions_selected])
    actions_list = ", ".join([action[0] for action in actions_selected])
    return (
        f"Gain pour l'investisseur: {gain}€",
        f"Couts pour l'entreprise: {cost}€",
        f"Actions à acheter: {actions_list},",
    )


print("\nOPTIMIZED")
start_time = datetime.now()
print(optimized(max_cost=500, actions=base_action_list))
end_time = datetime.now()
print(f"Temp de traitement: {(end_time - start_time).total_seconds()} secondes")

print("\nOPTIMIZED WITH FILE DATASET 1")
start_time = datetime.now()
# max_cost is *100 to go with temporary value
# in from_csv_to_list function
print(
    optimized_with_file(
        max_cost=500, actions=from_csv_to_list('dataset1_Python+P7.csv')
    )
)
end_time = datetime.now()

print(f"Temp de traitement: {(end_time - start_time).total_seconds()} secondes")
start_time = datetime.now()
print("\nOPTIMIZED WITH FILE DATASET 2")
# max_cost is *100 to go with temporary value
# in from_csv_to_list function
print(
    optimized_with_file(
        max_cost=500, actions=from_csv_to_list('dataset2_Python+P7.csv')
    )
)
end_time = datetime.now()
print(f"Temp de traitement: {(end_time - start_time).total_seconds()} secondes")
