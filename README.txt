�����ļ���ʽ
Input.json
�������ݾ�Ϊ�ַ���
sample
{
	"name" : "A+B Problem",
	"test_count" : "1",
	"std_exe" : "std.exe",
	"output_file_ext" :"test",
	"data_generate" : [
	{"type":"line","data":[{"type":"int","min":"1","max":"4","var":"a"},{"type":"int","min":"1","max":"4","var":"b"}]},
	{"type":"array","data":["line","$a",[{"type":"int","min":"1","max":"5","repeat":"$b"}]]}
	]
}
name����Ŀ����
test_count��Ҫ���Ĳ��Ե���
std_exe����̣��������ɴ��ļ�������д��̾Ϳ��ԣ�����Ҫ�ļ����������
output_file_ext��������Ե�ǰ׺���ļ���Ϊ��ǰ׺+���֡���
data_generate��
	type����ʽ
֧�ָ�ʽ��line���У�array������
	data��
		line��
			type����ʽ��int=���֣������ޣ���
				int��
min����Сֵ
max�����ֵ
var��ѡ������������˱���������ȫ��ʹ�ã���ȡ��ǰ���Ե�˴���ֵ��
ʹ��ʱ��ӡ�$����������
		array��
			[0]����λ��ʽ���ж�λ���ж�λ��
			[1]�����������ñ�����
			[2]��
				type����ʽ��int=���֣������ޣ���
					int��
						min����Сֵ
						max�����ֵ
				repeat�������ظ�����
�X�m����������������ο�Project CYaRon https://github.com/luogu-dev/cyaron
