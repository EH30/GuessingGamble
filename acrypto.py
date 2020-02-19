class AbcEncrypt:
    def encrypt(self, plaintext):
        output_strs = ""
        texts = list(plaintext)
        word_list = {"0":"F", "1":"A", "2":"G", "3":"H", "4":"K", "5":"C", "6":"B", "7":"E", "8":"N", "9":"J"}

        for i in texts:
            output_strs += word_list[i]
        
        return output_strs[::-1]
    

    def decrypt(self, encryptedText):
        output_strs = ""
        texts = list(encryptedText)
        word_list = {"F":"0", "A":"1", "G":"2", "H":"3", "K":"4", "C":"5", "B":"6", "E":"7", "N":"8", "J":"9"}

        for i in texts[::-1]:
            output_strs += word_list[i]
        
        return output_strs

