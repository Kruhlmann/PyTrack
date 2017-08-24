import gspread
import requests
import socket
import datetime
import getpass
from oauth2client.service_account import ServiceAccountCredentials

def get_last_row(sheet):
	for i in range(2, sheet.row_count):
		if sheet.cell(i, 1).value == "":
			return i
	return -1

def track(sheet, row):
	request_json = requests.get('http://ip-api.com/json/').json()
	sheet.update_cell(row, 1, str(row_index - 1))
	sheet.update_cell(row, 2, str(datetime.datetime.now()))
	sheet.update_cell(row, 3, request_json['query'])
	sheet.update_cell(row, 4, request_json['isp'])
	sheet.update_cell(row, 5, getpass.getuser())
	sheet.update_cell(row, 6, socket.gethostname())
	sheet.update_cell(row, 7, request_json['country'])
	sheet.update_cell(row, 8, request_json['regionName'])
	sheet.update_cell(row, 9, request_json['city'])
	sheet.update_cell(row, 10, request_json['zip'])
	sheet.update_cell(row, 11, request_json['timezone'])
	sheet.update_cell(row, 12, str(request_json['lat']) + "/" + str(request_json['lon']))

if __name__ == "__main__":
	scope = ["https://spreadsheets.google.com/feeds"]
	credentials = ServiceAccountCredentials.from_json_keyfile_name("client_credentials.json", scope)
	client = gspread.authorize(credentials)

	sheet = client.open('PyTrack').sheet1
	row_index = get_last_row(sheet)
	if row_index == -1:
		print("Error: Couldn't find last row in sheet.")
		exit()
	track(sheet, row_index)
