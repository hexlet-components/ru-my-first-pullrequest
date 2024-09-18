// Шейкерная сортировка. Shaker sort

public class ShakerSort {
    public static void sort(int[] array) {
        if (array.length == 0 || array.length == 1) return; // Для пустых не работаем.
        int left = 0;
        int right = array.length - 1;
        while (left <= right) {
            for (int i = right; i > left; i--) {
                if (array[i] > array[i - 1]) {
                    swap(array, i, i - 1);
                }
            }
            left++;
            for (int i = left; i < right; i++) {
                if (array[i] < array[i + 1]) {
                    swap(array, i, i + 1);
                }
            }
            right--;
        }
    }

    private static void swap(int[] array, int i, int j) {
        int tmp = array[i];
        array[i] = array[j];
        array[j] = tmp;
    }
}
