import sys
import math
#math.ceil(m/2)
max_degree=0
node_list_w=[]
node_list_r=[]

class node:
	def __init__(self):
		self.is_leaf=False
		self.key=[]
		self.value=[] #leaf node일때 값들을 가진다
		self.child=[]
		self.parent=None
		self.right_child=None
		self.rightmost_child=None
		self.node_num=-1

	def split(self):
		right=node()
		leaf=False
		leaf=right.is_leaf=self.is_leaf
		mid=int(len(self.key)/2)
		if leaf==True:
			right.key=self.key[mid:]
			right.value=self.value[mid:]
			self.key=self.key[:mid]
			self.value=self.value[:mid]
		else:
			right.key=self.key[mid+1:]
			right.child=self.child[mid+1:]
			self.key=self.key[:mid]
			self.child=self.child[:mid+1]

		right.parent=None

		for i in range(len(right.child)):
			right.child[i].parent=right

		right.right_child=self.right_child
		self.right_child=right

		return self, right

	def set_key_node(self, key, left, right):
		key_tmp=[]
		child_tmp=[]

		for i in range(len(self.key)):
			if key<self.key[i]:
				key_tmp.append(key)
				child_tmp.append(left)
				child_tmp.append(right)
				key_tmp=key_tmp+self.key[i:]
				child_tmp=child_tmp+self.child[(i+1):]
				break
			else:
				key_tmp.append(self.key[i])
				child_tmp.append(self.child[i])
				if i==len(self.key)-1:
					key_tmp.append(key)
					child_tmp.append(left)
					child_tmp.append(right)

		self.key=key_tmp
		self.child=child_tmp
		self.is_leaf=False
		left.parent=self
		right.parent=self

	def set_key_value(self, key, val):
		tmp_key_list=[]
		tmp_val_list=[]

		for i in range(len(self.key)):
			if key < self.key[i]:
				tmp_key_list.append(key)
				tmp_key_list=tmp_key_list+self.key[i:]
				tmp_val_list.append(val)
				tmp_val_list=tmp_val_list+self.value[i:]
				break
			else:
				tmp_key_list.append(self.key[i])
				tmp_val_list.append(self.value[i])

				if i==len(self.key)-1:
					tmp_key_list.append(key)
					tmp_val_list.append(val)

		if len(self.key)==0:
			tmp_key_list.append(key)
			tmp_val_list.append(val)			

		self.key=tmp_key_list
		self.value=tmp_val_list

	def underflow_predict(self):
		global max_degree
		compare=math.ceil(max_degree/2)-1
		is_root=False
		if self.parent==None:is_root=True

		if is_root==True:
			if len(self.key)-1==0: return True
			else: return False
		else:
			if len(self.key)-1<compare: return True
			else: return False 

	def underflow(self):
		global max_degree
		compare=math.ceil(max_degree/2)-1
		is_root=False
		if self.parent==None:is_root=True

		if is_root==True:
			if len(self.key)==0: return True
			else: return False
		else:
			if len(self.key)<compare: return True
			else: return False		

	def delete_key_value(self, place):
		if place==0:
			key_tmp=self.key[(place+1):]
			self.key=key_tmp
			value_tmp=self.value[(place+1):]
			self.value=value_tmp
		elif place==len(self.key)-1:
			key_tmp=self.key[:place]
			self.key=key_tmp
			value_tmp=self.value[:place]
			self.value=value_tmp
		else:
			key_tmp=self.key[:place]+self.key[(place+1):]
			self.key=key_tmp
			value_tmp=self.value[:place]+self.value[(place+1):]
			self.value=value_tmp

	def delete_key(self, place):
		key=self.key[place]
		if place==0:
			key_tmp=self.key[(place+1):]
			self.key=key_tmp
		elif place==len(self.key)-1:
			key_tmp=self.key[:place]
			self.key=key_tmp
		else:
			key_tmp=self.key[:place]+self.key[(place+1):]
			self.key=key_tmp
		return key

	def delete_child(self, place):
		if place==0:
			child_tmp=self.child[(place+1):]
			self.child=child_tmp
		elif place==len(self.child)-1:
			child_tmp=self.child[:place]
			self.child=child_tmp
		else:
			child_tmp=self.child[:place]+self.child[(place+1):]
			self.child=child_tmp

	def set_rightmost(self):
		length=len(self.child)-1
		self.rightmost_child=self.child[length]

class bptree:
	def __init__(self):
		self.root=node()
		self.root.is_leaf=True

	def rightmost(self, node):
		for i in range(len(node.child)):
			node.set_rightmost()
		for i in range(len(node.child)):
			self.rightmost(node.child[i])

	def traversal(self, node):
		print(node.key)
		for i in range(len(node.child)):
			print(node.child[i].key)
		print("**********************************")
		for i in range(len(node.child)):
			self.traversal(node.child[i])

	def node_num_ch(self, node):
		print(node.node_num)
		for i in range(len(node.child)):
			print(node.child[i].node_num)
		print("**********************************")
		for i in range(len(node.child)):
			self.node_num_ch(node.child[i])

	def parent_ch(self,node):
		print(node.key)
			#print(node.child[i].key)
		if node.parent==None: print("none")
		else: 
			print(node.parent.key)
		print("**********************************")
		for i in range(len(node.child)):
			self.parent_ch(node.child[i])

	def search_node(self, key):
		current_node=self.root

		while True:
			if current_node.is_leaf==True: break

			key_tmp=current_node.key
			child_tmp=current_node.child

			for kk in range(len(key_tmp)):
				if key<key_tmp[kk]:
					current_node=child_tmp[kk]
					break
				elif kk==len(key_tmp)-1 and key>=key_tmp[kk]:
					current_node=child_tmp[kk+1] 

		return current_node

	def insert(self, key, value):
		#print(key)
		current_node=self.search_node(key)

		signal=False
		for i in range(len(current_node.key)):
			if current_node.key[i]==key: 
				signal=True
				break

		if signal==True: return

		current_node.set_key_value(key,value)
		if len(current_node.key)>=max_degree:
			left,right=current_node.split()
			if current_node.parent==None:#부모가 없다는게 root라는 소리임
				new_parent=node()
				new_parent.key.append(right.key[0])
				new_parent.child.append(left)
				new_parent.child.append(right)
				left.parent=right.parent=new_parent
				new_parent.is_leaf=False
				self.root=new_parent
			else:
				current_node.parent.set_key_node(right.key[0], left,right)
				current_node=left.parent

				while True:
					if current_node.parent==None: self.root=current_node

					if len(current_node.key)<max_degree: break
					mid=int(len(current_node.key)/2)
					new_key=current_node.key[mid]
					left,right=current_node.split()
					if current_node.parent==None:#부모가 없다는게 root라는 소리임
						new_parent=node()
						new_parent.key.append(new_key)
						new_parent.child.append(left)
						new_parent.child.append(right)
						left.parent=right.parent=new_parent
						new_parent.is_leaf=False
						current_node=new_parent
					else:
						current_node.parent.set_key_node(new_key, left,right)
						current_node=left.parent

	def read_index_file(self,file_name):
		global node_list_r, max_degree
		index_f=open(file_name, 'r')
		cnt=-1
		node_num=-1
		node_child_num=[]
		node_right_num=[]

		while True:
			line=index_f.readline()
			if not line: break
			if cnt==-1: max_degree=int(line)
			
			elif cnt==0: 
				new=node()
				node_list_r.append(new)
				node_num=int(line)
				node_list_r[node_num].node_num=node_num
			
			elif cnt==1:
				if int(line)==0: node_list_r[node_num].is_leaf=False
				else: node_list_r[node_num].is_leaf=True
			
			elif cnt==2:
				tmp=line.split(" ")
				for i in range(len(tmp)-1):
					node_list_r[node_num].key.append(int(tmp[i]))		
			
			elif cnt==3:
				if node_list_r[node_num].is_leaf==True:
					tmp=line.split(" ")
					for i in range(len(tmp)-1):
						node_list_r[node_num].value.append(int(tmp[i]))			
			
			elif cnt==4:
				tmp=line.split(" ")
				arr=[]
				scope=len(tmp)-1
				if scope==0: scope=1
				for i in range(scope):
					arr.append(int(tmp[i]))
				node_child_num.append(arr)


			elif cnt==5:
				tmp=int(line)
				if tmp!=-1: node_list_r[node_num].parent=node_list_r[tmp]
			
			elif cnt==6:
				tmp=int(line)
				node_right_num.append(tmp)
			
			cnt=(cnt+1)%7

		index_f.close()

		for i in range(len(node_list_r)):
			if node_child_num[i][0]!=-1:
				for j in range(len(node_child_num[i])): 
					turn=node_child_num[i][j]
					node_list_r[i].child.append(node_list_r[turn])

			if node_right_num[i]!=-1:
				turn=node_right_num[i]
				node_list_r[i].right_child=node_list_r[turn]
		
		if len(node_list_r)>0: self.root=node_list_r[0]

	def write_index_file(self,file_name):
		global node_list_w
		index_f=open(file_name,'w')
		index_f.write("%d\n" %max_degree)

		for i in range(len(node_list_w)):
			now=node_list_w[i]
			index_f.write("%d" %now.node_num)
			index_f.write("\n")

			leaf=0
			if now.is_leaf==True: leaf=1
			index_f.write("%d" %leaf)
			index_f.write("\n")

			for i in range(len(now.key)):
				index_f.write("%d" %now.key[i])
				index_f.write(" ")
			index_f.write("\n")
			#키가 없을 수는 없으니까!

			if len(now.value)==0: 
				index_f.write("-1")
				index_f.write("\n")
			else:
				for i in range(len(now.value)):
					index_f.write("%d " %now.value[i])
				index_f.write("\n")

			if len(now.child)==0: 
				index_f.write("-1")
				index_f.write("\n")
			else:
				for i in range(len(now.child)):
					index_f.write("%d " %now.child[i].node_num)

				index_f.write("\n")			

			if now.parent==None:index_f.write("-1")
			else: index_f.write("%d" %now.parent.node_num)
			index_f.write("\n")

			if now.right_child==None:index_f.write("-1")
			else: index_f.write("%d" %now.right_child.node_num)
			index_f.write("\n")
		index_f.close()

	def make_node_list(self):
		global node_list_w
		leftmost_node=self.root
		current_node=self.root
		node_list_w.append(current_node)

		while True:
			
			if len(leftmost_node.child)==0: break

			leftmost_node=leftmost_node.child[0]
			current_node=leftmost_node

			while True:
				node_list_w.append(current_node)
				if current_node.right_child==None: break

				current_node=current_node.right_child

		for i in range(len(node_list_w)): 
			node_list_w[i].node_num=i

	def find_key(self, key):
		current_node=self.root

		while True:
			if current_node.is_leaf==True: break

			key_tmp=current_node.key
			child_tmp=current_node.child

			for i in range(len(key_tmp)):
				print("%d"%key_tmp[i], end='')
				if i<len(key_tmp)-1:print(",",end='')
			print("\n",end='')

			for kk in range(len(key_tmp)):
				if key<key_tmp[kk]:
					current_node=child_tmp[kk]
					break
				elif kk==len(key_tmp)-1 and key>=key_tmp[kk]:
					current_node=child_tmp[kk+1] 

		use_key=current_node.key
		use_value=current_node.value
		is_find=False

		for i in range(len(current_node.key)):
			if use_key[i]==key:
				print(use_value[i])
				is_find=True

		if is_find==False: print("NOT FOUND")

	def find_range(self, left, right):
		current_node=self.search_node(left)
		sign=True
		while sign:
			key_tmp=current_node.key
			value_tmp=current_node.value
			for i in range(len(key_tmp)):
				if key_tmp[i]>=left and key_tmp[i]<=right:
					ret=[key_tmp[i],value_tmp[i]]
					print("%d,%d"%(ret[0],ret[1]))

				elif key_tmp[i]>right:
					sign=False
					break

			if current_node.right_child==None: sign=False
			else: current_node=current_node.right_child

	def find_and_change_key(self, start_node, find_key, change_key):
		node_=start_node
		done=False
		while node_!=None:
			if done==True: break

			for i in range(len(node_.key)):
				if find_key==node_.key[i]:
					node_.key[i]=change_key

			node_=node_.parent

	def delete(self,key):
		current_node=self.search_node(key)
		parent_node=current_node.parent
		place_key=-1#key에 해당하는건 어느위치에 있는가?
		for i in range(len(current_node.key)):
			if current_node.key[i]==key:
				place_key=i
				break

		if place_key==-1: return
		############delete in leaf node###############
		###현재 노드에서 underflow 없을 때
		if current_node.underflow_predict()==False:
			current_node.delete_key_value(place_key)

			if place_key==0:
				self.find_and_change_key(current_node,key,current_node.key[0])

		else:
			left=None
			right=None
			using_node=None
			leftright=False #true면 왼쪽꺼 아니면 오른쪽꺼
			need_merge=False
			left_parent=-1
			right_parent=-1
			#key가 하나일 때 예외처리 필요함!

			for i in range(len(parent_node.key)-1):
				a=parent_node.key[i]
				b=parent_node.key[i+1]

				if key>=a and key<b: 
					left=parent_node.child[i]
					left_parent=i
					right_parent=i+1

			#양쪽 끝 점 처리하기#
			if left_parent==-1 and right_parent==-1:
				if key<parent_node.key[0]:
					right_parent=0
					right=parent_node.child[1]
				elif key>=parent_node.key[len(parent_node.key)-1]:
					left_parent=len(parent_node.key)-1
					left=parent_node.child[left_parent]

			######################################

			if left!=None and left.underflow_predict()==False: leftright=True
			elif right!=None and right.underflow_predict()==False: leftright=False
			else:
				need_merge=True
				if left==None:leftright=False
				else: leftright=True
			
			index_key=-1

			############사용할 노드, 그 노드가 왼쪽껀지 오른쪽껀지, 병합이 필요한지 아닌지#############
			if leftright==True and need_merge==False:
				current_node.delete_key_value(place_key)
				##이건 값을 앞에 집어넣어야되서 길어졌다
				keys=[]
				values=[]
				length=len(left.key)
				new_top=left.key[len(left.key)-1]
				keys.append(new_top)
				values.append(new_top)
				keys=keys+current_node.key
				values=values+current_node.value
				current_node.key=keys
				current_node.value=values
				##왼쪽노드 값 갱신
				left.key=left.key[:length-1]
				left.value=left.value[:length-1]
				#위쪽 노드들 키값 갱신
				#1
				parent_node.key[left_parent]=new_top
				#2
				self.find_and_change_key(parent_node,key,current_node.key[place_key])

			elif leftright==False and need_merge==False:
				current_node.delete_key_value(place_key)
				#이미 지웠다니까!
				current_node.key.append(right.key[0])
				current_node.value.append(right.value[0])
				#위쪽 노드들 키값 갱신
				#1
				parent_node.key[right_parent]=right.key[1]
				#2
				self.find_and_change_key(parent_node,key,current_node.key[place_key])
				##오른쪽 노드 값 갱신
				right.key=right.key[1:]
				right.value=right.value[1:]

			elif leftright==True and need_merge==True:
				current_node.delete_key_value(place_key)
				new=merge_leaf(left,current_node)
				#parent key 갱신
				index_key=parent_node.delete_key(left_parent)

				#parent child 갱신
				parent_node.delete_child(left_parent+1)
				parent_node.child[left_parent]=new			

			elif leftright==False and need_merge==True:
				current_node.delete_key_value(place_key)
				new=merge_leaf(current_node,right)
				#parent key 갱신
				index_key=parent_node.delete_key(right_parent)
				#parent child 갱신
				parent_node.delete_child(right_parent+1)
				parent_node.child[right_parent]=new				
				self.find_and_change_key(parent_node,key,new.key[place_key])

			if need_merge==True: self.change_index(parent_node,index_key)

	def change_index(self, current_node, key):
		#이제 여기서부터 index node들을 처리해주자
		if current_node.underflow()==False: return
		elif current_node.parent==None: return
		parent_node=current_node.parent		
		left=None
		right=None
		using_node=None
		leftright=False #true면 왼쪽꺼 아니면 오른쪽꺼
		need_merge=False
		left_parent=-1
		right_parent=-1
		#key가 하나일 때 예외처리 필요함!

		for i in range(len(parent_node.key)-1):
			a=parent_node.key[i]
			b=parent_node.key[i+1]
			if key>=a and key<b: 
				left=parent_node.child[i]
				left_parent=i
				right_parent=i+1

			#양쪽 끝 점 처리하기#
		if left_parent==-1 and right_parent==-1:
			if key<parent_node.key[0]:
				right_parent=0
				right=parent_node.child[1]
			elif key>=parent_node.key[len(parent_node.key)-1]:
				left_parent=len(parent_node.key)-1
				left=parent_node.child[left_parent]

			######################################

		if left!=None and left.underflow_predict()==False: leftright=True
		elif right!=None and right.underflow_predict()==False: leftright=False
		else:
			need_merge=True
			if left==None:leftright=False
			else: leftright=True

		index_key=-1
		if leftright==True and need_merge==False:
			last=len(left.key)
			sub_key=left.key[last-1]
			sub_child=left.child[last]
			split_key=parent_node.key[left_parent]
			parent_node.key[left_parent]=sub_key
			
			left.key=left.key[:last-1]
			left.child=left.child[:last]

			key_tmp=[]
			key_tmp.append(split_key)
			key_tmp=key_tmp+current_node.key
			current_node.key=key_tmp
			child_tmp=[]
			child_tmp.append(sub_child)
			child_tmp=child_tmp+current_node.child
			current_node.child=child_tmp

		if leftright==False and need_merge==False:
			sub_key=right.key[0]
			sub_child=right.child[0]
			split_key=parent_node.key[right_parent]
			parent_node.key[right_parent]=sub_key

			right.key=right.key[1:]
			right.child=right.child[1:]

			current_node.key.append(split_key)
			current_node.child.append(sub_child)

		if leftright==True and need_merge==True:
			del_=parent_node.key[left_parent]
			new=merge_index(left,current_node,del_)
			index_key=parent_node.key[left_parent]
			key_tmp=parent_node.key[:left_parent]+parent_node.key[left_parent+1:]
			child_tmp=parent_node.child[:left_parent]+parent_node.child[left_parent+1:]
			child_tmp[left_parent]=new
			parent_node.key=key_tmp
			parent_node.child=child_tmp
			#self.traversal(self.root)
			for i in range(len(new.child)):
				new.child[i].parent=new

		if leftright==False and need_merge==True:
			del_=parent_node.key[right_parent]
			new=merge_index(current_node,right,del_)
			index_key=parent_node.key[right_parent]
			key_tmp=parent_node.key[:right_parent]+parent_node.key[right_parent+1:]
			child_tmp=parent_node.child[:right_parent]+parent_node.child[right_parent+1:]
			child_tmp[right_parent-1]=new
			parent_node.key=key_tmp
			parent_node.child=child_tmp
			for i in range(len(new.child)):
				new.child[i].parent=new
		
		if len(parent_node.key)==0 and parent_node.parent==None:
			new.parent=None
			parent_node=new
			self.root=new

		if need_merge==True: self.change_index(parent_node,index_key)

def merge_leaf(left, right):
	#이미 지웠다고 가정하고 병합하자
	#parent 똑같잖아
	left.key=left.key+right.key
	left.value=left.value+right.value
	left.right_child=right.right_child
	return left

def merge_index(left, right, split_key):
	#delete_key함수로 key만 지웠다고 가정하고 병합하자
	left.is_leaf=False
	left.key.append(split_key)
	left.key=left.key+right.key
	left.child=left.child+right.child
	left.right_child=right.right_child
	return left	

def main(argv):
	global max_degree
	#argv[1]-> 명령의 종류가 저장됨
	if argv[1]=="-c":
		index_f=open(argv[2],'w')
		index_f.write(argv[3])
		index_f.close()

	if argv[1]=="-s":#그냥 search
		search_key=int(argv[3])
		Tree=bptree()
		Tree.read_index_file(argv[2])
		Tree.find_key(search_key)

	if argv[1]=="-r":#범위 search
		begin=int(argv[3])
		end=int(argv[4])
		Tree=bptree()
		Tree.read_index_file(argv[2])
		Tree.find_range(begin,end)

	if argv[1]=="-i":
		Tree=bptree()
		Tree.read_index_file(argv[2])
		input_key=[]
		input_val=[]
		data_f=open(argv[3],'r')
		while True:
			line=data_f.readline()
			if not line: break
			sp=line.split(',')
			input_key.append(int(sp[0]))
			input_val.append(int(sp[1]))

		for i in range(len(input_key)):
			Tree.insert(input_key[i], input_val[i])

		Tree.rightmost(Tree.root)

		Tree.make_node_list()
		Tree.write_index_file(argv[2])
		#Tree.traversal(Tree.root)

	if argv[1]=="-d":
		Tree=bptree()
		Tree.read_index_file(argv[2])
		input_key=[]
		data_f=open(argv[3],'r')
		while True:
			line=data_f.readline()
			if not line: break
			input_key.append(int(line))	

		for i in range(len(input_key)):
			Tree.delete(input_key[i])

		Tree.rightmost(Tree.root)
		Tree.make_node_list()
		Tree.write_index_file(argv[2])
		#Tree.traversal(Tree.root)

if __name__== "__main__":
	main(sys.argv)