from Car import Car


class Minivan(Car):
    def __init__(self, details):
        """
        Initializes minivan details.
        details: Dictionary containing minivan details.
        """

        super().__init__(details)
        self.has_sliding_doors = details.get("has_sliding_doors", False)
        self.sliding_doors_status = "closed"

    def open_sliding_doors(self):
        """
        Open the sliding doors.
        """

        if self.has_sliding_doors:
            if self.sliding_doors_status == "closed":
                print("Sliding doors opened.")
                self.sliding_doors_status = "opened"
            else:
                print("Sliding doors are already opened.")
        else:
            print("This minivan does not have sliding doors.")

    def close_sliding_doors(self):
        """
        Close the sliding doors.
        """

        if self.has_sliding_doors:
            if self.sliding_doors_status == "opened":
                print("Sliding doors closed.")
                self.sliding_doors_status = "closed"
            else:
                print("Sliding doors are already closed.")
        else:
            print("This minivan does not have sliding doors.")
