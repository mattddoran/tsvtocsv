# Matthew Doran
# create dictionary of all genres

def main():

	out = open("titleGenreId.csv", "a")
	with open("titleGenre.csv", "r") as f:
		genreDict = {}
		i = 1
		for line in f.readlines():
			genres = line.split(",")
			title = genres[0]
			genres = genres[1:]
			genres[len(genres)-1] = genres[len(genres)-1][:-1] # shave off newline (could have just used .replace)
			for genre in genres:
				if genre not in genreDict:
					genreDict[genre] = i
					i += 1
				out.write("{},{}\n".format(title, genreDict[genre]))

		out.close()
main()