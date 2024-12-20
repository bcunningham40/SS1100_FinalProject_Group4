function [deltaV, exceedances] = calculateAndCheckThrustLimits(mass, thrustParams)
    % Inputs:
    % mass: Spacecraft mass in kg
    % thrustParams: A struct array with fields:
    %   - flow_rate (kg/s)
    %   - exhaust_velocity (m/s)
    %   - time_elapsed (s)
    %   - direction (3-element array for thrust direction in X, Y, Z)

    % Initialize velocity change vector
    deltaV = [0, 0, 0]; % X, Y, Z

    % Thruster Maximum limits
    THRUST_LIMIT = 100; % Newtons
    FLOW_RATE_LIMIT = 0.05; % kg/s
    EXHAUST_VELOCITY_LIMIT = 2000; % m/s

    % Initialize exceedances log
    exceedances = [];

    for i = 1:length(thrustParams)
        % Extract thruster parameters
        flow_rate = thrustParams(i).flow_rate;
        exhaust_velocity = thrustParams(i).exhaust_velocity;
        time_elapsed = thrustParams(i).time_elapsed;
        direction = thrustParams(i).direction;

        % Calculate thrust magnitude
        thrust = flow_rate * exhaust_velocity;

        % Calculate deltaV for this thruster in each direction
        thrust_deltaV = (thrust * time_elapsed / mass) * direction;

        % Accumulate velocity change
        deltaV = deltaV + thrust_deltaV;

        % Check for limit exceedances and log
        if flow_rate > FLOW_RATE_LIMIT
            percentage_exceedance = ((flow_rate - FLOW_RATE_LIMIT) / FLOW_RATE_LIMIT) * 100;
            exceedances = [exceedances; struct('parameter', 'Flow Rate', 'thruster', i, 'exceedance', percentage_exceedance)];
        end

        if exhaust_velocity > EXHAUST_VELOCITY_LIMIT
            percentage_exceedance = ((exhaust_velocity - EXHAUST_VELOCITY_LIMIT) / EXHAUST_VELOCITY_LIMIT) * 100;
            exceedances = [exceedances; struct('parameter', 'Exhaust Velocity', 'thruster', i, 'exceedance', percentage_exceedance)];
        end

        if thrust > THRUST_LIMIT
            percentage_exceedance = ((thrust - THRUST_LIMIT) / THRUST_LIMIT) * 100;
            exceedances = [exceedances; struct('parameter', 'Thrust', 'thruster', i, 'exceedance', percentage_exceedance)];
        end
    end
end

% --- Test Case ---

% Spacecraft mass in kg
spacecraftMass = 500;

% Thruster parameters
thrustParams = [
    struct('flow_rate', 0.04, 'exhaust_velocity', 2000, 'time_elapsed', 15, 'direction', [1, 0, 0]), % Thruster 1
    struct('flow_rate', 0.03, 'exhaust_velocity', 2000, 'time_elapsed', 4, 'direction', [0, 1, 0]),  % Thruster 2
    struct('flow_rate', 0.01, 'exhaust_velocity', 2000, 'time_elapsed', 3, 'direction', [0, 0, 1])   % Thruster 3
];

% Perform calculation and check limits
[deltaV, exceedances] = calculateAndCheckThrustLimits(spacecraftMass, thrustParams);

% Display the results
fprintf('Change in Velocity (Delta V):\n');
fprintf('X-axis: %.2f m/s\n', deltaV(1));
fprintf('Y-axis: %.2f m/s\n', deltaV(2));
fprintf('Z-axis: %.2f m/s\n', deltaV(3));

if ~isempty(exceedances)
    fprintf('\nExceedance Report:\n');
    for i = 1:length(exceedances)
        fprintf('Thruster %d - %s exceeded by %.2f%%\n', ...
            exceedances(i).thruster, exceedances(i).parameter, exceedances(i).exceedance);
    end
else
    fprintf('\nNo parameter exceedances detected.\n');
end
