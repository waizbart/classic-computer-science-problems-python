from stack import Stack

test_cases = [
    {
        "input": ["2", "1", "+", "3", "*"],
        "result": 9.0
    },
    {
        "input": ["4", "13", "5", "/", "+"],
        "result": 6.0
    }
]



for test in test_cases:
    duracell = Stack()
    
    in_list = test["input"]
    expected_result = test["result"]
    
    for item in in_list:
        if item.isdigit():
            duracell.push(int(item))
        else:
            n2 = duracell.pop()
            n1 = duracell.pop()
            
            if item == "+":
                duracell.push(int(n2 + n1))
            elif item == "-":
                duracell.push(int(n2 - n1))
            elif item == "/":
                duracell.push(float(n1 / n2))
            else:
                duracell.push(float(n2 * n1))
                
    r = duracell.peek()
    
    assert r == expected_result
    
    print("Teste", in_list)
    print("Resultado: ", r)
    print("Passou")
                
