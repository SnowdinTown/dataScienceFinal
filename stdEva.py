import numpy as np
from matplotlib import pyplot as plt
import json


def getPos(type, rank):
	pass


def getAbilityFigure(userEva):
	
	# 中文和负号的正常显示
	plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'
	plt.rcParams['axes.unicode_minus'] = False
	
	# 使用ggplot的风格绘图
	plt.style.use('ggplot')
	
	# 构造数据
	values = list(map(getPos, userEva.items()))
	feature = list(userEva.keys())
	
	N = len(values)
	
	# 设置雷达图的角度，用于平分切开一个平面
	angles = np.linspace(0, 2 * np.pi, N, endpoint=False)
	
	# 使雷达图封闭起来
	values = np.concatenate((values, [values[0]]))
	angles = np.concatenate((angles, [angles[0]]))
	
	# 绘图
	fig = plt.figure()
	# 设置为极坐标格式
	ax = fig.add_subplot(111, polar=True)
	# 绘制折线图
	ax.plot(angles, values, 'b', linewidth=2)
	ax.fill(angles, values, 'b', alpha=0.5)
	
	
	# 添加每个特质的标签
	ax.set_thetagrids(angles[0:-1] * 180 / np.pi, feature)
	# 设置极轴范围
	ax.set_ylim(0, 100)
	# 添加标题
	plt.title("能力评估\n")
	# 增加网格纸
	ax.grid(True)
	plt.show()
	
if __name__ == '__main__':
	f = open('user.json', encoding='utf-8')
	data =  json.loads(f.read())['snow']['type_evaluates']
	getAbilityFigure(data)