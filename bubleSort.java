class bubleSort {
	public static void main(String[] args) {
		int[] array = {2,3,5,6,8,7,4,3,6,5,1,2,99,0,1,-5};
		int count = array.length - 1;
		boolean isSwap;

		do {
			isSwap = false;
			for (int i = 0; i < count; i++) {
				if (array[i] > array[i + 1]) {
					int temp = array[i];
					array[i] = array[i + 1];
					array[i + 1] = temp;
					isSwap = true;
				}
			}
			count--;
		} while(count > 0);

		for (var item: array) {
			System.out.print(item + " ");
		}
		System.out.println();
	}
}
