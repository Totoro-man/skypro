from dlls.jsonData import get_list_from_file
from dlls.utils import *
from data.testsource import *


def test_get_list_from_file():
    assert get_list_from_file("data/testjsondata") == result_from_json


def test_repair_date():
    assert repair_date(source).get("date") == result.get("date")


def test_check_and_repair_from():
    assert check_and_repair_from(source).get("from") == result.get("from")


def test_hide_account_number():
    assert (hide_account_number(source_2).get("from") == result.get("from2")
            and hide_account_number(source_2).get("to") == result.get("to"))


def test_get_latest_receipts():
    assert get_latest_receipts(3, receipts_source) == receipts_latest_result


def test_get_executed_receipts():
    assert get_executed_receipts(receipts_source) == receipts_executed_result


def test_get_formatted_receipt():
    assert get_formatted_receipt(result_from_json[0]) == formatted_receipt_result