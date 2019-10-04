class Node{
   public int data;
   public Node next;
  
   public Node(int data){
     this.data = data;
   }

   public Node addNext(int data){
     Node n = new Node(data); 
     this.next = n;
     return n;
   }
 }

 class LinkedList{
   Node head;

   public Node addNode(int data){
     if(this.head == null){
       this.head = new Node(data);
       return this.head;
     }
     Node temp = this.head;
     while(temp.next !=null ){
       temp = temp.next;
     }
     temp.addNext(data);
     return temp;
   }

   public void removeDuplicates(){
     if(head == null){
       return;
     }
     Node p1 = head;
     while(p1 !=null){
       Node p2 = p1;
       while(p2 !=null && p2.next !=null){
         if(p1.data == p2.next.data){
           p2.next = p2.next.next;
         }
          p2 = p2.next;
       }
       p1 = p1.next;
     }
   }

   public void remove(int data){
    if(this.head.data == data){
      this.head = head.next;
      return;
    }
    Node temp = this.head;
    while(temp.next != null){
      if(temp.next.data == data){
        temp.next = temp.next.next;
      }
      temp = temp.next;
    }
   }

   public void removeAt(int data){
    if(data == 0){
      this.head = head.next;
      return;
    }
    
    Node temp = this.head;
    int counter = 0;
    while(temp.next!=null){
      counter++;
      if(counter == data){
        temp.next = temp.next.next;
      }
      temp = temp.next;
    }
   }

   public void print(){
     Node temp = head;
     while(temp!=null){
       System.out.print((temp.data));
       if(temp.next!=null){
          System.out.print("-");
       }
       temp = temp.next;
     }
     System.out.println();
   }

   public void reverse() {

     if(head == null)
      return;

      Node current = head, prev =null, next = null;
      while(current.next != null){
        next = current.next;
        current.next = prev;
        prev = current;
        current = next;
      }  
      current.next = prev;
      prev = current;
      head = prev;
   }
  
  public Node recursiveReverse(Node node){
    if(node == null){
      return;
    }
  }

 }

 class Main {
  public static void main(String[] args) {
    LinkedList list = new LinkedList();
    list.addNode(5);
    list.addNode(4);
    list.addNode(8);
    list.addNode(4);

    list.print();
    list.reverse();
    list.print();

    list.remove(8);
    list.print();

    System.out.println();
    list.removeDuplicates();
    list.print();

    System.out.println();
    list.removeAt(0);
    list.print();
  }
}
