# -*- coding: utf-8 -*-
"""
    Time: 2018-10-01
    Author: Tsystem
"""

import json
from django.http import HttpResponse


def handle_country(request):

    resp = {
        "status": 200,
        "message": "success",
        "data": [
            {
                "name": "不丹",
                "id": "不丹",
                "img": "",
                "percent": 20
            },
            {
                "name": "丹麦",
                "id": "丹麦",
                "img": "",
                "percent": 50
            },
            {
                "name": "俄罗斯",
                "id": "俄罗斯",
                "img": "",
                "percent": 80
            },
            {
                "name": "古巴",
                "id": "古巴",
                "img": "",
                "percent": 100
            },
            {
                "name": "冰岛",
                "id": "冰岛",
                "img": "",
                "percent": 20
            },
            {
                "name": "埃及",
                "id": "埃及",
                "img": "",
                "percent": 40
            },
            {
                "name": "喀麦隆",
                "id": "喀麦隆",
                "img": "",
                "percent": 20
            },
            {
                "name": "尼泊尔",
                "id": "尼泊尔",
                "img": "",
                "percent": 90
            }
        ]
    }

    return HttpResponse(json.dumps(resp), content_type="application/json")
