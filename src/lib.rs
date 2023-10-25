use crumsort::ParCrumSort;

wai_bindgen_rust::export!("crum-sort.wai");

struct CrumSort;

impl crum_sort::CrumSort for CrumSort {
    fn par_crumsort_u8(mut arr: Vec<u8>) -> Vec<u8> {
        arr.par_crumsort();
        arr
    }

    fn par_crumsort_u16(mut arr: Vec<u16>) -> Vec<u16> {
        arr.par_crumsort();
        arr
    }

    fn par_crumsort_u32(mut arr: Vec<u32>) -> Vec<u32> {
        arr.par_crumsort();
        arr
    }

    fn par_crumsort_u64(mut arr: Vec<u64>) -> Vec<u64> {
        arr.par_crumsort();
        arr
    }

    fn par_crumsort_i8(mut arr: Vec<i8>) -> Vec<i8> {
        arr.par_crumsort();
        arr
    }

    fn par_crumsort_i16(mut arr: Vec<i16>) -> Vec<i16> {
        arr.par_crumsort();
        arr
    }

    fn par_crumsort_i32(mut arr: Vec<i32>) -> Vec<i32> {
        arr.par_crumsort();
        arr
    }

    fn par_crumsort_i64(mut arr: Vec<i64>) -> Vec<i64> {
        arr.par_crumsort();
        arr
    }
}
