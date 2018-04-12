################
#data_processing week 3
#Tijs Teulings
#10782982
#
# creates json from csv
# test
################


# creates json from csv
def csv_to_json(file_name_org, file_name_omzet):


	
	# determines which rows, columns are used
	start_row_org = 2
	end_row_org = 80

	straat_org = 4
	huisnummer_org = 5

	start_row_omzet = 2
	end_row_omzet = -1

	oud_straat_omzet = 1
	nw_straat_omzet = 0
	oud_nummer_omzet = 6
	nw_nummer_omzet = 7



	datapoints = []

	with open(file_name_org, 'r') as infile_org:
	    data_org=infile_org.read()
	if not data_org:
		print('error org')

	infile_org.close()  

	
	# creates rows
	rows_org  = data_org.split("\n")
	# selects rows
	rows_org = rows_org[start_row_org:end_row_org]

	

	with open(file_name_omzet, 'r') as infile_omzet:
	    data_omzet=infile_omzet.read()
	if not data_omzet:
		print('error omzet')

	infile_omzet.close()  

	
	# creates rows
	rows_omzet  = data_omzet.split("\n")
	# selects rows
	rows_omzet = rows_omzet[start_row_omzet:end_row_omzet]

	print(columns_omzet_sel)




	for row_omzet in rows_omzet:
		columns_omzet = row_omzet.split(";")
		columns_omzet_sel = [columns_omzet[0], columns_omzet[1], columns_omzet[6], columns_omzet[7]]


	# writes selected data to json
	with open('result.csv', 'w') as outfile:
		for row_org in rows_org:
			
			columns = row_org.split(";")

			if columns[straat_org] in columns_omzet_sel:
				print(columns_omzet_sel)


	outfile.close()


csv_to_json('Cholerakaart adressenlijst.csv', 'omnummering.csv')



