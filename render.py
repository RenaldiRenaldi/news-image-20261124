from PIL import Image,ImageDraw,ImageFont
W=H=1024; BG=(10,20,30); INK=(239,244,238); MUTED=(163,184,188); GOLD=(246,184,66); RED=(232,96,78); CYAN=(80,201,193); BLUE=(89,157,220); GREEN=(124,196,137); PANEL=(19,35,47)
im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im); fp='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; fb='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def F(n,b=0): return ImageFont.truetype(fb if b else fp,n)
def T(x,y,s,n=12,c=INK,b=0): d.text((x,y),s,font=F(n,b),fill=c)
def B(a,fill=PANEL,ol=(48,77,91)): d.rounded_rectangle(a,7,fill=fill,outline=ol,width=2)
T(32,22,'THE TUESDAY ATLAS',35,GOLD,1); T(35,63,'24 NOVEMBER 2026  /  FIELD NOTES, PLACES, AND WHAT COMES NEXT',13,MUTED,1); d.line((32,94,992,94),fill=GOLD,width=3)
T(35,108,'CIKANDE: 24 KILLED',30,INK,1); T(37,146,'SEARCH CONTINUES IN THE CANDY FACTORY RUINS',18,RED,1); T(38,178,'MON 23 NOV  •  ~30 STILL MISSING  •  AC SHORT-CIRCUIT SUSPECTED  •  DNA ID 2–3 WEEKS',12,MUTED)
B((34,208,420,458),(25,43,55),(105,139,147)); T(52,224,'FIELD SKETCH / SERANG, INDONESIA',11,GOLD,1); d.rectangle((55,268,398,408),fill=(41,52,58),outline=(115,142,143),width=2)
# A compact field illustration: damaged factory, searchlight, rubble and properly proportioned crews.
d.rectangle((56,269,397,407),fill=(28,39,48)); d.rectangle((61,337,392,407),fill=(35,43,47))
d.polygon([(57,312),(77,284),(98,292),(120,273),(149,290),(174,279),(202,294),(230,270),(260,290),(286,277),(315,295),(345,268),(397,296),(397,338),(57,338)],fill=(49,64,67))
d.polygon([(57,312),(77,284),(98,292),(120,273),(149,290),(174,279),(202,294),(230,270),(260,290),(286,277),(315,295),(345,268),(397,296),(397,312),(346,294),(314,313),(276,298),(235,313),(190,298),(151,314),(112,298),(78,320)],fill=(64,78,77))
for x in (76,112,148,184,220,256,292,328,364):
 d.rectangle((x,337,x+24,405),fill=(56,64,63),outline=(139,141,126),width=1)
for x in (89,167,243,320):
 d.rectangle((x,314,x+38,337),fill=(30,42,47),outline=(115,125,116),width=1)
# warm rescue beam and its bright landing point
d.polygon([(328,314),(359,302),(394,277),(394,337),(359,329)],fill=(109,103,70))
d.polygon([(350,302),(362,298),(394,288),(394,316),(365,317)],fill=(188,155,73))
d.ellipse((370,294,386,310),fill=(246,197,83),outline=(255,226,145),width=1)
# rubble in the foreground
for p in [[(63,399),(78,378),(94,397),(111,389),(126,407)],[(274,407),(288,384),(303,398),(320,386),(345,407)],[(349,407),(359,393),(372,399),(392,388),(397,407)]]: d.polygon(p,fill=(81,80,72),outline=(126,117,93))
# stretchers and covered body bags
for x in (71,276):
 d.line((x,388,x+69,388),fill=(179,166,128),width=3); d.line((x+8,388,x+2,406),fill=(157,148,119),width=2); d.line((x+60,388,x+66,406),fill=(157,148,119),width=2)
 d.polygon([(x+10,375),(x+24,366),(x+57,368),(x+65,380),(x+55,389),(x+19,388)],fill=(122,136,132),outline=(201,205,180))
 d.ellipse((x+19,369,x+31,378),fill=(156,165,153))
# two rescuers with helmets, vests, arms, legs and shadows
for x,y,scale in [(143,367,1),(227,359,1)]:
 d.ellipse((x-15,y+25,x+16,y+34),fill=(18,27,31))
 d.ellipse((x-9,y-31,x+9,y-12),fill=(211,166,124),outline=(15,20,24))
 d.pieslice((x-12,y-38,x+12,y-15),180,360,fill=(244,183,55),outline=(255,210,91)); d.line((x-12,y-27,x+12,y-27),fill=(87,67,39),width=2)
 d.polygon([(x-13,y-12),(x+13,y-12),(x+18,y+26),(x-16,y+26)],fill=(214,137,43),outline=(239,201,112))
 d.rectangle((x-3,y-11,x+3,y+25),fill=(241,206,116)); d.line((x-12,y-5,x-30,y+16),fill=(224,211,178),width=4); d.line((x+12,y-5,x+30,y+11),fill=(224,211,178),width=4)
 d.line((x-8,y+25,x-17,y+43),fill=(47,57,61),width=5); d.line((x+8,y+25,x+17,y+43),fill=(47,57,61),width=5)
d.ellipse((332,355,367,390),outline=CYAN,width=4); d.line((360,384,387,408),fill=CYAN,width=5); T(54,420,'24 body bags recovered; toll confirmed Monday',11,INK,1); T(54,438,'29 safe  •  5 hospitalised  •  unstable structure',10,MUTED)
B((438,208,990,458),(25,39,52),(82,117,134)); T(457,224,'CO-LEAD / MON 23 NOV',11,GOLD,1); T(457,246,'HUANG RETURNS TO NVIDIA',24,INK,1); T(458,281,'Resigned 12 Nov, reinstated by unanimous board',13,CYAN,1); T(458,302,'almost 1 trillion added to Nvidia value; tech stocks rally',13,INK)
# Small upward market mark in the spare right edge; the text column remains unobstructed.
d.polygon([(935,285),(949,267),(958,277),(973,248),(973,305),(935,305)],fill=(42,100,151),outline=CYAN)
d.line((940,296,968,296),fill=INK,width=2); d.line((946,291,953,284),fill=INK,width=2); d.line((953,284,959,289),fill=INK,width=2); d.line((959,289,970,271),fill=INK,width=2)
d.rectangle((740,359,910,405),outline=CYAN,width=3); T(760,370,'NVIDIA',18,CYAN,1); T(458,335,'No senior executive was told beforehand.',11,MUTED); T(458,358,'Developing story; numbers use almost and nearly.',11,MUTED)
B((34,475,990,676),(13,38,52),(67,111,122)); T(52,490,'WHERE THE DAY LANDED  /  REAL-LOCATION DOTS',12,CYAN,1); mx,my,mw,mh=52,518,920,137; d.rectangle((mx,my,mx+mw,my+mh),fill=(10,48,63),outline=(52,102,113))
for i in range(1,10): d.line((mx+i*mw/10,my,mx+i*mw/10,my+mh),fill=(27,72,81))
for i in range(1,5): d.line((mx,my+i*mh/5,mx+mw,my+i*mh/5),fill=(27,72,81))
for s in [
 [(75,550),(91,540),(111,533),(133,536),(151,542),(169,548),(188,558),(180,568),(161,570),(151,580),(139,584),(128,600),(111,598),(98,592),(91,577),(84,568)],
 [(158,585),(170,578),(185,579),(197,588),(205,601),(212,614),(222,624),(215,639),(205,649),(198,640),(191,624),(182,612),(175,598)],
 [(218,536),(246,530),(273,527),(299,530),(321,535),(345,532),(368,531),(393,538),(416,537),(441,544),(464,554),(485,562),(512,570),(539,581),(563,590),(589,591),(578,603),(557,613),(538,608),(514,601),(493,603),(470,609),(449,616),(426,608),(402,603),(382,599),(361,603),(337,608),(317,600),(295,598),(274,590),(253,581),(238,570)],
 [(459,596),(475,590),(490,592),(505,600),(516,612),(520,624),(511,635),(507,647),(493,650),(479,645),(469,633),(454,622),(449,611)],
 [(536,554),(560,548),(582,545),(605,547),(626,552),(647,558),(667,562),(683,570),(704,575),(725,583),(748,585),(765,592),(781,599),(772,607),(750,607),(732,613),(716,608),(702,600),(685,598),(670,603),(652,597),(635,590),(616,586),(598,581),(579,577),(560,570)],
 [(778,617),(797,613),(813,616),(826,625),(840,630),(855,635),(862,645),(849,651),(833,648),(821,641),(806,639),(791,633)],
 [(848,536),(868,531),(889,534),(906,541),(926,548),(950,550),(968,557),(960,568),(942,569),(925,563),(906,566),(891,558),(874,554),(856,548)]]: d.polygon(s,fill=(40,84,77),outline=(104,152,126))
for x,y,l in [(140,575,'Cikande'),(378,550,'Antalya'),(248,554,'Brussels'),(292,567,'Dymer'),(308,576,'Benghazi'),(462,565,'Delhi'),(652,620,'Wellington'),(755,560,'Doha'),(837,650,'NYC ×7'),(870,610,'DC'),(720,600,'Gaza'),(938,540,'Tokyo')]: d.ellipse((x-5,y-5,x+5,y+5),fill=GOLD,outline=INK); T(x+8,y-7,l,9,INK,1)
T(55,650,'Cluster rule: New York is one dot for BTC, stocks, GTA VI, n0n, Pannun, UNSC and Consumer Confidence.',10,MUTED)
B((34,692,990,798),(23,46,53),(64,133,132)); T(52,706,'BESOK  /  WEDNESDAY 25 NOVEMBER 2026',13,CYAN,1)
events=['UNSC open debate — New York','UEFA Champions League Matchday 5 — Europe','Falcon 9 USSF-266 — Vandenberg, 15:55 UTC','Progress MS-36 — Baikonur, 05:03 UTC','FIFA U-17 Matchday 2 groups I–L — Doha','Consumer Confidence November — New York, 10:00 ET','White House Turkey Pardon — Washington DC, 14:00 ET']
for i,e in enumerate(events): x=54+(i%2)*460; y=735+(i//2)*15; d.ellipse((x,y+4,x+6,y+10),fill=GOLD); T(x+14,y,e,10)
cards=[('COP31','NO DEAL',RED),('NATO','3× KH-101',BLUE),('NEPAL','RAIL + $2bn',GOLD),('INDIA–NZ','DRAW',GREEN),('BTC','~$61.5k FLAT',CYAN),('GAZA','CONTAMINATION',RED),('WAYMO','FREEWAYS HALT',BLUE),('SENEGAL','BOAT CAPSIZES',GOLD),('DENMARK','GHETTO LAW',GREEN),('FIFA','2031 / 2035 HOSTS',CYAN),('ALCARAZ','ATP FINALS',GOLD),('MERKURY','UKRAINE CLAIMS SUNK',RED)]
for i,(a,b,c) in enumerate(cards):
 x=34+(i%4)*240; y=810+(i//4)*60; B((x,y,x+228,y+52),(18,34,47)); T(x+8,y+6,a,10,c,1); T(x+8,y+22,b,9,INK,1); d.ellipse((x+190,y+17,x+208,y+35),outline=c,width=2); d.line((x+199,y+35,x+199,y+46),fill=c,width=2)
d.line((34,974,990,974),fill=GOLD,width=2); T(38,983,'DATE CHECK  •  TUESDAY 24 NOVEMBER 2026  •  36 DISTINCT THREADS  •  SOURCES LEDGER INCLUDED',10,INK,1); im.save('entry.png',optimize=True)
