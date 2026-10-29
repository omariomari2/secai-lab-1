"""Render the precise diagram using Pillow (optional authoring dependency)."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math

HERE = Path(__file__).resolve().parent
im = Image.new('RGB', (1600, 1220), 'white')
d = ImageDraw.Draw(im)
fontpath = 'C:/Windows/Fonts/arial.ttf'
boldpath = 'C:/Windows/Fonts/arialbd.ttf'
font = ImageFont.truetype(fontpath, 22)
small = ImageFont.truetype(fontpath, 19)
bold = ImageFont.truetype(boldpath, 25)
title = ImageFont.truetype(boldpath, 34)
ink = '#152a3a'


def text(x, y, s, f=font, fill=ink):
    d.multiline_text((x, y), s, font=f, fill=fill, spacing=5, align='center')


def region(box, label, fill):
    d.rounded_rectangle(box, 18, fill=fill, outline='#74899b', width=3)
    text(box[0]+18, box[1]+14, label, bold)


def node(box, label):
    d.rounded_rectangle(box, 10, fill='white', outline='#234a67', width=3)
    lines = label.split('\n')
    for i, line in enumerate(lines):
        b = d.textbbox((0, 0), line, font=font)
        text((box[0]+box[2]-(b[2]-b[0]))/2, (box[1]+box[3])/2-len(lines)*15+i*29, line)


def arrow(points, label='', pos=None):
    d.line(points, fill='#234a67', width=3)
    a, b = points[-2:]
    angle = math.atan2(b[1]-a[1], b[0]-a[0])
    tri = [b, (b[0]-15*math.cos(angle-.45), b[1]-15*math.sin(angle-.45)),
           (b[0]-15*math.cos(angle+.45), b[1]-15*math.sin(angle+.45))]
    d.polygon(tri, fill='#234a67')
    if label and pos:
        bb=d.multiline_textbbox(pos, label, font=small, spacing=5)
        d.rectangle((bb[0]-5,bb[1]-3,bb[2]+5,bb[3]+3),fill='white')
        text(*pos,label,small)


text(44, 24, 'GramHelp: data flows and trust boundaries', title)
region((35, 90, 350, 640), 'TB1  Client devices', '#f2f5f8')
region((410, 90, 1110, 950), 'University application', '#eaf3fa')
region((1160, 90, 1565, 400), 'TB2  Model provider', '#fff3df')
region((1160, 470, 1565, 950), 'TB3  Internal APIs', '#ebf6ec')
node((75,190,310,290),'Student user\nAuthenticated session')
node((75,480,310,580),'Staff uploader\nStaff-authenticated')
node((480,190,1000,300),'Chatbot / orchestrator\nEscaped response to user')
node((1200,190,1525,300),'LLM\nNo service credentials')
node((480,400,1000,505),'Vector database\nACL-filtered retrieved chunks')
node((480,610,1000,720),'Document upload / review\nQuarantine, scan, approve')
node((480,815,740,910),'Separate human\napproval UI')
node((810,815,1060,910),'Tool policy\ngateway')
node((1200,560,1525,670),'Balance API\nRead own account only')
node((1200,800,1525,910),'Ticketing system\nCreate approved ticket')
arrow([(310,220),(480,220)],'Question', (330,184))
arrow([(480,270),(310,270)],'Answer', (335,281))
arrow([(1000,220),(1200,220)],'Scoped prompt', (1010,180))
arrow([(1200,275),(1000,275)],'Answer / tool call', (1010,290))
arrow([(700,300),(700,400)],'Query / chunks', (715,340))
arrow([(195,580),(195,665),(480,665)],'Policy PDF', (250,630))
arrow([(750,610),(750,505)],'TB4: reviewed content\nto automatic indexing', (775,535))
arrow([(100,290),(55,325),(55,860),(480,860)],'Exact ticket\nconfirmation', (210,775))
arrow([(1000,300),(1080,330),(1080,780),(935,780),(935,815)],'Tool arguments +\nserver-bound identity', (865,742))
arrow([(740,860),(810,860)])
arrow([(1060,840),(1135,840),(1135,615),(1200,615)],'Scoped read / result', (1180,705))
arrow([(1060,880),(1200,880)],'Create / ID', (1070,915))
text(435,970,'Approval is bound to user + exact payload; expires in 300 seconds; single use.',small)
text(45,1035,'Boundary rules',bold)
text(45,1080,'TB1: authenticate clients.  TB2: minimize model context.  TB3: enforce API permissions.',font)
text(45,1120,'TB4: review before indexing. Retrieved text remains untrusted after approval.',font)
text(45,1160,'Arrows with paired labels summarize request and response. Synthetic design; not a deployment.',small)
im.save(HERE/'architecture.png')
