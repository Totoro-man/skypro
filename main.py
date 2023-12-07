from dlls import *

JSON_URL = "https://www.jsonkeeper.com/b/PLZ0"
JSON_PATH = "data/operations"

operation_list = jsonData.get_list_from_file(JSON_PATH)
operation_list = utils.get_executed_receipts(operation_list)
operation_list = utils.get_latest_receipts(5, operation_list)

for i in operation_list:
    print(utils.get_formatted_receipt(i))
