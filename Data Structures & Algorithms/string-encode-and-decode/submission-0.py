class Solution:

    def encode(self, strs: List[str]) -> str:
        # Tối ưu: Dùng mảng tạm thời để chứa các chuỗi đã nối, 
        # sau đó dùng "".join() sẽ nhanh hơn việc cộng chuỗi (+=) liên tục trong Python.
        encoded_strs = []
        for s in strs:
            encoded_strs.append(str(len(s)) + "#" + s)        
        return "".join(encoded_strs)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        
        while i < len(s):
            j = i
            # Tìm vị trí dấu '#'
            while s[j] != '#':
                j += 1
                
            # Lấy chiều dài
            length = int(s[i:j])
            
            # Cắt nội dung và thêm vào kết quả
            word = s[j + 1 : j + 1 + length]
            result.append(word)
            
            # Cập nhật con trỏ i sang cụm tiếp theo
            i = j + 1 + length
            
        return result