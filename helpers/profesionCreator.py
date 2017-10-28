# Matthew Doran
# create dictionary of all genres
# problems in file creation???
import re
def main():

	out = open("PersonProfessions.csv", "w")
	out2 = open("Profession.csv", "w")

	with open("nameProfession.csv", "r") as f:
		professionDict = {}
		i = 1
		for line in f.readlines():
			sepList = re.split(' |,',line)
			actorId = sepList[0][2:]
			professions = sepList[1:]
			#for genre in genres:
                         #       genre = genre.split(" ")
			professions[len(professions)-1] = professions[len(professions)-1][:-1] # shave off newline (could have just used .replace)
			for pro in professions:
				if pro not in professionDict:
					professionDict[pro] = i
					i += 1
				out.write("{},{}\n".format(actorId, professionDict[pro]))

		for k, v in professionDict.iteritems():
			out2.write("{},{}\n".format(v, k))

		out.close()
		out2.close()
main()
