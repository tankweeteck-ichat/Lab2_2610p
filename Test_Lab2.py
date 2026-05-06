import Lab2

def test_find_min_max():
    expected_result = (1, 6)
    inputlist = [3,5,4,6,1,2]
    result = Lab2.find_min_max(inputlist)
    assert (result == expected_result)


def test_calc_average():
    expected_result = 21/6
    inputlist = [3,5,4,6,1,2]
    result = Lab2.calc_average(inputlist)
    assert ( round(result, 4) == round(expected_result, 4))


def test_calc_median_temperature():
    expected_result = 3.5
    inputlist = [3,5,4,6,1,2]
    result = Lab2.calc_median_temperature(inputlist)
    assert ( round(result, 4) == round(expected_result, 4))



