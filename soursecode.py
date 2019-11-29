def parser(filename:str, separator:str, ending:str):
	"""
	Parsing text file(filename), with separator
	stops by ending, like:
	LENNIE,KIARA,JACALYN,CARLOTA,1
	separator = ","
	ending = "1"
	Return list with ['LENNIE', 'KIARA', 'JACALYN', 'CARLOTA']
	RUS:
	Сортирует значения в файле с именем filename и расширением .txt по разделителю separator
	останавливается по значению ending
	Пример текста:
	LENNIE,KIARA,JACALYN,CARLOTA,1
	separator = ","   #разделитель
	ending = "1"      #значение по которому останавливается 
	Возвращает список с ['LENNIE', 'KIARA', 'JACALYN', 'CARLOTA']
	"""
	list = []
	sortedlist = []
	file = open(filename)
	for x in file:
		list.append(x)
	namesstr = list[0] #make str variable with names(делаем строку из сортируемых значений)
	i = 0
	while 1:
		if namesstr[:i]== ending: #end if meet ending(выполнение программы останавливается если встречается значение ending)
			break
		else:
			if namesstr[i]==separator:
				sortedlist.append(namesstr[:i]) #select a word or value, cut and append to list(находим слово или значение, делаем срез и отпраляем его в список)
				namesstr = namesstr[i+1:] #cutiing word or value from string with values(Вырезаем значение из строки)
				i = 0
			else:
				i+=1
	return sortedlist			
