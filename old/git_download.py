
def extract_filename(input_str, num):

	filename_pos = input_str.find("filename=")
	
	# "filename=" nicht gefunden
	if filename_pos == -1:
	
		print("Filename not found: {0}".format(num))
		return None
	
	# "filename=" gefunden	
	else:
	
		# vorne abschneiden
		filename = input_str[filename_pos + 9:]
	
		# evtl hinten abschneiden
		if filename.find(";") != -1:
	
			filename = filename[:filename.find(";")]
	
		return filename

for i in range(1148,9000):

	print("Download file ... {0}".format(i))

	# Request to URL
	gabc_download = urllib.request.urlopen("https://gregobase.selapa.net/download.php?id={0}&format=gabc".format(i))
	
	# Get Info Header
	info_str = gabc_download.info()['Content-Disposition']
	
	# Check if anything is found
	if info_str:
	
		#Extract filename
		filename = extract_filename(info_str, i)
	
		# Check if filename was found
		if filename:
	
			# Write the file
			with open("SCORES2/" + filename, "w") as f:
	
				f.write(gabc_download.read().decode("utf-8"))