from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (8, 17, 27); PANEL = (16, 31, 43); INK = (239, 244, 238)
MUTED = (157, 181, 187); GOLD = (247, 188, 63); CYAN = (76, 211, 201)
RED = (237, 92, 76); BLUE = (95, 163, 229); GREEN = (125, 202, 142); ORANGE = (244, 139, 68)
im = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(im)
FP = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; FB = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def font(n, bold=False): return ImageFont.truetype(FB if bold else FP, n)
def text(x, y, s, n=12, c=INK, bold=False, anchor=None): d.text((x, y), s, font=font(n, bold), fill=c, anchor=anchor)
def box(x0, y0, x1, y1, fill=PANEL, outline=(52, 83, 96), r=8, w=2): d.rounded_rectangle((x0,y0,x1,y1), r, fill=fill, outline=outline, width=w)
def line(points, fill, width=2): d.line(points, fill=fill, width=width)

text(32,18,'THE TUESDAY ATLAS',34,GOLD,True); text(34,59,'24 NOVEMBER 2026  /  HUANG RETURNS TO NVIDIA — COP31: NO DEAL',13,MUTED,True); text(990,23,'V3',17,CYAN,True,'ra'); line((32,91,992,91),GOLD,3)
text(34,99,'HUANG RETURNS, NVIDIA ADDS $1 TRILLION, COP31 NO DEAL',14,INK,True); text(990,99,'39 STORIES  •  9 REGIONS',12,CYAN,True,'ra')

box(32,126,632,414,(15,38,55),(64,139,163),10,2); text(51,141,'LEAD / NEW YORK — MON 23 NOV',11,GOLD,True); text(51,162,'HUANG RETURNS TO NVIDIA',25,INK,True); text(51,199,'THE BOARD REINSTATED HIM UNANIMOUSLY',12,CYAN,True); text(51,223,'+31% IN ONE SESSION',20,GOLD,True); text(51,251,'≈$1.1T ADDED TO NVIDIA VALUE',18,INK,True); text(51,280,'Q3 REVENUE  $115.8B  /  +103% YoY',12,MUTED); text(51,300,'NASDAQ +6.5%  •  S&P 500 +4.7%',12,MUTED); text(51,320,'AMD +6.85%  •  TSMC +14.08%  •  GOLD +3.2%',10,MUTED)
gx,gy,gw,gh=51,350,550,46
for i in range(1,6): line((gx,gy+i*gh/5,gx+gw,gy+i*gh/5),(35,73,88),1)
for i in range(1,10): line((gx+i*gw/10,gy,gx+i*gw/10,gy+gh),(28,62,78),1)
pts=[(gx,gy+39),(gx+46,gy+37),(gx+91,gy+40),(gx+136,gy+31),(gx+186,gy+34),(gx+236,gy+25),(gx+286,gy+29),(gx+337,gy+18),(gx+385,gy+21),(gx+437,gy+9),(gx+492,gy+13),(gx+550,gy-7)]
line(pts,CYAN,5)
for x,y in pts[::2]: d.ellipse((x-3,y-3,x+3,y+3),fill=GOLD)
text(51,400,'NVIDIA  $164.92 CLOSE',11,CYAN,True); text(600,399,'+31.38%',12,GOLD,True,'ra')
d.rounded_rectangle((472,166,600,274),10,fill=(20,65,82),outline=CYAN,width=2)
for xx in (487,506,525,544,563,582): line((xx,156,xx,166),CYAN,3); line((xx,274,xx,284),CYAN,3)
for yy in (180,198,216,234,252): line((462,yy,472,yy),CYAN,3); line((600,yy,610,yy),CYAN,3)
d.ellipse((493,184,579,256),outline=GOLD,width=3); text(536,220,'N',38,GOLD,True,'mm'); line((441,288,441,207),GOLD,4); line((441,207,430,222),GOLD,4); line((441,207,452,222),GOLD,4)

box(648,126,992,414,(27,40,46),(116,141,141),10,2); text(666,141,'CO-LEAD / ANTALYA, TURKEY',11,GOLD,True); text(666,163,'COP31: NO DEAL',27,INK,True); text(666,199,'CLIMATE SUMMIT ENDS WITHOUT A PACT',11,RED,True)
ix0,iy0,ix1,iy1=666,225,974,362; d.rectangle((ix0,iy0,ix1,iy1),fill=(24,56,65),outline=(107,130,127),width=2); d.rectangle((ix0,318,ix1,iy1),fill=(39,72,70))
# A summit hall scene: delegates, climate placards, and a storm front over the globe.
d.ellipse((785,236,913,364),fill=(32,105,122),outline=(155,217,207),width=2); d.arc((800,252,894,342),190,350,fill=(111,207,154),width=6); d.arc((795,260,900,350),20,170,fill=(93,181,209),width=5); d.polygon([(666,263),(718,241),(770,263),(770,274),(666,274)],fill=(70,78,77),outline=(138,151,137)); d.rectangle((674,274,764,318),fill=(54,69,68),outline=(132,146,132),width=2)
for x in (693,728,864,911):
 d.ellipse((x-7,300,x+7,314),fill=(211,165,123)); d.polygon([(x-11,314),(x+11,314),(x+15,350),(x-14,350)],fill=(206,137,43),outline=(242,198,106)); d.line((x-8,350,x-14,362),fill=(35,48,53),width=4); d.line((x+8,350,x+14,362),fill=(35,48,53),width=4)
d.rectangle((675,286,763,308),fill=(238,202,112),outline=GOLD,width=2); text(719,297,'ACT NOW',10,(34,55,57),True,'mm'); d.line((927,242,947,218),fill=(132,196,201),width=3); d.line((942,220,961,238),fill=(132,196,201),width=3)
text(667,372,'44 hours overtime; no final agreement',10,INK,True); text(667,390,'FIRST NO-DEAL COP SINCE 2009  •  $5.1–6.8T NEEDED',9,MUTED)

box(32,428,992,626,(10,41,54),(61,116,129),10,2); text(51,441,'WHERE THE DAY LANDED  /  REAL-LOCATION DOTS',12,CYAN,True); mx,my,mw,mh=51,469,922,126; d.rectangle((mx,my,mx+mw,my+mh),fill=(9,48,63),outline=(57,106,115),width=2)
for i in range(1,12): line((mx+i*mw/12,my,mx+i*mw/12,my+mh),(24,70,82),1)
for i in range(1,5): line((mx,my+i*mh/5,mx+mw,my+i*mh/5),(24,70,82),1)
continents=[[(75,520),(112,495),(168,500),(203,529),(179,550),(140,548),(109,570),(84,551)],[(222,492),(298,486),(380,501),(456,532),(524,544),(587,550),(553,568),(455,559),(381,545),(316,556),(270,539)],[(589,490),(666,484),(731,503),(789,518),(770,540),(714,530),(658,550),(612,535)],[(799,493),(890,500),(952,519),(954,548),(902,544),(856,529),(814,529)]]
for shape in continents: d.polygon(shape,fill=(42,85,79),outline=(102,150,125))
marks=[(345,550,'SENEGAL'),(295,505,'BRUSSELS'),(330,522,'DYMER'),(367,514,'BENGHAZI'),(473,511,'DELHI'),(556,523,'DOHA'),(611,545,'NYC ×8'),(682,566,'WELLINGTON'),(727,505,'ANTALYA'),(783,528,'Gaza'),(849,508,'TOKYO'),(913,560,'VANUATU')]
for x,y,label in marks: d.ellipse((x-4,y-4,x+4,y+4),fill=GOLD,outline=INK); text(x+7,y-7,label,8,INK,True)
text(53,602,'Nine regions: Southeast Asia  •  East Asia  •  South Asia  •  Middle East  •  Europe  •  Africa  •  North America  •  Oceania  •  Central Asia',9,MUTED)

box(32,637,992,716,(20,47,54),(66,139,137),9,2); text(51,648,'BESOK  /  WEDNESDAY 25 NOVEMBER 2026',12,CYAN,True); events=['UNSC open debate — New York','UEFA Champions League — Europe','Falcon 9 USSF-266 — Vandenberg','Progress MS-36 — Baikonur','FIFA U-17 Groups I–L — Doha','Consumer Confidence — New York','White House Turkey Pardon — DC']
for i,event in enumerate(events): x=52+(i%2)*458; y=673+(i//2)*12; d.ellipse((x,y+4,x+5,y+9),fill=GOLD); text(x+12,y,event,9,INK)

cards=[('SENEGAL','4 DEAD / DOZENS MISSING',RED),('NATO','3× KH-101 CONFIRMED',BLUE),('NEPAL','$2bn + RAIL',GOLD),('INDIA–NZ','DRAW',GREEN),('BTC','SPIKES TO $64.5K',CYAN),('ANTHROPIC','IPO  $83 → ~$86',ORANGE),('GAZA','CONTAMINATION',RED),('DYMER','9 DEAD',BLUE),('TRILATERAL','TRUMP–XI–PUTIN',GOLD),('U17 WORLD CUP','MATCHDAY 2',GREEN),('BAHRAIN','ESCALATION',CYAN),('VANUATU','M6.5 / 598km',GOLD),('MERKURY','SUNK CLAIM',RED),('WAYMO','FREEWAYS PAUSED',ORANGE)]
def icon(x,y,c,i):
 if i==0: d.ellipse((x,y,x+17,y+17),outline=c,width=2); line((x+8,y+1,x+8,y+16),c,1)
 elif i==1: d.polygon([(x+8,y),(x+17,y+4),(x+15,y+13),(x+8,y+17),(x+2,y+13),(x+1,y+4)],outline=c); line((x+5,y+9,x+8,y+12),c,2); line((x+8,y+12,x+14,y+6),c,2)
 elif i==2: line([(x,y+16),(x+6,y+6),(x+11,y+12),(x+16,y+3),(x+19,y+16)],c,2)
 elif i==3: line((x+3,y+2,x+15,y+16),c,3); d.ellipse((x+12,y+2,x+18,y+8),outline=c)
 elif i==4: d.ellipse((x+1,y,x+17,y+17),outline=c,width=2); text(x+4,y-1,'B',12,c,True)
 elif i==5: text(x+1,y-2,'A',18,c,True); line((x+2,y+16,x+16,y+16),c,2)
 elif i==6: d.polygon([(x+9,y),(x+17,y+17),(x+1,y+17)],outline=c); line((x+9,y+6,x+9,y+12),c,2)
 elif i==7: d.rectangle((x+1,y+7,x+17,y+14),outline=c,width=2); d.ellipse((x+3,y+12,x+7,y+17),fill=c); d.ellipse((x+12,y+12,x+16,y+17),fill=c)
 elif i==8: d.polygon([(x,y+10),(x+18,y+10),(x+14,y+16),(x+4,y+16)],outline=c); line((x+9,y+2,x+9,y+10),c,2)
 elif i==9: d.rectangle((x+2,y+5,x+16,y+17),outline=c); d.polygon([(x+1,y+5),(x+9,y),(x+17,y+5)],outline=c)
 elif i==10: d.polygon([(x+10,y),(x+3,y+10),(x+9,y+10),(x+6,y+17),(x+17,y+6),(x+10,y+6)],outline=c)
 elif i==11: line([(x,y+11),(x+4,y+7),(x+8,y+13),(x+13,y+4),(x+18,y+10)],c,2)
 elif i==12: d.polygon([(x,y+11),(x+18,y+11),(x+14,y+16),(x+4,y+16)],outline=c); line((x+9,y+2,x+9,y+11),c,2)
 else: d.rounded_rectangle((x+1,y+2,x+17,y+15),3,outline=c,width=2); line((x+5,y+16,x+13,y+16),c,2)
for i,(head,sub,col) in enumerate(cards):
 x=32+(i%4)*240; y=727+(i//4)*54; box(x,y,x+228,y+48,(16,32,44),(48,75,87),6,1); text(x+9,y+5,head,9,col,True); text(x+9,y+22,sub,8,INK,True); icon(x+195,y+15,col,i)
text(990,948,'14 ILLUSTRATED CARDS',9,MUTED,True,'ra'); line((32,963,992,963),GOLD,2); text(36,973,'DATE CHECK  •  TUESDAY 24 NOVEMBER 2026  •  39 DISTINCT THREADS  •  9 REGIONS  •  SOURCES LEDGER INCLUDED',9,INK,True)
im.save('entry.png',optimize=True)
