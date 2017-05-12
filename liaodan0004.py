from multiprocessing import Process, Queue
from multiprocessing import Pool
import os, time, random, threading
import subprocess
import multiprocessing

print('============进程（Process）和线程（Thread）=========')
# def run_pro(name):
# 	print('Run child process %s (%s)...' % (name, os.getpid()))

# if __name__ == '__main__':
# 	print('Parent process %s.' % os.getpid())
# 	p = Process(target = run_pro, args = ('test',))

# 	print('Child process will start.')
# 	p.start()
# 	p.join()
# 	print('Child process end.')

# def long_time_task(name):
# 	print('Run task %s (%s)...' % (name, os.getpid()))
# 	start = time.time()
# 	time.sleep(random.random()*3)
# 	end = time.time()
# 	print('Task %s runs %0.2f seconds.' % (name, (end - start)))

# if __name__ == '__main__':
# 	print('Parent process %s.' % os.getpid())
# 	p = Pool(4)
# 	for i in range(5):
# 		p.apply_async(long_time_task, args = (i,))
# 	print('Waiting for all subprocesses done...')
# 	p.close()
# 	# 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
# 	p.join()
# 	print('All subprocesses done.')

# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code:', r)

# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q = mx\npython.org\nexit\n')
# print(output.decode('gbk'))
# print('Exit code:', p.returncode)

# # 写数据进程执行的代码
# def write(q):
# 	print('Process to write: %s' % os.getpid())
# 	for value in ['A', 'B', 'C']:
# 		print('Put %s to queue...' % value)
# 		q.put(value)
# 		time.sleep(random.random())

# # 读数据进程执行的代码
# def read(q):
# 	print('Process to read: %s' % os.getpid())
# 	while True:
# 		value = q.get(True)
# 		print('Get %s from queue.' % value)

# if __name__ == '__main__':
# 	# 父进程创建Queue，并传给各个子进程:
# 	q = Queue()
# 	pw = Process(target = write, args = (q,))
# 	pr = Process(target = read, args = (q,))
# 	# 启动子进程pw，写入：
# 	pw.start()
# 	# 启动子进程pr，读取：
# 	pr.start()
# 	# 等待pw 结束：
# 	pw.join()
# 	# pr 进程里是死循环，无法等待其结束，只能强行终止
# 	pr.terminate()

# threading.current_thread() 函数永远返回的是当前线程的实例。
# def loop():
# 	print('thread %s is running...' % threading.current_thread().name)
# 	n = 0
# 	while n < 5:
# 		n = n + 1
# 		print('thread %s >>> %s' % (threading.current_thread().name, n))
# 		time.sleep(1)
# 	print('thread %s ended.' % threading.current_thread().name)	

# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target = loop, name = 'LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)


# 这是你的银行存款
# balance = 0
# lock = threading.Lock()

# def change_it(n):
# 	# 先存后取，结果应该为0
# 	global balance
# 	balance = balance + n
# 	balance = balance - n

# # 当多个线程同时执行lock.acquire() 时，
# # 只有一个线程能成功获取锁，然后继续执行代码
# # 其他线程就继续等待知道获得锁为止
# def run_thread(n):
# 	for i in range(1000000):
# 		lock.acquire()
# 		# 使用try...finally 来确保锁一定会被释放
# 		try:
# 			# 放心地改吧：
# 			change_it(n)
# 		finally:
# 			# 改完了一定要释放锁：
# 			lock.release()

# t1 = threading.Thread(target = run_thread, args = (5,))
# t2 = threading.Thread(target = run_thread, args = (8,))
# t1.start()
# t2.start()

# t1.join()
# t2.join()
# print(balance)

def loop():
	x = 0
	while True:
		x = x ^ 1

for i in range(multiprocessing.cpu_count()):
	t = threading.Thread(target = loop)
	t.start()