'''
@Author: YuleZhang
@Description: 
@Date: 2020-04-01 21:26:56
'''
from bs4 import BeautifulSoup
import requests
import pymysql
import json
import re

def get_pages_data():
    headers = {"Content-Type":'text/javascript;charset=utf-8'}
    cid = ['3508','3509','3510','3511']
    cid_type = ['省政府预算','省政府决算','省级部门预算','省级部门决算']
    year = ['2018','2019','2020']
    for idx in range(len(cid)):
        for y in year:
            page = 1
            cur_page = 1
            while cur_page <= page:
                url = 'https://jyxc.henan.gov.cn/open/newslist?&webId=450001&cid={0}&start={1}&pageSize=15&year={2}'.format(cid[idx],cur_page,y)
                response = requests.get(url.format(y))
                json_start = response.text.find('{')
                json_end = response.text.rfind('}')
                standard_data = json.loads(response.text[json_start:json_end+1])
                if not len(standard_data['data']): break
                total_page = int(standard_data['totalPage'])
                if total_page > page : page = total_page
                for per in standard_data['data']:
                    son_url = per['url']
                    print(son_url)
                    res = requests.get(son_url,headers=headers)
                    res=res.content.decode("utf-8","ignore")
                    soup = BeautifulSoup(res,'lxml')
                    table = []
                    for p in soup.find("div", class_="content"):
                        if p.find('a')!=-1 and p.find('a') is not None:
                            row = []
                            row.append(p.find('a').text)
                            row.append(p.find('a').get('href'))
                            row.append(y)
                            row.append(cid_type[idx])
                            table.append(row)
                            print(row)
                    save_to_mysql(table)
                cur_page+=1

def save_to_mysql(table):
    if not len(table): return

    db_name = 'financial_data'
    table_name='file'
    user = 'root'
    password = ''

    conn = pymysql.connect(host="localhost", user=user,password=password)
    cursor = conn.cursor()
    # 选择连接database
    conn.select_db(db_name)
    # clear_sql='truncate table file;'
    # cursor.execute(clear_sql)
    # conn.commit()
    for row in table:
        s = 'NULL,\''+'\',\''.join(row)+'\''
        insert_sql = 'INSERT INTO {} VALUES ({})'.format(table_name,s)+';'
        # print(insert_sql)
        # try:
            #执行sql
        cursor.execute(insert_sql)
        conn.commit()
        # except:
            #发生异常
            # print('rollback')
            # conn.rollback()
    conn.close()

# def getDate(s):
#     t = re.findall("\d{4}",s)
#     if t:
#         return t[0]

if __name__ == "__main__":
    get_pages_data()
