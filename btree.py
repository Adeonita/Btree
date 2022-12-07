from node import Node

class BTree:
  def __init__(self, t):
    self.root = Node(True)
    self.order = t

    # Insert node
  def insert(self, k):
    root = self.root
    rule = len(root.keys) == (2 * self.order) - 1

    if rule:
      temp = Node() 
      self.root = temp
      temp.child.insert(0, root)
      self.split_child(temp, 0)
      self.insert_non_full(temp, k)
    else:
      self.insert_non_full(root, k)

  def insert_non_full(self, node, k):
    i = len(node.keys) - 1
    if node.leaf:
      node.keys.append((None, None))
      while i >= 0 and k[0] < node.keys[i][0]: #Move a chave para a posição correta
        node.keys[i + 1] = node.keys[i]
        i -= 1
      node.keys[i + 1] = k
    else: #Se não for uma folha
      while i >= 0 and k[0] < node.keys[i][0]: #Encontra o filho que terá a nova chave
        i -= 1
      i += 1
      if len(node.child[i].keys) == (2 * self.order) - 1: #Quebra o nó quando o filho está cheio
        self.split_child(node, i) 
        if k[0] > node.keys[i][0]:
          i += 1
      self.insert_non_full(node.child[i], k) 

  def split_child(self, node, i):
    t = self.order
    node_child = node.child[i]
    leaf = Node(node_child.leaf)
    node.child.insert(i + 1, leaf)
    node.keys.insert(i, node_child.keys[t - 1])
    leaf.keys = node_child.keys[t: (2 * t) - 1]
    node_child.keys = node_child.keys[0: t - 1]
    if not node_child.leaf:
      leaf.child = node_child.child[t: 2 * t]
      node_child.child = node_child.child[0: t - 1]

  def print_tree(self, node, l=0):
    print (node)
    print("Level ", l, " ", len(node.keys), end=":")
    for i in node.keys:
      print(i, end=" ")
    print()
    l += 1
    if len(node.child) > 0:
      for i in node.child:
        self.print_tree(i, l)

  def search_key(self, key, node=None):
    if node is not None:
      i = 0
      while i < len(node.keys) and key > node.keys[i][0]:
        i += 1
      if i < len(node.keys) and key == node.keys[i][0]:
        return (node, i)
      elif node.leaf:
        return None
      else:
        return self.search_key(key, node.child[i])
    else:
      return self.search_key(key, self.root)


def main():
  B = BTree(2)

  for i in range(10):
    B.insert((i, 2 * i))

  B.print_tree(B.root)

  if B.search_key(8) is not None:
    print("\nFound")
  else:
    print("\nNot Found")


if __name__ == '__main__':
  main()