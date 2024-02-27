from pydantic import BaseModel, validator
from random import randint

class Roll(BaseModel):
    """
    Represents a dice roll with a specified number of sides.

    Attributes:
        num_sides (int): The number of sides on the dice. Must be positive.
        result (int, optional): The result of the dice roll. Defaults to None. Set by calling the roll() method.

    Methods:
        roll(): Rolls the dice and updates the result attribute with the outcome.
    """

    num_sides: int # We've made this mutable... for now!
    result: int = None

    @validator('num_sides')
    def sides_must_be_positive(cls, v):
        """
        Validates that the number of sides (num_sides) is a positive integer.

        Parameters:
            v (int): The number of sides to validate.

        Returns:
            int: The validated number of sides.

        Raises:
            ValueError: If num_sides is not positive.
        """
        if v <= 0:
            raise ValueError('num_sides must be positive')
        return v

    def roll(self):
        """
        Simulates rolling the dice by generating a random number between 1 and num_sides (inclusive).

        Updates the result attribute with the outcome of the roll.
        """
        self.result = randint(1, self.num_sides)


"""
# Example usage
dice = Roll(num_sides=6)
dice.roll()
print(f"Rolled a {dice.num_sides}-sided dice and got: {dice.result}")
"""