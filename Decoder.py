class BitReader:
    def __init__(self, data:bytes):
        self.data = data
        self.position = 0

    @property
    def bits_remaining(self) -> int:
        return len(self.data) * 8 - self.position
    def readbits(self,count:int) -> int:
        if count<0:
            raise ValueError("HOW THE FUCK IS COUNT NEGATIVE?!")
        
        if count > self.bits_remaining:
            raise EOFError("Yo we outta bits bro")

        value = 0

        for _ in range(count):
            byte_index = self.position//8
            bit_index = 7 - (self.position%8)
            bit = (self.data[byte_index] >> bit_index) & 1
            value = (value << 1) | bit
            self.position += 1
        return value
if __name__ == "__main__":
    reader = BitReader(bytes[0b10110010])
    print(reader.read_bits(4))
    print(reader.read_bits(4))