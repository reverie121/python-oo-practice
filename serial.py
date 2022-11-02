"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__ (self, start):
        self.start_num = start
        self.generate_num = start - 1

    def reset(self):
        """Reinitializes number generation."""
        self.generate_num = self.start_num - 1

    def generate(self):
        """Increments the count by 1 and returns that number."""
        self.generate_num += 1
        return self.generate_num