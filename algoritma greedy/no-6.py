# Nama: [Raka Restu Saputra]
# NIM: [247006111172]

import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(data):
    heap = [Node(char, freq) for char, freq in data.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def generate_codes(node, current_code="", codes={}):
    if node:
        if node.char is not None:
            codes[node.char] = current_code
        generate_codes(node.left, current_code + "0", codes)
        generate_codes(node.right, current_code + "1", codes)
    return codes

dataset = {'A': 5, 'B': 9, 'C': 12, 'D': 13, 'E': 16, 'F': 45}
root = build_huffman_tree(dataset)
huffman_codes = generate_codes(root)

print("Huffman Codes Table:")
print(f"{'Simbol':<8} | {'Freq':<6} | {'Code':<10} | {'Length':<8}")
print("-" * 40)
total_weighted_length = 0
for char, freq in dataset.items():
    code = huffman_codes[char]
    print(f"{char:<8} | {freq:<6} | {code:<10} | {len(code):<8}")
    total_weighted_length += freq * len(code)