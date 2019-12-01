def parser_in_file(filename:str, separator:str):
	"""
	Parsing text file(filename), with separator
	parse while have values,
	 like:
	LENNIE,KIARA,JACALYN,CARLOTA
	separator = ","
	Return list with ['LENNIE', 'KIARA', 'JACALYN', 'CARLOTA']
	RUS:
	Сортирует значения в файле с именем filename и расширением .txt по разделителю separator
	Сортирует пока есть значения
	Пример текста:
	LENNIE,KIARA,JACALYN,CARLOTA
	separator = ","   #разделитель
	Возвращает список с ['LENNIE', 'KIARA', 'JACALYN', 'CARLOTA']
	"""
	try:
		List = []
		sortedlist = []
		file = open(filename)
		for x in file:
			List.append(x)
		namesstr = List[0] #make str variable with names(делаем строку из сортируемых значений)
		i = 0
		while 1:
			if namesstr[i]==separator:
				sortedlist.append(namesstr[:i]) #select a word or value, cut and append to list(находим слово или значение, делаем срез и отпраляем его в список)
				namesstr = namesstr[i+1:] #cutiing word or value from string with values(Вырезаем значение из строки)
				i = 0
			else:
				i+=1
	except Exception:
		return sorted(sortedlist)


def score(string:str):
	alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	summ = 0
	for i in range(len(string)):
		if string[i] in alphabet:
			summ+= (alphabet.index(string[i]))+1
	return summ


def score_in_list(plase:int,List:list):
	scorer = score(List[plase-1].lower())
	return scorer*plase

List = parser_in_file("names.txt",",")
print(score_in_list(938,List))
