class HotBeverage:
    """Base class for all hot beverages."""

    price = 0.30
    name = "hot beverage"
    description_text = "Just some hot water in a cup."

    def description(self) -> str:
        """Return the instance description string."""
        return self	.description_text

    def __str__(self) -> str:
        return (
            f"name : {self.name}\n"
            f"price : {self.price:.2f}\n"
            f"description : {self.description()}"
        )


class Coffee(HotBeverage):
    name = "coffee"
    price = 0.40
    description_text = "A coffee, to stay awake."


class Tea(HotBeverage):
    name = "tea"

class Chocolate(HotBeverage):
    name = "chocolate"
    price = 0.50
    description_text = "Chocolate, sweet chocolate..."


class Cappuccino(HotBeverage):
    name = "cappuccino"
    price = 0.45
    description_text = "Un po' di Italia nella sua tazza!"
    
if __name__ == "__main__":
    beverages = [HotBeverage(), Coffee(), Tea(), Chocolate(), Cappuccino()]
    for bev in beverages:
        print(bev)