pub fn get_index_of_lowest<T: std::cmp::PartialOrd>(values: &[T]) -> usize {
    values
        .iter()
        .enumerate()
        .fold(0, |lowest, (index, val)| {
            if val < &values[lowest] { index } else { lowest }
        })
}

pub fn collect_array<T, I, const N: usize>(itr: I) -> [T; N]
where
    T: Default + Copy,
    I: IntoIterator<Item = T>,
{
    let mut res = [T::default(); N];
    for (it, elem) in res.iter_mut().zip(itr) {
        *it = elem
    }

    res
}