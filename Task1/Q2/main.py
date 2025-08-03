class Codec:
    def encode(self, commands):
        encoded = []
        for str in commands:
            ln = len(str)
            encoded.append(f"{ln}:{str}")
        return "".join(encoded)
    
    def decode(self, encoded):
        decode = []
        i = 0
        while i < len(encoded):
            j = encoded.find(':', i)
            if j == -1:
                break
            l = j + 1
            r = l + int(encoded[i:j])
            decode.append(encoded[l:r])
            i = r
        return decode
    

if __name__ == "__main__":
    lst = ["Push","Box,box","Push","Overtake", "", "F1: white"]
    print(f"Original list: {lst}\n")
    codec = Codec()
    enc = codec.encode(lst)
    print(f"Enoded list: {enc}\n")
    dec = codec.decode(enc)
    print(f"Decoded string: {dec}\n")
    
    if dec == lst:
        print("GGWP")
    else:
        print("BETTER LUCK NEXT TIME")