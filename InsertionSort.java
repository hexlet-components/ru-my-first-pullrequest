
public class InsertionSort {
    /**
    * сортировка вставками по убыванию
    */
    public static void insertionSort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int x = arr[i];
            int j = i - 1;
            while (j >= 0 && arr[j] < x) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = x;
        }
    }

    /**
     * Сортировка вставками по возрастанию
     * @param list принимает список, элементы которого реализуют интерфейс {@code Comparable}
     * @throws UnsupportedOperationException если список неизменяемый (unmodifiable)
     */
    public static <T extends Comparable<? super T>> void insertionSort(List<T> list) {
        for (int i = 1; i < list.size(); i++) {
            T value = list.get(i);
            int j = i - 1;
            while (j >= 0 && list.get(j).compareTo(value) > 0) {
                list.set(j + 1, list.get(j));
                j--;
            }
            list.set(j + 1, value);
        }
    }
}
