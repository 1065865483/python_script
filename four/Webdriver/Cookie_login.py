from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()

driver.get('http://www.baidu.com')
#手动添加cookie
driver.add_cookie({'name':'BAIDUID','value':'6B1E947B1EC046E5ABB73D61D692B000:FG=1'})
driver.add_cookie({'name':'BDUSS','value':'NYTmFDSGwzMGcwWnd0SVVWM35LWjBOVH5Bd0I1aEZNTUVCVVBmVEtXMk5xQ1phSVFBQUFBJCQAAAAAAAAAAAEAAADsqN4VMTA2NTg2NTQ4MwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI0b~1mNG~9ZZF'})
sleep(3)
driver.refresh()
sleep(2)
driver.quit()