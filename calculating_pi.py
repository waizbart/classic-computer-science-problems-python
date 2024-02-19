def calculate_pi(n_terms: int) -> float:
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0
    
    for _ in range(n_terms):
        pi += numerator / denominator * operation
        
        denominator +=2
        operation *= -1
        
    print(pi)
    
calculate_pi(1000000)