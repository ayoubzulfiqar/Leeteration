import time

class TrafficLightIntersection:
    """
    Simulates a two-way traffic light controlled intersection (North-South and East-West).
    The lights cycle through a predefined sequence of phases.
    """

    # Define the possible states for a traffic light
    RED = "RED"
    YELLOW = "YELLOW"
    GREEN = "GREEN"

    def __init__(self, green_duration=10, yellow_duration=3):
        """
        Initializes the traffic light intersection.

        Args:
            green_duration (float): The duration in seconds for which a light stays GREEN.
            yellow_duration (float): The duration in seconds for which a light stays YELLOW.
        """
        if not isinstance(green_duration, (int, float)) or green_duration <= 0:
            raise ValueError("Green duration must be a positive number.")
        if not isinstance(yellow_duration, (int, float)) or yellow_duration <= 0:
            raise ValueError("Yellow duration must be a positive number.")

        self._green_duration = float(green_duration)
        self._yellow_duration = float(yellow_duration)

        # Define the sequence of phases for the intersection.
        # Each phase is a tuple: (NS_light_state, EW_light_state, duration_of_phase)
        self._phases = [
            (self.GREEN, self.RED, self._green_duration),  # Phase 0: NS Green, EW Red
            (self.YELLOW, self.RED, self._yellow_duration), # Phase 1: NS Yellow, EW Red
            (self.RED, self.GREEN, self._green_duration),  # Phase 2: NS Red, EW Green
            (self.RED, self.YELLOW, self._yellow_duration)  # Phase 3: NS Red, EW Yellow
        ]

        self._current_phase_index = 0
        self._time_in_current_phase = 0.0

        # Initialize lights to the state of the first phase
        self._ns_light, self._ew_light, _ = self._phases[self._current_phase_index]

    def _set_lights_for_current_phase(self):
        """
        Internal method to set the current light states based on the active phase.
        """
        self._ns_light, self._ew_light, _ = self._phases[self._current_phase_index]

    def update(self, dt):
        """
        Updates the state of the traffic lights after a specified time step `dt`.
        This method handles phase transitions.

        Args:
            dt (float): The time in seconds that has passed since the last update.
        """
        if dt < 0:
            raise ValueError("Time step (dt) cannot be negative.")

        self._time_in_current_phase += dt
        current_phase_duration = self._phases[self._current_phase_index][2]

        # Loop to handle multiple phase transitions if dt is larger than a single phase duration
        while self._time_in_current_phase >= current_phase_duration:
            self._time_in_current_phase -= current_phase_duration # Carry over remaining time
            self._current_phase_index = (self._current_phase_index + 1) % len(self._phases)
            self._set_lights_for_current_phase()
            current_phase_duration = self._phases[self._current_phase_index][2] # Get duration of the new phase

    def get_status(self):
        """
        Returns the current status of the traffic lights.

        Returns:
            dict: A dictionary containing the state of 'NS_Light' and 'EW_Light'.
        """
        return {
            "NS_Light": self._ns_light,
            "EW_Light": self._ew_light
        }

    def run_simulation(self, total_simulation_time, update_interval=1.0):
        """
        Runs a simulation of the traffic light intersection for a specified total time.

        Args:
            total_simulation_time (float): The total time in seconds to run the simulation.
            update_interval (float): The time step in seconds for each update iteration.
                                     This determines how frequently the status is printed.
        """
        print(f"Starting Traffic Light Simulation for {total_simulation_time:.1f} seconds...")
        print(f"Green Duration: {self._green_duration:.1f}s, Yellow Duration: {self._yellow_duration:.1f}s")
        print("-" * 40)
        
        elapsed_time = 0.0
        while elapsed_time < total_simulation_time:
            # Determine the actual time step for the current iteration
            # This ensures we don't simulate past total_simulation_time
            dt = min(update_interval, total_simulation_time - elapsed_time)
            
            if dt <= 0: # Break if no time left to simulate
                break

            self.update(dt)
            status = self.get_status()
            
            # Print the status at each update interval
            print(f"Time: {elapsed_time + dt:.1f}s | NS Light: {status['NS_Light']:<6} | EW Light: {status['EW_Light']:<6}")
            
            elapsed_time += dt

        print("-" * 40)
        print("Simulation Finished.")


if __name__ == "__main__":
    # Example 1: Default traffic light durations
    print("--- Simulation 1: Default Durations ---")
    default_intersection = TrafficLightIntersection()
    default_intersection.run_simulation(total_simulation_time=40, update_interval=1.0)

    print("\n--- Simulation 2: Custom Durations ---")
    # Example 2: Custom traffic light durations
    custom_intersection = TrafficLightIntersection(green_duration=5, yellow_duration=2)
    custom_intersection.run_simulation(total_simulation_time=25, update_interval=0.5)

    print("\n--- Simulation 3: Short Total Time ---")
    # Example 3: A very short simulation to see initial state
    short_intersection = TrafficLightIntersection(green_duration=8, yellow_duration=2)
    short_intersection.run_simulation(total_simulation_time=3, update_interval=1.0)

    print("\n--- Simulation 4: Large Update Interval ---")
    # Example 4: Large update interval to test phase transition logic
    large_step_intersection = TrafficLightIntersection(green_duration=10, yellow_duration=3)
    large_step_intersection.run_simulation(total_simulation_time=30, update_interval=15.0)
