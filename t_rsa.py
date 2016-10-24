#!/bin/evn python
#coding: utf-8

"""
这里使用pycrypto库
安装方法:
#pip install rsa 
#pip install pycrypto
#pip install Crypto

openssl genrsa -out t_rsa_private.pem 1024
openssl rsa -in t_rsa_private.pem -pubout -out t_rsa_public.pem

openssl pkcs8 -topk8 -inform PEM -in t_rsa_private.pem -outform PEM -nocrypt -out private.pem

"""
import sys
import time
import traceback
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
import base64
import rsa
import json
import Crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES
from Crypto.Hash import SHA
from Crypto.Hash import SHA256




#'--------------------------------------------'
BS = AES.block_size
pad_data = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad_data = lambda s: s[0: -ord(s[-1])]

class AESCrypt(object):
    """ AES的加密方法 """
    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_CBC
     
    #加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数
    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        #这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用
        length = 16
        count = len(text)
        add = length - (count % length)
        text = text + ('\0' * add)
        ciphertext = cryptor.encrypt(text)
        return base64.b64encode(ciphertext)
     
    #解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode,self.key)
        plain_text = cryptor.decrypt(base64.b64decode(text))
        return plain_text.rstrip('\0')

    def encrypt_iv(self, data, iv):
        aes = AES.new(self.key, AES.MODE_CBC, base64.b64decode(iv))
        data = pad_data(data)
        data_enc = aes.encrypt(data)
        return base64.b64encode(data_enc)

    def decrypt_iv(self, data, iv):
        aes = AES.new(self.key, AES.MODE_CBC, base64.b64decode(iv))
        data = aes.decrypt(base64.b64decode(data))
        return unpad_data(data)

class RSACrypt(object):
    """ RSA的加密方法 """
    def __init__(self, prifile='', pubfile='' , priVal='', pubVal=''  ):
        if prifile:
            with open(  prifile ) as  privatefile:
                p = privatefile.read()
                self.priv = rsa.PrivateKey.load_pkcs1(p)
        if priVal:
            #self.priv = rsa.PrivateKey.load_pkcs1(priVal) 
            self.priv = RSA.importKey(priVal)
        if pubfile:
            with open( pubfile) as publicfile:
                p = publicfile.read()
                # self.pub = rsa.PublicKey.load_pkcs1(p) 
                self.pub = rsa.PublicKey.load_pkcs1_openssl_pem(p)
        if pubVal:
            #self.pub = rsa.PublicKey.load_pkcs1(pubVal) 
            self.pub = RSA.importKey(pubVal)                        

    def encrypt(self, text):
        encrypted = rsa.encrypt(text, self.pub)
        return base64.b64encode(encrypted)

    def decrypt(self, text):
        decrypted = rsa.decrypt(base64.b64decode(text), self.priv)
        return decrypted

    def encrypt_pkcs(self, content):
        pubKeyEncrypt = self.pub
        #256 - 11 = 245 - 42 = 203
        #sha256 256 - 11 = 245 -55 = 190
        if len(content) > 190:
            encryptStr = ''
            for i in range(len(content) / 190 + 1):
                t = content[i * 190:(i + 1) * 190]
                encryptStr += PKCS1_OAEP.new(pubKeyEncrypt, hashAlgo=SHA256).encrypt(t)
                #encryptStr += PKCS1_OAEP.new(pubKeyEncrypt).encrypt(t)
                #print len(encryptStr), encryptStr
            return base64.b64encode(encryptStr)
        else:
            return base64.b64encode(PKCS1_OAEP.new(pubKeyEncrypt, hashAlgo=SHA256).encrypt(content))   
            #return base64.b64encode(PKCS1_OAEP.new(pubKeyEncrypt).encrypt(content))  
        
    def decrypt_pkcs(self, content):
        decryptData = ''
        content = base64.b64decode(content)
        #print content
        privatekey = self.priv
        for i in range(len(content) / 256):
            t = content[i * 256:(i + 1) * 256]
            decryptData += PKCS1_OAEP.new(privatekey, hashAlgo=SHA256).decrypt(t)
            #decryptData += PKCS1_OAEP.new(privatekey).decrypt(t)
            print len(decryptData), decryptData
        return decryptData 



if __name__ == '__main__':
    # aseKey = '1234567890123456'
    # print '------------------------------------------'
    # s = time.time()
    # pc = AESCrypt(aseKey)      #初始化密钥

    # text = '{"status": 0, "data": [{"attr": "tcp", "result": [{"host": "client.map.baidu.com", "list": [{"ip": "14.215.177.49", "port": 80}], "ttl": 3000}]}, {"priv": "", "attr": "udp", "result": [{"host": "client.map.baidu.com", "list": [{"ip": "61.136.173.30", "port": 80}, {"ip": "59.38.112.30", "port": 80}, {"ip": "119.146.74.30", "port": 80}, {"ip": "58.215.118.30", "port": 80}, {"ip": "222.216.229.30", "port": 80}], "ttl": 3000}]}], "check": 0}'


    # e = pc.encrypt(text)
    # d = pc.decrypt(e)                     
    # print 'AESCrypt encrypt:', e
    # print 'AESCrypt decrypt:', d
    # print 'cost:', (time.time() - s)
    # print '------------------------------------------'
    # exit()
    rsaC = RSACrypt('t_rsa_private.pem' , 't_rsa_public.pem')
    # text = '{"status": 0, "data": [{"attr": "tcp", "result": [{"host": "client.map.baidu.com", "list": [{"ip": "14.215.177.49", "port": 80}], "ttl": 3000}]}, {"priv": "", "attr": "udp", "result": [{"host": "client.map.baidu.com", "list": [{"ip": "61.136.173.30", "port": 80}, {"ip": "59.38.112.30", "port": 80}, {"ip": "119.146.74.30", "port": 80}, {"ip": "58.215.118.30", "port": 80}, {"ip": "222.216.229.30", "port": 80}], "ttl": 3000}]}], "check": 0}'
    
    text = 'dn=client.map.baidu.com&key=12312323242&method=1&svc=tieba'
    print 'text:', len(text), text 
    encrypt = rsaC.encrypt( text )
    print 'len(encrypt):', len(encrypt), encrypt    
    
    s = time.time()
    decrypt = rsaC.decrypt( encrypt )
    print 'decrypt:', decrypt
    print 'cost:', (time.time() - s) * 1000, 'ms'
    print '------------------------------------------'





