from double_linked_list import DoubleLinkedList
# Tests that a new empty list is created
def test_create_empty_list():
    """Tests that a new empty list is created"""
    dll = DoubleLinkedList()
    assert dll.head is  None
    assert dll.tail is None
    assert dll.length() == 0

# Tests that a node is inserted at the beginning of the list
def test_insert_at_beginning():
    """Tests that a node is inserted at the beginning of the list"""
    dll = DoubleLinkedList()
    dll.insert_at_beginning(1)
    assert dll.head.data == 1
    assert dll.tail.data == 1
    assert dll.length() == 1
    dll.insert_at_beginning(2)
    assert dll.head.data == 2
    assert dll.tail.data == 1
    assert dll.length() == 2

# Tests that a node is inserted at the end of the list
def test_insert_at_end():
    """Tests that a node is inserted at the end of the list"""
    dll = DoubleLinkedList()
    dll.inset_at_end(1)
    assert dll.head.data == 1
    assert dll.tail.data == 1
    assert dll.length() == 1
    dll.inset_at_end(2)
    assert dll.head.data == 1
    assert dll.tail.data == 2
    assert dll.length() == 2
    
# Tests that the first node of the list is deleted
def test_delete_first_node():
    """Tests that the first node of the list is deleted"""
    dll = DoubleLinkedList()
    dll.insert_at_beginning(1)
    dll.insert_at_beginning(2)
    dll.delete_first_node()
    assert dll.head.data == 1
    assert dll.tail.data == 1
    assert dll.length() == 1
    dll.delete_first_node()
    assert dll.head is None
    assert dll.tail is None
    assert dll.length() == 0

# Tests that a node cannot be inserted at an invalid index
def test_insert_at_invalid_index():
    """Tests that a node cannot be inserted at an invalid inde"""
    dll = DoubleLinkedList()
    dll.insert_node_at_meddle(1, -1)
    assert dll.head is None
    assert dll.tail is None
    assert dll.length() == 0
    dll.insert_node_at_meddle(1, 1)
    assert dll.head is None
    assert dll.tail is None
    assert dll.length() == 0