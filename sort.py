while True:
	last_name = str(input())

	with open("names.txt", "r") as file:
		contents = file.read().split("\n")
		contents = list(filter(lambda x: len(x) > 0, contents))
		matching = set([name for name in contents if last_name in name.split(" ")[1].lower()])
		if len(matching) == 0:
			print("No Names Found")
		else:
			print(matching)