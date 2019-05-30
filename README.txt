输入文件格式
Input.json
所有内容均为字符串
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
name：题目名称
test_count：要出的测试点数
std_exe：标程，用来生成答案文件（正常写标程就可以，不需要文件输入输出）
output_file_ext：输出测试点前缀（文件名为“前缀+数字”）
data_generate：
	type：格式
支持格式：line（行）array（矩阵）
	data：
		line：
			type：格式（int=数字（无上限））
				int：
min：最小值
max：最大值
var（选填）：变量名（此变量可以在全局使用，获取当前测试点此处数值，
使用时添加“$变量名”）
		array：
			[0]：定位方式（行定位或列定位）
			[1]：行数（可用变量）
			[2]：
				type：格式（int=数字（无上限））
					int：
						min：最小值
						max：最大值
				repeat：单行重复次数
蒟蒻制作，特殊题型请参考Project CYaRon https://github.com/luogu-dev/cyaron
