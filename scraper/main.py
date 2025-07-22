import requests
import json
import pandas as pd
import time
import random

url = "https://api.ouedkniss.com/graphql"
USER_AGENT = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ",
    "(KHTML, like Gecko) Chrome/116.0.5845.111 Safari/537.36",
]
PAGES = 1000
OUTPUT_DIR = "../data/raw.csv"

res = []


def get_data(page):
    payload = json.dumps(
        {
            "operationName": "SearchQuery",
            "variables": {
                "mediaSize": "MEDIUM",
                "q": None,
                "filter": {
                    "categorySlug": "immobilier",
                    "origin": None,
                    "connected": False,
                    "delivery": None,
                    "regionIds": [],
                    "cityIds": [],
                    "priceRange": [None, None],
                    "exchange": None,
                    "hasPictures": False,
                    "hasPrice": False,
                    "priceUnit": None,
                    "fields": [],
                    "page": page,
                    "orderByField": {"field": "REFRESHED_AT"},
                    "count": 48,
                },
            },
            "query": "query SearchQuery($q: String, $filter: SearchFilterInput, $mediaSize: MediaSize = MEDIUM) {\n  search(q: $q, filter: $filter) {\n    announcements {\n      data {\n        ...AnnouncementContent\n        smallDescription {\n          valueText\n          __typename\n        }\n        noAdsense\n        __typename\n      }\n      paginatorInfo {\n        lastPage\n        hasMorePages\n        __typename\n      }\n      __typename\n    }\n    active {\n      category {\n        id\n        name\n        slug\n        icon\n        delivery\n        deliveryType\n        priceUnits\n        children {\n          id\n          name\n          slug\n          icon\n          __typename\n        }\n        specifications {\n          isRequired\n          specification {\n            id\n            codename\n            label\n            type\n            class\n            datasets {\n              codename\n              label\n              __typename\n            }\n            dependsOn {\n              id\n              codename\n              __typename\n            }\n            subSpecifications {\n              id\n              codename\n              label\n              type\n              __typename\n            }\n            allSubSpecificationCodenames\n            __typename\n          }\n          __typename\n        }\n        parentTree {\n          id\n          name\n          slug\n          icon\n          children {\n            id\n            name\n            slug\n            icon\n            __typename\n          }\n          __typename\n        }\n        parent {\n          id\n          name\n          icon\n          slug\n          __typename\n        }\n        __typename\n      }\n      count\n      filter {\n        cities {\n          id\n          name\n          __typename\n        }\n        regions {\n          id\n          name\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    suggested {\n      category {\n        id\n        name\n        slug\n        icon\n        __typename\n      }\n      count\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment AnnouncementContent on Announcement {\n  id\n  title\n  slug\n  createdAt: refreshedAt\n  isFromStore\n  isCommentEnabled\n  userReaction {\n    isBookmarked\n    isLiked\n    __typename\n  }\n  hasDelivery\n  deliveryType\n  paymentMethod\n  likeCount\n  description\n  status\n  cities {\n    id\n    name\n    slug\n    region {\n      id\n      name\n      slug\n      __typename\n    }\n    __typename\n  }\n  store {\n    id\n    name\n    slug\n    imageUrl\n    isOfficial\n    isVerified\n    __typename\n  }\n  user {\n    id\n    __typename\n  }\n  defaultMedia(size: $mediaSize) {\n    mediaUrl\n    mimeType\n    thumbnail\n    __typename\n  }\n  price\n  pricePreview\n  priceUnit\n  oldPrice\n  oldPricePreview\n  priceType\n  exchangeType\n  category {\n    id\n    slug\n    __typename\n  }\n  __typename\n}",
        }
    )
    headers = {
        "User-Agent": random.choice(USER_AGENT),
        "Content-Type": "application/json",
    }

    r = requests.request("POST", url, headers=headers, data=payload)
    return r.json()


for x in range(1, PAGES):
    data = get_data(x)

    for p in data["data"]["search"]["announcements"]["data"]:
        res.append(p)

    print(len(res))

    if x == 1:
        df = pd.json_normalize(res)
        df.to_csv(OUTPUT_DIR, index=False)
    else:
        df = pd.json_normalize(res)
        df_to_csv = df.to_csv(OUTPUT_DIR, index=False, mode="a", header=False)
    time.sleep(random.uniform(1, 4))

df = pd.json_normalize(res)
df.to_csv("data.csv", index=False)
