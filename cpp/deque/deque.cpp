#include <iostream>

using namespace std;

#define MAX_SIZE 10

class Deque {
    int array[MAX_SIZE];
    int head;
    int tail;
    int size;

public :
    Deque(int size) {
        head = -1;
        tail =-1;
        this->size = size;
    }

    bool isFull() {
        return ((head == 0 && tail == size -1) || (head == tail+1));
    }

    bool isEmpty() {
        return (head == -1);
    }

    void insertHead(int key) {
        if (isFull()) {
            std::cout << "Overflow! Deque is full" << std::endl;
            return;
        }

        // Case deque is empty
        if (head == -1) {
            head = 0;
            tail = 0;
        }
        else if (head == 0) {
            head = size -1;
        }
        else {
            head = head -1;
        }
        array[head] = key;
    }

    void insertTail(int key) {
        if (isFull()) {
            std::cout << "Overflow! Deque is full" << std::endl;
            return;
        }

        if (tail == -1) {
            head = 0;
            tail = 0;
        }
        else if (tail == size - 1) {
            tail = 0;
        }
        else {
            tail = tail + 1;
        }
        array[tail] = key;
    }

    void removeHead() {
        if (isEmpty()) {
            std::cout << "Underflow! Deque is empty!" << std::endl;
            return;
        }

        if (head == tail) {
            head = -1;
            tail = -1;
        }
        else {
            if (head == size -1) {
                head = 0;
            }
            else {
                head = head + 1;
            }
        }
    }
    
    void removeTail() {
        if (isEmpty()) {
            std::cout << "Underflow! Deque is empty!" << std::endl;
            return;
        }

        if (head == tail) {
            head = -1;
            tail = -1;
        }
        else if (tail == 0) {
            tail = size - 1;
        }
        else {
            tail = tail - 1;
        }
    }
    
    int getHead() {
        if (isEmpty()) {
            std::cout << "Underflow! Deque is empty!" << std::endl;
            return -1;
        }
        
        return array[head];
    }
    
    int getTail() {
        if (isEmpty()) {
            std::cout << "Underflow! Deque is empty!" << std::endl;
            return -1;
        }
        
        return array[tail];
    }
};

int main() {
    Deque dq(5);

    dq.insertTail(1);
    dq.insertTail(3);
    dq.insertHead(99);
    dq.insertHead(4);
    std::cout << dq.getTail() << std::endl;
    std::cout << dq.getHead() << std::endl;
    dq.removeTail();
    dq.removeTail();
    std::cout << dq.getTail() << std::endl;
    dq.removeTail();
    std::cout << "Underflow caused:" << std::endl;
    dq.removeTail();
    std::cout << dq.getHead() << std::endl;
    dq.insertHead(66);
    dq.insertHead(77);
    dq.insertHead(88);
    dq.insertHead(99);
    dq.insertHead(100);
    std::cout << dq.getHead() << std::endl;
    std::cout << "Overflow caused:" << std::endl;
    dq.insertHead(120);
    std::cout << dq.getHead() << std::endl;
}
