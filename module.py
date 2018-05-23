# Define a function
def world():
    print("Hello, World!")
    
    
class stats:
    def mean(self, x):
        return sum(x) / len(x)
    
    def median(self, v):
        n = len(v)
        sorted_v = sorted(v)
        mid = n // 2
        if n % 2 == 1:
            return sorted_v[mid]
        else:
            return (sorted_v[mid - 1] + sorted_v[mid]) / 2 
        
    def quantile(self, x, p):
        p_idx = int(p * len(x))
        return sorted(x)[p_idx]
    
    
if __name__ == '__main__':
    print('Script executed!')