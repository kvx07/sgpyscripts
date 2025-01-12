import requests
from requests.exceptions import Timeout
import time
from threading import Thread
def P0J1E():
    print("--🟢欢迎使用C1rrus付费版破解机工具 多线程版(此版本可能不稳定)--\n(=මᆽම=)此版本所有接口均为本人开发，如有异常随时可以删key~\n")
    key = 'cirrus'
    name, phone = input("请输入姓名:"), input("请输入手机号:")
    try:
        response = requests.get(f"http://110.42.46.20:7777/diqu?key={key}&phone={phone}", timeout=15)
        if response.status_code == 401:
            print("🔴请先找开发者购买正确的秘钥哦 @c0nt1n3n5al~")
            return
        response.raise_for_status()
    except Timeout:
        print("\n(━┳━ _ ━┳━)请求超时，请检查网络并重启程序喵~")
        return
    except requests.exceptions.HTTPError as err:
        print(f"🔴归属地生成失败，接口返回错误: {err}")
        return
    regions = response.text.split(' ')
    if regions:
        regions = [item + '*' * 14 for item in regions]
        print(f"--✅匹配到模糊身份证{len(regions)}个--")
        print("准备补齐身份证......\n")
    else:
        print("🔴归属地生成失败啦,请联系开发者更换新版哦~")
        return
    matched_ids = []
    for region in regions:
        print(f"正在匹配{region[:4] + '...' + region[-4:] if len(region) > 8 else region}")
        try:
            response = requests.get(f"http://110.42.46.20:7777/buqi?key={key}&name={name}&id={region}", timeout=15)
            response.raise_for_status()
        except Timeout:
            print("\n(━┳━ _ ━┳━)请求超时，请检查网络并重启程序喵~")
            return
        except requests.exceptions.HTTPError as err:
            print(f"🔴补齐接口抽风啦，请重新运行程序~")
            return
        ids = response.text.split(" ")
        matched_ids.extend(filter(None, ids))
        time.sleep(0.5)
    if matched_ids:
        print(f"\n--✅匹配到身份证{len(matched_ids)}个--")
        print("准备核验身份证,请稍候一会喵......\n")
    else:
        print("🔴身份证生成失败啦,可能是手机号和户籍地不匹配哦~")
        if input("是否尝试输入模糊身份证? y/n:") == "y":
            region = input("\n请输入模糊身份证(如:110xxxxxxxxxxxxx):")
            if 'x' in region:
                region = region.replace('x', '*')
                response = requests.get(f"http://110.42.46.20:7777/buqi?key={key}&name={name}&id={region}", timeout=15)
                if response.status_code == 200:
                    matched_ids.extend(filter(None, response.text.split(" ")))
                elif response.status_code == 402:
                    print("\n(━┳━ _ ━┳━)请求超时，请检查网络并重启程序喵~")
                    return
                if matched_ids:
                    print(f"\n--✅匹配到身份证{len(matched_ids)}个--")
                    print("准备核验身份证,请稍候一会喵......\n")
                else:
                    print("🔴身份证生成失败啦,请重启再换一个模糊身份证试试吧~")
                    return
            else:
                print("🔴输入格式错误~")
        else:
            return
    def verify_id(id_card):
        response = requests.get(url=f"http://110.42.46.20:7777/3ys?key={key}&name={name}&id={id_card}&phone={phone}", timeout=15)
        if response.status_code == 200:
            print(f"--✅找到你啦--\n--姓名:{name}--\n--身份证:{id_card}--\n--手机号:{phone}--\n核验通过!")
            return True
        return False
    threads = []
    try:
        for id_card in matched_ids:
            thread = Thread(target=verify_id, args=(id_card,))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
        print(f"--核验完毕,其余结果核验失败 共核验{len(matched_ids)}条--")
    except Exception as e:
        print(f"🔴傻逼三要素接口抽风啦，重开吧~")
        return
    if input("( ཀ͝ ∧ ཀ͝ )是否查看所有身份证? y/n:") == "y":
        [print(id) for id in matched_ids]
if __name__ == "__main__":
    P0J1E()