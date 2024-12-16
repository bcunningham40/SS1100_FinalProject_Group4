function checkThrustLimits(flow_rate, exhaust_velocity)

%Spacecraft Mass in kg
spacecraftMass = 500

%Input Values to be tested below
flow_rate = 0.05
exhaust_velocity = 2000
time_elapsed = 10

%Equations for Thrust and DeltaV
thrust = flow_rate * exhaust_velocity %Newtons
deltaV = thrust * time_elapsed/spacecraftMass %m/s

%Thruster Maximum limits
THRUST_LIMIT = 100; % Newtons
FLOW_RATE_LIMIT = 0.05; % kg/s
EXHAUST_VELOCITY_LIMIT = 2000; % m/s

    % Check limits for Flow Rate
    if flow_rate > FLOW_RATE_LIMIT
        percentage_exceedance = ((flow_rate - FLOW_RATE_LIMIT) / FLOW_RATE_LIMIT) * 100;
        fprintf('Parameter Exceeding Limit: Flow Rate\n'); %This line was created with ChatGPT
        fprintf('Exceeded by: %.2f%%\n', percentage_exceedance); %This line was created with ChatGPT
    end
    
    % Check limits for Exhaust Velocity
    if exhaust_velocity > EXHAUST_VELOCITY_LIMIT
        percentage_exceedance = ((exhaust_velocity - EXHAUST_VELOCITY_LIMIT) / EXHAUST_VELOCITY_LIMIT) * 100;
        fprintf('Parameter Exceeding Limit: Exhaust Velocity\n'); %This line was created with ChatGPT
        fprintf('Exceeded by: %.2f%%\n', percentage_exceedance); %This line was created with ChatGPT
    end
    
    % Check limits for Thrust
    if thrust > THRUST_LIMIT
        percentage_exceedance = ((thrust - THRUST_LIMIT) / THRUST_LIMIT) * 100;
        fprintf('Parameter Exceeding Limit: Thrust\n'); %This line was created with ChatGPT
        fprintf('Exceeded by: %.2f%%\n', percentage_exceedance); %This line was created with ChatGPT
    end
end
