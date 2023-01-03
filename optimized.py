from datetime import datetime
import csv


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
                    # row["profit"] is now in percent
                    (
                        row["name"],
                        int(float(row["price"]) * 100),
                        int(
                            (float(row["price"]) * (float(row["profit"])) / 100)
                            * 100
                        ),
                    )
                )
    return data_set


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
            if actions[i - 1][1] <= budget:
                matrix[i][budget] = max(
                    actions[i - 1][2]
                    + matrix[i - 1][budget - actions[i - 1][1]],
                    matrix[i - 1][budget],
                )
            # else keep the previous choice.
            else:
                matrix[i][budget] = matrix[i - 1][budget]

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

    gain = sum([action[1] * action[2] for action in actions_selected])
    cost = sum([action[1] for action in actions_selected])
    actions_list = ", ".join([action[0] for action in actions_selected])
    return (
        f"Gain pour l'investisseur: {gain}€",
        f"Couts pour l'entreprise: {cost}€",
        f"Actions à acheter: {actions_list},",
    )


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
            if actions[i - 1][1] <= budget:
                matrix[i][budget] = max(
                    actions[i - 1][2]
                    + matrix[i - 1][budget - actions[i - 1][1]],
                    matrix[i - 1][budget],
                )
            # else keep the previous choice.
            else:
                matrix[i][budget] = matrix[i - 1][budget]

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
    gain = matrix[-1][-1] / 100
    cost = sum([(float(action[1]) / 100) for action in actions_selected])
    actions_list = ", ".join([action[0] for action in actions_selected])
    return (
        f"Gain pour l'investisseur: {gain}€",
        f"Couts pour l'entreprise: {cost}€",
        f"Actions à acheter: {actions_list},",
    )


print("\nOPTIMIZED")
start_time = datetime.now()
print(optimized(max_cost=500, actions=actions_tuple_list))
end_time = datetime.now()
start_time = datetime.now()
print("\nOPTIMIZED WITH FILE")
# max_cost is *100 to go with temporary value
# in from_csv_to_list function
print(
    optimized_with_file(
        max_cost=50000, actions=from_csv_to_list("dataset1_Python+P7.csv")
    )
)
end_time = datetime.now()
print(f"Temp de traitement: {(end_time - start_time).total_seconds()} secondes")
