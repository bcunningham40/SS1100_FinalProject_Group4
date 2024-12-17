# %% Dictionary for System Codes, Commands, and Parameter Range
command_dict = {

    "Reaction Control Subsystem": {
        "Code": "RCS",
        "Commands": {"CMD01":['THRUST_X', range(0,60)],
                     "CMD02":['THRUST_Y', range(0,60)],
                     "CMD03":['THRUST_Z', range(0,60)],
                     "CMD04":['SAFE_MODE', {0, 1}]}
    },
    "Thermal Control Subsystem": {
        "Code": "TCS",
        "Commands": {"CMD01":['HEATER_ON', {0, 1}],
                     "CMD02":['HEATER_OFF', {0, 1}],
                     "CMD03":['VENT_OPEN_RADIATOR', {0, 1}],
                     "CMD04":['TEMP_SETPOINT', range(-30,60)]}
    },
    "Attitude Control Subsystem": {
        "Code": "ACS",
        "Commands": {"CMD01":['ROTATE_X', range(-360,360)],
                     "CMD02":['ROTATE_Y', range(-360,360)],
                     "CMD03":['ROTATE_Z', range(-360,360)],
                     "CMD04":['SAFE_MODE', {0, 1}]}
    },
    "Command & Data Handling": {
        "Code": "CDH",
        "Commands": {"CMD01":['TRANSMIT_HIGH', {0, 1}],
                     "CMD02":['TRANSMIT_LOW', {0, 1}],
                     "CMD03":['RECEIVE_MODE',{0, 1}],
                     "CMD04":['SAFE_MODE', {0,1}]}
    },
    "Telemetry, Tracking, & Command": {
        "Code": "TTC",
        "Commands": {"CMD01":['TRANSMIT_MODE', {0,1}],
                     "CMD02":['RECEIVE_MODE', {0,1}],
                     "CMD03":['TRACKING_MODE', {0,1}],
                     "CMD04":['SAFE_MODE', {0,1}]}
    },
    "Electrical Power Subsystem": {
        "Code": "EPS",
        "Commands": {"CMD01":['BATTERY_CHARGE_MODE', {0,1}],
                     "CMD02":['POWER_ON_MODULE', {0,1,2,3,4}],
                     "CMD03":['POWER_OFF_MODULE', {0,1,2,3,4}],
                     "CMD04":['VOLTAGE_SETPOINT', range(0,120)]}
    },
    "Payload System 1": {
        "Code": "PL1",
        "Commands": {"CMD01":['START_DATA_ACQUISITION', {0,1}],
                     "CMD02":['STOP_DATA_ACQUISITION', {0,1}],
                     "CMD03":['CALIBRATE_SENSOR', {0,1}],
                     "CMD04":['SAFE_MODE', {0,1}]}
    },
    "Payload System 2": {
        "Code": "PL2",
        "Commands": {"CMD01":['START_DATA_ACQUISITION', {0,1}],
                     "CMD02":['STOP_DATA_ACQUISITION', {0,1}],
                     "CMD03":['CALIBRATE_SENSOR', {0,1}],
                     "CMD04":['SAFE_MODE', {0,1}]}
    }
}
# %%
import sys
input_command = ('ACS:CMD04:1') # Input command entry
x = input_command.index(':') # Indexing the first occurance of ':'
y = input_command[x + 1:].index(":") + x + 1 #Indexing the second occurance of ':'
code_in = input_command[0:x] # Splice subsystem code using first occurance of ':'
command_in = input_command[x + 1:y] # Splice command code using first and second occurance of ':'
parameter_in = input_command[y + 1:] # Splice paraemeter using second occurance of ':'
command_elements = (code_in,command_in,parameter_in) # Create command elements list
try:
    parameter_in = int(parameter_in)  # Convert parameter to an integer
except:
    print("Parameter input must be numeric.")
    sys.exit()
# The following function was adapted from suggestions generated by ChatGPT prompt:
# 'How to match an item in a list with an item in a nested dictionary in python'
def process_command(command_elements, command_dict):
    code_in, command_in, parameter_in = command_elements
    parameter_in = int(parameter_in)  # Convert parameter to an integer if needed
    
    # Iterate through subsystems in the dictionary
    for subsystem, details in command_dict.items():
        if details['Code'] == code_in:  # Match system code
            commands = details['Commands']
            if command_in in commands:  # Match command
                description, param_range = commands[command_in]
                
                # Validate the parameter
                if (isinstance(param_range, range) and parameter_in in param_range) or \
                   (isinstance(param_range, set) and parameter_in in param_range):
                    return f"{subsystem} {description} executed with parameter {parameter_in}" # Correct action taken
                else:
                    return f"Invalid parameter '{parameter_in}' for {description} in {subsystem}." # Parameter error detection
            else:
                return f"No match found for command '{command_in}' in {subsystem}." # Command code error detection
    return f"No match found for subsystem code '{code_in}'." # Subsystem code error detection
result = process_command(command_elements, command_dict)
print(result)