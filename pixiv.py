import urllib.request as r
import os

def url_open(url):
    req = r.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0')
    res = r.urlopen(req)
    html = res.read()

    return html

def save_page(url):
    filename = url[17:]
    try:
        img = url_open(url)
    except:
        return False
    with open(filename,'wb') as f:
        f.write(img)
        print('%s 保存成功！'%filename)
    return True

def download(pid,folder='pixiv'):
    if not os.path.exists(folder):
        os.makedirs(folder)
    os.chdir(folder)
    i = 1
    while True:
        url = 'https://pixiv.re/%d-%d.png'%(pid,i)
        if not save_page(url):
            break
        i+=1
    if i == 1:
        url = 'https://pixiv.re/%d.png'%(pid)
        if not save_page(url):
            print('找不到这张图！')
        else:
            print('下载完成！')
    else:
        print('下载完成！')
    os.chdir('../')

now_folder = 'pixiv'

def main():
    global now_folder
    print('当前文件夹：' + now_folder)
    get_input = input('请输入pid：')
    if get_input == 'FOLDER':
        folder = input('请更换文件夹：')
        now_folder = folder
    else:
        pid = int(get_input)
        download(pid, now_folder)
    
if __name__ == '__main__':
    while True:
        main()
