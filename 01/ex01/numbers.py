def read_and_print_numbers():
	try:
		with open("numbers.txt", "r") as file:
			content = file.read().strip()
			numbers = content.split(",")

			for number in numbers:
				print(number.strip())
	except FileNotFoundError:
		print("numbers.txt file not found")
	except Exception as e:
		print(f"Error printing file: {e}")

if __name__ == '__main__':
	read_and_print_numbers()