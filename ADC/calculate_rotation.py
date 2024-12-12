#Calculating Roatation Function
#Following based from multiple requests to ChatGPT for function to calculate rotation based on current state.
def calculate_rotation(input_data):

    # Define input
    current_orientation, desired_orientation = input_data

    # Calculate rotation
    rotation_x = desired_orientation[0] - current_orientation[0]
    rotation_y = desired_orientation[1] - current_orientation[1]
    rotation_z = desired_orientation[2] - current_orientation[2]

    # Return the result as a tuple
    return (rotation_x, rotation_y, rotation_z)

#Following based from ChatGPT requesting test to ensure code works after code input.
# To Test:
#input_1 = [(30, 60, 90), (0, 10, 15)]
#result = calculate_rotation(input_1)
#print("Required rotation:", result)
