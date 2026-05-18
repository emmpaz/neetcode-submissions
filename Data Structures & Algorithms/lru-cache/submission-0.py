class ListNode:

    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cur = 0
        self.hm = {}
        self.dh = ListNode()
        self.dt = ListNode()

        self.dh.next = self.dt
        self.dt.prev = self.dh
        

    def get(self, key: int) -> int:
        if not key in self.hm:
            return -1
        else:
            node = self.hm[key]

            if node.prev == self.dh:
                return node.val

            #remove
            node.prev.next = node.next
            node.next.prev = node.prev

            #add
            tmp = self.dh.next
            
            self.dh.next = node
            node.prev = self.dh
            node.next = tmp
            tmp.prev = node

            return node.val

    def put(self, key: int, value: int) -> None:
            
            if key in self.hm:
                node = self.hm[key]
                node.val = value

                #remove
                node.prev.next = node.next
                node.next.prev = node.prev

                #add
                tmp = self.dh.next
                
                self.dh.next = node
                node.prev = self.dh
                node.next = tmp
                tmp.prev = node
            else:
                node = ListNode(key, value)
                self.hm[key] = node

                tmp = self.dh.next
                self.dh.next = node
                node.prev = self.dh
                node.next = tmp
                tmp.prev = node
                self.cur += 1

                if self.cur > self.cap:
                    remove = self.dt.prev
                    del self.hm[remove.key]
                    
                    remove.prev.next = self.dt
                    self.dt.prev = remove.prev
                    self.cur -= 1









