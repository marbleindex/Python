# cProfile profiler practice to see the difference between loops and list comprehension.
import cProfile

def loop_algorithm():
	y = []
	for v in range(10000000) :
	    if v % 4 :
	        y += [v * 2]
	        
	       
def list_comp_algorithm():
	y = [v * 2 for v in range(10000000) if v % 4]


def main():
    loop_algorithm()
    list_comp_algorithm()

if __name__ == '__main__':
    cProfile.run('main()')


