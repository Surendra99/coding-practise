import java.util.Arrays;

public class MinHeap { 
  public int size=0;
  public int capacity =10;
  public int[] array = new int[capacity];

  public int getLeftChildIndex(int index){ return 2*index +1; }
  public int getRightChildIndex(int index){ return 2*index +2; }
  public int getParentIndex(int index){ return (index-1)/2; }

  public boolean hasLeftChild(int index){ return getLeftChildIndex(index) < size;}
  public boolean hasRightChild(int index){ return getRightChildIndex(index) < size;}
  public boolean hasParent(int index){ return getParentIndex(index) >= 0;}

  public int getLeftChild(int index){ return array[getLeftChildIndex(index)];}
  public int getRightChild(int index){ return array[getRightChildIndex(index)];}
  public int getParent(int index){ return array[getParentIndex(index)];}

  public void swap(int index1,int index2){
    int temp = array[index1];
    array[index1] = array[index2];
    array[index2] = temp;
  }

  public void increaseCapacity(){
    if(size == capacity){
      array = Arrays.copyOf(array, capacity*2);
      capacity*=2;
    }
  }

  public int peek(){
    if(size==0){throw new IllegalStateException();}
    return array[0];
  }

  public int poll(){
    if (size==0) throw new IllegalStateException();
    int item = array[0];
    array[0] = array[size-1];
    size--;
    heapifydown(0);
    return item;
  }

  public void add(int value){
    increaseCapacity();
    array[size++] = value;
    heapifyUp();
  }

  public void heapifyUp(){
    int index = size -1;
    while(hasParent(index) && getParent(index) > array[index]){
      swap(getParentIndex(index), index);
      index = getParentIndex(index);
    }
  }

  public void heapifydown(int index){
    while(hasLeftChild(index)){
      int smallerChildIndex = getLeftChildIndex(index);
      if(hasRightChild(index) && getRightChild(index) < array[smallerChildIndex]){
        smallerChildIndex = getRightChildIndex(index);
      }
      if(array[index] > array[smallerChildIndex]){
        swap(index, smallerChildIndex);
      }else{
        break;
      }
      index = smallerChildIndex;
    }
  }
  public void print(){
    for (int i=0;i<size;i++){
      System.out.print(array[i]+",");
    }
  }
  public static void main(String[] args) {
    MinHeap heap = new MinHeap();
    heap.add(10);
    heap.add(15);
    heap.add(5);

    heap.add(20);
    heap.poll();
    heap.print();
  }
}
