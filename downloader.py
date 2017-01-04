import urllib

from bs4 import BeautifulSoup

from DBSession import DBSession, Image, Girl


class Meizhi(object):
    def download(self, urls):
        i = 1
        session = DBSession()
        for url in urls:

            print('第', i, '帖子开始--------------')

            # 下载
            response = urllib.request.urlopen(url)
            print('下载帖子结果', response.getcode())

            try:
                # 解析DOM
                soup = BeautifulSoup(response.read(), "html.parser", from_encoding='utf-8')

                # 获取头像图片
                head_pic = soup.find('div', class_='user-face').find('a').find('img').get('src')
                print('头像地址-', head_pic)

                user = soup.find('span', class_='from').find('a')

                # 用户主页
                user_address = user.get('href')
                print('用户主页-', user_address)

                # 用户姓名
                user_name = user.get_text()
                print('用户名字-', user_name)

                # 发帖时间
                time = soup.find('div', class_='topic-doc').find('span', class_='color-green').get_text()
                print('发帖时间-', time)

                check_user = session.query(Girl).filter(Girl.address == user_address).all()
                print('检查数据库是否已存在用户', check_user)

                if len(check_user) <= 0:
                    girl = Girl(name=user_name, address=user_address, avatar=head_pic)
                    session.add(girl)
                    session.commit()
                    print('存储')
                else:
                    print('不存储')

                users = session.query(Girl).filter(Girl.address == user_address).all()

                # 获取用户发出的图片
                links = soup.find_all('div', class_="topic-figure cc")
                for link in links:
                    img_url = link.find('img').get('src')
                    print('用户发的图片', img_url)

                    check_image = session.query(Image).filter(Image.address == img_url).all()
                    if len(check_image) <= 0:
                        # 保存到数据库
                        image = Image(address=img_url, time=time, uid=users[0].id)
                        session.add(image)
                        session.commit()
                        print('存储')
                        # 保存图片到本地
                        # img_request = urllib.request.Request(img_url)
                        # img_response = urllib.request.urlopen(img_request)
                        # img_data = img_response.read()
                        # img_name = datetime.timestamp(datetime.now())
                        # with open('images/' + str(img_name) + '.jpg', 'wb') as f:
                        #     f.write(img_data)
                    else:
                        print('不存储')



            except AttributeError as e:
                print(e)
                print(print('第', i, '帖子解析出错------------'))
            finally:
                print('第', i, '帖子结束------------')
                i += 1

        session.close()
