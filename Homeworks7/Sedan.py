from Car import Car


class Sedan(Car):
    def __init__(self, details):
        """
        Initializes sedan details.

        details: Dictionary containing sedan details.
        """

        super().__init__(details)
        self.trunk_capacity = details.get("trunk_capacity", 0)
        self.trunk_status = "closed"

    def open_trunk(self):
        """
        Open the trunk.
        """

        if self.trunk_status == "closed":
            print("Trunk opened.")
            self.trunk_status = "opened"
        else:
            print("Trunk is already opened.")

    def close_trunk(self):
        """
        Close the trunk.
        """

        if self.trunk_status == "opened":
            print("Trunk closed.")
            self.trunk_status = "closed"
        else:
            print("Trunk is already closed.")
