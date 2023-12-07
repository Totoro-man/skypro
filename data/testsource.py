result_from_json = [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }
]
source = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "to": "Счет 64686473678894779589"
}
source_2 = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
}
result = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "26.08.2019",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Касса в отделении банка",
    "from2": "Maestro 1596 83** **** 5199",
    "to": "Счет **9589"
}
receipts_source = [
  {
    "id": 594226727,
    "state": "CANCELED",
    "date": "2018-09-12T21:27:25.241689"
  },
  {
    "id": 615064591,
    "state": "CANCELED",
    "date": "2018-10-14T08:21:33.419441"
  },
  {
    "id": 147815167,
    "state": "EXECUTED",
    "date": "2018-01-26T15:40:13.413061"
  },
  {
    "id": 518707726,
    "state": "EXECUTED",
    "date": "2018-11-29T07:18:23.941293"
  },
  {
    "id": 649467725,
    "state": "EXECUTED",
    "date": "2018-04-14T19:35:28.978265"
  },
  {
    "id": 782295999,
    "state": "EXECUTED",
    "date": "2019-09-11T17:30:34.445824"
  }
]
receipts_latest_result = [
    {
        "id": 782295999,
        "state": "EXECUTED",
        "date": "2019-09-11T17:30:34.445824"
    },
    {
        "id": 518707726,
        "state": "EXECUTED",
        "date": "2018-11-29T07:18:23.941293"
    },
    {
        "id": 615064591,
        "state": "CANCELED",
        "date": "2018-10-14T08:21:33.419441"
    }
]
receipts_executed_result = [
  {
    "id": 147815167,
    "state": "EXECUTED",
    "date": "2018-01-26T15:40:13.413061"
  },
  {
    "id": 518707726,
    "state": "EXECUTED",
    "date": "2018-11-29T07:18:23.941293"
  },
  {
    "id": 649467725,
    "state": "EXECUTED",
    "date": "2018-04-14T19:35:28.978265"
  },
  {
    "id": 782295999,
    "state": "EXECUTED",
    "date": "2019-09-11T17:30:34.445824"
  }
]
formatted_receipt_result = "26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.\n"