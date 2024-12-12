#Complete code with check and check plus tasking complete
#Code compiled from ChatGPT after numerous prompts based on tasking
from rotate_me import main as rotate_me_main  # Import main function from rotate_me
from calculate_rotation import calculate_rotation  # Import the calculate_rotation function


# Function to read the current state from the current_state.txt file
def read_current_state():
    try:
        with open("current_state.txt", "r") as file:
            state = file.readline().strip()
            current_orientation = tuple(map(float, state.split(",")))
            return current_orientation
    except FileNotFoundError:
        print("current_state.txt not found. Initializing to (0, 0, 0).")
        return (0.0, 0.0, 0.0)  # Default to (0.0, 0.0, 0.0) if file doesn't exist


# Function to write the updated state to the current_state.txt file
def write_current_state(state):
    with open("current_state.txt", "w") as file:
        file.write(",".join(map(lambda x: f"{x:.1f}", state)))


# Main loop to iteratively correct orientation
def correct_orientation(target_orientation):
    # Convert target orientation to floats for comparison
    target_orientation_float = tuple(map(float, target_orientation))

    while True:
        # Get the current state
        current_orientation = read_current_state()

        # Calculate the required rotation
        required_rotation = calculate_rotation([current_orientation, target_orientation_float])

        print(f"Current Orientation: {current_orientation}")
        print(f"Target Orientation: {target_orientation_float}")
        print(f"Required Rotation: {required_rotation}")

        # If no rotation is required, we are done
        if all(abs(current_orientation[i] - target_orientation_float[i]) <= 0.1 for i in range(3)):
            print("Target orientation achieved!")
            break

        # Apply the rotation (introducing randomness as per rotate_me)
        rotate_me_main(required_rotation)

        # Read the updated state from current_state.txt
        updated_orientation = read_current_state()

        # Update the current_state.txt file
        write_current_state(updated_orientation)


# Define the target orientation (can be modified as needed)
target_orientation = (3, 30, 300)  # Replace with your desired target orientation as integers

# Run the correction process
if __name__ == "__main__":
    correct_orientation(target_orientation)
