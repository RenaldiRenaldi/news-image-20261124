from PIL import Image,ImageDraw,ImageFont
W=H=1024; BG=(10,20,30); INK=(239,244,238); MUTED=(163,184,188); GOLD=(246,184,66); RED=(232,96,78); CYAN=(80,201,193); BLUE=(89,157,220); GREEN=(124,196,137); PANEL=(19,35,47)
im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im); fp='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; fb='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def F(n,b=0): return ImageFont.truetype(fb if b else fp,n)
def T(x,y,s,n=12,c=INK,b=0): d.text((x,y),s,font=F(n,b),fill=c)
def B(a,fill=PANEL,ol=(48,77,91)): d.rounded_rectangle(a,7,fill=fill,outline=ol,width=2)
T(32,22,'THE TUESDAY ATLAS',35,GOLD,1); T(35,63,'24 NOVEMBER 2026  /  FIELD NOTES, PLACES, AND WHAT COMES NEXT',13,MUTED,1); d.line((32,94,992,94),fill=GOLD,width=3)
T(35,108,'CIKANDE: 24 KILLED',30,INK,1); T(37,146,'SEARCH CONTINUES IN THE CANDY FACTORY RUINS',18,RED,1); T(38,178,'MON 23 NOV  •  ~30 STILL MISSING  •  AC SHORT-CIRCUIT SUSPECTED  •  DNA ID 2–3 WEEKS',12,MUTED)
B((34,208,420,458),(25,43,55),(105,139,147)); T(52,224,'FIELD SKETCH / SERANG, INDONESIA',11,GOLD,1); d.rectangle((55,268,398,408),fill=(41,52,58),outline=(115,142,143),width=2)
for x in (70,130,190,250,310,370): d.rectangle((x,302,x+28,408),fill=(70,79,78),outline=(169,165,132),width=1)
d.polygon([(55,305),(100,255),(150,280),(210,245),(260,277),(330,245),(398,282),(398,268),(55,268)],fill=(55,71,70))
for x,y in [(112,370),(185,355),(260,375)]:
 d.ellipse((x-10,y-34,x+10,y-14),fill=(222,177,132),outline=(15,20,24)); d.arc((x-12,y-40,x+12,y-17),180,360,fill=GOLD,width=4); d.rectangle((x-14,y-14,x+14,y+30),fill=(197,142,43),outline=INK,width=1); d.line((x-12,y+4,x-30,y+20),fill=INK,width=3); d.line((x+12,y+4,x+30,y+20),fill=INK,width=3)
d.ellipse((310,355,350,395),outline=CYAN,width=4); d.line((345,390,380,418),fill=CYAN,width=5); T(54,420,'24 body bags recovered; toll confirmed Monday',11,INK,1); T(54,438,'29 safe  •  5 hospitalised  •  unstable structure',10,MUTED)
B((438,208,990,458),(25,39,52),(82,117,134)); T(457,224,'CO-LEAD / MON 23 NOV',11,GOLD,1); T(457,246,'HUANG RETURNS TO NVIDIA',24,INK,1); T(458,281,'Resigned 12 Nov → reinstated by unanimous board vote',13,CYAN,1); T(458,302,'almost $1 trillion added to Nvidia value; tech stocks rally',13,INK)
d.ellipse((805,260,865,320),fill=(190,140,103),outline=INK,width=2); d.pieslice((800,248,870,290),180,360,fill=(26,30,36),outline=(10,15,20)); d.rectangle((817,319,853,379),fill=(30,69,103)); d.rectangle((740,359,910,405),outline=CYAN,width=3); T(760,370,'NVIDIA',18,CYAN,1); T(458,335,'No senior executive was told beforehand.',11,MUTED); T(458,358,'Developing story; numbers use “almost” and “nearly”.',11,MUTED)
B((34,475,990,676),(13,38,52),(67,111,122)); T(52,490,'WHERE THE DAY LANDED  /  REAL-LOCATION DOTS',12,CYAN,1); mx,my,mw,mh=52,518,920,137; d.rectangle((mx,my,mx+mw,my+mh),fill=(10,48,63),outline=(52,102,113))
for i in range(1,10): d.line((mx+i*mw/10,my,mx+i*mw/10,my+mh),fill=(27,72,81))
for i in range(1,5): d.line((mx,my+i*mh/5,mx+mw,my+i*mh/5),fill=(27,72,81))
for s in [[(75,550),(110,535),(155,540),(190,555),(175,574),(142,580),(125,604),(94,595)],[(200,535),(270,526),(340,536),(410,531),(475,548),(540,570),(590,590),(555,612),(500,600),(450,615),(390,598),(330,608),(275,590),(235,570)],[(460,596),(500,600),(520,624),(505,650),(475,646),(450,620)],[(650,595),(690,585),(730,600),(718,619),(680,625)]]: d.polygon(s,fill=(40,84,77),outline=(104,152,126))
for x,y,l in [(140,575,'Cikande'),(378,550,'Antalya'),(248,554,'Brussels'),(292,567,'Dymer'),(308,576,'Benghazi'),(462,565,'Delhi'),(652,620,'Wellington'),(755,560,'Doha'),(837,650,'NYC ×7'),(870,610,'DC'),(720,600,'Gaza'),(938,540,'Tokyo')]: d.ellipse((x-5,y-5,x+5,y+5),fill=GOLD,outline=INK); T(x+8,y-7,l,9,INK,1)
T(55,650,'Cluster rule: New York is one dot for BTC, stocks, GTA VI, n0n, Pannun, UNSC and Consumer Confidence.',10,MUTED)
B((34,692,990,798),(23,46,53),(64,133,132)); T(52,706,'BESOK  /  WEDNESDAY 25 NOVEMBER 2026',13,CYAN,1)
events=['UNSC open debate — New York','UEFA Champions League Matchday 5 — Europe','Falcon 9 USSF-266 — Vandenberg, 15:55 UTC','Progress MS-36 — Baikonur, 05:03 UTC','FIFA U-17 Matchday 2 groups I–L — Doha','Consumer Confidence November — New York, 10:00 ET','White House Turkey Pardon — Washington DC, 14:00 ET']
for i,e in enumerate(events): x=54+(i%2)*460; y=735+(i//2)*15; d.ellipse((x,y+4,x+6,y+10),fill=GOLD); T(x+14,y,e,10)
cards=[('COP31','NO DEAL',RED),('NATO','3× KH-101',BLUE),('NEPAL','RAIL + $2bn',GOLD),('INDIA–NZ','DRAW',GREEN),('BTC','~$61.5k FLAT',CYAN),('GAZA','CONTAMINATION',RED),('WAYMO','FREEWAYS HALT',BLUE),('SENEGAL','BOAT CAPSIZES',GOLD),('DENMARK','GHETTO LAW',GREEN),('FIFA','2031 / 2035 HOSTS',CYAN),('ALCARAZ','ATP FINALS',GOLD),('MERKURY','UKRAINE CLAIMS SUNK',RED)]
for i,(a,b,c) in enumerate(cards):
 x=34+(i%4)*240; y=810+(i//4)*60; B((x,y,x+228,y+52),(18,34,47)); T(x+8,y+6,a,10,c,1); T(x+8,y+22,b,9,INK,1); d.ellipse((x+190,y+17,x+208,y+35),outline=c,width=2); d.line((x+199,y+35,x+199,y+46),fill=c,width=2)
d.line((34,974,990,974),fill=GOLD,width=2); T(38,983,'DATE CHECK  •  TUESDAY 24 NOVEMBER 2026  •  36 DISTINCT THREADS  •  SOURCES LEDGER INCLUDED',10,INK,1); im.save('entry.png',optimize=True)
