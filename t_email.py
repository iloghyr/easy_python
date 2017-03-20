#coding=utf-8
import smtplib, mimetypes  
from email.mime.text import MIMEText  
from email.mime.multipart import MIMEMultipart  
from email.mime.image import MIMEImage  
from email.utils import COMMASPACE


#mailto = ['huangyourong@baidu.com']
def sendMail(mailfrom='digauto@baixdu.com', mailto='huangyourong@bxaidu.com', subject='x日志分析平台后台', content='测试内容'):
	msg = MIMEMultipart()  
	#msg['From'] = "auto@baidu.com"  
	#mailto = ['huangyourong@baidu.com']
	msg['To'] = COMMASPACE.join(mailto) 
	msg['Subject'] = subject  
	  
	#添加邮件内容  
	txt = MIMEText(content)  
	msg.attach(txt)  
	  
	# #添加二进制附件  
	# fileName = r'e:/PyQt4.rar'  
	# ctype, encoding = mimetypes.guess_type(fileName)  
	# if ctype is None or encoding is not None:  
	#     ctype = 'application/octet-stream'  
	# maintype, subtype = ctype.split('/', 1)  
	# att1 = MIMEImage((lambda f: (f.read(), f.close()))(open(fileName, 'rb'))[0], _subtype = subtype)  
	# att1.add_header('Content-Disposition', 'attachment', filename = fileName)  
	# msg.attach(att1)  
	  
	#发送邮件  
	smtp = smtplib.SMTP()
	smtp.connect('xxx.baixdu.com')  
	#smtp.login('from', '密码')  
	ret = smtp.sendmail(mailfrom, mailto, msg.as_string())  
	smtp.quit()  
	print '邮件发送成功' ,mailto
if __name__ == '__main__':
	mailto = ['huangyourong@baixdu.com']
	sendMail(mailto=mailto)