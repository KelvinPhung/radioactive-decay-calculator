import math
from typing import Dict, Tuple


class RadioactiveDecayCalculator:
    """
    A calculator for radioactive decay using the exponential decay model.
    
    The decay formula is: N(t) = N₀ * (1/2)^(t/T)
    where:
    - N(t) = remaining quantity at time t
    - N₀ = initial amount
    - T = half-life
    - t = elapsed time
    """
    
    def __init__(self):
        pass
    
    def calculate_remaining_quantity(
        self, 
        initial_amount: float, 
        half_life: float, 
        time_elapsed: float
    ) -> Dict:
        """
        Calculate the remaining quantity after radioactive decay.
        
        Args:
            initial_amount: Initial quantity (can be in any unit: grams, moles, etc.)
            half_life: Half-life period (must match the time_elapsed unit)
            time_elapsed: Time that has passed (must match the half_life unit)
        
        Returns:
            Dictionary containing:
            - remaining_quantity: Amount remaining after decay
            - decay_constant: Lambda (λ) value
            - steps: Detailed breakdown of the calculation
        """
        if initial_amount <= 0:
            raise ValueError("Initial amount must be positive")
        if half_life <= 0:
            raise ValueError("Half-life must be positive")
        if time_elapsed < 0:
            raise ValueError("Time elapsed cannot be negative")
        
        # Calculate decay constant: λ = ln(2) / T
        decay_constant = math.log(2) / half_life
        
        # Method 1: Using the half-life formula: N(t) = N₀ * (1/2)^(t/T)
        remaining_qty_method1 = initial_amount * (0.5 ** (time_elapsed / half_life))
        
        # Method 2: Using the exponential decay formula: N(t) = N₀ * e^(-λt)
        remaining_qty_method2 = initial_amount * math.exp(-decay_constant * time_elapsed)
        
        # Calculate percentage remaining
        percentage_remaining = (remaining_qty_method1 / initial_amount) * 100
        
        # Count number of half-lives
        num_half_lives = time_elapsed / half_life
        
        steps = [
            f"Starting Formula: N(t) = N₀ × (1/2)^(t/T)",
            f"",
            f"Where:",
            f"  N₀ (initial amount)    = {initial_amount}",
            f"  T (half-life)          = {half_life}",
            f"  t (time elapsed)       = {time_elapsed}",
            f"",
            f"Step 1: Calculate the exponent",
            f"  t/T = {time_elapsed} / {half_life} = {num_half_lives}",
            f"  (Number of half-lives that have passed)",
            f"",
            f"Step 2: Calculate (1/2)^(t/T)",
            f"  (1/2)^{num_half_lives} = {0.5 ** num_half_lives}",
            f"",
            f"Step 3: Multiply by initial amount",
            f"  N(t) = {initial_amount} × {0.5 ** num_half_lives}",
            f"  N(t) = {remaining_qty_method1}",
            f"",
            f"Results:",
            f"  Remaining Quantity: {remaining_qty_method1:.6f}",
            f"  Amount Decayed:     {initial_amount - remaining_qty_method1:.6f}",
            f"  Percentage Remaining: {percentage_remaining:.2f}%",
            f"",
            f"Decay Constant (λ):",
            f"  λ = ln(2) / T",
            f"  λ = {math.log(2):.6f} / {half_life}",
            f"  λ = {decay_constant:.6f}",
            f"",
            f"Verification using exponential formula: N(t) = N₀ × e^(-λt)",
            f"  N(t) = {initial_amount} × e^(-{decay_constant:.6f} × {time_elapsed})",
            f"  N(t) = {initial_amount} × e^({-decay_constant * time_elapsed:.6f})",
            f"  N(t) = {initial_amount} × {math.exp(-decay_constant * time_elapsed):.6f}",
            f"  N(t) = {remaining_qty_method2:.6f}",
        ]
        
        return {
            "remaining_quantity": remaining_qty_method1,
            "amount_decayed": initial_amount - remaining_qty_method1,
            "percentage_remaining": percentage_remaining,
            "decay_constant": decay_constant,
            "number_of_half_lives": num_half_lives,
            "steps": steps
        }
    
    def calculate_half_life_from_data(
        self,
        initial_amount: float,
        remaining_amount: float,
        time_elapsed: float
    ) -> Dict:
        """
        Solve for half-life given initial amount, remaining amount, and time elapsed.
        
        Rearranging: N(t) = N₀ * (1/2)^(t/T)
        To solve for T: T = t * ln(2) / ln(N₀/N(t))
        
        Args:
            initial_amount: Initial quantity
            remaining_amount: Quantity remaining after decay
            time_elapsed: Time that has passed
        
        Returns:
            Dictionary containing:
            - half_life: Calculated half-life
            - steps: Detailed breakdown of the calculation
        """
        if initial_amount <= 0:
            raise ValueError("Initial amount must be positive")
        if remaining_amount <= 0 or remaining_amount > initial_amount:
            raise ValueError("Remaining amount must be positive and less than initial amount")
        if time_elapsed <= 0:
            raise ValueError("Time elapsed must be positive")
        
        # Using the formula: T = t * ln(2) / ln(N₀/N(t))
        ratio = initial_amount / remaining_amount
        half_life = time_elapsed * math.log(2) / math.log(ratio)
        
        # Verify the calculation
        verification_remaining = initial_amount * (0.5 ** (time_elapsed / half_life))
        
        steps = [
            f"Starting Formula: N(t) = N₀ × (1/2)^(t/T)",
            f"",
            f"Rearranging to solve for T (half-life):",
            f"  N(t) = N₀ × (1/2)^(t/T)",
            f"  N(t) / N₀ = (1/2)^(t/T)",
            f"  log(N(t) / N₀) = (t/T) × log(1/2)",
            f"  log(N(t) / N₀) = (t/T) × log(0.5)",
            f"",
            f"  T = t × log(0.5) / log(N(t) / N₀)",
            f"  T = t × ln(2) / ln(N₀ / N(t))  [Using natural logarithms]",
            f"",
            f"Given Data:",
            f"  N₀ (initial amount)    = {initial_amount}",
            f"  N(t) (remaining amount) = {remaining_amount}",
            f"  t (time elapsed)       = {time_elapsed}",
            f"",
            f"Step 1: Calculate the ratio N₀ / N(t)",
            f"  N₀ / N(t) = {initial_amount} / {remaining_amount}",
            f"  N₀ / N(t) = {ratio:.6f}",
            f"",
            f"Step 2: Calculate ln(N₀ / N(t))",
            f"  ln({ratio:.6f}) = {math.log(ratio):.6f}",
            f"",
            f"Step 3: Calculate ln(2)",
            f"  ln(2) = {math.log(2):.6f}",
            f"",
            f"Step 4: Apply the formula T = t × ln(2) / ln(N₀ / N(t))",
            f"  T = {time_elapsed} × {math.log(2):.6f} / {math.log(ratio):.6f}",
            f"  T = {time_elapsed * math.log(2):.6f} / {math.log(ratio):.6f}",
            f"  T = {half_life:.6f}",
            f"",
            f"Result:",
            f"  Half-life: {half_life:.6f} time units",
            f"",
            f"Verification:",
            f"  Using the calculated half-life to find remaining amount:",
            f"  N(t) = {initial_amount} × (1/2)^({time_elapsed}/{half_life:.6f})",
            f"  N(t) = {initial_amount} × (0.5)^{time_elapsed/half_life:.6f}",
            f"  N(t) = {verification_remaining:.6f}",
            f"  Expected: {remaining_amount}",
            f"  Match: {abs(verification_remaining - remaining_amount) < 1e-6}",
        ]
        
        return {
            "half_life": half_life,
            "verification_remaining": verification_remaining,
            "error": abs(verification_remaining - remaining_amount),
            "steps": steps
        }
    
    def calculate_time_elapsed_from_data(
        self,
        initial_amount: float,
        remaining_amount: float,
        half_life: float
    ) -> Dict:
        """
        Solve for time elapsed given initial amount, remaining amount, and half-life.
        
        Rearranging: N(t) = N₀ * (1/2)^(t/T)
        To solve for t: t = T * ln(N₀/N(t)) / ln(2)
        
        Args:
            initial_amount: Initial quantity
            remaining_amount: Quantity remaining after decay
            half_life: Half-life period
        
        Returns:
            Dictionary containing:
            - time_elapsed: Calculated time elapsed
            - steps: Detailed breakdown of the calculation
        """
        if initial_amount <= 0:
            raise ValueError("Initial amount must be positive")
        if remaining_amount <= 0 or remaining_amount > initial_amount:
            raise ValueError("Remaining amount must be positive and less than initial amount")
        if half_life <= 0:
            raise ValueError("Half-life must be positive")
        
        # Using the formula: t = T * ln(N₀/N(t)) / ln(2)
        ratio = initial_amount / remaining_amount
        time_elapsed = half_life * math.log(ratio) / math.log(2)
        
        # Verify the calculation
        verification_remaining = initial_amount * (0.5 ** (time_elapsed / half_life))
        
        steps = [
            f"Starting Formula: N(t) = N₀ × (1/2)^(t/T)",
            f"",
            f"Rearranging to solve for t (time elapsed):",
            f"  N(t) = N₀ × (1/2)^(t/T)",
            f"  N(t) / N₀ = (1/2)^(t/T)",
            f"  log(N(t) / N₀) = (t/T) × log(1/2)",
            f"  t/T = log(N(t) / N₀) / log(1/2)",
            f"  t = T × log(N(t) / N₀) / log(1/2)",
            f"  t = T × ln(N₀ / N(t)) / ln(2)  [Using natural logarithms]",
            f"",
            f"Given Data:",
            f"  N₀ (initial amount)    = {initial_amount}",
            f"  N(t) (remaining amount) = {remaining_amount}",
            f"  T (half-life)          = {half_life}",
            f"",
            f"Step 1: Calculate the ratio N₀ / N(t)",
            f"  N₀ / N(t) = {initial_amount} / {remaining_amount}",
            f"  N₀ / N(t) = {ratio:.6f}",
            f"",
            f"Step 2: Calculate ln(N₀ / N(t))",
            f"  ln({ratio:.6f}) = {math.log(ratio):.6f}",
            f"",
            f"Step 3: Calculate ln(2)",
            f"  ln(2) = {math.log(2):.6f}",
            f"",
            f"Step 4: Apply the formula t = T × ln(N₀ / N(t)) / ln(2)",
            f"  t = {half_life} × {math.log(ratio):.6f} / {math.log(2):.6f}",
            f"  t = {half_life * math.log(ratio):.6f} / {math.log(2):.6f}",
            f"  t = {time_elapsed:.6f}",
            f"",
            f"Result:",
            f"  Time elapsed: {time_elapsed:.6f} time units",
            f"",
            f"Verification:",
            f"  Using the calculated time to find remaining amount:",
            f"  N(t) = {initial_amount} × (1/2)^({time_elapsed:.6f}/{half_life})",
            f"  N(t) = {initial_amount} × (0.5)^{time_elapsed/half_life:.6f}",
            f"  N(t) = {verification_remaining:.6f}",
            f"  Expected: {remaining_amount}",
            f"  Match: {abs(verification_remaining - remaining_amount) < 1e-6}",
        ]
        
        return {
            "time_elapsed": time_elapsed,
            "verification_remaining": verification_remaining,
            "error": abs(verification_remaining - remaining_amount),
            "steps": steps
        }


def print_section(title: str):
    """Print a formatted section header."""
    print(f"\n{'='*70}")
    print(f"  {title}")
    print(f"{'='*70}\n")


def main():
    """Main function demonstrating the calculator."""
    calculator = RadioactiveDecayCalculator()
    
    # Example 1: Forward calculation (remaining quantity)
    print_section("EXAMPLE 1: Calculate Remaining Quantity")
    print("Scenario: Carbon-14 dating")
    print("  Initial amount: 100 grams")
    print("  Half-life: 5,730 years")
    print("  Time elapsed: 10,000 years\n")
    
    result1 = calculator.calculate_remaining_quantity(
        initial_amount=100,
        half_life=5730,
        time_elapsed=10000
    )
    
    for step in result1["steps"]:
        print(step)
    
    # Example 2: Backward calculation (solve for half-life)
    print_section("EXAMPLE 2: Solve for Half-life from Data")
    print("Scenario: Unknown radioactive element")
    print("  Initial amount: 200 grams")
    print("  Remaining amount: 50 grams")
    print("  Time elapsed: 30 days\n")
    
    result2 = calculator.calculate_half_life_from_data(
        initial_amount=200,
        remaining_amount=50,
        time_elapsed=30
    )
    
    for step in result2["steps"]:
        print(step)
    
    # Example 3: Backward calculation (solve for time elapsed)
    print_section("EXAMPLE 3: Solve for Time Elapsed from Data")
    print("Scenario: Uranium-235 decay")
    print("  Initial amount: 1000 grams")
    print("  Remaining amount: 100 grams")
    print("  Half-life: 704 million years\n")
    
    result3 = calculator.calculate_time_elapsed_from_data(
        initial_amount=1000,
        remaining_amount=100,
        half_life=704_000_000
    )
    
    for step in result3["steps"]:
        print(step)
    
    # Example 4: Interactive mode
    print_section("EXAMPLE 4: Interactive Mode")
    try:
        print("Let's calculate with custom values:\n")
        
        initial = float(input("Enter initial amount: "))
        half_life = float(input("Enter half-life: "))
        time_elapsed = float(input("Enter time elapsed: "))
        
        result4 = calculator.calculate_remaining_quantity(
            initial_amount=initial,
            half_life=half_life,
            time_elapsed=time_elapsed
        )
        
        print("\n")
        for step in result4["steps"]:
            print(step)
        
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
