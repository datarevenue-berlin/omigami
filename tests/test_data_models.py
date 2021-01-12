def test_n_features(dataset):
    assert dataset.n_features == 12


def test_input_data_slice(dataset):
    assert dataset[:5, 3:7].X.shape == (5, 4)
    assert dataset[[1,2,5], [3,4,7]].X.shape == (3, 3)
