from electricity_bill import units_cost, fixed_charge, total_bill, gst, final_bill


def test_units_cost_100():
    assert units_cost(100) == 500


def test_units_cost_zero():
    assert units_cost(0) == 0


def test_units_cost_one():
    assert units_cost(1) == 5


def test_fixed_charge():
    assert fixed_charge() == 60


def test_total_bill_100():
    assert total_bill(100) == 560


def test_total_bill_zero_units():
    assert total_bill(0) == 60


def test_gst_on_550():
    assert gst(550) == 27.5


def test_gst_zero():
    assert gst(0) == 0


def test_final_bill_100():
    assert final_bill(100) == 588


def test_final_bill_zero_units():
    assert final_bill(0) == 63