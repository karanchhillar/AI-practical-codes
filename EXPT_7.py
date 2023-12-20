def calculate_mean(data):
    return sum(data) / len(data)

def calculate_mode(data):
    # Calculate the frequency of each element
    frequency_dict = {}
    for value in data:
        frequency_dict[value] = frequency_dict.get(value, 0) + 1
    
    # Find the mode(s)
    max_frequency = max(frequency_dict.values())
    mode = [key for key, value in frequency_dict.items() if value == max_frequency]
    
    return mode

def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    
    # If the number of elements is odd, return the middle element
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        # If the number of elements is even, return the average of the middle two elements
        middle1 = sorted_data[(n // 2) - 1]
        middle2 = sorted_data[n // 2]
        return (middle1 + middle2) / 2

def calculate_standard_deviation(data):
    mean_value = calculate_mean(data)
    squared_diff = [(x - mean_value) ** 2 for x in data]
    variance = sum(squared_diff) / len(data)
    std_deviation = variance ** 0.5
    return std_deviation

# Example usage:
data = [10, 12, 14, 18, 20, 23, 25, 28, 31, 33, 35]

mean_result = calculate_mean(data)
mode_result = calculate_mode(data)
median_result = calculate_median(data)
std_deviation_result = calculate_standard_deviation(data)

print("Mean:", mean_result)
print("Mode:", mode_result)
print("Median:", median_result)
print("Standard Deviation:", std_deviation_result)
