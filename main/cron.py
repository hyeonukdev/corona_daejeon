# DB 업데이트 관련 함수
def get_daejeon_mask_stores():
    from pprint import pprint
    import json
    import requests

    url = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByAddr/json"
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }
    gu_list = [
        "대전광역시 대덕구",
        "대전광역시 동구",
        "대전광역시 서구",
        "대전광역시 유성구",
        "대전광역시 중구",
    ]

    daejeon_mask_stores = {
        'stores': [],
        'count': 0,
    }
    for gu in gu_list:
        params = {
            'address': gu
        }
        mask_json = json.loads(requests.get(
            url, params=params, headers=headers).text)
        # pprint(mask_json)
        daejeon_mask_stores['count'] += mask_json['count']
        daejeon_mask_stores['stores'] += mask_json['stores']

    print("I GET DATA!")
    return daejeon_mask_stores


get_daejeon_mask_stores()
