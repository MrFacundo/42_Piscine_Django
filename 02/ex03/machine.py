import random

from beverages import HotBeverage

class CoffeeMachine:
	"""A cheap coffee machine that can serve drinks and breaks after 10 uses.

	Usage:
		machine = CoffeeMachine()
		drink = machine.serve(Coffee)  # where Coffee is a subclass of HotBeverage
	"""

	class EmptyCup(HotBeverage):
		name = "empty cup"
		price = 0.90
		description_text = "An empty cup?! Gimme my money back!"

	class BrokenMachineException(Exception):
		def __init__(self):
			super().__init__("This coffee machine has to be repaired.")

	def __init__(self):
		self._served_count = 0
		self._broken = False

	def repair(self) -> None:
		self._broken = False
		self._served_count = 0

	def serve(self, beverage_class):
		if self._broken:
			raise CoffeeMachine.BrokenMachineException()

		if not isinstance(beverage_class, type) or not issubclass(beverage_class, HotBeverage):
			raise TypeError("serve() expects a HotBeverage subclass as parameter")

		if self._served_count >= 10:
			self._broken = True
			raise CoffeeMachine.BrokenMachineException()

		if random.choice([True, False]):
			drink = beverage_class()
		else:
			drink = CoffeeMachine.EmptyCup()

		self._served_count += 1
		return drink

def main():
	from beverages import Coffee, Tea, Chocolate, Cappuccino

	machine = CoffeeMachine()
	options = [Coffee, Tea, Chocolate, Cappuccino]

	print("--- First run: requesting drinks until the machine breaks ---")
	try:
		while True:
			cls = random.choice(options)
			drink = machine.serve(cls)
			print(drink)
	except CoffeeMachine.BrokenMachineException as e:
		print(e)

	print("\nRepairing the machine...")
	machine.repair()

	print("--- Second run: requesting drinks until the machine breaks again ---")
	try:
		while True:
			cls = random.choice(options)
			drink = machine.serve(cls)
			print(drink)
	except CoffeeMachine.BrokenMachineException as e:
		print(e)

if __name__ == "__main__":
	main()

