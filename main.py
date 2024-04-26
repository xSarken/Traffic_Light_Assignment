import pandas as pd

file_path = "data.txt"

TRAFFIC_LIGHT_DISABLED = 0
TRAFFIC_LIGHT_ENABLED = 1

RED = "Red"
GREEN = "Green"
YELLOW = "Yellow"

def read_all_data():
    df = pd.read_csv(file_path)
    records = df.to_dict(orient='records')
    return records


def find_total_occurrences_based_on_color(data):
    red_total = 0
    yellow_total = 0
    green_total = 0

    for entry in data:
        if entry[RED] == TRAFFIC_LIGHT_ENABLED:
            red_total += 1
        if entry[YELLOW] == TRAFFIC_LIGHT_ENABLED:
            yellow_total += 1
        if entry[GREEN] == TRAFFIC_LIGHT_ENABLED:
            green_total += 1
        # Assumption was made that even if there is a mistake in the data, we still add to the total times activated, otherwise elif would be used.
    return print(f"Red = {red_total}, Yellow = {yellow_total}, Green = {green_total}")


def color_active_time(data):
    red_time_total = 0
    yellow_time_total = 0
    green_time_total = 0
    for entry in data:
        if entry[RED] == TRAFFIC_LIGHT_ENABLED:
            red_time_total += entry["TimeActive"]
        if entry[YELLOW] == TRAFFIC_LIGHT_ENABLED:
            yellow_time_total += entry["TimeActive"]
        if entry[GREEN] == TRAFFIC_LIGHT_ENABLED:
            green_time_total += entry["TimeActive"]
        # Assumption was made that even if there is a mistake in the data, we still add to the total time active, otherwise elif would be used.
    return print(f"Red = {red_time_total} seconds, Yellow = {yellow_time_total} seconds, Green = {green_time_total} seconds")


def green_active_at_time(data):
    active_times = []
    for entry in data:
        if entry[GREEN] == TRAFFIC_LIGHT_ENABLED:
            active_times.append(entry["Time"])
    return print(active_times)


def completed_cycles(data):
    cycle_timer = 0
    complete_cycles = 0

    for entry in data:
        if entry[RED] == TRAFFIC_LIGHT_ENABLED:
            if cycle_timer == 4:
                complete_cycles += 1
            cycle_timer = 1
        elif entry[YELLOW] == TRAFFIC_LIGHT_ENABLED and (cycle_timer == 1 or cycle_timer == 3):
            cycle_timer += 1
        elif entry[GREEN] == TRAFFIC_LIGHT_ENABLED and cycle_timer == 2:
            cycle_timer += 1
        else:
            cycle_timer = 0
    return print(f"Completed cycles {complete_cycles}")


def find_mistakes(data):
    mistake_count = 0
    for entry in data:
        red, yellow, green = entry[RED], entry[YELLOW], entry[GREEN]
        if is_mistake(red, yellow, green):
            mistake_count += 1

    return print(f"Mistakes {mistake_count}")


def is_mistake(red, yellow, green):
    return red == yellow == green or (red + yellow + green == 2)


data = read_all_data()
find_total_occurrences_based_on_color(data)
color_active_time(data)
green_active_at_time(data)
completed_cycles(data)
find_mistakes(data)
