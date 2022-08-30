alurl = "https://openapi.alipaydev.com/gateway.do?"

from alipay import AliPay

app_private_key_string = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAm3D7RIhku5VZHSEEYGa737odzuWwh34xPE7YRODFB4lnCkHT5l8vsqZGb0cc8ksN67WA1UU7Emo5ATjIt+zNqMLEz7P/09xezP4u4nsML/P/N7v4hIpP2NUtbckAQt7gemZ5mXyxMRaZ1MYbIvUpcvnytNgzkgrx0tSjV6HgkoWHegN55voDpHX85ODHxgAaghh77VXnCZ/eDbwaCIrgRKh7uVG4YZsnKPIdFgcj/2u5jGmJiFRH5YyQb4zf+5zH6FSHcvTEweeertkM4OGG3BUT0HHGai+7mtxlOkbigNz9tXd+EcfXmhT2Akqy8iF9UVj28jxDd4OobZpy2mxH3QIDAQABAoIBAA27l5dgbXXdJfha2GYj7WlAqi2DQWtXDMaFOLotGXsm+oF/e1cZBb/EzOg74iTN2LcAXBd7fFKOK+cduy30r96/BmBLSMjQ6Vc3BbFgqZz684tbAgPDrHY9rzvJzEocIrztnMSgrY7mrkSMFA2slzLfPkAX8cZvTRoRSzUMyihnnGXCWI9bcUvC+a/EB8Dee297CPDQLqCKPUOb5HqRQAwBEqnC0H6ejQ6Bg+6pq0wTs387fioHe3pCBE5rcs/qbLB9sJTWcD84x+E+mk256sB0zAp7AxZZaybV2lfSyInbzjBNsq7/oMGo3ckDDMXkzVvD7PZCiZlxEbLV8JtnP4kCgYEAyuRGqG+ZrgVFUUQRvTxqxQT7PEsuU2MyyEVVJlVFm6ienPpIeaUmO7ezLo++tpfSUlb4OJ58R3ndB7jr/EYMcBW9C9jcqIpmrw6nP+0n7gCc7hqUrtKiYtKMS1IjPLRY61V3624ZnJ9IyfxMNBv17B8iZIS20I4RjRnTRZxLTu8CgYEAxCERV3LHJdE6gqcwKB8ETEs4Sfx6jBoNU2yP+pPNVQBxkShgmdeley4aeto4EeSBGq1OxGwGoAuWIVJF7kKkCStbZH+yi+qz0nF7qIFJ+rsf37UFb0CxcpeiBavIBRijMkr1GDlJnBsAi8vyvnaZExJ/wivAs7sUaSX89z31VfMCgYBqTs/jA46vit12JkdxMw3yq5iEUBQ25xw9qW5jRnzRgbmSIOYGrwzob2l4dSMFg2lVcXJgIFKYFPdGS5OCvKVZuVozse50dQg2o2Po7/djEnknnU/Yhk9FnnKaKLCD5y9MJ51NA4Rx91fpVcQL7baegPXBW3R6tGXn2+dCaxFeiwKBgQCxwqLcFoyHKx6T4oJUKuCTYa2v6SUNLGOdlAze+O0muJM2FFmRthEnFv8rD/O3y9pz2lZE0wAiOL4mj1IQg9f285QO/2pNRDkdaHvCmwP5O3bFJGW7kvABw4s3Bp3weIcZgzSncuzTjumsyvnFROqyjZa73zn17H6wWpzvXfmpnwKBgQCRRuVIw+h+l2fMrLWaBViTxEHHe/q9bbJzbEWIA5xKhg9VMD8T6nPI65V57woY7ZmWkXlA3BG9WtNV8SursxA9AQLD185NBP5eBC5eaUvVPZOO+64HfgCBg0RDduFK7z8COzyJ1e4fTqwRPnmV+Qa30PiZo6ORYJI9o8N2oUK+ig==
-----END RSA PRIVATE KEY-----"""

alipay_public_key_string = """-----BEGIN RSA PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAl74ByPl6JpB2ZvJxMZe9ro53UmT3OCl3UjN+9ivhHFXVFdCPy81+kZGRqk0AiBMFia3YhWhGifBejBYGYORET1aWIoVsSWRvtl2n57ll9Y/+mZZ2Ft/gTWUVV4hNqTHJkTTgCkMr/mZDNlXAhDnndn5JtNiSbyTFmU9R054SrvPXlboIP1SqFgNAp1Ec789qYL0HWWxaWHTZLhEGxi7zZPlj3aSayVtxfOQM8j60iW8Wl6Gb/IicI0RXG1+m7ddLN7+JhXQHmTVLtNLMez+xNkcB1f5CEX48P9HoMwP4Wk63wIIVQGWd2kiyeRtkhzUgd0mYa0jP9vI99les3IeJDQIDAQAB
-----END RSA PUBLIC KEY-----
"""
alpay = AliPay(
    appid="2021000117673792",
    app_notify_url="http://127.0.0.1:8000",
    app_private_key_string=app_private_key_string,
    alipay_public_key_string=alipay_public_key_string,
    debug=True,
)

ret = alpay.api_alipay_trade_page_pay(
    **{"subject": "套餐2",
       "out_trade_no": "1223456189876",
       "total_amount": 1,
       "return_url": "http://127.0.0.1:8000/v1/api/page_pay/"}
)
print(alurl + ret)

if __name__ == '__main__':
    ...
