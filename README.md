# Radioactive Decay Calculator

A comprehensive Python application for calculating radioactive decay using exponential decay models. This calculator supports forward calculations (finding remaining quantity) and backward calculations (solving for half-life or time elapsed).

## Features

✨ **Forward Calculations**
- Calculate remaining quantity after radioactive decay
- Determine amount decayed and percentage remaining
- Compute decay constant (λ)

🔄 **Backward Calculations**
- Solve for half-life given initial amount, remaining amount, and time elapsed
- Solve for time elapsed given initial amount, remaining amount, and half-life

📊 **Detailed Output**
- Step-by-step logarithmic equation breakdowns
- Verification of calculations using alternative formulas
- Multiple calculation methods to ensure accuracy

## Mathematical Formulas

### Primary Decay Formula
```
N(t) = N₀ × (1/2)^(t/T)
```

Where:
- **N(t)** = remaining quantity at time t
- **N₀** = initial amount
- **T** = half-life
- **t** = elapsed time

### Alternative Exponential Formula
```
N(t) = N₀ × e^(-λt)
```

Where:
- **λ** = decay constant = ln(2) / T

### Solving for Half-life
```
T = t × ln(2) / ln(N₀/N(t))
```

### Solving for Time Elapsed
```
t = T × ln(N₀/N(t)) / ln(2)
```

## Installation

No external dependencies required! The calculator uses only Python's built-in `math` module.

```bash
# Clone the repository
git clone https://github.com/KelvinPhung/radioactive-decay-calculator.git
cd radioactive-decay-calculator

# Run the calculator
python radioactive_decay_calculator.py
```

## Usage

### Basic Usage - Forward Calculation

```python
from radioactive_decay_calculator import RadioactiveDecayCalculator

calculator = RadioactiveDecayCalculator()

# Calculate remaining quantity
result = calculator.calculate_remaining_quantity(
    initial_amount=100,      # grams
    half_life=5730,          # years (Carbon-14)
    time_elapsed=10000       # years
)

print(f"Remaining quantity: {result['remaining_quantity']:.2f}")
print(f"Percentage remaining: {result['percentage_remaining']:.2f}%")

# Print detailed steps
for step in result['steps']:
    print(step)
```

### Backward Calculation - Solve for Half-life

```python
# Solve for half-life given observed decay
result = calculator.calculate_half_life_from_data(
    initial_amount=200,      # grams
    remaining_amount=50,     # grams after decay
    time_elapsed=30          # days
)

print(f"Calculated half-life: {result['half_life']:.2f} days")
print(f"Verification error: {result['error']:.6f}")

for step in result['steps']:
    print(step)
```

### Backward Calculation - Solve for Time Elapsed

```python
# Solve for time elapsed given known quantities and half-life
result = calculator.calculate_time_elapsed_from_data(
    initial_amount=1000,     # grams
    remaining_amount=100,    # grams
    half_life=704_000_000    # years (Uranium-235)
)

print(f"Time elapsed: {result['time_elapsed']:.2f} years")

for step in result['steps']:
    print(step)
```

### Interactive Mode

Run the script directly to use the interactive mode:

```bash
python radioactive_decay_calculator.py
```

The script will prompt you for input and show detailed calculations with step-by-step breakdowns.

## Examples

### Example 1: Carbon-14 Dating
```
Initial amount: 100 grams
Half-life: 5,730 years
Time elapsed: 10,000 years

Result: ~29.79 grams remaining (29.79%)
```

### Example 2: Finding Half-life
```
Initial amount: 200 grams
Remaining amount: 50 grams
Time elapsed: 30 days

Result: Half-life ≈ 14.98 days
```

### Example 3: Ancient Uranium Sample
```
Initial amount: 1000 grams
Remaining amount: 100 grams
Half-life: 704 million years

Result: ~2.34 billion years elapsed
```

## Class Methods

### `calculate_remaining_quantity(initial_amount, half_life, time_elapsed)`
Calculates the remaining quantity after radioactive decay.

**Parameters:**
- `initial_amount` (float): Initial quantity in any unit
- `half_life` (float): Half-life period (must match time unit)
- `time_elapsed` (float): Time elapsed (must match half-life unit)

**Returns:** Dictionary containing:
- `remaining_quantity`: Amount left after decay
- `amount_decayed`: Total amount that decayed
- `percentage_remaining`: Percentage of original amount
- `decay_constant`: Lambda (λ) value
- `number_of_half_lives`: How many half-lives passed
- `steps`: Detailed step-by-step calculations

---

### `calculate_half_life_from_data(initial_amount, remaining_amount, time_elapsed)`
Solves for half-life given decay data.

**Parameters:**
- `initial_amount` (float): Starting quantity
- `remaining_amount` (float): Quantity remaining
- `time_elapsed` (float): Time elapsed

**Returns:** Dictionary containing:
- `half_life`: Calculated half-life
- `verification_remaining`: Verification amount
- `error`: Calculation error margin
- `steps`: Detailed derivation steps

---

### `calculate_time_elapsed_from_data(initial_amount, remaining_amount, half_life)`
Solves for time elapsed given decay data.

**Parameters:**
- `initial_amount` (float): Starting quantity
- `remaining_amount` (float): Quantity remaining
- `half_life` (float): Known half-life

**Returns:** Dictionary containing:
- `time_elapsed`: Calculated time elapsed
- `verification_remaining`: Verification amount
- `error`: Calculation error margin
- `steps`: Detailed derivation steps

## Real-World Applications

- 🔬 **Archaeology**: Carbon-14 dating of fossils and artifacts
- ☢️ **Nuclear Science**: Tracking uranium and plutonium decay
- 🏥 **Medical**: Calculating radioactive isotope doses
- 🌍 **Geology**: Dating rocks using radiometric methods
- ♻️ **Environmental**: Monitoring radioactive contamination

## Error Handling

The calculator includes validation for all inputs:

```python
try:
    result = calculator.calculate_remaining_quantity(-100, 5730, 1000)
except ValueError as e:
    print(f"Error: {e}")  # "Initial amount must be positive"
```

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Add new decay calculation methods
- Enhance documentation

## License

This project is open source and available under the MIT License.

## Author

Created by **Kelvin Phung**

## References

- [Radioactive Decay - Wikipedia](https://en.wikipedia.org/wiki/Radioactive_decay)
- [Half-life - Wikipedia](https://en.wikipedia.org/wiki/Half-life)
- [Exponential Decay - Math World](https://mathworld.wolfram.com/ExponentialDecay.html)
