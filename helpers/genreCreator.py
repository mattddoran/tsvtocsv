# Matthew Doran
# create dictionary of all genres
import re
def main():

	out = open("titleGenreId.csv", "a")
	out2 = open("genreId.csv", "a")

	with open("titleGenre.csv", "r") as f:
		genreDict = {}
		i = 1
		for line in f.readlines():
			genres = re.split(' |,',line)
			title = genres[0][2:]
			genres = genres[1:]
			#for genre in genres:
                         #       genre = genre.split(" ")
			genres[len(genres)-1] = genres[len(genres)-1][:-1] # shave off newline (could have just used .replace)
			for genre in genres:
				if genre not in genreDict:
					genreDict[genre] = i
					i += 1
				out.write("{},{}\n".format(title, genreDict[genre]))

		for k, v in genreDict.iteritems():
			out2.write("{},{}\n".format(v, k))

		out.close()
		out2.close()
main()
