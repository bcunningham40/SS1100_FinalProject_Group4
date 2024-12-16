#Check Plus Complete
#Instructions: Inputs are located adjusted in null.txt file. Output Gives total energy for every line in null.txt.


#Function to calculate available power
#Code segment based on ChatGPT request to make python code to calculate power from voltage and current and restrict max values.
def calculate_power(voltage, current, max_voltage=28, max_current=10, max_power=280):
    # Cap voltage and current to system limits
    voltage = min(voltage, max_voltage)
    current = min(current, max_current)

    # Calculate and cap power
    power = min(voltage * current, max_power)
    return power

#Function to calculate total energy available from .txt file inputs and power function.
#Code segment based on ChatGPT prompt make energy availble function from calculate power function and later adapted to take input values from.txt file.

def calculate_energy_from_intervals(intervals):

    total_energy = 0
    for voltage, current, duration in intervals:
        power = calculate_power(voltage, current)
        energy = power * duration
        total_energy += energy
    return total_energy

#Takes inputs form .txt file and gives results individualized for each line.
#Code segment based on ChatGPT prompt read input data from .txt file but display outputs one line at a time.
def read_intervals_from_file(filename):

    all_intervals = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip().replace(' ', '').replace('[', '').replace(']', '')
            line_intervals = []
            tuples = line.split('),')
            for t in tuples:
                t = t.replace('(', '').replace(')', '')
                if t:  # Avoid empty lines
                    v, a, d = map(float, t.split(','))
                    line_intervals.append((v, a, d))
            all_intervals.append(line_intervals)
    return all_intervals


# Main execution
if __name__ == "__main__":
    # Read data from file
    filename = "null.txt"
    all_lines_intervals = read_intervals_from_file(filename)

    # Calculate and print total energy for each line
    for i, intervals in enumerate(all_lines_intervals):
        total_energy = calculate_energy_from_intervals(intervals)
        print(f"Total Energy for Line {i + 1}: {total_energy:.2f} J")
