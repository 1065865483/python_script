˵�������ɲ��Ա����ģ�飨BSTestRunner.py��HTMLTestRunner.py����Ҫ�����޸ģ����ļ�Ϊ�޸ĺ��ļ���ֱ�ӽ������LibĿ¼���ɡ�

�޸�ԭ�����ڴ�ģ�����python2д�ģ�����������ʹ��python3,��ˣ�������Ҫ����python3��һЩ��ͬ���Խ����޸ġ�


���ص�ַ��http://tungwaiyip.info/software/HTMLTestRunner.html

�޸����ݣ�

	* 94�����������Ҫ�ģ��� import StringIO �ĳ�import io��
	* 539�� self.outputBuffer = StringIO.StringIO() Ҫ�ĳ�self.outputBuffer=io.StringIO()
	* 631�� print >>sys.stderr, '\nTime Elapsed: %s' % (self.stopTime-self.startTime)----�޸�Ϊ��print (sys.stderr, '\nTime Elapsed: %s' %(self.stopTime-self.startTime))
	* 642�У�if not rmap.has_key(cls): ��Ҫ���� if not cls in rmap:
	* 766�е�uo = o.decode('latin-1')���ĳ� uo=o
	* 772�У��� ue = e.decode('latin-1') ֱ�Ӹĳ� ue = e

�޸ĺ���·����
���޸���ɵ�ģ�����Python·����LibĿ¼����
