说明：生成测试报告的模块（BSTestRunner.py和HTMLTestRunner.py）需要进行修改，此文件为修改后文件，直接将其放在Lib目录即可。

修改原因：由于此模块基于python2写的，而现在我们使用python3,因此，我们需要根据python3的一些不同特性进行修改。


下载地址：http://tungwaiyip.info/software/HTMLTestRunner.html

修改内容：

	* 94行引入的名称要改，从 import StringIO 改成import io。
	* 539行 self.outputBuffer = StringIO.StringIO() 要改成self.outputBuffer=io.StringIO()
	* 631行 print >>sys.stderr, '\nTime Elapsed: %s' % (self.stopTime-self.startTime)----修改为：print (sys.stderr, '\nTime Elapsed: %s' %(self.stopTime-self.startTime))
	* 642行，if not rmap.has_key(cls): 需要换成 if not cls in rmap:
	* 766行的uo = o.decode('latin-1')，改成 uo=o
	* 772行，把 ue = e.decode('latin-1') 直接改成 ue = e

修改后存放路径：
将修改完成的模块放在Python路径下Lib目录即可
