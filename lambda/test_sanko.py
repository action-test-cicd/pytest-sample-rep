from sankou import is_prime

def test_is_prime():
    assert not is_prime(1)

def test_is_prime_2():
    assert is_prime(2)

def test_is_prime_3():
    assert is_prime(3)

def test_is_prime_4():
    #assert not is_prime(4)
    assert is_prime(4)

def test_is_prime_5():
    assert is_prime(5)

def test_is_prime_6():
    assert not is_prime(6)

def test_is_prime_7():
    assert is_prime(7)

def test_is_prime_8():
    assert not is_prime(8)

def test_is_prime_9():
    assert not is_prime(9)
    
def test_is_prime_10():
    assert not is_prime(10)