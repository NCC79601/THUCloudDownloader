# THUCloudDownloader

一个自动批量下载清华云盘（基于 Seafile）分享链接中的大量文件的小工具

---
## 使用方法 Usage
1. 执行 `pip install -r requirements.txt` 安装依赖
2. 将分享链接网页加载完毕后的 HTML 文件保存至本目录下
3. 执行 `python main.py`
4. 在 `download` 文件夹中看到下载的所有文件

---
## 局限 Limitation
- 无法下载二级菜单及更高级菜单中的文件
- 只能下载“预览及下载”权限的分享连接中的文件