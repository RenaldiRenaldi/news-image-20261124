from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (255, 255, 255); PANEL = (249, 250, 251); INK = (17, 24, 39)
MUTED = (107, 114, 128); GOLD = (184, 134, 11); CYAN = (30, 64, 175)
RED = (220, 38, 38); BLUE = (30, 64, 175); GREEN = (107, 114, 128); ORANGE = (184, 134, 11)
im = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(im)
# Deterministic paper grain keeps the large white field tactile while remaining
# below normal viewing contrast. It also survives downsampling as a clean tint.
grain_state = 1234567
for yy in range(H):
    for xx in range(W):
        grain_state = (1664525 * grain_state + 1013904223) & 0xffffffff
        if im.getpixel((xx, yy)) == BG and grain_state % 10 < 2:
            shade = 249 + ((grain_state >> 8) % 4)
            im.putpixel((xx, yy), (shade, shade + 1, shade + 2))
d = ImageDraw.Draw(im)
FP = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; FB = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def font(n, bold=False): return ImageFont.truetype(FB if bold else FP, n)
def text(x, y, s, n=12, c=INK, bold=False, anchor=None): d.text((x, y), s, font=font(n, bold), fill=c, anchor=anchor)
def box(x0, y0, x1, y1, fill=PANEL, outline=(229, 231, 235), r=8, w=1): d.rounded_rectangle((x0,y0,x1,y1), r, fill=fill, outline=outline, width=w)
def line(points, fill, width=2): d.line(points, fill=fill, width=width)

# Barely-visible horizontal drafting rules add depth without competing with the masthead.
for yy in range(12,88,8): line((32,yy,992,yy),(248,249,251),1)
text(32,18,'THE TUESDAY ATLAS',34,INK,True); text(34,59,'24 NOVEMBER 2026  /  HUANG RETURNS TO NVIDIA — COP31: NO DEAL',13,MUTED,True); text(990,23,'V5',17,BLUE,True,'ra')
line((32,91,992,91),GOLD,3)
text(34,99,'HUANG RETURNS, NVIDIA ADDS $1 TRILLION, COP31 NO DEAL',14,INK,True); text(990,99,'39 STORIES  •  9 REGIONS',12,GOLD,True,'ra')

box(32,126,632,414,(255,255,255),BLUE,10,2); text(51,141,'LEAD / NEW YORK — MON 23 NOV',11,GOLD,True); text(51,162,'HUANG RETURNS TO NVIDIA',25,INK,True); text(51,199,'THE BOARD REINSTATED HIM UNANIMOUSLY',12,BLUE,True); text(51,223,'+31% IN ONE SESSION',20,GOLD,True); text(51,251,'≈$1.1T ADDED TO NVIDIA VALUE',18,INK,True); text(51,280,'Q3 REVENUE  $115.8B  /  +103% YoY',12,MUTED); text(51,300,'NASDAQ +6.5%  •  S&P 500 +4.7%',12,MUTED); text(51,320,'AMD +6.85%  •  TSMC +14.08%  •  GOLD +3.2%',10,MUTED)
gx,gy,gw,gh=51,350,550,46
for i in range(1,6): line((gx,gy+i*gh/5,gx+gw,gy+i*gh/5),(229,231,235),1)
for i in range(1,10): line((gx+i*gw/10,gy,gx+i*gw/10,gy+gh),(243,244,246),1)
pts=[(gx,gy+39),(gx+46,gy+37),(gx+91,gy+40),(gx+136,gy+31),(gx+186,gy+34),(gx+236,gy+25),(gx+286,gy+29),(gx+337,gy+18),(gx+385,gy+21),(gx+437,gy+9),(gx+492,gy+13),(gx+550,gy-7)]
line(pts,CYAN,5)
for x,y in pts[::2]: d.ellipse((x-3,y-3,x+3,y+3),fill=GOLD)
# A fine gray market benchmark gives the dominant NVIDIA trace context.
bench=[(gx,gy+34),(gx+46,gy+35),(gx+91,gy+31),(gx+136,gy+34),(gx+186,gy+30),(gx+236,gy+31),(gx+286,gy+26),(gx+337,gy+28),(gx+385,gy+23),(gx+437,gy+25),(gx+492,gy+20),(gx+550,gy+18)]
line(bench,(156,163,175),2)
text(51,400,'NVIDIA  $164.92 CLOSE',11,CYAN,True); text(600,399,'+31.38%',12,GOLD,True,'ra')
d.rounded_rectangle((472,166,600,274),10,fill=(249,250,251),outline=BLUE,width=2)
for xx in (487,506,525,544,563,582): line((xx,156,xx,166),CYAN,3); line((xx,274,xx,284),CYAN,3)
for yy in (180,198,216,234,252): line((462,yy,472,yy),CYAN,3); line((600,yy,610,yy),CYAN,3)
d.ellipse((493,184,579,256),outline=GOLD,width=3); text(536,220,'N',38,GOLD,True,'mm'); line((441,288,441,207),GOLD,4); line((441,207,430,222),GOLD,4); line((441,207,452,222),GOLD,4)

box(648,126,992,414,(255,255,255),(229,231,235),10,1); text(666,141,'CO-LEAD / ANTALYA, TURKEY',11,GOLD,True); text(666,163,'COP31: NO DEAL',27,INK,True); text(666,199,'CLIMATE SUMMIT ENDS WITHOUT A PACT',11,RED,True)
ix0,iy0,ix1,iy1=666,225,974,362; d.rectangle((ix0,iy0,ix1,iy1),fill=(239,244,248),outline=(156,163,175),width=2); d.rectangle((ix0,318,ix1,iy1),fill=(219,226,232))
# A compact summit hall: flag wall, podium, delegates, and a broken progress ring.
d.rectangle((666,242,974,246),fill=(156,163,175)); d.rectangle((675,247,965,252),fill=(203,213,225))
for fx,fc in ((690,RED),(708,BLUE),(726,GOLD),(744,BLUE),(916,RED),(934,GOLD)):
 d.line((fx,253,fx,286),fill=(75,85,99),width=1); d.polygon([(fx,253),(fx+13,258),(fx,253),(fx,269),(fx+13,264),(fx,258)],fill=fc)
d.ellipse((806,246,906,346),fill=(214,230,238),outline=BLUE,width=2)
d.arc((821,260,891,330),205,340,fill=GOLD,width=7); d.arc((818,258,895,334),350,150,fill=(156,163,175),width=5)
d.line((856,286,856,307),fill=RED,width=3); d.line((849,296,856,307),fill=RED,width=3); d.line((863,296,856,307),fill=RED,width=3)
d.polygon([(680,276),(736,264),(773,276),(773,286),(680,286)],fill=(156,163,175),outline=(107,114,128)); d.rectangle((687,286,766,318),fill=(203,213,225),outline=(107,114,128),width=2)
d.rectangle((688,288,765,309),fill=(254,243,199),outline=GOLD,width=2); text(726,298,'ACT NOW',9,INK,True,'mm'); d.rectangle((716,309,738,350),fill=(184,134,11),outline=(107,114,128)); d.line((727,350,727,360),fill=(75,85,99),width=3)
for x in (783,938):
 d.ellipse((x-6,297,x+6,309),fill=(156,163,175)); d.polygon([(x-10,309),(x+10,309),(x+13,349),(x-13,349)],fill=GOLD,outline=(156,163,175)); d.line((x-7,349,x-12,362),fill=(75,85,99),width=3); d.line((x+7,349,x+12,362),fill=(75,85,99),width=3)
d.line((927,242,947,218),fill=BLUE,width=3); d.line((942,220,961,238),fill=BLUE,width=3)
text(667,372,'44 hours overtime; no final agreement',10,INK,True); text(667,390,'FIRST NO-DEAL COP SINCE 2009  •  $5.1–6.8T NEEDED',9,MUTED)

box(32,428,992,626,(249,250,251),(229,231,235),10,1); text(51,441,'WHERE THE DAY LANDED  /  REAL-LOCATION DOTS',12,BLUE,True); mx,my,mw,mh=51,469,922,126; d.rectangle((mx,my,mx+mw,my+mh),fill=(249,250,251),outline=(209,213,219),width=2)
for i in range(1,12): line((mx+i*mw/12,my,mx+i*mw/12,my+mh),(229,231,235),1)
for i in range(1,5): line((mx,my+i*mh/5,mx+mw,my+i*mh/5),(229,231,235),1)
continents=[[(75,520),(88,508),(105,500),(112,492),(132,496),(150,494),(169,501),(181,513),(198,519),(203,529),(191,536),(179,550),(161,548),(151,555),(140,548),(129,556),(116,568),(109,570),(98,561),(84,551),(82,539)],[(222,492),(246,488),(271,486),(298,486),(323,491),(348,497),(380,501),(407,514),(432,520),(456,532),(487,536),(524,544),(554,546),(587,550),(574,558),(553,568),(525,566),(493,562),(455,559),(425,550),(381,545),(352,551),(316,556),(294,548),(270,539),(257,526),(242,514)],[(589,490),(615,487),(642,484),(666,484),(689,489),(712,496),(731,503),(751,509),(775,518),(789,526),(770,540),(748,535),(729,531),(714,530),(695,537),(680,545),(658,550),(644,543),(625,540),(612,535),(600,520)],[(799,493),(822,490),(850,496),(871,499),(890,500),(912,507),(934,512),(952,519),(954,536),(954,548),(937,550),(920,545),(902,544),(884,537),(856,529),(838,532),(814,529),(806,515)]]
for shape in continents: d.polygon(shape,fill=(226,232,240),outline=(75,85,99))
marks=[(345,550,'SENEGAL'),(295,505,'BRUSSELS'),(330,522,'DYMER'),(367,514,'BENGHAZI'),(473,511,'DELHI'),(556,523,'DOHA'),(611,545,'NYC ×8'),(682,566,'WELLINGTON'),(727,505,'ANTALYA'),(783,528,'Gaza'),(849,508,'TOKYO'),(913,560,'VANUATU')]
for x,y,label in marks:
 c = BLUE if label.startswith('NYC') else RED if label == 'ANTALYA' else GOLD
 d.ellipse((x-4,y-4,x+4,y+4),fill=c,outline=INK); text(x+7,y-7,label,8,INK,True)
text(53,602,'Nine regions: Southeast Asia  •  East Asia  •  South Asia  •  Middle East  •  Europe  •  Africa  •  North America  •  Oceania  •  Central Asia',9,MUTED)

box(32,637,992,716,(255,255,255),(229,231,235),9,1); text(51,648,'BESOK  /  WEDNESDAY 25 NOVEMBER 2026',12,BLUE,True); events=['UNSC open debate — New York','UEFA Champions League — Europe','Falcon 9 USSF-266 — Vandenberg','Progress MS-36 — Baikonur','FIFA U-17 Groups I–L — Doha','Consumer Confidence — New York','White House Turkey Pardon — DC']
for i,event in enumerate(events): x=52+(i%2)*458; y=673+(i//2)*12; d.ellipse((x,y+4,x+5,y+9),fill=GOLD); text(x+12,y,event,9,INK)

cards=[('SENEGAL','4 DEAD / DOZENS MISSING',RED),('NATO','3× KH-101 CONFIRMED',BLUE),('NEPAL','$2bn + RAIL',GOLD),('INDIA–NZ','DRAW',GREEN),('BTC','SPIKES TO $64.5K',CYAN),('ANTHROPIC','IPO  $83 → ~$86',ORANGE),('GAZA','CONTAMINATION',RED),('DYMER','9 DEAD',BLUE),('TRILATERAL','TRUMP–XI–PUTIN',GOLD),('U17 WORLD CUP','MATCHDAY 2',GREEN),('BAHRAIN','ESCALATION',CYAN),('VANUATU','M6.5 / 598km',GOLD),('MERKURY','SUNK CLAIM',RED),('WAYMO','FREEWAYS PAUSED',ORANGE)]
def icon(x,y,c,i):
 navy=(17,24,39); gray=(156,163,175)
 if i==0: # Senegal rescue scene
  d.ellipse((x+6,y,x+12,y+6),fill=navy); d.polygon([(x+3,y+8),(x+15,y+8),(x+18,y+17),(x,y+17)],fill=c); line((x+18,y+4,x+18,y+16),c,2); line((x+18,y+5,x+12,y+8),c,1)
 elif i==1: # NATO shield and missile
  d.polygon([(x+8,y),(x+17,y+4),(x+15,y+14),(x+8,y+18),(x+1,y+14),(x,y+4)],outline=c,width=2); line((x+3,y+3,x+18,y+3),navy,1); line((x+9,y+8,x+18,y),c,2); line((x+16,y,x+18,y),GOLD,1)
 elif i==2: # Nepal mountain and rail
  d.polygon([(x,y+16),(x+7,y+4),(x+11,y+10),(x+16,y+1),(x+20,y+16)],fill=(226,232,240),outline=c); line((x+1,y+15,x+19,y+15),navy,1); line((x+2,y+18,x+17,y+18),c,2)
 elif i==3: # cricket bat and ball
  line((x+4,y+2,x+15,y+16),c,4); line((x+2,y+2,x+7,y+7),navy,2); d.ellipse((x+13,y+1,x+19,y+7),fill=RED,outline=navy)
 elif i==4: # bitcoin coin and chart
  d.ellipse((x,y+1,x+18,y+19),fill=(254,243,199),outline=c,width=2); text(x+9,y+2,'B',11,c,True,'ma'); line((x+3,y+15,x+7,y+11,x+11,y+13,x+16,y+6),BLUE,2)
 elif i==5: # Anthropic A and spark
  text(x,y+1,'A',17,c,True); line((x+1,y+18,x+17,y+18),c,2); line((x+17,y+2,x+17,y+10),GOLD,2); line((x+13,y+6,x+21,y+6),GOLD,2)
 elif i==6: # Gaza warning and pin
  d.polygon([(x+8,y),(x+17,y+17),(x,y+17)],fill=(254,242,242),outline=c); line((x+8,y+6,x+8,y+12),c,2); d.ellipse((x+6,y+13,x+10,y+17),fill=c); d.ellipse((x+16,y+2,x+21,y+7),outline=BLUE,width=2); line((x+18,y+7,x+18,y+11),BLUE,1)
 elif i==7: # Dymer house and flame
  d.polygon([(x,y+9),(x+9,y+1),(x+18,y+9)],fill=(226,232,240),outline=c); d.rectangle((x+3,y+9,x+15,y+18),outline=c); d.rectangle((x+8,y+13,x+11,y+18),fill=c); d.polygon([(x+16,y+13),(x+20,y+8),(x+20,y+18),(x+15,y+18)],fill=RED)
 elif i==8: # three flags
  line((x+9,y,x+9,y+18),c,2); line((x+2,y+18,x+17,y+18),navy,2)
  for j,fc in enumerate((RED,BLUE,GOLD)): d.polygon([(x+9,y+2+j*5),(x+18,y+4+j*5),(x+9,y+6+j*5)],fill=fc)
 elif i==9: # football goal and ball
  d.rectangle((x,y+4,x+15,y+17),outline=c); line((x+3,y+6,x+3,y+15),gray,1); line((x+12,y+6,x+12,y+15),gray,1); d.ellipse((x+15,y+1,x+21,y+7),fill=(255,255,255),outline=c); line((x+17,y+4,x+19,y+2),c,1)
 elif i==10: # Bahrain lightning over map
  d.polygon([(x+2,y+13),(x+9,y+8),(x+18,y+9),(x+13,y+16),(x+5,y+17)],fill=(226,232,240),outline=c); d.polygon([(x+12,y),(x+5,y+10),(x+10,y+10),(x+7,y+19),(x+17,y+7),(x+12,y+7)],fill=GOLD,outline=c)
 elif i==11: # Vanuatu wave and seismograph
  line([(x,y+14),(x+4,y+10),(x+8,y+14),(x+12,y+8),(x+16,y+13),(x+20,y+9)],BLUE,2); line((x,y+18,x+20,y+18),c,1); line((x+14,y+1,x+14,y+9),GOLD,2)
 elif i==12: # sinking ship
  d.polygon([(x,y+11),(x+20,y+11),(x+15,y+17),(x+5,y+17)],fill=(226,232,240),outline=c); line((x+10,y+2,x+10,y+11),c,2); line((x+10,y+3,x+16,y+6),RED,2); line((x+2,y+19,x+18,y+19),BLUE,2)
 else: # Waymo car with pause symbol
  d.rounded_rectangle((x,y+7,x+20,y+16),3,fill=(226,232,240),outline=c); d.polygon([(x+4,y+7),(x+8,y+2),(x+14,y+2),(x+18,y+7)],outline=c); d.ellipse((x+3,y+14,x+7,y+18),fill=navy); d.ellipse((x+14,y+14,x+18,y+18),fill=navy); line((x+10,y,x+10,y+5),RED,2); line((x+14,y,x+14,y+5),RED,2)
for i,(head,sub,col) in enumerate(cards):
 x=32+(i%4)*240; y=727+(i//4)*54; box(x,y,x+228,y+48,(249,250,251),(229,231,235),6,1); text(x+9,y+5,head,9,col,True); text(x+9,y+22,sub,8,INK,True); icon(x+195,y+15,col,i)
text(990,948,'14 ILLUSTRATED CARDS',9,MUTED,True,'ra'); line((32,963,992,963),GOLD,2); text(36,973,'DATE CHECK  •  TUESDAY 24 NOVEMBER 2026  •  39 DISTINCT THREADS  •  9 REGIONS  •  SOURCES LEDGER INCLUDED',9,INK,True)
im.save('entry.png',optimize=True)
