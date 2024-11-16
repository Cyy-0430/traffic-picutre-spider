import asyncio
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests

headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}
cookies = [
    {'domain': '.vcg.com', 'expiry': 1747313407, 'httpOnly': False, 'name': 'ssxmod_itna2', 'path': '/',
     'sameSite': 'Lax', 'secure': False,
     'value': 'QqGxcDgDRmiQ0=DCDzEDUijfoCDx9nDiq2wByD5ikfeDlE4Q9d08D+rYD==='},
    {'domain': '.vcg.com', 'expiry': 1763297408, 'httpOnly': False,
     'name': 'Hm_up_5fd2e010217c332a79f6f3c527df12e9', 'path': '/', 'sameSite': 'Lax', 'secure': False,
     'value': '%7B%22uuid%22%3A%7B%22value%22%3A%22c8f63bb4-da24-422c-9ec1-1da94b5a417f%22%2C%22scope%22%3A1%7D%2C%22uid_%22%3A%7B%22value%22%3A%223d4053bc24f908d1f397bab416c0f1532%22%2C%22scope%22%3A1%7D%2C%22userId%22%3A%7B%22value%22%3A%223d4053bc24f908d1f397bab416c0f1532%22%2C%22scope%22%3A1%7D%7D'},
    {'domain': '.vcg.com', 'httpOnly': False, 'name': 'Hm_lpvt_5fd2e010217c332a79f6f3c527df12e9', 'path': '/',
     'sameSite': 'Lax', 'secure': False, 'value': '1731761409'},
    {'domain': '.vcg.com', 'expiry': 1747313407, 'httpOnly': False, 'name': 'ssxmod_itna', 'path': '/',
     'sameSite': 'Lax', 'secure': False,
     'value': 'QqGxcDgDRmiQ0=DCDzEDUijfoCDx9nDiq2wByD55Ds=KTDSxGKidDqxBne67erPxK5QjRDhW=FiAPxs6ini23AYF6lyKDHxY=DU=7TnoD445GwD0eG+DD4DW0x03DoxGAgwx04kg92u9QD3qDwDB=DmqG24m=Dm4DfDDd9Ygx47qGEDA3DGb6KswDD0wGbqb+xDYP9fkLqqQrDAkGS8Ax9D0tDIqGXQGydxDUzVpGZfwFkT1Pu3jiDtqD97CUUbn+ySMU2b64rFrxrIDd3YfxN+DxbKBq2Zrmx+7D08A4P8bhxGVza/E/NBnNlvDD==='},
    {'domain': '.vcg.com', 'expiry': 1731772799, 'httpOnly': False, 'name': 'sajssdk_2015_cross_new_user',
     'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1'},
    {'domain': '.vcg.com', 'expiry': 1766321408, 'httpOnly': False, 'name': 'sensorsdata2015jssdkcross',
     'path': '/', 'sameSite': 'Lax', 'secure': False,
     'value': '%7B%22distinct_id%22%3A%223d4053bc24f908d1f397bab416c0f1532%22%2C%22first_id%22%3A%2219335057836c83-033d9832018b8da-4c657b58-2073600-193350578382665%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219335057836c83-033d9832018b8da-4c657b58-2073600-193350578382665%22%7D'},
    {'domain': '.vcg.com', 'expiry': 1739566179, 'httpOnly': False, 'name': 'name', 'path': '/',
     'sameSite': 'Lax', 'secure': True, 'value': '18317917211'},
    {'domain': '.vcg.com', 'httpOnly': False, 'name': 'clientIp', 'path': '/', 'sameSite': 'Lax', 'secure': True,
     'value': '222.178.10.248'},
    {'domain': '.vcg.com', 'expiry': 1739566179, 'httpOnly': False, 'name': 'abBoss3', 'path': '/',
     'sameSite': 'Lax', 'secure': True, 'value': '1.0'},
    {'domain': '.vcg.com', 'expiry': 1739566208, 'httpOnly': False, 'name': '_fp_', 'path': '/',
     'sameSite': 'Lax', 'secure': True,
     'value': 'eyJpcCI6IjIyMi4xNzguMTAuMjQ4IiwiZnAiOiI4NGFmNTQxYTc4NDJhMzY1YTM1ZDE0YTcyODg0MTI3MyIsImhzIjoiJDJhJDA4JEEuV2xVNUVMby9GWEs3dGx6TFpWcHVSMHAwNmQ5WUxNVUpOeG8uN1FHV1pSeTdDLm9RZHNlIn0%3D'},
    {'domain': '.vcg.com', 'expiry': 1739566208, 'httpOnly': False, 'name': 'fingerprint', 'path': '/',
     'sameSite': 'Lax', 'secure': True, 'value': '84af541a7842a365a35d14a728841273'},
    {'domain': '.vcg.com', 'httpOnly': False, 'name': 'HMACCOUNT', 'path': '/', 'sameSite': 'Lax',
     'secure': False, 'value': '9AF83B2647217F52'},
    {'domain': '.vcg.com', 'httpOnly': False, 'name': 'uuid', 'path': '/', 'sameSite': 'Lax', 'secure': True,
     'value': 'c8f63bb4-da24-422c-9ec1-1da94b5a417f'},
    {'domain': '.vcg.com', 'expiry': 1739537379, 'httpOnly': False, 'name': 'api_token', 'path': '/',
     'sameSite': 'Lax', 'secure': True, 'value': 'ST-130-18921ddfa4779b592cdf2a8229a313256'},
    {'domain': '.vcg.com', 'expiry': 1763297408, 'httpOnly': False,
     'name': 'Hm_lvt_5fd2e010217c332a79f6f3c527df12e9', 'path': '/', 'sameSite': 'Lax', 'secure': False,
     'value': '1731761371'},
    {'domain': 'www.vcg.com', 'expiry': 1731763168, 'httpOnly': True, 'name': 'acw_tc', 'path': '/',
     'sameSite': 'Lax', 'secure': False,
     'value': '1a0c639717317613748157411e0036eddf0d6e5233bfa8b62c048ed0203502'}]

session = requests.Session()
driver = webdriver.Edge()


async def search_type(name):
    print(f"正在解析{name}")
    driver.get(f"https://www.vcg.com/creative-image/{name}/")
    driver.delete_all_cookies()
    for cookie in cookies:
        driver.add_cookie(cookie)
    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_all_elements_located((By.CSS_SELECTOR, "figure"))
    # )

    a_button = driver.find_element(By.CSS_SELECTOR, 'a[title="正常显示"]')
    a_button.click()
    figures = driver.find_elements(By.CSS_SELECTOR, "article div a img")

    task = []
    for fig in figures:
        img_url = fig.get_attribute("data-src")
        task.append(download_picture("https:" + img_url))
    await asyncio.gather(*task)


async def download_picture(url):
    resp = await asyncio.to_thread(session.get, url, headers=headers)
    if resp.status_code != 200:
        return

    picture_name = url.split('/')[-1]
    print(f"{picture_name}下载成功")

    with open(f"data/{picture_name}", 'wb') as f:
        f.write(resp.content)


async def main():
    params = [
        "honglvdeng",  # 红绿灯
        "jinzhitongxinglupai",  # 禁止通行标志
        "TINGCHERANGXINGBIAOZHI",  # 停车让行标志
        "XUEXIAOSHEYOUERTONGGUOMALUJIAOTONGJINGGAOBIAOZHI",  # 学校路段标志
        "LANSESANJIAOXINGRENXINGHENGDAOZHISHIPAI",  # 人行横道标志
    ]

    for param in params:
        await search_type(param)


if __name__ == '__main__':
    if not os.path.exists("data"):
        os.mkdir("data")

    asyncio.run(main())
